import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
st.set_option('deprecation.showPyplotGlobalUse', False)
import sqlite3

conn = sqlite3.connect('data1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable1(author TEXT, title TEXT, articles TEXT, postdate DATE)')
    
def add_data(author, title, articles, postdate):
    c.execute('INSERT INTO blogtable1 (author, title, articles, postdate) VALUES (?, ?, ?, ?)', (author, title, articles, postdate))
    conn.commit()
    
def view_all_notes():
    c.execute('SELECT * FROM blogtable1')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable1')
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable1 WHERE title = "{}"'.format(title))
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable1 WHERE author = "{}"'.format(author))
    data = c.fetchall()
    return data

def delete_data(title):
    c.execute('DELETE FROM blogtable1 WHERE title = "{}"'.format(title))
    conn.commit()

def readingTime(mytext):
    total_words = len([token for token in mytext.split(" ")])
    estimatedTime = total_words / 200.0
    return estimatedTime

title_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
            <h4 style="color:white;text-align:center;">{}</h1>
            <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
            <h6>Author:{}</h6>
            <br/>
            <br/> 
            <p style="text-align:justify">{}</p>
        </div>
        """
article_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
            <h4 style="color:white;text-align:center;">{}</h1>
            <h6>Author:{}</h6> 
            <h6>Post Date: {}</h6>
            <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
            <br/>
            <br/>
            <p style="text-align:justify">{}</p>
        </div>
        """
head_message_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
            <h4 style="color:white;text-align:center;">{}</h1>
            <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
            <h6>Author:{}</h6> 
            <h6>Post Date: {}</h6> 
        </div>
        """
full_message_temp ="""
        <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
            <p style="text-align:justify;color:black;padding:10px">{}</p>
        </div>
        """

def main():
    st.title('Simple Blog')
    
    menu = ['Home', 'View Posts', 'Add post', 'Search', 'Manage Blog']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        st.subheader('Home')
        result = view_all_notes()
        st.write(result)
        for i in result:
            b_author = i[0]
            b_title = i[1]
            b_article = str(i[2])[0:30]
            b_post_date = i[3]
            st.markdown(title_temp.format(b_author, b_title, b_article, b_post_date), unsafe_allow_html = True)
        
    elif choice == 'View Posts':
        st.subheader('View Articles')
        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.sidebar.selectbox('View Posts', all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            b_author = i[0]
            b_title = i[1]
            b_article = i[2]
            b_post_date = i[3]
            st.text('Reading Time: {}'.format(readingTime(b_article)))
            st.markdown(head_message_temp.format(b_author, b_title, b_post_date), unsafe_allow_html = True)
            st.markdown(full_message_temp.format(b_article), unsafe_allow_html = True)
        
    elif choice == 'Add post':
        st.subheader('Add Articles')
        create_table()
        blog_author = st.text_input('Enter Author Name: ', max_chars = 50)
        blog_title = st.text_input('Enter Post Title: ')
        blog_article = st.text_area('Post Articles Here', height = 200)
        blog_post_date = st.date_input('Date')
        if st.button('Add'):
            add_data(blog_author, blog_title, blog_article, blog_post_date)
            st.success('Post: {} saved'.format(blog_title))
        
        
    elif choice == 'Search':
        st.subheader('Search Articles')
        search_term = st.text_input('Enter Search Term: ')
        search_choice = st.radio('Field to Search By', ('title', 'author'))
        
        if st.button('Search'):
            if search_choice == 'title':
                articles_result = get_blog_by_title(search_term)
            elif search_choice == 'author':
                articles_result = get_blog_by_author(search_term)
                
            for i in articles_result:
                b_author = i[0]
                b_title = i[1]
                b_article = i[2]
                b_post_date = i[3]
                st.text('Reading Time: {}'.format(readingTime(b_article)))
                st.markdown(head_message_temp.format(b_author, b_title, b_post_date), unsafe_allow_html = True)
                st.markdown(full_message_temp.format(b_article), unsafe_allow_html = True)
            
        
    if choice == 'Manage Blog':
        st.subheader('Manage Articles')
        
        result = view_all_notes()
        clean_db = pd.DataFrame(result, columns =['Author','Title', 'Articles','Post Date'])
        st.dataframe(clean_db)
        unique_titles = [i[0] for i in view_all_titles()]
        delete_blog_by_title = st.selectbox('Delete Title', unique_titles)
        new_df = clean_db
        if st.button('Delete'):
            delete_data(delete_blog_by_title)
            st.warning('Delete: "{}"'.format(delete_blog_by_title))
        
        if st.checkbox('Metrics'):
            new_df['Length'] = new_df['Articles'].str.len()
            st.dataframe(new_df)
            
            st.subheader('Author Status')
            new_df['Author'].value_counts().plot(kind = 'bar')
            st.pyplot()

            st.subheader('Author Status')
            new_df['Author'].value_counts().plot.pie()
            st.pyplot()

        if st.checkbox("BarH Plot"):
            st.subheader('Length of Articles')
            new_df['Length'] = new_df['Articles'].str.len()
            barh_plot = new_df.plot.barh(x = 'Author', y = 'Length', figsize = (20, 10))
            st.pyplot()

        
if __name__ == '__main__':
    main()
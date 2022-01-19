from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1.Khai bao chromedriver
driver = webdriver.Chrome(executable_path = 'C:/Program Files/Google/chromedriver/chromedriver.exe')
driver.set_window_size(700, 800)

# 2. Dang nhap vao facebook
driver.get('https://www.facebook.com/login')
driver.find_element_by_id('email').send_keys('0941245819')
sleep(1)
driver.find_element_by_id('pass').send_keys('Duongteacher123456')  
sleep(1)
driver.find_element_by_name('login').click()
sleep(4)


# 3. Truy cap vao link
#driver.get('https://www.facebook.com/sam.cao.940/posts/3057069604574046?__cft__[0]=AZUXOmBeKovfu4flAbGO0GB3BJEydOiAwCjMWhp6AEHtH7fesrZc8lOUCa7d7pIUVZkGLUdvO1YPWp2B0essXnM-zOswrtxciwXbYJfHSy-bIni4KvT9JHZ3tNLYq1PeFSVLtTotFDz94QZ5SH4pvnQrvQsiKMrrKAUlTHvPTp8k-w&__tn__=%2CO%2CP-R')
driver.get('https://www.facebook.com/groups/miaigroup/permalink/730028114435130/')
sleep(5)

# 4. Lay link hien comments
#showcomment_link = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[4]/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/span")
showcomment_link = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div")
showcomment_link.click()

# 5. Lay comment
showmore_link = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]/span")
showmore_link.click()
sleep(5)

showmore_link.click()
sleep(5)

driver.close()
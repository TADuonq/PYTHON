from tkinter import Tk, Canvas 
from datetime import date, datetime

def get_events():
    list_events = []
    with open(r'C:/Users/Administrator/Duong/Python/Keras/Phan4/events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

root = Tk()
c = Canvas(root, width = 800, height = 800, bg = 'black')
c.pack()
c.create_text(100, 50, anchor = 'w', fill = 'orange',
              font = 'Arial 28 bold underline',
              text = 'Duong Teacher')

events = get_events()
today = date.today()

vertical_space = 100

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'It is %s days until %s' %(days_until, event_name)
    if(int(days_until) <= 7):
        text_col = 'red'
    else:
        text_col = 'lightblue'
    c.create_text(100, 100, anchor = 'w', font = 'Arial 28 bold', 
                  text = display, fill = 'lightblue')
    vertical_space = vertical_space + 30
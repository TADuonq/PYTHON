import fbchat
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.searchForUsers(name)  # return a lduongist of names
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.sendMessage(msg, thread_id=friend.uid)
    if sent:
        print("Message sent successfully!")

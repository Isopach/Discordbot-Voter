#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randint


# Bot list 
id_list =   ["1234567890",  # Bot ids / names
             "1234567890",  # Bot ids / names
             "1234567890",  # Bot ids / names
             "1234567890",  # Bot ids / names
             ]  
             

url = "https://top.gg/bot/" + id_list[randint(0,len(id_list))] + "/vote"
user_profile = "C:/Users/YourUserName/AppData/Local/Google/Chrome/User Data/Profile 2"

# Chrome Profile
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+user_profile) # Path to your chrome profile
options.add_argument("--window-size=0,120")
options.add_argument("--disable-notifications") # Disables restore pages popup
options.add_argument("--app="+url) # Hides address bar
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36") # Sets User Agent

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', chrome_options=options)

# Minimize
driver.minimize_window()

# Go to vote page
driver.get(url)

# Set cookie
driver.add_cookie({'name' : 'connect.sid', 'value' : 'YOUR COOKIE VALUE', 'domain' : 'top.gg', 'path': '/' })

for i in range(0,len(id_list)):
    url = "https://top.gg/bot/" + id_list[i] + "/vote"
    driver.get(url)

    vote_btn = driver.find_element_by_id('votingvoted')
    
    # Scroll down to vote button
    actions = ActionChains(driver)
    actions.move_to_element(vote_btn).perform()

    driver.execute_script("arguments[0].click();", vote_btn) 
       
    print("Voted!")
    sleep(randint(10,20))

driver.quit()

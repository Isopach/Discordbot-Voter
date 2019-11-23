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

# Chrome Profile
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=PATH") # Path to your chrome profile
options.add_argument("--window-size=0,120")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', chrome_options=options)

# Go to vote page
driver.get(url)

# Set cookie
driver.add_cookie({'name' : 'connect.sid', 'value' : 'YOUR COOKIE ID HERE', 'domain' : 'top.gg', 'path': '/' })

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

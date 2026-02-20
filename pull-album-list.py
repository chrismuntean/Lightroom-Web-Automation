# File: pull-album-list.py
# Desc: This script is meant to pull the list of folders and albums in Lightroom, and save them to a text file.

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://lightroom.adobe.com/signin")

# Wait 5 minutes until the URL include /libraries/*
WebDriverWait(driver, 300).until(
    EC.url_contains("/libraries/")
)

print("User has logged in")

# Pull all the inner text content of the element with xpath "/html/body/sp-theme/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div/div[1]"
album_list_element = WebDriverWait(driver, 600).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/sp-theme/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div/div[1]"))
)

# Get the innerText of anything with the class "SidebarAlbum-*" AND the attribute dir="auto"
album_elements = album_list_element.find_elements(By.XPATH, ".//div[contains(@class, 'SidebarAlbum-') and @dir='auto']")
album_names = [album_element.get_attribute("innerText") for album_element in album_elements]

# Save the album names to a text file called "album_names.txt"
with open("album_names.txt", "w") as f:
    for album_name in album_names:
        f.write(album_name + "\n")
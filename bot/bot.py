import os
import time
import sys
from tqdm import tqdm
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from instabot import Bot
driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.instagram.com/")
time.sleep(6)
logusername=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
logusername.send_keys("username goes here")
password=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("password goes here")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
driver.close()
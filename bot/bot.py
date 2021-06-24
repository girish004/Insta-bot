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
password.send_keys("Password goes here")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
time.sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
time.sleep(11)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
time.sleep(6)
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(6)
while(1):
    print(driver.find_element_by_class_name("bqXJH").get_attribute("innerHTML"))
    driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.oNO81 > div.Igw0E.IwRSH.eGOV_._4EzTm.i0EQd > div > div > div > div > div:nth-child(1) > a > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl").click()

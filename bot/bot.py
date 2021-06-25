import os
import time
import sys
from tqdm import tqdm
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from instabot import Bot

def login(driver):
    time.sleep(3)
    logusername=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    logusername.send_keys("username goes here")
    password=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("password goes here")
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    time.sleep(6)

def notification(driver):
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(6)
    try:
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(6)

driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.instagram.com/")
login(driver)
notification(driver)
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(6)
variable="Message you wanna provide"
while(1):
    try:
        num=int(driver.find_element_by_class_name("bqXJH").get_attribute("innerHTML"))
        print("Total messages:",num)
        driver.find_element_by_css_selector("div._41V_T.Sapc9.Igw0E.IwRSH.eGOV_._4EzTm").click()
        print(driver.find_elements_by_css_selector("div._7UhW9.xLCgt.MMzan.KV-D4.p1tLr.hjZTB")[-1].get_attribute("innerHTML"))
        driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(variable)
    except:
        print("No messages found")
        break
        
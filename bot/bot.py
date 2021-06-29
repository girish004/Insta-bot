import os
import time
import sys
from tqdm import tqdm
import datetime
from selenium import webdriver
import threading
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from instabot import Bot

def message(driver):
    variable1="Hello there from Nanbargal iyakkam!\n"
    variable2="Press the respective keys to know about us\n"
    variable3="1. To know the name of our NGO's head\n"
    variable4="2. Details about our previous service.\n"
    variable5="3. Details about our next service\n"
    variable6="4. Exit"
    while(1):
        try:
            flag=0
            num=int(driver.find_element_by_class_name("bqXJH").get_attribute("innerHTML"))
            print("Total messages:",num)
            driver.find_element_by_css_selector("div._41V_T.Sapc9.Igw0E.IwRSH.eGOV_._4EzTm").click()
            msg=driver.find_elements_by_css_selector("div._7UhW9.xLCgt.MMzan.KV-D4.p1tLr.hjZTB")[-1].get_attribute("innerHTML")
            msg=msg[6:len(msg)-7]
            print(msg)
            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(variable1+variable2+variable3+variable4+variable5+variable6)
            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            time.sleep(2)
            one="Jey vishvak is the name of our head. Thanks for your interest. Have a nice day!"
            two="We did our previous service near saidapet, We served 100 poor by feeding them with sambhar rice. Thanks for your interest. Stay in touch! Have a great day"
            three="We are looking to serve the poor in the teynampet slum. Do help us by offering us anything you can. Thanks. Have a great day!"
            variable6="4. Exit"
            starttimer=int(time.perf_counter())
            endtimer=int(time.perf_counter())
            while(1):
                try:
                    msg=driver.find_elements_by_css_selector("div._7UhW9.xLCgt.MMzan.KV-D4.p1tLr.hjZTB")[-1].get_attribute("innerHTML")
                    msg=msg[6:len(msg)-7]
                    time.sleep(1)
                    if(msg!=one and msg!=two and msg !=three and msg!=variable6 and msg!="Please enter the proper message"):
                        flag=1
                        starttimer=int(time.perf_counter())
                        if(msg=="1"):
                            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(one)
                        elif(msg=="2"):
                            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(two)
                        elif(msg=="3"):
                            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(three)
                        elif(msg=="4"):
                            time.sleep(2)
                            driver.get("https://www.instagram.com/direct/inbox/")
                            time.sleep(6)
                            break
                        else:
                            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Please enter the proper message")
                        driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        time.sleep(1)
                    else:
                        endtimer=int(time.perf_counter())
                        if(endtimer-starttimer>20):
                            flag=1
                            break
                except:
                    msg=msg
        except:
            a=1

def login(driver):
    time.sleep(3)
    logusername=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    logusername.send_keys("arch.anakrish")
    password=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("12345678a")
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    time.sleep(6)

def notification(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    except:
        print("Privacy accepted")
    time.sleep(6)
    try:
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)

driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.instagram.com/")
login(driver)
notification(driver)
driver.get("https://www.instagram.com/direct/inbox/")
message(driver)
time.sleep(6)
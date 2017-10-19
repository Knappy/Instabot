# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:04:32 2017

@author: BLK
"""
url="https://instagram.com"
#from bs4 import BeautifulSoup
#import requests
#from robobrowser import RoboBrowser'
from selenium import webdriver
import time
import json
import random
userName = input("Type Username:")
password = input("Type Password:")
passkey = "0"
tags=["brød","surdeig","baking", "sourdough"]
tag=tags[-1]
driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.set_window_size(50,50)
driver.get(url)
total = 0
nxtPress= 0
likeNames={}
if len(json.load(open("likeNames.txt","r"))) > 0:
    likeNames = json.load(open("likeNames.txt","r"))
tagLikes={}
if len(json.load(open("taglikes.txt","r"))) > 0:
    tagLikes = json.load(open("taglikes.txt","r"))
total = sum(likeNames.values())


def login():
    element= driver.find_element_by_class_name("_b93kq")
    element.click()
    user=driver.find_element_by_name("username")
    user.send_keys(userName)
    passW=driver.find_element_by_name("password")
    passW.send_keys(password)
    loginbutton=driver.find_element_by_css_selector("button")
    loginbutton.click()
    time.sleep(3)
    while len(driver.find_elements_by_name("verificationCode")) > 0:
        sec = driver.find_element_by_name("verificationCode")
        sec.click()
        keys = input("tast inn kode")
        sec.send_keys(keys)    
        sec.submit()


def openTag(tag =tag):
    tag=tag
#    from selenium.webdriver.common.by import By
#    from selenium.webdriver.support.ui import WebDriverWait
#    from selenium.webdriver.support import expected_conditions as EC  
    
    driver.get(url+"/explore/tags/"+tag)
    time.sleep(3)
    
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]').click()
    driver.find_element_by_id("react-root").click()
#    driver.find_element_by_class_name("_e3il2").click()
    
#    
def liker(total = total, nxtPress = nxtPress):

    tottemp= total
    nxtpresstemp = nxtPress
    while tottemp - total < 20:
        name = driver.find_element_by_class_name("_eeohz").text
        likeNames.setdefault(name,0)
        likeNames[name] += 1
        print(name)
        print("likes:", tottemp - total)
        print("next press:", nxtpresstemp - nxtPress)
        
        #driver.find_element_by_class_name("_si7dy").click()
        like=driver.find_element_by_xpath("//span[contains(@class,'coreSpriteHeart')]").text
        heart = driver.find_element_by_xpath("//span[contains(@class, 'coreSpriteHeart')]")
        nxt = driver.find_element_by_link_text("Next")
        if nxtpresstemp - tottemp > 150:
            break
        elif name.lower() != userName and like.lower() == "like":
            heart.click()
            likeNames.setdefault(name,0)
            likeNames[name] += 1
            tagLikes.setdefault(tag,0)
            tagLikes[tag]+=1
            tottemp += 1
            nxt.click()
            nxtpresstemp += 1
            time.sleep(random.randrange(2, 8))
        
        else:
            nxt.click()    
            nxtpresstemp += 1
            time.sleep(random.randrange(2, 8))
    
    total = tottemp
    nxtPress = nxtpresstemp
    print("Total likes:" , total,"\n","Total next", nxtPress)
    for i in likeNames:
        print(i,":", likeNames[i])
    tSleep = random.randrange(850, 950)
    print("sleeping for", tSleep ,"min")
    
    time.sleep(tSleep)
    print("resuming")
    liker(total, nxtPress)



json.dump(likeNames, open("likeNames.txt",'w'))
json.dump(tagLikes, open("tagLikes.txt",'w'))
json.dump(total, open("total.txt",'w'))
json.dump(nxtPress, open("nxtpress.txt",'w'))
#
#
#
#
#test = json.load(open("tagLikes.txt","r"))
#
#
#



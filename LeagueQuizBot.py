#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import keyboard
import json

qa = {}


def save():
    jf = json.dumps(qa)
    f = open("questions.json", "w")
    f.write(jf)
    f.close()


driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://mb-hextech-chest-quiz.com/")
with open("questions.json") as json_file:
    qa = json.load(json_file)

print(len(qa))

save()
time.sleep(5)
for x in range(1):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'frame')))
    driver.switch_to.frame(driver.find_element_by_id("frame"))
print(driver.page_source)
input("Enter To Start")
while True:
    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'frame')))
        driver.switch_to.frame(driver.find_element_by_id("frame"))
        #print(driver.page_source)
        quest = driver.find_element_by_class_name("question-text").text
        ans = driver.find_elements_by_class_name("choice")
        if quest != "":
            if quest in qa:
                rep = qa[quest]
                for x in ans:
                    if rep == x.text:
                        x.click()
            else:
                print("Not Found")
                print("----------------------------------------------")
                print(quest)
                print("----")
                for x in range(len(ans)):
                    print(x+1, ": ", ans[x].text)
                out = input("correct answer A, B, C")
                if out == "1":
                    qa[quest] = ans[0].text
                    save()
                elif out == "2":
                    qa[quest] = ans[1].text
                    save()
                elif out == "3":
                    qa[quest] = ans[2].text
                    save()
                print("----------------------------------------------")
                print(qa[quest])
                print("----------------------------------------------")
    except:
        pass
    if keyboard.is_pressed('ESC'):
        exit()
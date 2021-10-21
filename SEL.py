from typing import Counter
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import shutil
from selenium.webdriver.common.keys import Keys


def calculate(seg):
    # return the calculated
    if seg[1] == "+":
        return int(seg[0]) + int(seg[2])
    elif seg[1] == "-":
        return int(seg[0]) - int(seg[2])

    elif seg[1] == "*":
        return int(seg[0]) * int(seg[2])

    elif seg[1] == "%":
        return int(seg[0]) % int(seg[2])


def main():
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get("https://aiot.codingmaster.cc/AIoT/Homework/")
    browser.find_element_by_name('userID').send_keys('ntustB10707114')
    browser.find_element_by_tag_name('button').click()
    CCcounter = 1
    time.sleep(1)
    while True:
        # if the input is empty, can input and submit
        # if Overtime or submited, will clear to empty
        Q1 = browser.find_element_by_id('Q1a').get_attribute("value")

        if not Q1:
            seg = browser.find_element_by_id('Q1').get_attribute(
                "value").replace(" ", "").split("|")
            q1a = seg[0] + "ntustB10707114"+seg[1]
            print("q1a =  ", q1a)
            browser.find_element_by_name('Q1a').send_keys(q1a)

            seg = browser.find_element_by_id(
                'Q2').get_attribute("value").split(" ")

            browser.find_element_by_name('Q2a').send_keys(calculate(seg=seg))

            CCcounter += 1
            if(CCcounter == 100):
                break
            browser.find_element_by_id('btnSubmit').click()


if __name__ == ("__main__"):
    main()

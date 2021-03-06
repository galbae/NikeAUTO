from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os, sys

usernamelist = ['1', '2', '3', '4'] #input your usernaem
passwordlist = ['1', '2', '3', '4'] #input your password
#ALL_DRAW_COUNT_xpath /html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[1]/span
options = webdriver.ChromeOptions()
options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options) 

for i in range(len(usernamelist)):
    driver.delete_all_cookies()
    driver.get('https://www.nike.com/kr/ko_kr/login?successUrl=/account/theDrawList')
    def login():
        
        elem = driver.find_element_by_id("j_username")
        elem.send_keys(usernamelist[i])

        elem = driver.find_element_by_id("j_password")
        elem.send_keys(passwordlist[i])

        driver.find_element_by_xpath("//button[@type='submit']").click()
        
        time.sleep(1)

    #첫번째 제품 xpath_(/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/span[2])
    #두번째 제품 xpath_(/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[2])
    #첫번째 제품 결과 xpath_(/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[1]/span[2])
    #두번째 제품 결과 xpath_(/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2])

    def infor():
        c_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[1]/span"
        c = driver.find_element_by_xpath(c_xpath)
        k = int(c.text)
        if k >= 8:
            k = 8
        else:
            k = k 
            
        name_list = [] #ITEM_NAME
        for p in range(1,k+1):
            name_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div["+str(p)+"]/div[2]/div[1]/div[2]/span[2]"
            name = driver.find_element_by_xpath(name_xpath)
            name_list.append(name.text)
        print(name_list)

        time.sleep(1)

        result_list = [] #DRAW_RESULT
        for p in range(1,k+1):
            result_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div["+str(p)+"]/div[1]/span[2]"
            result = driver.find_element_by_xpath(result_xpath)
            result_list.append(result.text)
        print(result_list)


    time.sleep(1)


    def logout():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

        posting = driver.find_element_by_xpath('/html/body/footer/div/div[1]/div/div/p[4]/a')
        posting.click()
        #driver.close()

    login()
    infor()
    logout()

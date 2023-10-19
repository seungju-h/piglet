from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

url = "https://www.safe182.go.kr/home/lcm/lcmMssList.do"

service = webdriver.chrome.service.Service("../chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(url)

# time.sleep(10)

# page_text = driver.find_element(By.TAG_NAME, 'body').text
#
# with open('webpage_text.txt', 'w', encoding='utf-8') as text_file:
#     text_file.write(page_text)
#
# img_elements = driver.find_elements(By.CLASS_NAME, 'img-responsive')
# img_counter = 1
# for img_element in img_elements:
#     img_url = img_element.get_attribute('src')
#     if img_url and "blobImgView.do?msspsnIdntfccd" in img_url:
#         base_url = "https://www.safe182.go.kr"
#         full_img_url = base_url + img_url
#         img_data = requests.get(full_img_url).content
#         with open(f'img_{img_counter}.jpg', 'wb') as img_file:
#             img_file.write(img_data)
#         img_counter += 1
#
# driver.quit()

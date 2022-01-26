from selenium import webdriver
import cv2
import numpy as np
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("C:\\Programming\\chromedriver\\chromedriver.exe")
browser.maximize_window()
browser.get("https://www.teamliquid.com/")

# Element to be saved
time.sleep(5)
element = browser.find_element(By.XPATH, '/html/body/header/div/div/div/div/div[1]/div/a/img')

png = browser.get_screenshot_as_png()
location = element.location
size = element.size

nparr = np.frombuffer(png, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

left = location['x']
top = location['y']
right = location['x'] + 1.8*size['width']
bottom = location['y'] + 2*size['height']

# im = img[left:right, top:bottom]
im = img[top:int(bottom), left:int(right)]
cv2.imwrite('filename.png', im)

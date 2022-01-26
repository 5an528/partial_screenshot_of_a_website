from selenium import webdriver
from PIL import Image
from io import BytesIO

from selenium.webdriver.common.by import By

browser = webdriver.Chrome("C:\\Programming\\chromedriver\\chromedriver.exe")
browser.maximize_window()
browser.get("https://www.yahoo.com/")

# now that we have the preliminary stuff out of the way time to get that image :D
element = browser.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div/div/div[3]/div/div[1]/a/img[1]") # find part of the page you want image of

location = element.location
size = element.size
png = browser.get_screenshot_as_png()
browser.save_screenshot('ss.png')# saves screenshot of entire page
browser.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + 1.5*size['width']
bottom = location['y'] + 1.7*size['height']

print(left, top, right, bottom)

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('Yahoo.png') # saves new cropped image
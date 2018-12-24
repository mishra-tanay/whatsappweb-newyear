from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time 
options = Options()
options.add_argument("user-data-dir=/tmp/tanay")

# Replace below path with the absolute path 
# to chromedriver in your computer

driver = webdriver.Chrome('chromedriver',chrome_options=options)
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 100)
print("Whatsapp connected")
prev="1"
while True:
    element1 = driver.find_elements_by_xpath('//*[@id="main"]/header/div[2]/div[1]')
    if(len(element1)>0):
        target=element1[0].text     
        a=target.split(' ')
        reciever=a[0]
        image = Image.open('w.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('Charm-Regular', size=32)
        font2= ImageFont.truetype('Acme-Regular', size=26)
        (x, y) = (50, 50)
        message = "Wishing " + reciever.upper() + " and Family "
        color = 'rgb(255,58,249)'
        draw.text((x, y), message, fill=color, font=font)
        message="a very Happy New Year "
        (x, y) = (60, 87)
        draw.text((x, y), message, fill=color, font=font)
        (x,y) =(50,132)
        message="May Light always surround you"
        draw.text((x, y), message, fill=color, font=font)
        (x, y) = (500,300)
        name = ' - - - Tanay Mishra'
        color = 'rgb(18, 20, 234)' 
        draw.text((x, y), name, fill=color, font=font2)
        image.save('g.png')        
        if(target!=prev):
            driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span').click()
            element =driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input')
            element.send_keys("D:\greetings\g.png")
            time.sleep(5)
            prev=target
            '''string = "Hello How are you " +reciever
            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            message.send_keys(string)
            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()'''
            
            #print(target)
            
    

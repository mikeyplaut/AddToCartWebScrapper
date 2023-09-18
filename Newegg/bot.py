import time
import os.path
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from playsound import playsound

#import info

# make sure this path is correct
PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"

audio_file = os.path.dirname(__file__) + '//chime.wav'

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(executable_path=PATH, options=chrome_options)
#browser = webdriver.Chrome(PATH)

#url = "https://www.newegg.com/p/N82E16824012040"
url = "https://www.newegg.com/p/N82E16824012015?Description=monitor&cm_re=monitor-_-24-012-015-_-Product"
browser.get(url)

readyToBuy = False

while not readyToBuy:

    try:
        #if this works then the button is not readyToBuy
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-message")
        
        #button isnt open restart script
        print("Button isn't ready! - Newegg")
        
        #Refresh page after delay
        time.sleep( random.randrange(30,60) )
        browser.refresh()
        
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        
        id = browser.find_element_by_xpath("//li/em")
        #Click the button and end the script
        #addToCartBtn.click()
        #addToCartLink = addToCartBtn.get_attribute('href')
        print("ITEM FOUND! ITEM FOUND! - Newegg")
		
        readyToBuy = True

addToCartLink = "https://secure.newegg.com/Shopping/AddtoCart.aspx?Submit=ADD&ItemList=" + id.text
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(addToCartLink)
playsound(audio_file)
playsound(audio_file)
browser.quit()

		
		



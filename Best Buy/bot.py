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
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")

browser = webdriver.Chrome(executable_path=PATH, options=chrome_options)
#browser = webdriver.Chrome(PATH)

#url = "https://www.bestbuy.com/site/gigabyte-28-led-uhd-freesync-monitor-with-hdr-hdmi-displayport-usb-ss-ips-display/6465953.p?skuId=6465953"
url = "https://www.bestbuy.com/site/samsung-t350-series-lf24t350fhnxza-24-ips-led-fhd-freesync-4ms-hdmi-dark-blue-gray/6420870.p?skuId=6420870"
browser.get(url)

readyToBuy = False

while not readyToBuy:

    try:
        #if this works then the button is not readyToBuy
        addToCartBtn = addButton = browser.find_element_by_class_name("c-button-disabled")
        
        #button isnt open restart script
        print("Button isn't ready! - BB")
        
        #Refresh page after delay
        time.sleep( random.randrange(1,3) )
        browser.refresh()
        
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("c-button-primary")
        skuId = browser.find_element_by_xpath("//span/strong[contains(text(), 'SKU')]//parent::span//following-sibling::span")
        #Click the button and end the script
        #addToCartBtn.click()
        print("Item added to cart! - BB")
        readyToBuy = True
		
addToCartLink = "https://api.bestbuy.com/click/-/" + skuId.text + "/cart"
print(addToCartLink)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(addToCartLink)
playsound(audio_file)
playsound(audio_file)
browser.quit()
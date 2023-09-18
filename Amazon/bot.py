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

browser = webdriver.Chrome(executable_path=PATH, options=chrome_options)
#browser = webdriver.Chrome(PATH)

link = "https://www.amazon.com/sm/dp/B09C43DLXG?smid=ATVPDKIKX0DER&tag=data20-20&aod=1&linkCode=osi&th=1&psc=1"

link1 = "https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_2?dchild=1&keywords=montir&qid=1633392938&sr=8-2"
browser.get(link1)

readyToBuy = False

while not readyToBuy:

    try:
        #if this works then the button is not readyToBuy
        addToCartBtn = addButton = browser.find_element_by_id("buybox-see-all-buying-choices")
        
        #button isnt open restart script
        print("Button isn't ready! - Amazon")
        
        #Refresh page after delay
        time.sleep(1)
        browser.refresh()
        
    except:
        addToCartBtn = addButton = browser.find_element_by_id("add-to-cart-button")
        
        asin = browser.find_element_by_xpath("//th[contains(text(),'ASIN')]//following-sibling::td")
        
        #Click the button and end the script
        #addToCartBtn.click()
        print("ITEM FOUND! ITEM FOUND! - Amazon")
        readyToBuy = True
		
addToCartLink = "http://www.amazon.com/gp/aws/cart/add.html?&ASIN.1=" + asin.text +"&Quantity.1=1"
print(addToCartLink)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(addToCartLink)
playsound(audio_file)
playsound(audio_file)
browser.quit()
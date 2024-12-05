from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British2English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.ID, value="sprachwahl"))
ButtonSelection.select_by_visible_text("British English / Brian")

def Speak(*args):
    Text =""
    for i in args:
        Text+=i
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI: {Text}.")
        print("")
        Data = str(Text)
        driver.find_element(By.ID, "voicetext").send_keys(Data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        driver.find_element(By.ID, "voicetext").click()
        if lengthoftext >= 30:
            sleep(7)
        elif lengthoftext >= 40:
            sleep(8)
        elif lengthoftext >= 55:
            sleep(12)
        elif lengthoftext >= 70:
            sleep(14)
        elif lengthoftext >= 100:
            sleep(16)
        elif lengthoftext >= 120:
            sleep(18)
        else:
            sleep(2)

Speak("Hi my name is Jarvis")
        

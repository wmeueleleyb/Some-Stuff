from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

bot = webdriver.Firefox()
bot.get("http://www.typeracer.com")
time.sleep(3)
START = bot.find_element_by_link_text("Enter a typing race")
START.click()
time.sleep(15)

TEXT1 = bot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]").text
TEXT2 = bot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]").text
TEXT3 = bot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]").text
INPUT = TEXT1 + TEXT2 + " " + TEXT3

for i in INPUT:
    bot.find_element_by_tag_name('body').send_keys(i)
    time.sleep(0.1)

#you can adjust the time delay inside the for loop to increase or decrease the typing speed of the bot
#to give you an idea a delay of 0.1 gives typing speeds a little over 100 wpm and 0.15 will give around 60 or 70wpm.

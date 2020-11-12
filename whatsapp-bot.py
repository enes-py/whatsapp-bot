from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import asyncio

async def send_msg():

    print("")

    target_input = input(" Who should receive the message? » ")

    target = f'"{target_input}"'

    msg_content = input(" Which message do you want to send? » ")

    send_time = input(" Time to send message (HH:MM:SS) » ")

    while True:
        time_str = time.strftime("%H:%M:%S")
        if time_str == send_time:

            x_arg = '//span[contains(@title,' + target + ')]'

            group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()

            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            message.send_keys(msg_content)

            send = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            send.click()
            break

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_msg())
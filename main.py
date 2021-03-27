from selenium.webdriver import Chrome
from time import sleep
from random import randint, random
from winsound import Beep
from loguru import logger


options = {
    "login": "*************",
    "password": "***************",
    "center": "Poland Visa Application Center-Minsk",
    "category": "D-visa",
    "sub_category": "National D-visa",
    "reset_category": "Poland Visa Application Center-Mogilev"
}


driver = Chrome()
driver.get("https://visa.vfsglobal.com/blr/en/pol/login")
logger.info("open site")

sleep(randint(5, 8) + random())
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/button[2]").click()
logger.info("skip cookie message")

user_name = driver.find_element_by_xpath(
    "/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[1]/mat-form-field/div/div[1]/div[3]/input"
)
password = driver.find_element_by_xpath(
    "/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[2]/mat-form-field/div/div[1]/div[3]/input"
)
submit = driver.find_element_by_xpath("/html/body/app-root/div/app-login/section/div/div/mat-card/form/button")

sleep(randint(3, 5) + random())
user_name.send_keys(options['login'])
sleep(randint(3, 5) + random())
password.send_keys(options['password'])
logger.info("set login and password")

sleep(randint(3, 5) + random())
submit.click()
logger.info("click login button")

sleep(randint(3, 5) + random())
driver.find_element_by_xpath("/html/body/app-root/div/app-dashboard/section/div/div[2]/button/span").click()
logger.info("open modal window for booking")

centre = driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]/mat-select")
category = driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]/div[3]/mat-select")
sub_category = driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]/mat-select")

count = 1
while True:
    logger.warning(f"try to booking {count=}")
    sleep(randint(3, 5) + random())
    centre.send_keys(options['center'])

    sleep(randint(3, 5) + random())
    category.send_keys(options['category'])

    sleep(randint(3, 5) + random())
    sub_category.send_keys(options['sub_category'])

    sleep(random())
    continue_btn = driver.find_element_by_xpath("/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button")
    if continue_btn.is_enabled():
        logger.error("continue button is enable!!!!")
        break
    logger.warning("continue button is dissable")
    count += 1
    centre.send_keys(options['reset_category'])
    sleep(300 + random())


continue_btn.click()
logger.error("we have the slot!!!!")
while True:
    sleep(0.2)
    Beep(1000, 1000)

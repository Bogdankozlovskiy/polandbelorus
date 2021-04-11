from selenium.webdriver import Firefox
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint, random
from utils import add_applicate, init_driver, get_centre_category_sub_category
from winsound import Beep
from loguru import logger


options = {
    "login": "*************",
    "password": "**********",
    "center": "Poland Visa Application Center-Minsk",
    "category": "D-visa",
    "sub_category": "National D-visa",
    "reset_category": "Poland Visa Application Center-Mogilev",
    "applicatest":[
        {
            "name": "Bahdan",
            "last_name": "Kazlouski",
            "gender": "Male",
            "date_born": "***********",
            "nationality": "BELARUS",
            "passport_number": "*********",
            "expare_date": "*************",
            "code_phone": "44",
            "phone_number": "************",
            "email": "*******************"
        }
    ]    
}


driver = init_driver(logger, options)
centre, category, sub_category = get_centre_category_sub_category(driver)
count = 1
while True:
	try:
	    logger.warning(f"try to booking {count=}")
	    sleep(randint(3, 5) + random())
	    centre.send_keys(options['center'])

	    sleep(randint(3, 5) + random())
	    category.send_keys(options['category'])

	    sleep(randint(5, 8) + random())
	    sub_category.send_keys(options['sub_category'])

	    sleep(random())
	    continue_btn = driver.find_element_by_xpath(
	        "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button"
	    )
	    if continue_btn.is_enabled():
	        logger.warning("continue button is enable")
	        break

	    logger.warning("continue button is dissable")
	    centre.send_keys(options['reset_category'])
	    sleep(100 + randint(0, 15) + random())
	    count += 1
	    try:
	        driver.find_element_by_css_selector(
	            "div.col-12:nth-child(2) > button:nth-child(1)"
	        ).click()
	    except NoSuchElementException:
	        pass
	    else:
	        logger.warning("close disconnect button")
	except Exception as e:
		driver.close()
		logger.critical(e.__str__())
		sleep(300 + randint(0, 20) + random())
		logger.critical("reinit driver")
		driver = init_driver(logger, options)
		centre, category, sub_category = get_centre_category_sub_category(driver)

logger.warning("we have the slot")
continue_btn.click()


while True:
    sleep(0.2)
    Beep(1000, 1000)

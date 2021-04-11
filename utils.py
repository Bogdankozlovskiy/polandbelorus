from time import sleep
from random import random, randint
from selenium.webdriver import Firefox


def init_driver(logger, options):
    driver = Firefox()
    driver.get("https://visa.vfsglobal.com/blr/en/pol/login")
    logger.info("open site")

    sleep(randint(5, 8) + random())
    driver.find_element_by_css_selector("#onetrust-accept-btn-handler").click()
    logger.info("skip cookie message")

    user_name = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[1]/mat-form-field/div/div[1]/div[3]/input"
    )
    password = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[2]/mat-form-field/div/div[1]/div[3]/input"
    )
    submit = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-login/section/div/div/mat-card/form/button"
    )

    sleep(randint(3, 5) + random())
    for letter in options['login']:
        user_name.send_keys(letter)
        sleep(random())
    for letter in options['password']:
        password.send_keys(letter)
        sleep(random())
    logger.info("set login and password")
    submit.click()
    logger.info("click login button")

    sleep(randint(3, 5) + random())
    driver.find_element_by_xpath(
        "/html/body/app-root/div/app-dashboard/section/div/div[2]/button/span"
    ).click()
    logger.info("open modal window for booking")
    return driver


def get_centre_category_sub_category(driver):
    centre = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-eligibility-criteria/section/form/"
        "mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]/mat-select"
    )
    category = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]"
        "/form/div[2]/mat-form-field/div/div[1]/div[3]/mat-select"
    )
    sub_category = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]"
        "/form/div[3]/mat-form-field/div/div[1]/div[3]/mat-select"
    )
    return centre, category, sub_category


def add_applicate(driver, data):
    sleep(3 + random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/"
        "mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[2]"
        "/div/div/div/app-input-control/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['name']:
        tmp.send_keys(letter)
        sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]"
        "/form/app-dynamic-form/div/div/app-dynamic-control[3]/div/div/div"
        "/app-input-control/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['last_name']:
        tmp.send_keys(letter)
        sleep(random())
    driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[4]/div/div[1]/div/"
        "app-dropdown/div/mat-form-field/div/div[1]/div[3]/mat-select"
    ).send_keys(data['gender'])
    sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[4]/div/div[2]/div/app-ngb-datepicker/div/div[2]/input"
    )
    for letter in data['date_born']:
        tmp.send_keys(letter)
        sleep(random())
    driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[5]/div/div/div/app-dropdown"
        "/div/mat-form-field/div/div[1]/div[3]/mat-select"
    ).send_keys(data['nationality'])
    sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[6]/div/div[1]/div/"
        "app-input-control/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['passport_number']:
        tmp.send_keys(letter)
        sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[6]/div/div[2]/div/app-ngb-datepicker/div/div[2]/input"
    )
    for letter in data['expare_date']:
        tmp.send_keys(letter)
        sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]"
        "/form/app-dynamic-form/div/div/app-dynamic-control[9]/div/div/div[2]"
        "/div[1]/app-input-control/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['code_phone']:
        tmp.send_keys(letter)
        sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/"
        "form/app-dynamic-form/div/div/app-dynamic-control[9]/div/div/div[2]"
        "/div[2]/app-input-control/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['phone_number']:
        tmp.send_keys(letter)
        sleep(random())
    tmp = driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form"
        "/app-dynamic-form/div/div/app-dynamic-control[10]/div/div/div/app-input-control"
        "/div/mat-form-field/div/div[1]/div[3]/input"
    )
    for letter in data['email']:
        tmp.send_keys(letter)
        sleep(random())
    driver.find_element_by_xpath(
        "/html/body/app-root/div/app-applicant-details/section/mat-card[2]/app-dynamic-form"
        "/div/div/app-dynamic-control/div/div/div[2]/button"
    ).click()
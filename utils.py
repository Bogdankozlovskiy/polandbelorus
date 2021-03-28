def add_applicate(data):
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
    ).send_keys(data['passport_number'])
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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AJIOSite:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ajio.com/")
        self.driver.find_element(By.XPATH, "//span[text()='Sign In / Join AJIO']").click()

    def login(self, email, password):
        self.driver.find_element(By.NAME, "username").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@class='login-btn']").click()
        self.driver.find_element(By.XPATH, "//input[@type='button']").click()
        self.driver.find_element(By.ID, "pwdInput").send_keys(password)

        time.sleep(20)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

class AJIOLogin(AJIOSite):
    def __init__(self, driver):
        super().__init__(driver)

    def ele(self):
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Sign Innnn / Join AJIO']").click()
        except:
            print("Invalid xpath")


driver = webdriver.Chrome()

ajio_login = AJIOLogin(driver)
while True:
    print("Enter 1 for login")
    print("Enter 2 for exceptional handling")
    print("Enter 3 to exit")
    choice = int(input())
    if choice == 1:
        ajio_login.login("rmyaduvanshi2@gmail.com", "Rahul123@")
    elif choice == 2:
        ajio_login.ele()
    elif choice ==3:
        quit()
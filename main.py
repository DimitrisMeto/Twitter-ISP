from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/dimitris/Development/chromedriver"
TWITTER_EMAIL = "yukimetochianaki@gmail.com"
TWITTER_PASSWORD = os.environ.get("PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path, driver_options):
        self.driver = webdriver.Chrome(service=Service(driver_path), options=driver_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        time.sleep(3)
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        time.sleep(2)

        go_button = self.driver.find_element(By.XPATH,
                                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH,
                                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(3)
        email = self.driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe")
        username.send_keys("YukiMeto22")
        username.send_keys(Keys.ENTER)

        time.sleep(2)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input.r-30o5oe')
        password = inputs[1]
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        cookie_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        cookie_button.click()

        time.sleep(2)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(2)
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
        tweet_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)
        tweet_adds = self.driver.find_elements(By.CSS_SELECTOR, 'div.css-18t94o4')
        for tweet_add in tweet_adds:
            if tweet_add.get_attribute("data-testid") == "tweetButton":
                tweet_add.click()
                time.sleep(2)
                self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(driver_path=CHROME_DRIVER_PATH, driver_options=options)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()











# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait


class TestWwww():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://onecwms.xmrbi.com/#/login?redirect=%2Foresmineralcheckout%2Fcheckout")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/form/div[1]/div/div/input").send_keys('admin')
        self.driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/form/div[2]/div/div/input").send_keys('admin!123\n')
        self.vars = {}

    def teardown(self):
        self.driver.quit()


    def test_wwww(self):
        pass
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable())
        # self.driver.close()


if __name__ == '__main__':
    pytest.main(['-v','test_selenium'])

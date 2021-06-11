import inspect
import logging
import string
import random

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("setup")
class BaseClass:

    def click1(self,by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", ele)

    def click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def clear(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clickAndSendText(self,by_locator,text):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ele.click()
        ele.send_keys(text)

    def getText(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def hoverToElement(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def hoverAndClick(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    @staticmethod
    def random_generatorString(size=3, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for x in range(size))

    @staticmethod
    def random_generatordigits(size=8, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @staticmethod
    def random_digits(size=3, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))



    @staticmethod
    def getLogger():
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # file handler object (File location)
        logger.setLevel(logging.DEBUG)
        return logger





import pytest
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from selenium import webdriver

@pytest.fixture()
def setup(request):
    url = ReadConfig.getApplicationURL()
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--start-maximized")
    chrome_option.add_experimental_option('excludeSwitches',['enable-logging'])
    chrome_option.add_argument('--disable-notifications')
    chrome_option.add_argument("--ignore-certifcate-errors")
    driver = webdriver.Chrome(executable_path="D:\driver\chromedriver.exe",options=chrome_option)
    driver.implicitly_wait(10)
    driver.get(url)
    #driver.find_element(By.XPATH,"//a[text()='Smart Water Subscription']").click()
    request.cls.driver = driver
    yield
    driver.quit()







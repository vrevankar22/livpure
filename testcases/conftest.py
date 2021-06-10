import pytest
from utilities.readProperties import ReadConfig
from selenium import webdriver

@pytest.fixture()
def setup(request):
    url = ReadConfig.getApplicationURL()

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--start-maximized")
    chrome_option.add_experimental_option('excludeSwitches',['enable-logging'])
    chrome_option.add_argument('--disable-notifications')
    driver = webdriver.Chrome(executable_path="D:\driver\chromedriver.exe",options=chrome_option)
    driver.implicitly_wait(10)
    driver.get(url)
    request.cls.driver = driver
    yield
    #driver.close()






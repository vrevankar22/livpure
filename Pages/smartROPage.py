import time

from selenium.webdriver.common.by import By

from Locators.smartWaterSubscription import SignUpPage
from utilities import XLUtils
from utilities.BaseClass import BaseClass
from Locators.smartRO import smartRO
from utilities.XLUtils import excel


class smartROPage(BaseClass):

    def redirectTOSmartRO(self):
        self.click(smartRO.smartROlink)

    def login(self, email, password):
        self.click(SignUpPage.loginBtn)
        self.send_keys(SignUpPage.loginUN, email)
        self.send_keys(SignUpPage.loginPWD, password)
        self.click(SignUpPage.submitLoginBtn)

# verify SmartRO landing page
    def verify_SmartROlandingPage(self):
        pass

# Sign up into SmartRO with valid details
    def signUp_smartRO(self,password,smartROPlan):
        log = self.getLogger()
        self.redirectTOSmartRO()
        username = "Test_" + self.random_generatorString()
        email = 'ro' + self.random_generator() + "@gmail.com"
        mobile = "95" + self.random_generatordigits()
        XLUtils.writeData(excel, 'SmartRO', 2,1, username)
        XLUtils.writeData(excel, 'SmartRO', 2,2, email)
        XLUtils.writeData(excel, 'SmartRO', 2,3, mobile)
        self.click(smartRO.subscribeNow)
        self.clickAndSendText(SignUpPage.yourNameTxtBox, username)
        self.clickAndSendText(SignUpPage.emailTxtBox, email)
        self.clickAndSendText(SignUpPage.mobileTxtBox, mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        self.clickAndSendText(SignUpPage.passwordTxtBox,password)
        self.click1(smartRO.signUpBtn)
        planname = self.getText(smartRO.smartBuyPlan)
        assert planname == smartROPlan, 'Does not redirect to smart buy plan page'
        log.info('Redirected to smart buy plan page')

# Login into the account and verify the customer dashboard, plan details, Recharge History
    def verify_profileTabs(self,email,password,name,phoneNo,smartROPlan):
        log = self.getLogger()
        self.redirectTOSmartRO()
        self.login(email,password)
        self.click(SignUpPage.menu_profileLink)
        # Customer Dashboard
        username = self.getText(smartRO.username)
        assert name in username,'Registered name not displayed in dashboard'
        log.info('Registered name displayed in dashboard')
        assert self.driver.find_element(By.XPATH,"//p[text()='Email: "+email+"']").is_displayed(),'incorrect email'
        log.info('Email displayed in customer dashboard')
        assert self.driver.find_element(By.XPATH,"//p[text()='Phone No: "+str(phoneNo)+"']").is_displayed(),'incorrect phone No'
        log.info('Phone No displayed in customer dashboard')
        # verify subscribe plan message displays for not paid account
        msg = self.getText(smartRO.subscribeMsg)
        assert msg == 'Please subscribe a plan to enjoy the services!', 'subscribe a plan message not displayed'
        log.info('subscribe a plan message displayed')
        self.click(smartRO.subscribeNow)
        planname = self.getText(smartRO.smartBuyPlan)
        assert planname == smartROPlan,'Does not redirect to smart buy plan page'
        log.info('Redirected to smart buy plan page')

        # Plan details
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.planDetailsTab)
        planalertmessage = self.getText(smartRO.planalertmsg)
        assert 'not subscribed any plan' in planalertmessage,'You have not subscribed any plan message not displayed'
        log.info('You have not subscribed any plan message displayed')
        self.click(smartRO.plansubscribe)
        assert planname == smartROPlan, 'Does not redirect to smart buy plan page'
        log.info('Redirected to smart buy plan page')

        # Recharge History
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.rechargeHisTab)
        histalertmessage = self.getText(smartRO.rechHisalert)
        assert 'not subscribed any plan' in histalertmessage, 'You have not subscribed any plan message not displayed'
        log.info('You have not subscribed any plan message displayed')

#  verify zinger smart plan details
    def verify_smartBuyplan(self,email,password,downpayment,monthinstall,duration,payrs):
        log = self.getLogger()
        self.redirectTOSmartRO()
        self.login(email,password)
        downpay = self.getText(smartRO.downpayment)
        assert str(downpayment) in downpay,'Incorrect Downpayment'
        log.info('Displayed correct Downpayment')
        monthlyInstall = self.getText(smartRO.monthlyinstall)
        assert str(monthinstall) in monthlyInstall, 'Incorrect monthly Install amount'
        log.info('Displayed correct monthly Install amount')
        period = self.getText(smartRO.duration)
        assert str(duration) in period, 'Incorrect duration'
        log.info('Displayed correct duration')
        pay = self.getText(smartRO.payBtn)
        assert str(payrs) in pay, 'Incorrect rupees displayed in pay rs button'
        log.info('Displayed correct rupees in pay rs button')

# make the payment
    def verify_completePayment(self,email,password):
        log = self.getLogger()
        self.redirectTOSmartRO()
        self.login(email,password)
        self.click(smartRO.payBtn)





















import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from utilities.XLUtils import *
from utilities import XLUtils
from Locators.smartAC import smartAC
from Locators.smartWaterSubscription import SignUpPage

class smartACPage(BaseClass):

    def redirectTOSmartAC(self):
        self.click(smartAC.smartAClink)

    def login(self, email, password):
        self.click(SignUpPage.loginBtn)
        self.send_keys(SignUpPage.loginUN, email)
        self.send_keys(SignUpPage.loginPWD, password)
        self.click(SignUpPage.submitLoginBtn)

# Verify Landing Page
    def verify_AClandingPage(self):
        pass

# Sign up into SmartAC with valid details
    def signUp_smartAC(self,password,smartACPlan):
        log = self.getLogger()
        self.redirectTOSmartAC()
        username = "Test_" + self.random_generatorString()
        email = 'ac' + self.random_generator() + "@gmail.com"
        mobile = "67" + self.random_generatordigits()
        XLUtils.writeData(excel, 'SmartAC', 2, 1, username)
        XLUtils.writeData(excel, 'SmartAC', 2, 2, email)
        XLUtils.writeData(excel, 'SmartAC', 2, 3, mobile)
        self.click(smartAC.smartBuyNow)
        self.clickAndSendText(SignUpPage.yourNameTxtBox, username)
        self.clickAndSendText(SignUpPage.emailTxtBox, email)
        self.clickAndSendText(SignUpPage.mobileTxtBox, mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        self.clickAndSendText(SignUpPage.passwordTxtBox, password)
        self.click1(smartAC.acSignUp)
        planname = self.getText(smartAC.ACPlan)
        assert smartACPlan in planname, 'Does not redirect to smart buy AC plan page'
        log.info('Redirected to smart buy AC plan page')

# Login into the account and verify the customer dashboard, plan details, Recharge History
    def verify_ACprofileTabs(self,email,password,name,phoneNo,smartACPlan):
        log = self.getLogger()
        self.redirectTOSmartAC()
        self.login(email,password)
        self.click(SignUpPage.menu_profileLink)
        # Customer Dashboard
        username = self.getText(smartAC.username)
        assert name in username,'Registered name not displayed in dashboard'
        log.info('Registered name displayed in dashboard')
        assert self.driver.find_element(By.XPATH,"//p[text()='Email: "+email+"']").is_displayed(),'incorrect email'
        log.info('Email displayed in customer dashboard')
        assert self.driver.find_element(By.XPATH,"//p[text()='Phone No: "+str(phoneNo)+"']").is_displayed(),'incorrect phone No'
        log.info('Phone No displayed in customer dashboard')
        # verify subscribe plan message displays for not paid account
        msg = self.getText(smartAC.subscribeMsg)
        assert msg == 'Please subscribe a plan to enjoy the services!', 'subscribe a plan message not displayed'
        log.info('subscribe a plan message displayed')
        self.click(smartAC.subscribeNow)
        planname = self.getText(smartAC.ACPlan)
        assert smartACPlan in planname, 'Does not redirect to smart buy AC plan page'
        log.info('Redirected to smart buy AC plan page')

        # Payment details
        self.click(SignUpPage.menu_profileLink)
        self.click(smartAC.paymentDetails)
        planalertmessage = self.getText(smartAC.planalertmsg)
        assert 'not subscribed any plan' in planalertmessage,'You have not subscribed any plan message not displayed'
        log.info('You have not subscribed any plan message displayed')
        self.click(smartAC.plansubscribe)
        assert smartACPlan in planname, 'Does not redirect to smart buy AC plan page'
        log.info('Redirected to smart buy AC plan page')

        # Payment History
        self.click(SignUpPage.menu_profileLink)
        self.click(smartAC.paymentHistory)
        histalertmessage = self.getText(smartAC.rechHisalert)
        assert 'not subscribed any plan' in histalertmessage, 'You have not subscribed any plan message not displayed'
        log.info('You have not subscribed any plan message displayed')

#  verify AC smart plan details
    def verify_ACsmartBuyplan(self,email,password,downpayment,monthinstall,duration,payrs):
        log = self.getLogger()
        self.redirectTOSmartAC()
        self.login(email,password)
        downpay = self.getText(smartAC.downpayment)
        assert str(downpayment) in downpay,'Incorrect Downpayment'
        log.info('Displayed correct Downpayment')
        monthlyInstall = self.getText(smartAC.monthlyinstall)
        assert str(monthinstall) in monthlyInstall, 'Incorrect monthly Install amount'
        log.info('Displayed correct monthly Install amount')
        period = self.getText(smartAC.duration)
        assert str(duration) in period, 'Incorrect duration'
        log.info('Displayed correct duration')
        pay = self.getText(smartAC.payBtn)
        assert str(payrs) in pay, 'Incorrect rupees displayed in pay rs button'
        log.info('Displayed correct rupees in pay rs button')

# Login and fill installation address
    def verify_AcinstallationAddress(self,email,password,username,mobile):
        # Install Address
        log = self.getLogger()
        self.redirectTOSmartAC()
        self.login(email,password)
        self.click(smartAC.payBtn)
        IAddpersonName = self.getText(SignUpPage.personName)
        IAddpersonEmail = self.getText(SignUpPage.personEmail)
        IAddpersonMobile = self.getText(SignUpPage.personMobile)
        assert username == IAddpersonName, "Incorrect username"
        log.info("Username displayed correctly in installation address page")
        assert email == IAddpersonEmail, "Incorrect email"
        log.info("Email displayed correctly in installation address page")
        assert mobile == IAddpersonMobile, "Incorrect mobile"
        log.info("Mobile number displayed correctly in installation address page")
        self.clickAndSendText(SignUpPage.addressLine1, 101)
        self.clickAndSendText(SignUpPage.addressLine2, 'HAL')
        self.click(SignUpPage.areaDropdown)
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,"//div[text()='Please enter a valid pincode.']").is_displayed(), 'Enter valid code message not displayed'
        log.info("Enter valid code message displayed")
        time.sleep(2)
        self.clickAndSendText(SignUpPage.pincode,'560008')
        self.click(SignUpPage.areaDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='v-list-item__content']//div[text()='BANGALORE NORTH']").click()
        self.click1(SignUpPage.IAddcityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        time.sleep(8)
        self.click1(SignUpPage.altmobileNumBox)
        self.click1(SignUpPage.altmobileNo)
        self.send_keys(SignUpPage.altmobileNo, '9856231452')
        self.click1(SignUpPage.saveAndContinueBtn)
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//span[text()='Review & Pay']").is_displayed(), "Reveiew and Pay page deos not display"
        log.info("Reveiew and Pay page displayed")
        time.sleep(5)


# verify installation address in review and pay and edit address
    def verify_editAddress(self,email, password,cityName):
        log = self.getLogger()
        self.redirectTOSmartAC()
        self.login(email,password)
        self.click(smartAC.payBtn)
        for i in range(1,5):
            addresstext = self.getText((By.XPATH,"(//div[@class='flex flex-column installation-address-wrapper']//span[@class='review-address-text'])["+str(i)+"]"))
            text = XLUtils.readData(excel,'SmartAC',5,i)
            assert addresstext == text, 'Address not displayed in Review and pay page'
            log.info('Address displayed in review and pay page {} == {}'.format(addresstext,text))
        self.click(SignUpPage.editaddress)
        self.click1(SignUpPage.IAddcityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Delhi']").click()
        self.click1(SignUpPage.saveAndContinueBtn)
        assert self.driver.find_element(By.XPATH,"//span[@class='review-address-text'][contains(.,'"+cityName+"')]").is_displayed(),'Address not edited'
        log.info('Address edited successfully')

# verify Pay details from Review and Pay page
    def verify_ReviewAndPay(self,email,password,downpayment,acplan,msg1,msg2):
        log = self.getLogger()
        self.redirectTOSmartAC()
        self.login(email,password)
        self.click(smartAC.payBtn)
        step1msg = self.getText(smartAC.step1)
        assert str(downpayment) in step1msg,'Incorrect downpayment displayed'
        log.info('Downpayment displayed')
        planname = self.getText(smartAC.acplanname)
        assert acplan in planname,'Plan name not displayed'
        log.info('Plan name displayed')
        plandetailsmsg = self.getText(smartAC.acplandetails)
        assert msg1 and msg2 in plandetailsmsg,'plandetails not displayed'
        log.info('Plan details displayed')
        window_before = self.driver.window_handles[0]
        self.click(smartAC.termsAndCondilink)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert self.driver.find_element(By.XPATH,"//h2[text()='TERMS & CONDITIONS']").is_displayed(),'Not redirected to Terms and Condiation page'
        log.info('Terms and Condiation page displayed')
        self.driver.close()
        self.driver.switch_to.window(window_before)





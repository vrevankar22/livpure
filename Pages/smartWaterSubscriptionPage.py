from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from Locators.smartWaterSubscription import SignUpPage
from utilities.BaseClass import BaseClass
import time
from selenium.webdriver.common.by import By
from utilities import XLUtils
from utilities.XLUtils import *
from datetime import date


class smartWaterSubscriptionPage(BaseClass):
# Login into the account
    def login(self,email,password):
        self.click(SignUpPage.loginBtn)
        self.send_keys(SignUpPage.loginUN, email)
        self.send_keys(SignUpPage.loginPWD, password)
        self.click(SignUpPage.submitLoginBtn)

# Verify All menu link without sign up and login into the account
    def verify_menu_link(self,liter,voucher,extraVoucher):
        log = self.getLogger()
        self.click(SignUpPage.menu_planLink)
        self.click1(SignUpPage.menu_proceedToPay)
        assert self.driver.find_element(By.XPATH,"//a[text()='Sign Up']").is_displayed(),'SignUp page not displayed'
        log.info('Sign Up page displayed')
        self.click(SignUpPage.menu_HowItWorkLink)
        window_before = self.driver.window_handles[0]
        self.click1(SignUpPage.desktop_AndroidPS)
        self.driver.switch_to.window(window_before)
        self.click1(SignUpPage.desktop_ApplePS)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        android = self.driver.title
        assert 'Google Play' in android,'Google Play store not opened'
        log.info('Google Play store opened')
        window_after1 = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(window_after1)
        time.sleep(5)
        apple = self.driver.title
        assert self.driver.find_element(By.XPATH,"//a//span[text()='App Store']").is_displayed(), 'App store not opened'
        log.info('App store opened')
        self.driver.close()
        self.driver.switch_to.window(window_before)
        # need to verify refer and earn
        self.click(SignUpPage.menu_ReferEarnLink)
        try:
            self.driver.find_element(By.XPATH, "(//img[@alt='LivpureSmart Whatapp Icon'])[1]").click()
            window_after1 = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after1)
            fbTitle = self.driver.title
            assert 'Facebook' in fbTitle, 'Does not Redirect to FB page'
            log.info('Redirected to FB page')
            self.driver.close()
            self.driver.switch_to.window(window_before)
            self.click((By.XPATH,"//span[@class='close1']"))
        except NoSuchElementException:
            log.info('This smart electric Scooter refer now pop up message not displayed')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//p[@class='bannerPara']//b[contains(.,'"+str(liter)+"L free water*')]").is_displayed()
        self.driver.find_element(By.XPATH,"//p[@class='bannerPara']//b[contains(.,'"+str(voucher)+" Shopping Voucher')]").is_displayed()
        self.driver.find_element(By.XPATH,"(//b[contains(.,'"+str(extraVoucher)+"')])[1]").is_displayed()
        self.click(SignUpPage.menu_invitenow)
        window_after1 = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after1)
        fbTitle = self.driver.title
        assert 'Facebook' in fbTitle, 'Does not Redirect to FB page'
        log.info('Redirected to FB page')

# Sign up with valid details
    def SignUp(self,username,email,mobile,password):
        log = self.getLogger()
        username = "Test_" + self.random_generatorString()
        email = self.random_generator() + "@gmail.com"
        mobile = "95" + self.random_generatordigits()
        XLUtils.writeData(excel,'SignUp',2,1,username)
        XLUtils.writeData(excel,'SignUp',2,2,email)
        XLUtils.writeData(excel,'SignUp',2,3,mobile)
        self.click(SignUpPage.subscribeBtn)
        element = self.driver.find_element(By.XPATH, "//a[@class='v-tab v-tab--active']")
        elementText = element.get_attribute('aria-selected')
        if elementText == "true":
            assert True
            log.info("SignUp page selected by default")
        else:
            log.info("SignUp page not selected by default")
            self.click(SignUpPage.signUpBtn)
            assert False
        self.clickAndSendText(SignUpPage.yourNameTxtBox,username)
        self.clickAndSendText(SignUpPage.emailTxtBox,email)
        self.clickAndSendText(SignUpPage.mobileTxtBox,mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(5)
        cityList = self.driver.find_elements(By.XPATH, "//div[@class='v-list-item__content']")
        for city in cityList:
            if city.text == "Bengaluru":
                city.click()
        time.sleep(10)
        self.clickAndSendText(SignUpPage.passwordTxtBox,password)
        check_pwd_encrypt = self.driver.find_element(By.XPATH,"//*[@type='password']")
        assert check_pwd_encrypt.is_displayed(),'Password not Encrypted'
        log.info("Password displayed in encrypted form")
        self.click(SignUpPage.passwordview)
        check_pwd = self.driver.find_element(By.XPATH,"//input[@name='password'][@type='text']")
        assert check_pwd.is_displayed(),'password not displayed on view'
        log.info("Password displayed on view")
        time.sleep(10)
        ele = self.driver.find_element(By.XPATH,"//button[@type='submit']//span[contains(.,'Sign Up For 7 Days Trial')]")
        self.driver.execute_script("arguments[0].click();", ele)
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,"//span[text()='Select Plan & Duration']").is_displayed(), "Sign Up Failed"
        log.info("Signed Up successfully")


# verify mandtory field and sign up with already existed email address
    def verifyMandatoryField(self,username,email,mobile,password):
        log = self.getLogger()
        self.click(SignUpPage.subscribeBtn)
        time.sleep(5)
        self.click1(SignUpPage.submitSignUpBtn)
        time.sleep(10)
        for i in range(1,6):
            assert self.driver.find_element(By.XPATH,"(//div[text()='This information is required.'])["+str(i)+"]").is_displayed(),"Mandatory message not displayed"
            log.info("Mandatory message displayed")
        time.sleep(10)
        self.clickAndSendText(SignUpPage.yourNameTxtBox,username)
        self.clickAndSendText(SignUpPage.emailTxtBox,email)
        self.clickAndSendText(SignUpPage.mobileTxtBox,mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(5)
        cityList = self.driver.find_elements(By.XPATH, "//div[@class='v-list-item__content']")
        for city in cityList:
            if city.text == "Bengaluru":
                city.click()
        time.sleep(10)
        self.clickAndSendText(SignUpPage.passwordTxtBox,password)
        self.click1(SignUpPage.submitSignUpBtn)
        existMsg = self.getText(SignUpPage.emailexistMsg)
        assert "already registered with us" in existMsg, "Already exist message not displayed"
        log.info("already registered with us message displayed")

# Subscribe with name-spl charcater, invalid email address, invalid mobile number
    def verify_invalid_details(self):
        log = self.getLogger()
        self.click(SignUpPage.subscribeBtn)
        self.clickAndSendText(SignUpPage.yourNameTxtBox, "name@$")
        self.clickAndSendText(SignUpPage.emailTxtBox,"test@gmailcom")
        self.clickAndSendText(SignUpPage.mobileTxtBox,"456785")
        self.click1(SignUpPage.submitSignUpBtn)
        time.sleep(5)
        # name
        name = self.driver.find_element(By.XPATH,"//div[text()='Special characters are not allowed']")
        assert name.is_displayed(),"Special characters are not allowed message not displayed"
        log.info("Special characters are not allowed message displayed")
        # Email
        email = self.driver.find_element(By.XPATH, "//div[text()='Enter a valid email address.']")
        assert email.is_displayed(), "Enter a valid email address message not displayed"
        log.info("Enter a valid email address message displayed")
        # Mobile
        mobile = self.driver.find_element(By.XPATH, "//div[text()='Enter a valid mobile number.']")
        assert mobile.is_displayed(), "Enter a valid mobile number message not displayed"
        log.info("Enter a valid mobile number message displayed")

# Verify referral code diplays for not paid registered account
    def verify_referralCode(self,email,password,voucher):
        log = self.getLogger()
        self.login(email,password)
        # verify Referral code diplays for not paid registered account - In Customer dashboard
        self.click(SignUpPage.menu_profileLink)
        referralCode = self.driver.find_element(By.XPATH,"(//h2[@class='heading02 text-right'])[2]").text
        RC = referralCode.split(':')[-1]
        RCode = RC.strip()
        refCode1 = self.driver.find_element(By.XPATH, "//input[@class='RefCode']").get_attribute("value")
        assert refCode1 == RCode, 'Referral code does not show for not paid registered account'
        log.info('Referral code diplays for not paid registered account')

        # verify Referral code diplays for not paid registered account - In Refer and Earn
        self.click(SignUpPage.menu_ReferEarnLink)
        try:
            self.driver.find_element(By.XPATH, "(//img[@alt='LivpureSmart Whatapp Icon'])[3]").click()
            window_before = self.driver.window_handles[0]
            window_after1 = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after1)
            fbTitle = self.driver.title
            assert 'Facebook' in fbTitle, 'Does not Redirect to FB page'
            log.info('Redirected to FB page')
            self.driver.close()
            self.driver.switch_to.window(window_before)
            self.click((By.XPATH, "//span[@class='close1']"))
        except NoSuchElementException:
            log.info('This smart electric Scooter refer now pop up message not displayed')
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//h2[contains(.,'GET RS "+str(voucher)+" SHOPPING VOUCHER SHARE REFERRAL CODE...')])[1]").is_displayed()
        REcode = self.driver.find_element(By.XPATH, "(//h2[@class='heading02 text-center'])[1]").text
        REcode1 = REcode.split(' ')[-1]
        REC = REcode1.strip()
        assert REC == RCode, 'Referral Code not displayed in Refer and Earn Page'
        log.info('Referral Code displayed in Refer and Earn Page')

# Login, select the plan, update the installation address - Do not upload KYC Doc
    def verify_processTillkycPage(self,username,password,ltr_month,email,mobile,flatNo,street,pinCode):
        log = self.getLogger()
        self.click(SignUpPage.loginBtn)
        self.send_keys(SignUpPage.loginUN, email)
        self.send_keys(SignUpPage.loginPWD, password)
        check_pwd_encrypt = self.driver.find_element(By.XPATH, "//*[@type='password']")
        assert check_pwd_encrypt.is_displayed(), 'Password not Encrypted'
        log.info("Password displayed in encrypted form")
        time.sleep(3)
        self.click(SignUpPage.passwordview)
        check_pwd = self.driver.find_element(By.XPATH, "//input[@name='password'][@type='text']")
        assert check_pwd.is_displayed(), 'password not displayed on view'
        log.info("Password displayed on view")
        time.sleep(10)
        self.click(SignUpPage.submitLoginBtn)
        self.click(SignUpPage.menu_profileLink)
        self.driver.find_element(By.XPATH,"//label[text()='Please subscribe a plan to enjoy the services!']").is_displayed()
        self.click((By.XPATH,"//a[text()='Subscribe Now']"))
        self.click(SignUpPage.silverPlanTab)
        ltrsPerMonth = self.getText(SignUpPage.silverltrs)
        assert str(ltr_month) in ltrsPerMonth, "liters per month value not displayed"
        log.info("liters per month value displayed")
    # Select the 1 month plan
        self.click(SignUpPage.silver6_radio)
        price = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabsilver'][@data-duration='6']//div[@class='price-month']//span[1])[1]").text
        actprice = ''
        for val in price:
            if val.isdigit():
                actprice = actprice + val
        months = self.driver.find_element(By.XPATH,"//button[@data-parent='tabsilver'][@data-duration='6']//p//span[1]").text
        finalValue = int(actprice) * int(months)
        log.info("Actualprice {},{},{}".format(actprice, months, finalValue))
        self.click1(SignUpPage.proceedToPaySilver)
        time.sleep(5)
    # Install Address
        IAddpersonName = self.getText(SignUpPage.personName)
        IAddpersonEmail = self.getText(SignUpPage.personEmail)
        IAddpersonMobile = self.getText(SignUpPage.personMobile)
        assert username == IAddpersonName, "Incorrect username"
        log.info("Username displayed correctly in installation address page")
        assert email == IAddpersonEmail, "Incorrect email"
        log.info("Email displayed correctly in installation address page")
        assert mobile == IAddpersonMobile, "Incorrect mobile"
        log.info("Mobile number displayed correctly in installation address page")
        self.clickAndSendText(SignUpPage.addressLine1,flatNo)
        self.clickAndSendText(SignUpPage.addressLine2,street)
        self.click(SignUpPage.areaDropdown)
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,"//div[text()='Please enter a valid pincode.']").is_displayed(),'Enter valid code message not displayed'
        log.info("Enter valid code message displayed")
        time.sleep(2)
        self.clickAndSendText(SignUpPage.pincode, pinCode)
        self.click(SignUpPage.areaDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='v-list-item__content']//div[text()='BANGALORE NORTH']").click()
        self.click1(SignUpPage.IAddcityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        time.sleep(8)
        self.click1(SignUpPage.altmobileNumBox)
        self.click1(SignUpPage.altmobileNo)
        self.send_keys(SignUpPage.altmobileNo,'9856231452')
        self.click1(SignUpPage.saveAndContinueBtn)
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//span[text()='Review & Pay']").is_displayed(), "Reveiew and Pay page deos not display"
        log.info("Reveiew and Pay page displayed")
        time.sleep(5)
        TotalPayAmount = self.getText(SignUpPage.totalPayAmount)
        finalPay = ''
        for i in TotalPayAmount:
            if i.isdigit():
                finalPay = finalPay + i
        time.sleep(4)
        assert int(finalPay) == finalValue, "Incorrect Total Pay Amount"
        log.info("Displayed correct total pay amount")
        # Edit installtion address - Need to write code
        time.sleep(5)
        self.click(SignUpPage.payBtn)
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.frame(0)
        self.click1(SignUpPage.netBanking)
        self.click1(SignUpPage.sbibank)
        self.click1(SignUpPage.paymentBtn)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(5)
        self.click(SignUpPage.successBtn)
        self.driver.switch_to.window(window_before)
        self.driver.switch_to.default_content()
        kycpage = self.driver.find_element(By.XPATH,"//p[@class='thanksinfo']").text
        assert 'KYC' in kycpage, 'kyc page not displayed'
        log.info('KYC page displayed')


# Upload KYC document
    def upload_KYCDoc(self,email,password,flatNum):
        log = self.getLogger()
        self.login(email,password)
        kycpage = self.driver.find_element(By.XPATH,"//p[@class='thanksinfo']").text
        assert 'KYC' in kycpage, 'kyc page not displayed'
        log.info('KYC page displayed')
        self.click1(SignUpPage.verifyBtn)
        expectedText = 'Nothing entered'
        emailtxt = self.driver.find_element(By.XPATH, "//div[@class='emailVerify verifyCommon']//div[4]").text
        assert expectedText.casefold() == emailtxt.casefold(), 'Nothing Entered message not displayed'
        log.info('Nothing Entered message displyed for email')
        mobiletxt = self.driver.find_element(By.XPATH, "//div[@class='mobileVerify verifyCommon']//div[4]").text
        assert expectedText.casefold() == mobiletxt.casefold(), 'Nothing Entered message not displayed'
        log.info('Nothing Entered message displyed for mobile')
        self.clickAndSendText(SignUpPage.emailOTP,'5678')
        self.clickAndSendText(SignUpPage.mobileOTP,'8769')
        self.click1(SignUpPage.verifyBtn)
        expectedOTPText = 'Wrong OTP Entered'
        emailOTPtxt = self.driver.find_element(By.XPATH, "//div[@class='emailVerify verifyCommon']//div[4]").text
        assert expectedOTPText.casefold() == emailOTPtxt.casefold(),'Wrong OTP Entered message not displayed'
        log.info('Wrong OTP Entered message displyed for email')
        mobileOTPtxt = self.driver.find_element(By.XPATH,"//div[@class='mobileVerify verifyCommon']//div[4]").text
        assert expectedOTPText.casefold() == mobileOTPtxt.casefold(),'Wrong OTP Entered message not displayed'
        log.info('Wrong OTP Entered message displyed for mobile')
        self.click(SignUpPage.permanentAdd)
        flatNo = self.getText(SignUpPage.flattextbox)
        assert flatNo == str(flatNum),'Address not displayed on checking permanent address checkbox'
        log.info('Address displayed on checking permanent address checkbox')
        self.click(SignUpPage.addressSubmit)
        assert self.driver.find_element(By.XPATH,"//i[text()='please verify your mobile number and email id']").is_displayed()
        self.click(SignUpPage.menu_profileLink)
        self.driver.find_element(By.XPATH,"//span[contains(.,'Kindly upload your eKYC documents to process your order!')]").is_displayed()
        self.click(SignUpPage.uploadkycBtn)
        # Need to complete kyc - Pending due to OTP


# Login into the account with invalid credentials
    def login_invalidcredentials(self,email,password):
        log = self.getLogger()
        self.click(SignUpPage.loginBtn)
        # Invalid email and Valid Password
        self.send_keys(SignUpPage.loginUN,"Test@gmail.com")
        self.send_keys(SignUpPage.loginPWD, password)
        self.click(SignUpPage.submitLoginBtn)
        assert self.driver.find_element(
            By.XPATH,"//div[contains(.,'Invalid username and password')][@class='v-alert__content']").is_displayed(),'Invalid username and password message not displayed'
        log.info('Invalid username and password message displayed')
        # valid email and InValid Password
        self.send_keys(SignUpPage.loginUN,email)
        self.send_keys(SignUpPage.loginPWD,'new123')
        self.click(SignUpPage.submitLoginBtn)
        assert self.driver.find_element(
            By.XPATH,"//div[contains(.,'Invalid username and password')][@class='v-alert__content']").is_displayed(), 'Invalid username and password message not displayed'
        log.info('Invalid username and password message displayed')
        # Invalid email and InValid Password
        self.send_keys(SignUpPage.loginUN, "Test@gmail.com")
        self.send_keys(SignUpPage.loginPWD, 'new123')
        self.click(SignUpPage.submitLoginBtn)
        assert self.driver.find_element(
            By.XPATH, "//div[contains(.,'Invalid username and password')][@class='v-alert__content']").is_displayed(), 'Invalid username and password message not displayed'
        log.info('Invalid username and password message displayed')

# verify Forgot password link with inalid email id/mobile number
    def verify_ForgotPassword_Invalid(self):
        log = self.getLogger()
        self.click(SignUpPage.loginBtn)
        self.click(SignUpPage.forgotPWD)
        self.clickAndSendText(SignUpPage.emailIdField,"missing@gmail.com")
        self.click(SignUpPage.proceedBtn)
        alertMsg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-error alert-dismissible fade in']").text
        assert 'provide correct email id' in alertMsg,'Please provide correct email id alert message not displayed'
        log.info('Please provide correct email id alert message displayed')
        self.clickAndSendText(SignUpPage.emailIdField, "6756453467")
        self.click(SignUpPage.proceedBtn)
        alertMsg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-error alert-dismissible fade in']").text
        assert 'provide correct email id' in alertMsg, 'Please provide correct email id alert message not displayed'
        log.info('Please provide correct email id alert message displayed')

# verify Forgot password link with inalid email id/mobile number
    def verify_ForgotPassword_valid(self,email):
        log = self.getLogger()
        self.click(SignUpPage.loginBtn)
        self.click(SignUpPage.forgotPWD)
        self.clickAndSendText(SignUpPage.emailIdField,email)
        self.click(SignUpPage.proceedBtn)
        assert self.driver.find_element(By.XPATH,"//h2[text()='OTP Verification']"),'OTP Verification page not displayed'
        log.info('OTP Verification page displayed')
        self.click(SignUpPage.OTPSubmitBtn)
        assert self.driver.find_element(By.XPATH,"//label[text()='Please enter the otp']"),'Please enter the otp message not displayed'
        log.info('Please enter the otp message displayed')
        assert self.driver.find_element(By.XPATH,"//label[text()='Please enter the new password']"),'Please enter the new password message not displayed'
        log.info('Please enter the new password message not displayed')
        # Cannot continue due to OTP

# Login into the account and verify the customer Dashboard
    def verify_CustomerDashboard(self,email,password,username,PhNo,Address,City,State,Pincode,fbiD,fbpwd):
        log = self.getLogger()
        self.login(email,password)
        assert self.driver.find_element(By.XPATH,"//h2[text()='Welcome "+username+"']").is_displayed(),'Username not displayed'
        log.info('Username displayed')
        assert self.driver.find_element(By.XPATH,"//p[text()='Email: "+email+"']").is_displayed(),'Email not displayed'
        log.info('Email displayed')
        assert self.driver.find_element(By.XPATH,"//p[text()='Phone No: "+str(PhNo)+"']").is_displayed(),'Phone No not displayed'
        log.info('Phone No displayed')
        assert self.driver.find_element(By.XPATH,"//p[text()='Address: "+str(Address)+"']").is_displayed(),'Address not displayed'
        log.info('Address displayed')
        assert self.driver.find_element(By.XPATH,"//p[text()='City: "+City+"']").is_displayed(),'City not displayed'
        log.info('City displayed')
        assert self.driver.find_element(By.XPATH, "//p[text()='State: "+State+"']").is_displayed(),'State not displayed'
        log.info('State displayed')
        assert self.driver.find_element(By.XPATH, "//p[text()='Pincode: "+str(Pincode)+"']").is_displayed(),'PinCode not displayed'
        log.info('Pincode displayed')
        referralCode = self.driver.find_element(By.XPATH,"(//h2[@class='heading02 text-right'])[2]").text
        RC = referralCode.split(':')[-1]
        RCode = RC.strip()
        XLUtils.writeData(excel,'SignUp',15,9,RCode)
        # verify whatsapp and facebook icon redircts to respected page
        window_before = self.driver.window_handles[0]
        self.click(SignUpPage.whatsappicon)
        window_After = self.driver.window_handles[1]
        self.driver.switch_to_window(window_After)
        whatsapp = self.driver.title
        assert whatsapp == 'WhatsApp', 'Not redirected to WhatsApp page'
        log.info('Redirected to WhatsApp page')
        self.driver.close()
        self.driver.switch_to_window(window_before)
        time.sleep(5)
        self.click(SignUpPage.facebookicon)
        window_After1 = self.driver.window_handles[1]
        self.driver.switch_to_window(window_After1)
        self.send_keys(SignUpPage.fbID,fbiD)
        self.send_keys(SignUpPage.fbPwd,fbpwd)
        self.click(SignUpPage.fbLogin)
        fbtext = self.getText((By.XPATH,"(//div[contains(.,'Get Rs.100 instant discount on the plan purchase of LivpureSmart RO')])[10]"))
        assert RCode in fbtext,'Referral code not displayed on inviting to FB'
        log.info('Referral code displayed on inviting to FB')
        self.driver.close()
        self.driver.switch_to_window(window_before)
        self.click(SignUpPage.knowMore)
        assert self.driver.find_element(By.XPATH,"//button[text()='Invite']"), 'invite page not displayed'
        log.info('invite page displayed')
        self.click(SignUpPage.custDashboard)
        self.click(SignUpPage.invitelink)
        # Pending to verify fb page
        window_After2 = self.driver.window_handles[1]
        self.driver.switch_to_window(window_After2)
        FBtitle = self.driver.title
        assert 'Facebook' in FBtitle, 'FB not opened'
        log.info('FB page displayed')

# verify refer and Earn
    def verify_ReferAndEarn(self,email,password,referRs,refCode,liter):
        log = self.getLogger()
        self.login(email,password)
        self.click(SignUpPage.referEarnBtn)
        self.driver.find_element(By.XPATH,"(//b[contains(.,'"+str(liter)+"L free water*')])[1]").is_displayed()
        self.driver.find_element(By.XPATH,"(//b[contains(.,'₹ "+str(referRs)+" Shopping Voucher')])[1]").is_displayed()
        invitePage = self.getText((By.XPATH,"//h4[@class='refTit']['Refer now & Earn up to Rs. "+str(referRs)+"']"))
        assert str(referRs) in invitePage,'invite page and message not displayed'
        log.info('invite page and message displayed')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//b[contains(.,'"+str(liter)+"L free water*')])[2]").is_displayed()
        assert self.driver.find_element(By.XPATH,"(//b[contains(.,'₹ "+str(referRs)+" Shopping Voucher')])[2]").is_displayed(),'Fail'
        log.info('Pass')
        self.click(SignUpPage.inviteRefCode)
        refCode1 = self.driver.find_element(By.XPATH,"//input[@class='RefCode']").get_attribute("value")
        assert refCode1 == refCode, 'referral Code are not same from Customer dashboard and invite page'
        log.info('referral Code are same from Customer dashboard and invite page')
        self.hoverToElement(SignUpPage.copyCode)
        tooltiptext = self.getText(SignUpPage.codeToolTip)
        expectedText = 'Copy to clipboard'
        assert tooltiptext.casefold() == expectedText.casefold(), 'Tooltip not displayed for Copy Icon'
        log.info('Tooltip displayed for Copy Icon')
        self.click(SignUpPage.copyCode)
        copiedText = self.getText(SignUpPage.codeToolTip)
        log.info(copiedText)
        window_before = self.driver.window_handles[0]
        self.click(SignUpPage.inviteWhatsapp)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        assert self.driver.find_element(By.XPATH,"//div[text()='WhatsApp Web']").is_displayed(),'Whatapp not opened'
        log.info('Whatsapp opened')
        self.driver.close()
        self.driver.switch_to_window(window_before)
        self.click(SignUpPage.inviteFB)
        window_After1 = self.driver.window_handles[1]
        self.driver.switch_to_window(window_After1)
        FBtitle = self.driver.title
        assert 'Facebook' in FBtitle, 'FB not opened'
        log.info('FB page displayed')
        self.driver.close()
        self.driver.switch_to_window(window_before)
        self.click(SignUpPage.howdoesitwork)
        assert self.driver.find_element(By.XPATH,"//div[@class='popup bgOuter']").is_displayed(),'How does it work popup not displayed'
        log.info('How does it work popup displayed')
        self.click(SignUpPage.inviteTC)
        assert self.driver.find_element(By.XPATH,"//div[@class='term_condition_panel']").is_displayed(), 'TC page not displayed'
        log.info('TC page displayed')

# Verify LeaderBoard page
    def verify_LeaderBoard(self,email,password):
        log = self.getLogger()
        self.login(email,password)
        time.sleep(5)
        self.click(SignUpPage.referEarnBtn)
        time.sleep(5)
        self.click(SignUpPage.leaderBoard)
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//div[@class='LeadBdgradintBg']").is_displayed(),'LeaderBoard not displayed'
        log.info('LeaderBoard displayed')
        time.sleep(5)
        cm = date.today()
        cmonth = cm.strftime("%b")
        monthtxt = self.driver.find_element(By.XPATH,"//div[@id='Pmonths']").text
        assert cmonth.casefold() == monthtxt.casefold(), 'Leaderboard not displayed for the current month'
        log.info('Leaderboard displayed for the current month')


# Login into the account and verify the subscribed Plan details
    def verify_PlanDetails(self,email,password):
        log = self.getLogger()
        self.login(email, password)
        self.click(SignUpPage.planDetailsTab)
        # Need to verify plan details here from the subscription box

        # Verify Renew plan link which should redirects to plan tab
        self.click(SignUpPage.renewplanLink)
        assert self.driver.find_element(By.XPATH,"//span[text()='Select Plan & Duration']").is_displayed(), "Renew Plan link not redirected to plan page"
        log.info("Renew Plan link redirected to plan page")

# Verify the price of the silver plan in plan details tab and menu plan
    def verify_SilverPlanPrice(self,email,password,month12,month6,month1,price12,price6,price1):
        log = self.getLogger()
        log.info("verify plan price for Silver")
        self.login(email, password)
        time.sleep(5)
        for a in range(1,4):
            self.click(SignUpPage.planDetailsTab)
            self.click(SignUpPage.silverplan)
            self.click1(SignUpPage.updateNowBtn)
            monthtxt = self.driver.find_element(By.XPATH, "(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan details Page')
            else:
                raise AssertionError("Month and price does not match in Plan details Page")
        self.click(SignUpPage.menu_planLink)
        for b in range(1, 4):
            monthtxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabsilver']//p[@class='monthnew']//span[1])["+str(b)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabsilver']//div[@class='price-month'])["+str(b)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan Page')
            else:
                raise AssertionError("Month and price does not match in Plan Page")

# Verify the price of the plan in plan details tab
    def verify_GoldPlanPrice(self,email,password,month12,month6,month1,price12,price6,price1):
        log = self.getLogger()
        log.info("verify plan price for Gold")
        self.login(email, password)
        time.sleep(5)
        for a in range(4,7):
            self.click(SignUpPage.planDetailsTab)
            self.click(SignUpPage.goldplan)
            self.click1(SignUpPage.updateNowBtn)
            monthtxt = self.driver.find_element(By.XPATH, "(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan details Page')
            else:
                raise AssertionError("Month and price does not match in Plan details Page")
        self.click(SignUpPage.menu_planLink)
        for b in range(1, 4):
            monthtxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabgold']//p[@class='monthnew']//span[1])["+str(b)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabgold']//div[@class='price-month'])["+str(b)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan Page')
            else:
                raise AssertionError("Month and price does not match in Plan Page")

# Verify the price of the plan in plan details tab
    def verify_PlatinumPlanPrice(self,email,password,month12,month6,month1,price12,price6,price1):
        log = self.getLogger()
        log.info("verify plan price for Platinum")
        self.login(email, password)
        time.sleep(5)
        for a in range(7,10):
            self.click(SignUpPage.planDetailsTab)
            self.click(SignUpPage.platinumplan)
            self.click1(SignUpPage.updateNowBtn)
            monthtxt = self.driver.find_element(By.XPATH, "(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan details Page')
            else:
                raise AssertionError("Month and price does not match in Plan details Page")
        self.click(SignUpPage.menu_planLink)
        for b in range(1, 4):
            monthtxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabplatinum']//p[@class='monthnew']//span[1])["+str(b)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabplatinum']//div[@class='price-month'])["+str(b)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan Page')
            else:
                raise AssertionError("Month and price does not match in Plan Page")

# Verify the price of the plan in plan details tab
    def verify_TitaniumPlanPrice(self,email,password,month12,month6,month1,price12,price6,price1):
        log = self.getLogger()
        log.info("verify plan price for Titanium")
        self.login(email, password)
        time.sleep(5)
        for a in range(10,13):
            self.click(SignUpPage.planDetailsTab)
            self.click(SignUpPage.titaniumplan)
            self.click1(SignUpPage.updateNowBtn)
            monthtxt = self.driver.find_element(By.XPATH, "(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan details Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan details Page')
            else:
                raise AssertionError("Month and price does not match in Plan details Page")
        self.click(SignUpPage.menu_planLink)
        for b in range(1, 4):
            monthtxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabtitanium']//p[@class='monthnew']//span[1])["+str(b)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabtitanium']//div[@class='price-month'])["+str(b)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            if int(expectedtxt1) == month12 and int(expectedprice1) == price12:
                log.info('month 12 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month6 and int(expectedprice1) == price6:
                log.info('month 6 and Price is matching in Plan Page')
            elif int(expectedtxt1) == month1 and int(expectedprice1) == price1:
                log.info('month 1 and price is matching in Plan Page')
            else:
                raise AssertionError("Month and price does not match in Plan Page")

# Login into the account and change the plan and verify it in Recharge History tab
    def verify_SilverChangePlan(self,email,password):
        log = self.getLogger()
        log.info("Check for the Silver Plan change")
        self.login(email, password)
        for a in range(1,4):
            self.click(SignUpPage.planDetailsTab)
            # Silver Plan for 12, 6, 1 months
            self.click(SignUpPage.silverplan)
            self.click1(SignUpPage.updateNowBtn)
            time.sleep(5)
            ele = self.driver.find_element(By.XPATH,"(//input[@name='planDuration'])["+str(a)+"]")
            self.driver.execute_script("arguments[0].click();", ele)
            time.sleep(5)
            monthtxt = self.driver.find_element(By.XPATH,"(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            finalPrice = int(expectedtxt1) * int(expectedprice1)
            self.click(SignUpPage.proceedToPayBtn)
            payableAmt = self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount']").text
            expectedPayableAmt = ''
            for k in payableAmt:
                if k.isdigit():
                    expectedPayableAmt = expectedPayableAmt + k
            assert finalPrice == int(expectedPayableAmt), 'incorrect amount'
            log.info('Amount displayed correctly')

            self.click1(SignUpPage.payBtn)
            window_before1 = self.driver.window_handles[-1]
            window_before = self.driver.window_handles[0]
            self.driver.switch_to.frame(0)
            self.click1(SignUpPage.netBanking)
            self.click1(SignUpPage.sbibank)
            self.click1(SignUpPage.paymentBtn)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to_window(window_after)
            self.click(SignUpPage.successBtn)
            self.driver.switch_to_window(window_before1)
            time.sleep(5)
            assert self.driver.find_element(By.XPATH,"//h2[text()='Recharge Details']").is_displayed(),'Recharge History not displayed'
            log.info('Recharge History displayed')
            # Get the current date
            currentDate = date.today()
            cd = currentDate.strftime("%d-%m-%Y")

            # Get the recharge date from history
            rechargeDate = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[1])[1]").text
            rdt = rechargeDate.split(':')[-1]
            date1 = rdt.strip()
            assert cd == date1, 'Rechrage date not displayed'
            log.info('Recharge date displayed')

            # Get the recharge date from history and match with plan amount
            rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
            rAmt = rechargeAmt.split(':')[-1]
            amt = rAmt.strip()
            assert finalPrice == int(amt), 'Amount not displayed'
            log.info('Amount displayed')

# Login into the account and change the plan and verify it in Recharge History tab
    def verify_GoldChangePlan(self,email,password):
        log = self.getLogger()
        log.info("Check for the Gold Plan change")
        self.login(email, password)
        for a in range(4,7):
            self.click(SignUpPage.planDetailsTab)
            # Silver Plan for 12, 6, 1 months
            self.click(SignUpPage.goldplan)
            self.click1(SignUpPage.updateNowBtn)
            time.sleep(5)
            ele = self.driver.find_element(By.XPATH,"(//input[@name='planDuration'])["+str(a)+"]")
            self.driver.execute_script("arguments[0].click();", ele)
            time.sleep(5)
            monthtxt = self.driver.find_element(By.XPATH,"(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            finalPrice = int(expectedtxt1) * int(expectedprice1)
            self.click(SignUpPage.proceedToPayBtn)
            payableAmt = self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount']").text
            expectedPayableAmt = ''
            for k in payableAmt:
                if k.isdigit():
                    expectedPayableAmt = expectedPayableAmt + k
            assert finalPrice == int(expectedPayableAmt), 'incorrect amount'
            log.info('Amount displayed correctly')
            self.click1(SignUpPage.payBtn)
            window_before1 = self.driver.window_handles[-1]
            window_before = self.driver.window_handles[0]
            self.driver.switch_to.frame(0)
            self.click1(SignUpPage.netBanking)
            self.click1(SignUpPage.sbibank)
            self.click1(SignUpPage.paymentBtn)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to_window(window_after)
            self.click(SignUpPage.successBtn)
            self.driver.switch_to_window(window_before1)
            time.sleep(5)
            assert self.driver.find_element(By.XPATH,"//h2[text()='Recharge Details']").is_displayed(),'Recharge History not displayed'
            log.info('Recharge History displayed')
            # Get the current date
            currentDate = date.today()
            cd = currentDate.strftime("%d-%m-%Y")

            # Get the recharge date from history
            rechargeDate = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[1])[1]").text
            rdt = rechargeDate.split(':')[-1]
            date1 = rdt.strip()
            assert cd == date1, 'Rechrage date not displayed'
            log.info('Recharge date displayed')

            # Get the recharge date from history and match with plan amount
            rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
            rAmt = rechargeAmt.split(':')[-1]
            amt = rAmt.strip()
            assert finalPrice == int(amt), 'Amount not displayed'
            log.info('Amount displayed')

# Login into the account and change the plan and verify it in Recharge History tab
    def verify_PlatinumChangePlan(self,email,password):
        log = self.getLogger()
        log.info("Check for the Platinum Plan change")
        self.login(email, password)
        for a in range(7,10):
            self.click(SignUpPage.planDetailsTab)
            # Silver Plan for 12, 6, 1 months
            self.click(SignUpPage.platinumplan)
            self.click1(SignUpPage.updateNowBtn)
            time.sleep(5)
            ele = self.driver.find_element(By.XPATH,"(//input[@name='planDuration'])["+str(a)+"]")
            self.driver.execute_script("arguments[0].click();", ele)
            time.sleep(5)
            monthtxt = self.driver.find_element(By.XPATH,"(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            finalPrice = int(expectedtxt1) * int(expectedprice1)
            self.click(SignUpPage.proceedToPayBtn)
            payableAmt = self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount']").text
            expectedPayableAmt = ''
            for k in payableAmt:
                if k.isdigit():
                    expectedPayableAmt = expectedPayableAmt + k
            assert finalPrice == int(expectedPayableAmt), 'incorrect amount'
            log.info('Amount displayed correctly')

            self.click1(SignUpPage.payBtn)
            window_before1 = self.driver.window_handles[-1]
            window_before = self.driver.window_handles[0]
            self.driver.switch_to.frame(0)
            self.click1(SignUpPage.netBanking)
            self.click1(SignUpPage.sbibank)
            self.click1(SignUpPage.paymentBtn)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to_window(window_after)
            self.click(SignUpPage.successBtn)
            self.driver.switch_to_window(window_before1)
            time.sleep(5)
            assert self.driver.find_element(By.XPATH,"//h2[text()='Recharge Details']").is_displayed(),'Recharge History not displayed'
            log.info('Recharge History displayed')
            # Get the current date
            currentDate = date.today()
            cd = currentDate.strftime("%d-%m-%Y")

            # Get the recharge date from history
            rechargeDate = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[1])[1]").text
            rdt = rechargeDate.split(':')[-1]
            date1 = rdt.strip()
            assert cd == date1, 'Rechrage date not displayed'
            log.info('Recharge date displayed')

            # Get the recharge date from history and match with plan amount
            rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
            rAmt = rechargeAmt.split(':')[-1]
            amt = rAmt.strip()
            assert finalPrice == int(amt), 'Amount not displayed'
            log.info('Amount displayed')

# Login into the account and change the plan and verify it in Recharge History tab
    def verify_TitaniumChangePlan(self,email,password):
        log = self.getLogger()
        log.info("Check for the Titanium Plan change")
        self.login(email, password)
        for a in range(10,13):
            self.click(SignUpPage.planDetailsTab)
            # Silver Plan for 12, 6, 1 months
            self.click(SignUpPage.titaniumplan)
            self.click1(SignUpPage.updateNowBtn)
            time.sleep(5)
            ele = self.driver.find_element(By.XPATH,"(//input[@name='planDuration'])["+str(a)+"]")
            self.driver.execute_script("arguments[0].click();", ele)
            time.sleep(5)
            monthtxt = self.driver.find_element(By.XPATH,"(//span[@class='planmonth'])["+str(a)+"]").text
            expectedtxt1 = ''
            for i in monthtxt:
                if i.isdigit():
                    expectedtxt1 = expectedtxt1 + i
            pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])["+str(a)+"]").text
            expectedprice1 = ''
            for j in pricetxt:
                if j.isdigit():
                    expectedprice1 = expectedprice1 + j
            finalPrice = int(expectedtxt1) * int(expectedprice1)
            self.click(SignUpPage.proceedToPayBtn)
            payableAmt = self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount']").text
            expectedPayableAmt = ''
            for k in payableAmt:
                if k.isdigit():
                    expectedPayableAmt = expectedPayableAmt + k
            assert finalPrice == int(expectedPayableAmt), 'incorrect amount'
            log.info('Amount displayed correctly')

            self.click1(SignUpPage.payBtn)
            window_before1 = self.driver.window_handles[-1]
            window_before = self.driver.window_handles[0]
            self.driver.switch_to.frame(0)
            self.click1(SignUpPage.netBanking)
            self.click1(SignUpPage.sbibank)
            self.click1(SignUpPage.paymentBtn)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to_window(window_after)
            self.click(SignUpPage.successBtn)
            self.driver.switch_to_window(window_before1)
            time.sleep(5)
            assert self.driver.find_element(By.XPATH,"//h2[text()='Recharge Details']").is_displayed(),'Recharge History not displayed'
            log.info('Recharge History displayed')
            # Get the current date
            currentDate = date.today()
            cd = currentDate.strftime("%d-%m-%Y")

            # Get the recharge date from history
            rechargeDate = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[1])[1]").text
            rdt = rechargeDate.split(':')[-1]
            date1 = rdt.strip()
            assert cd == date1, 'Rechrage date not displayed'
            log.info('Recharge date displayed')

            # Get the recharge date from history and match with plan amount
            rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
            rAmt = rechargeAmt.split(':')[-1]
            amt = rAmt.strip()
            assert finalPrice == int(amt), 'Amount not displayed'
            log.info('Amount displayed')

# Verify change password
    def verify_changePassword(self,email,password):
        log = self.getLogger()
        self.login(email, password)
        self.click(SignUpPage.changePWDTab)
        self.send_keys(SignUpPage.oldPWD,password)
        self.send_keys(SignUpPage.newPWD, password)
        self.send_keys(SignUpPage.confirmPWD, password)
        self.click(SignUpPage.changePWDBtn)
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'New password and old password cannot be same')]")\
            .is_displayed(),'Password cannot be same message not displayed'
        log.info("Password cannot be same message displayed")
        self.send_keys(SignUpPage.oldPWD,password)
        newpwd = 'Test@' + self.random_digits()
        self.send_keys(SignUpPage.newPWD,newpwd)
        self.send_keys(SignUpPage.confirmPWD,newpwd)
        self.click(SignUpPage.changePWDBtn)
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Password reset successful')]")\
            .is_displayed(), 'Password reset successful message not displayed'
        log.info("Password reset successful message displayed")
        XLUtils.writeData(excel,'SignUp',15,3,newpwd)
        time.sleep(5)
        self.hoverToElement(SignUpPage.profileicon)
        self.hoverAndClick(SignUpPage.logout)
        self.login(email,newpwd)
        assert self.driver.find_element(By.XPATH,"//a[text()='Customer Dashboard']").is_displayed(),'Passowrd not Changed'
        log.info('Password changed successfully')

# verify with different password in new and confirm password text box and mandatory field
    def verify_diffPWD(self,email,password):
        log = self.getLogger()
        self.login(email, password)
        self.click(SignUpPage.changePWDTab)
        time.sleep(5)
        self.click(SignUpPage.changePWDBtn)
        # Verify mandtory message for field
        self.driver.find_element(By.XPATH,"//label[text()='Please enter the Password']").is_displayed()
        self.driver.find_element(By.XPATH, "//label[text()='Please enter the New Password']").is_displayed()
        self.driver.find_element(By.XPATH, "//label[text()='This field is required.']").is_displayed()
        # verify with incorrect password into old and correct into new and confirm password field
        self.send_keys(SignUpPage.oldPWD,"@gmail.com")
        self.send_keys(SignUpPage.newPWD,'Test@1234')
        self.send_keys(SignUpPage.confirmPWD,'Test@1234')
        self.click(SignUpPage.changePWDBtn)
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Please Provide Correct Password')]").is_displayed()
        # verify with correct old and <5 char into New and match New and Confirm pwd
        self.send_keys(SignUpPage.oldPWD, password)
        self.send_keys(SignUpPage.newPWD,'Test')
        self.send_keys(SignUpPage.confirmPWD,'Test@1234')
        self.click(SignUpPage.oldPWD)
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Please enter at least 5 characters.')]").is_displayed()
        assert self.driver.find_element(By.XPATH,"//label[contains(text(),'Please enter the same value again.')]")\
            .is_displayed(),'Mandatory and error message not displayed'
        log.info("Mandatory and error message displayed")


# Sign up account with referral code and verify Rs 100 discount applied on plan
    def verify_signupWithRefCode(self,refCode,referUN):
        log = self.getLogger()
        username = "Test_" + self.random_generatorString()
        XLUtils.writeData(excel,'SignUp',25,1,username)
        email = self.random_generator() + "@gmail.com"
        XLUtils.writeData(excel, 'SignUp',25,2,email)
        mobile = "95" + self.random_generatordigits()
        XLUtils.writeData(excel, 'SignUp', 25, 4, mobile)
        self.click(SignUpPage.subscribeBtn)
        self.clickAndSendText(SignUpPage.yourNameTxtBox,username)
        self.clickAndSendText(SignUpPage.emailTxtBox, email)
        self.clickAndSendText(SignUpPage.mobileTxtBox, mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(4)
        cityList = self.driver.find_elements(By.XPATH, "//div[@class='v-list-item__content']")
        for city in cityList:
            if city.text == "Bengaluru":
                city.click()
        self.clickAndSendText(SignUpPage.passwordTxtBox,'Test@1234')
        self.clickAndSendText(SignUpPage.referralBox,'ref')
        self.driver.find_element(By.XPATH,"//div[text()='Please enter the six digit referral code']").is_displayed()
        self.clickAndSendText(SignUpPage.referralBox,'refcode1')
        self.driver.find_element(By.XPATH,"//div[text()='Invalid referral code']").is_displayed()
        self.clear(SignUpPage.referralBox)
        self.clickAndSendText(SignUpPage.referralBox,refCode)
        refmsg = self.driver.find_element(By.XPATH,"//div[contains(text(),'Subscribe and recharge to claim your referral benefits from "+referUN+"')]").text
        assert 'referral benefits' in refmsg, 'referral benefits message not displayed'
        log.info('referral benefits message displayed')
        time.sleep(5)
        ele = self.driver.find_element(By.XPATH,"//button[@type='submit']//span[contains(.,'Sign Up For 7 Days Trial')]")
        self.driver.execute_script("arguments[0].click();", ele)
        time.sleep(5)
        self.click(SignUpPage.silver6_radio)
        price = self.driver.find_element(By.XPATH,"(//button[@data-parent='tabsilver'][@data-duration='6']//div[@class='price-month']//span[1])[1]").text
        actprice = ''
        for val in price:
            if val.isdigit():
                actprice = actprice + val
        months = self.driver.find_element(By.XPATH,"//button[@data-parent='tabsilver'][@data-duration='6']//p//span[1]").text
        finalValue = int(actprice) * int(months) - 100
        self.click1(SignUpPage.proceedToPaySilver)
        time.sleep(5)
        self.clickAndSendText(SignUpPage.addressLine1,'109')
        self.clickAndSendText(SignUpPage.addressLine2,'HAL')
        self.clickAndSendText(SignUpPage.pincode,'560008')
        self.click(SignUpPage.areaDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='v-list-item__content']//div[text()='BANGALORE NORTH']").click()
        self.click1(SignUpPage.IAddcityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        time.sleep(8)
        self.click1(SignUpPage.saveAndContinueBtn)
        TotalPayAmount = self.getText(SignUpPage.totalPayAmount)
        finalPay = ''
        for i in TotalPayAmount:
            if i.isdigit():
                finalPay = finalPay + i
        time.sleep(4)
        assert int(finalPay) == finalValue, "Discount not applied"
        log.info("Discount applied")
        self.click1(SignUpPage.payBtn)
        window_before1 = self.driver.window_handles[-1]
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.frame(0)
        self.click1(SignUpPage.netBanking)
        self.click1(SignUpPage.sbibank)
        self.click1(SignUpPage.paymentBtn)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.click(SignUpPage.successBtn)
        self.driver.switch_to_window(window_before1)
        time.sleep(5)
        # also verify referral code can be applied for one time
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.planDetailsTab)
        self.click(SignUpPage.silverplan)
        self.click(SignUpPage.updateNowBtn)
        monthtxt = self.driver.find_element(By.XPATH,"(//span[@class='planmonth'])[1]").text
        expectedtxt1 = ''
        for i in monthtxt:
            if i.isdigit():
                expectedtxt1 = expectedtxt1 + i
        pricetxt = self.driver.find_element(By.XPATH,"(//div[@class='priceDetails']//div[@class='offerPrice blue'])[1]").text
        expectedprice1 = ''
        for j in pricetxt:
            if j.isdigit():
                expectedprice1 = expectedprice1 + j
        finalPrice = int(expectedtxt1) * int(expectedprice1)
        self.click(SignUpPage.proceedToPayBtn)
        payableAmt = self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount']").text
        expectedPayableAmt = ''
        for k in payableAmt:
            if k.isdigit():
                expectedPayableAmt = expectedPayableAmt + k
        assert finalPrice == int(expectedPayableAmt), 'Discount applied'
        log.info('Discount not applied')

# Verify Referral History page
    def verify_ReferralHistory(self,email,password,amount):
        log = self.getLogger()
        self.login(email, password)
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.referEarnBtn)
        self.click(SignUpPage.ReferralHistory)
        assert self.driver.find_element(By.XPATH,"//div[@class='amountvoucher']//span[contains(.,'Rs. "+str(amount)+"')]").is_displayed(), 'Referral History page not displayed'
        log.info('Referral History page displayed')
        self.click(SignUpPage.inviteNowBtn)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        # need to verify facebook page
        fbTitle = self.driver.title
        assert 'Facebook' in fbTitle,'Does not Redirect to FB page'
        log.info('Redirected to FB page')

# verify the referred username displays in the Referral History tab
    def verify_referredUNInReferralHistory(self,email,password,refName,refemail,refMobile,liter):
        log = self.getLogger()
        self.login(email,password)
        # verify username, email address, phone number in referral history from customer dashboard
        self.click(SignUpPage.refHistoryBtn)
        assert self.driver.find_element(By.XPATH,"//ul//li[text()='Name : "+str(refName)+"']").is_displayed(),'Name does not match'
        assert self.driver.find_element(By.XPATH,"//ul//li[text()='Email : "+str(refemail)+"']").is_displayed(),'Email does not match'
        assert self.driver.find_element(By.XPATH,"//ul//li[text()='Phone : "+str(refMobile)+"']").is_displayed(),'Phone does not match'
        self.click(SignUpPage.custDashboard)
        self.click(SignUpPage.referEarnBtn)
        self.click(SignUpPage.ReferralHistory)
        assert self.driver.find_element(By.XPATH,"//b[@class='phoNum'][text()='"+refName+"']").is_displayed(),'Referred username not displayed in History'
        log.info('Referred username displayed in History')
        # Bug in this, not fixed yet
        '''cd = date.today()
        a = cd.strftime("%d %b %Y")
        signUptext = self.driver.find_element(By.XPATH,"//b[@class='phoNum'][text()='"+refName+"']//following::p[@class='signInfo']").text
        new = signUptext.split(' ')[-3:]
        b = ' '.join(new)
        assert a == b, 'Signed up date not displayed'
        log.info('Signed up date displayed')'''
        # verify Free water
        count = self.driver.find_elements(By.XPATH,"//div[@class='referral_Item bg']")
        waterText = self.driver.find_element(By.XPATH,"//div[@id='ReferralsHistory']//div[@class='d-flex vouWatC water']//div[2]").text
        val = waterText.split(' ')[0]
        freewater = len(count) * liter
        assert int(val) == freewater, 'Incorrect Free water liter'
        log.info('Correct free water liter displayed')
        # verify Voucher
        count1 = self.driver.find_elements(By.XPATH,"//div[@id='ReferralsHistory']//div[contains(.,'Free Water and Voucher Won!')]")
        voucher = self.driver.find_element(By.XPATH,
                                           "//div[@id='ReferralsHistory']//div[@class='d-flex vouWatC Voucher rightborder']//div[2]").text
        assert len(count1) == int(voucher), 'Incorrect Voucher count'
        log.info('Voucher count displayed')
        # verify watsapp and call icon
        time.sleep(3)
        window_before = self.driver.window_handles[0]
        self.click((By.XPATH,"(//b[@class='phoNum'][text()='"+refName+"']//following::div[@class='shareAct']//a[@id='wshare'])[1]"))
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        whatsapp = self.driver.title
        assert whatsapp == 'WhatsApp', 'Not redirected to WhatsApp page'
        log.info('Redirected to WhatsApp page')
        self.driver.close()
        self.driver.switch_to_window(window_before)
        self.click((By.XPATH,"(//b[@class='phoNum'][text()='"+refName+"']//following::div[@class='shareAct']//img[@alt='Livpuresmart Call Icon'])[1]"))

# verify Add more liter without mapping RO to account
    def verify_AddMoreltr(self,email,password):
        log = self.getLogger()
        self.login(email,password)
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.addmoreltrTab)
        msg = self.getText(SignUpPage.addmoreltrMsg)
        log.info(msg)
        assert 'subscribe the plan first' in msg, 'Subscribe plan first message not displayed'
        log.info('Subscribe plan first message not displayed')

# verify Add more liter after mapping RO to account
    def verify_AddMoreltrwithRO(self,email,password):
        self.login(email,password)

# Verify details of the premium plan
    def verify_PremiumPlan(self,month,value,depositAmount):
        log = self.getLogger()
        self.click(SignUpPage.menu_planLink)
        assert self.driver.find_element(By.XPATH,"//div[@data-tier='silver'][contains(.,'Silver')]").is_displayed(),'Premium Activated'
        log.info("Premium not Activated")
        self.click(SignUpPage.premiumBth)
        monthtext = self.getText(SignUpPage.premiummonth)
        month_1 = ''
        for i in monthtext:
            if i.isdigit():
                month_1 = month_1 + i
        assert int(month_1) == month,'Month not displayed'
        log.info('Month displayed')
        monthprice = self.getText(SignUpPage.premiumPrice)
        price = ''
        for j in monthprice:
            if j.isdigit():
                price = price + j
        assert int(price) == value, 'Amount not displayed'
        log.info('Amount displayed')
        time.sleep(5)
        self.click1(SignUpPage.expandDeposit)
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//div[@id='depositPremium']//li[text()='One time 100% refundable security deposit, for which receipt will be provided on payment.']").is_displayed()
        assert self.driver.find_element(By.XPATH,"//div[@id='depositPremium']//li[text()='Security deposit is 100% refunded when you give back the RO machine.']").is_displayed()
        time.sleep(5)
        self.click1(SignUpPage.expandDeposit)
        depositTxt = self.getText(SignUpPage.depositText)
        amount = depositTxt.split(' ')[-1]
        depositAmt = amount.strip()
        assert int(depositAmt) == depositAmount, 'deposit not displayed'
        log.info('Desposit displayed')
        totalPay = int(month_1) * int(price) + int(depositAmt)
        XLUtils.writeData(excel, 'SignUp', 30, 4, totalPay)
        time.sleep(3)

# subscribe premium plan
    def subsribe_premiumPlan(self,password,planAmt,depositAmt,finalValue):
        log = self.getLogger()
        self.click(SignUpPage.menu_planLink)
        self.click(SignUpPage.premiumBth)
        self.click1(SignUpPage.premiumProceedToPay)
        username = "Test_" + self.random_generatorString()
        email = self.random_generator() + "@gmail.com"
        mobile = "95" + self.random_generatordigits()
        XLUtils.writeData(excel,'SignUp',30,5, username)
        XLUtils.writeData(excel,'SignUp',30,6, email)
        XLUtils.writeData(excel,'SignUp',30,7, mobile)
        self.clickAndSendText(SignUpPage.yourNameTxtBox, username)
        self.clickAndSendText(SignUpPage.emailTxtBox, email)
        self.clickAndSendText(SignUpPage.mobileTxtBox, mobile)
        self.click(SignUpPage.cityDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        self.clickAndSendText(SignUpPage.passwordTxtBox,password)
        ele = self.driver.find_element(By.XPATH, "//button[@type='submit']//span[contains(.,'Sign Up For 7 Days Trial')]")
        self.driver.execute_script("arguments[0].click();", ele)
        self.clickAndSendText(SignUpPage.addressLine1,'104')
        self.clickAndSendText(SignUpPage.addressLine2,'HAL')
        self.clickAndSendText(SignUpPage.pincode,'560008')
        self.click(SignUpPage.areaDropdown)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='v-list-item__content']//div[text()='BANGALORE NORTH']").click()
        self.click1(SignUpPage.IAddcityDropdown)
        self.driver.find_element(By.XPATH, "//div[@class='v-list-item__content']//div[text()='Bengaluru']").click()
        self.click1(SignUpPage.saveAndContinueBtn)
        time.sleep(5)
        planName = self.getText(SignUpPage.planname)
        assert planName.casefold() == 'Premium'.casefold(),'Plan Name not displayed'
        log.info('Plan name displayed')
        assert self.driver.find_element(By.XPATH,"//span[@class='success--text pay-amount'][contains(.,'"+str(planAmt)+"')]").is_displayed()
        assert self.driver.find_element(By.XPATH,"//span[@class='success--text'][contains(.,'"+str(depositAmt)+"')]").is_displayed()
        TotalPayAmount = self.getText(SignUpPage.totalPayAmount)
        finalPay = ''
        for i in TotalPayAmount:
            if i.isdigit():
                finalPay = finalPay + i
        time.sleep(4)
        assert int(finalPay) == finalValue, "Incorrect Total Pay Amount"
        log.info("Displayed correct total pay amount")
        time.sleep(5)
        self.click1(SignUpPage.payBtn)
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.frame(0)
        self.click1(SignUpPage.netBanking)
        self.click1(SignUpPage.sbibank)
        self.click1(SignUpPage.paymentBtn)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(5)
        self.click(SignUpPage.successBtn)
        # complete the OTP and KYC manually

# verify subscribed premium plan details in plan details Tab
    def verify_SubcribedPremiumPlan(self,email,password,liter,referRs,planprice):
        log = self.getLogger()
        self.login(email,password)
        # verify free water and voucher
        self.driver.find_element(By.XPATH, "(//b[contains(.,'"+str(liter)+"L free water*')])[1]").is_displayed()
        # Bug in this
        #self.driver.find_element(By.XPATH, "(//b[contains(.,'₹ "+str(referRs)+" Shopping Voucher')])[1]").is_displayed()
        # verify plan details
        self.click(SignUpPage.planDetailsTab)
        planname = self.getText(SignUpPage.subscribedName)
        assert 'Premium' in planname, 'Plan name not displayed'
        log.info('Plan name displayed')
        planliter = self.getText(SignUpPage.planliter)
        assert 'Unlimited water' == planliter, 'liter not displayed'
        assert self.driver.find_element(By.XPATH,"//div[@class='planPrice'][text()='₹ "+str(planprice)+"']").is_displayed(),'Plan amount not displayed'
        log.info('Plan Amount displayed')

# verify renew premium plan
    def verify_renewPremiumPlan(self,email,password):
        log = self.getLogger()
        self.login(email,password)
        self.click(SignUpPage.planDetailsTab)
        self.click(SignUpPage.renewplanLink)




























































































































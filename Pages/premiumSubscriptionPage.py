import time
from datetime import date

from selenium.webdriver.common.by import By

from Locators.smartWaterSubscription import SignUpPage
from utilities import XLUtils
from utilities.XLUtils import *
from utilities.BaseClass import BaseClass
from Locators.premiumSubscription import premiumPage


class premiumSubscriptionPage(BaseClass):

    def login(self,email,password):
        self.click(SignUpPage.loginBtn)
        self.send_keys(SignUpPage.loginUN, email)
        self.send_keys(SignUpPage.loginPWD, password)
        self.click(SignUpPage.submitLoginBtn)

# verify premium landing page
    def verify_premiumLandingPage(self,depositAmt,charge):
        log = self.getLogger()
        depo = self.getText(premiumPage.securityDeposit)
        deposit = ''
        for i in depo:
            if i.isdigit():
                deposit = deposit + i
        assert int(deposit) == depositAmt,'Deposit Amount not displayed'
        log.info('Deposit Amount displayed')
        monthCharge = self.getText(premiumPage.monthlyCharge)
        assert str(charge) in monthCharge, 'Monthly charge not displayed'
        log.info('Monthly charge displayed')
        time.sleep(5)
        self.click(premiumPage.subscribeNow1)
        assert self.driver.find_element(By.XPATH,"//a[text()='Sign Up']"),'Sign Up not displayed'
        log.info('Sign Up displayed')
        self.driver.back()
        self.click(premiumPage.subscribeNow2)
        assert self.driver.find_element(By.XPATH,"//a[text()='Sign Up']"),'Sign Up not displayed'
        log.info('Sign Up displayed')
        self.driver.back()
        self.click(premiumPage.subscribeNow3)
        assert self.driver.find_element(By.XPATH,"//a[text()='Sign Up']"),'Sign Up not displayed'
        log.info('Sign Up displayed')
        self.driver.back()
        self.click(premiumPage.subscribeNow4)
        assert self.driver.find_element(By.XPATH, "//a[text()='Sign Up']"),'Sign Up not displayed'
        log.info('Sign Up displayed')
        self.driver.back()

# verify premium plan details without sign up into the account
    def verify_PremiumPlan(self,month,value,depositAmount):
        log = self.getLogger()
        self.click(SignUpPage.menu_planLink)
        time.sleep(3)
        try:
            ele = self.driver.find_element(By.XPATH,"//div[@data-tier='silver'][contains(.,'Silver')]")
            if ele.is_displayed():
                raise Exception('Premium not activated')
        except:
            log.info("Premium Activated")
        monthtext = self.getText(SignUpPage.premiummonth)
        month_1 = ''
        assert month in month_1, 'Month not displayed'
        log.info('month displayed')
        for i in monthtext:
            if i.isdigit():
                month_1 = month_1 + i
        assert int(month_1) == month,'1 Month not displayed'
        log.info('1 Month displayed')
        monthprice = self.getText(SignUpPage.premiumPrice)
        price = ''
        assert month in price,'Price per Month not displayed'
        log.info('Price per month displayed')
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

# Subscribe to premium plan
    def subsribe_premiumPlan(self,password,planAmt,depositAmt,finalValue):
        log = self.getLogger()
        self.click(SignUpPage.menu_planLink)
        self.click1(SignUpPage.premiumProceedToPay)
        username = "Test_" + self.random_generatorString()
        email = 'premium' + self.random_generator() + "@gmail.com"
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
        self.click(SignUpPage.successBtn)
        time.sleep(5)
        # KYC pending

# verify subscribed premium plan details in plan details Tab
    def verify_SubcribedPremiumPlan(self,email,password,liter,referRs,planprice):
        log = self.getLogger()
        self.login(email,password)
        self.click(SignUpPage.menu_profileLink)
        # Customer dashboard Get the referral code and save it in excel
        referralCode = self.driver.find_element(By.XPATH, "(//h2[@class='heading02 text-right'])[2]").text
        RC = referralCode.split(':')[-1]
        RCode = RC.strip()
        XLUtils.writeData(excel, 'SignUp', 30, 9, RCode)
        # verify free water and voucher
        self.driver.find_element(By.XPATH, "(//b[contains(.,'"+str(liter)+"L free water*')])[1]").is_displayed()
        # Bug in this
        #self.driver.find_element(By.XPATH, "(//b[contains(.,'₹ "+str(referRs)+" Shopping Voucher')])[1]").is_displayed()
        # verify plan details
        time.sleep(5)
        self.click(SignUpPage.planDetailsTab)
        planname = self.getText(SignUpPage.subscribedName)
        assert 'Premium' in planname, 'Plan name not displayed'
        log.info('Plan name displayed')
        planliter = self.getText(SignUpPage.planliter)
        assert 'Unlimited water' == planliter, 'liter not displayed'
        assert self.driver.find_element(By.XPATH,"//div[@class='planPrice'][text()='₹ "+str(planprice)+"']").is_displayed(),'Plan amount not displayed'
        log.info('Plan Amount displayed')
        # verify history
        self.click(SignUpPage.rechargeHisTab)
        # Get the current date
        currentDate = date.today()
        cd = currentDate.strftime("%d-%m-%Y")
        # Get the recharge date from history
        rechargeDate = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[1])[1]").text
        rdt = rechargeDate.split(':')[-1]
        date1 = rdt.strip()
        assert cd == date1,'Rechrage date not displayed'
        log.info('Recharge date displayed')
        # Get the recharge date from history and match with plan amount
        rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
        rAmt = rechargeAmt.split(':')[-1]
        amt = rAmt.strip()
        assert planprice == int(amt), 'Amount not displayed'
        log.info('Amount displayed')

# verify renew premium plan and recharge amount
    def verify_renewPremiumPlan(self,email,password,finalValue):
        log = self.getLogger()
        self.login(email,password)
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.planDetailsTab)
        self.click(SignUpPage.renewplanLink)
        plan = self.getText(SignUpPage.premiumplan)
        assert 'Premium' in plan, 'Premium plan page not displayed'
        log.info('Premium plan page displayed')
        self.click(SignUpPage.rechargePrePlan)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'1 Month')]").is_displayed()
        TotalPayAmount = self.getText(SignUpPage.totalPayAmount)
        finalPay = ''
        for i in TotalPayAmount:
            if i.isdigit():
                finalPay = finalPay + i
        time.sleep(4)
        assert int(finalPay) == finalValue, "Incorrect Total Pay Amount"
        log.info("Displayed correct total pay amount")

# Sign up premium plan with referral code
    def verify_signupPremPlanWithRefCode(self,refCode,actualAmt,depositAmt):
        log = self.getLogger()
        username = "Test_" + self.random_generatorString()
        email = self.random_generator() + "@gmail.com"
        mobile = "95" + self.random_generatordigits()
        self.click(premiumPage.subscribeNow1)
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
        self.clickAndSendText(SignUpPage.referralBox,refCode)
        time.sleep(5)
        ele = self.driver.find_element(By.XPATH,"//button[@type='submit']//span[contains(.,'Sign Up For 7 Days Trial')]")
        self.driver.execute_script("arguments[0].click();", ele)
        self.click1(SignUpPage.premiumProceedToPay)
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
        planAmt = self.getText(premiumPage.premiumPlanamt)
        preplanAmt = ''
        for j in planAmt:
            if j.isdigit():
                preplanAmt = preplanAmt + j
        planamount = actualAmt - 100
        assert str(planamount) in planAmt, 'Discount not applied to plan amount'
        log.info('Discount applied to plan amount')

        finalValue = planamount + depositAmt

        TotalPayAmount = self.getText(SignUpPage.totalPayAmount)
        finalPay = ''
        for i in TotalPayAmount:
            if i.isdigit():
                finalPay = finalPay + i
        time.sleep(4)

        assert int(finalPay) == finalValue, "Discount not applied"
        log.info("Discount applied")
        self.click1(SignUpPage.payBtn)
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.frame(0)
        self.click1(SignUpPage.netBanking)
        self.click1(SignUpPage.sbibank)
        self.click1(SignUpPage.paymentBtn)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.click(SignUpPage.successBtn)
        self.driver.switch_to.window(window_before)
        time.sleep(5)
        self.click(SignUpPage.menu_profileLink)
        self.click(SignUpPage.rechargeHisTab)
        rechargeAmt = self.driver.find_element(By.XPATH,"(//div[@class='history-box border-right']//ul//li[2])[1]").text
        rAmt = rechargeAmt.split(':')[-1]
        amt = rAmt.strip()
        assert planamount == int(amt), 'Amount not displayed with Discount'
        log.info('Amount displayed with Discount')

# verify menu in premium plan - Plan, How it work and Refer and Earn











from selenium.webdriver.common.by import By

class smartAC:

    # Sign Up
    smartAClink = (By.XPATH,"//a[text()='Smart Air Conditioner']")
    smartBuyNow = (By.XPATH,"//div[@class='item ac__banner']//a[text()='Smart Buy Now']")
    acSignUp = (By.XPATH,"//span[contains(text(),'Sign Up')]")

    # plan name and amount
    ACPlan = (By.XPATH,"//strong[contains(.,'Inverter 1.6T 3-Star Smart Ac')]")
    downpayment = (By.XPATH, "//strong[contains(.,'Down Payment')]")
    monthlyinstall = (By.XPATH,"//strong[contains(.,'Monthly instalment')]")
    duration = (By.XPATH, "//span[contains(.,'Months duration')]")
    payBtn = (By.XPATH, "//span[@class='v-btn__content']")

    # Customer dashboard
    username = (By.XPATH, "//h3[@class='user-name']")
    subscribeMsg = (By.XPATH, "//label[@for='Ekyc_pending']")
    subscribeNow = (By.XPATH,"(//a[text()='Subscribe Now'])[1]")

    # Payment details
    paymentDetails = (By.XPATH,"//ul[@class='account-tabs']//a[text()='Payment Details']")
    planalertmsg = (By.XPATH, "//span[@class='alert']")
    plansubscribe = (By.XPATH, "//span[@class='alert']/../a")

    # Recharge History
    paymentHistory = (By.XPATH, "//ul[@class='account-tabs']//a[text()='Payment History']")
    rechHisalert = (By.XPATH, "//div[@class='alert']")

    # Review and Pay
    step1 = (By.XPATH,"(//span[@class='mb-2 review-section-tile'])[1]")
    acplanname = (By.XPATH,"//span[@class='review-pay-title']//following-sibling::span[@class='review-address-text']")
    acplandetails = (By.XPATH,"//span[@class='review-pay-title']//following-sibling::span[@class='success--text pay-amount']")
    termsAndCondilink = (By.XPATH,"//strong[contains(.,'Terms & Conditions')]")


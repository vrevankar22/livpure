from selenium.webdriver.common.by import By


class smartRO:

    # Sign Up
    smartROlink = (By.XPATH,"//a[text()='Smart Ro']")
    subscribeNow = (By.XPATH,"(//a[text()='Subscribe Now'])[1]")
    signUpBtn = (By.XPATH,"//span[contains(text(),'Sign Up')]")

    # plan name and amount
    smartBuyPlan = (By.XPATH,"//strong[contains(.,'Zinger Smart')]")
    downpayment = (By.XPATH,"//strong[contains(.,'Down Payment of Pay')]")
    monthlyinstall = (By.XPATH,"//span[contains(.,'Monthly Installation')]")
    duration = (By.XPATH,"//span[contains(.,'Months duration')]")
    payBtn = (By.XPATH,"//span[@class='v-btn__content']")



    # Customer dashboard
    username = (By.XPATH,"//h3[@class='user-name']")
    subscribeMsg = (By.XPATH,"//label[@for='Ekyc_pending']")

    # Plan details
    planalertmsg = (By.XPATH,"//span[@class='alert']")
    plansubscribe = (By.XPATH,"//span[@class='alert']/../a")

    # Recharge History
    rechHisalert = (By.XPATH,"//div[@class='alert']")





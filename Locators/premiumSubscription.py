from selenium.webdriver.common.by import By


class premiumPage:

    # menu link
    menu_howItwork = (By.XPATH,"//ul[@class='menu-list']//a[@data-scroll='#smart-steps']")

    subscribeNow1 = (By.XPATH,"//a[@class='smartbuynow  load-fadein active showme']")

    monthly = (By.XPATH,"//a[@class='smartbuynow  load-fadein active showme']//preceding-sibling::p")
    securityDeposit = (By.XPATH,"(//p[contains(.,'100% Refundable Security Deposit')]//following::h4)[1]")
    monthlyCharge = (By.XPATH,"(//p[contains(., 'Subscription for lifetime')] // following::h4)[1]")
    premiumPlanamt = (By.XPATH,"(//span[@class='success--text pay-amount'])[1]")
    depositAmt = (By.XPATH,"//span[@class='success--text']")









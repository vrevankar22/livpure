from selenium.webdriver.common.by import By


class premiumPage:

    subscribeNow1 = (By.XPATH,"//a[@class='smartbuynow  load-fadein active showme']")
    subscribeNow2 = (By.XPATH,"//a[@class='smartbuynow'][contains(.,'Subscribe Now')]")
    subscribeNow3 = (By.XPATH,"//a[contains(@class,'advantage__btn')]//following::a[contains(text(),'Subscribe Now')]")
    subscribeNow4 = (By.XPATH,"//a[@class='smartbuynow smartbuynow-zinger'][contains(.,'Subscribe Now')]")

    securityDeposit = (By.XPATH,"(//p[contains(.,'100% Refundable Security Deposit')]//following::h4)[1]")
    monthlyCharge = (By.XPATH,"(//p[contains(., 'Subscription for lifetime')] // following::h4)[1]")
    premiumPlanamt = (By.XPATH,"(//span[@class='success--text pay-amount'])[1]")









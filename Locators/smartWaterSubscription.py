from selenium.webdriver.common.by import By

class SignUpPage:
# Fill Sign Up Details
    subscribeBtn = (By.XPATH, "//a[@class='btn subscribe-now']")
    signUpBtn = (By.XPATH, "//a[text()='Sign Up']")
    yourNameTxtBox = (By.XPATH, "//input[@name='name']")
    emailTxtBox = (By.XPATH, "//input[@name='email']")
    mobileTxtBox = (By.XPATH, "//input[@name='phone']")
    cityDropdown = (By.XPATH, "//div[@aria-haspopup='listbox']")
    passwordTxtBox = (By.XPATH, "//input[@name='password']")
    passwordview = (By.XPATH, "(//i[contains(@class,'v-icon notranslate v-icon--link mdi mdi-eye-off theme--light')])[1]")
    submitSignUpBtn = (By.XPATH,"//button[@type='submit']//span[contains(.,'Sign Up For 7 Days Trial')]")
    emailexistMsg = (By.XPATH,"//div[@class='v-alert__content']")
    referralBox = (By.XPATH,"//input[@name='referralCode']")

# Login into the account
    loginBtn = (By.XPATH,"//a[text()='Log In']")
    loginUN = (By.XPATH,"//input[@name='username']")
    loginPWD = (By.XPATH,"//input[@name='password']")
    submitLoginBtn = (By.XPATH,"//button[@type='submit']")

# verify Forgot password
    forgotPWD = (By.XPATH,"//a[text()='Forgot password?']")
    emailIdField = (By.XPATH,"//input[@placeholder='Email ID / Registered phone number']")
    proceedBtn = (By.XPATH,"//input[@value='Proceed']")
    OTPSubmitBtn = (By.XPATH,"//input[@value='Submit']")

# Select the Plan - Silver
    silverPlanTab = (By.XPATH,"//div[@data-tier='silver'][contains(.,'Silver')]")
    silverltrs = (By.XPATH,"(//div['plan-details-silver']//strong)[1]")
    silverAddionalUsage = (By.XPATH,"//span[text()='Additional usage @ ₹3.6 / Litre']")
    silverPlan_text = (By.XPATH,"(//div[@id='tabsilver']//div[contains(text(),'Select Convenient Plan Duration')])[1]")
    silver12_radio = (By.XPATH,"//div[@id='tabsilver']//button[@data-duration='12']")
    silver6_radio = (By.XPATH,"//div[@id='tabsilver']//button[@data-duration='6']")
    silver1_radio = (By.XPATH,"(//div[@id='tabsilver']//button[@data-duration='1'])[1]")
    proceedToPaySilver = (By.XPATH,"//button[@id='silver']//span[text()='Proceed to Pay']")

# Select the Plan - Gold
    goldPlanTab = (By.XPATH,"//div[@data-tier='gold'][contains(.,'Gold')]")
    proceedToPayGold = (By.XPATH,"//button[contains(@class,'subscribe-action-button')][@id='gold']")

# Installation Address
    personName = (By.XPATH,"(//div[@class='disabled-inputs']//span)[1]")
    personEmail = (By.XPATH,"(//div[@class='disabled-inputs']//span)[2]")
    personMobile = (By.XPATH,"(//div[@class='disabled-inputs']//span)[3]")

    addressLine1 = (By.XPATH,"//label[text()='Flat / House / Floor / Building']/../input")
    addressLine2 = (By.XPATH,"//label[text()='Colony / Street / Locality']/../input")
    pincode = (By.XPATH,"//label[text()='6 digit pincode (e.g. 110011)']/../input")
    areaDropdown = (By.XPATH,"(//div[@aria-haspopup='listbox'])[1]")
    IAddcityDropdown = (By.XPATH,"(//div[@aria-haspopup='listbox'])[2]")
    altmobileNo = (By.XPATH,"//input[@name='alternatePhNo']")
    altmobileNumBox = (By.XPATH,"//span[@class='show-alternate']")
    saveAndContinueBtn = (By.XPATH,"//div//button[@type='submit']//span[contains(text(),'Save & Continue')]")

    totalPayAmount = (By.XPATH,"//span[contains(text(),'Payable Amount')]//span[@class='success--text pay-amount']")
    payBtn = (By.XPATH,"(//span[contains(@class,'v-btn__content')][contains(text(),'Pay')])[1]")
    netBanking = (By.XPATH, "//div[text()='Netbanking']")
    sbibank = (By.XPATH, "//div[text()='SBI']")
    paymentBtn = (By.XPATH, "//div[@id='footer']//span[2]")
    successBtn = (By.XPATH, "//button[text()='Success']")
    paymentId = (By.XPATH,"//li[contains(text(),'Payment ID')]//strong")

# Customer Dashboard
    custDashboard = (By.XPATH,"//a[text()='Customer Dashboard']")
    whatsappicon = (By.XPATH,"//div[@class='large-screen-only']//h2[contains(.,'Referral Code')]//a[@id='wshare']")
    facebookicon = (By.XPATH,"//div[@class='large-screen-only']//h2[contains(.,'Referral Code')]//a[@data-tracking='facebook-share']")
    fbID = (By.XPATH,"//input[@id='email']")
    fbPwd = (By.XPATH,"//input[@id='pass']")
    fbLogin = (By.XPATH,"//input[@value='Log In']")
    knowMore = (By.XPATH,"//a[@onclick='knowMore()'][text()='Know more']")
    invitelink = (By.XPATH,"//a[contains(text(),'Invite')]")
    referEarnBtn = (By.XPATH,"//span[text()='Refer & Earn']")
    inviteTab = (By.XPATH,"//button[text()='Invite']")
    inviteRefCode = (By.XPATH,"//input[@class='RefCode']")
    copyCode = (By.XPATH, "//img[@alt='Livpuresmart Copyicon Icon']")
    codeToolTip = (By.XPATH,"//span[@class='tooltiptext']")
    inviteWhatsapp = (By.XPATH,"(//td[contains(.,'WhatsApp')])[1]")
    inviteFB = (By.XPATH,"(//td[contains(.,'Facebook')])[1]")
    howdoesitwork = (By.XPATH,"//h2[@id='howworklink']")
    inviteTC = (By.XPATH,"//a[text()='T&C Apply*']")

    ReferralHistory = (By.XPATH,"//button[text()='Referrals History']")
    inviteNowBtn = (By.XPATH,"//span[text()='Invite Now']")

    leaderBoard = (By.XPATH,"//button[text()='Leaderboard']")

# Plan Details Tab
    planDetailsTab = (By.XPATH,"//ul[@class='account-tabs']//a[text()='Plan Details']")
    renewplanLink = (By.XPATH,"//a[@class='reviewlink']")
    silverplan = (By.XPATH,"(//div[@class='planTop d-flex'])[1]")
    goldplan = (By.XPATH,"(//div[@class='planTop d-flex'])[2]")
    platinumplan = (By.XPATH,"(//div[@class='planTop d-flex'])[3]")
    titaniumplan = (By.XPATH,"(//div[@class='planTop d-flex'])[4]")
    updateNowBtn = (By.XPATH,"//a[text()='Update Now']")
    proceedToPayBtn = (By.XPATH,"//a[text()='Proceed to Pay']")

# Change Password
    changePWDTab = (By.XPATH,"//a[text()='Change Password']")
    oldPWD = (By.XPATH,"//input[@name='password']")
    newPWD = (By.XPATH,"//input[@name='newpassword']")
    confirmPWD = (By.XPATH,"//input[@name='confirmpassword']")
    changePWDBtn = (By.XPATH,"//input[@value='Change Password']")
    profileicon = (By.XPATH,"(//div[@class='user-account'])[1]")
    logout = (By.XPATH,"(//a[text()='Logout'])[1]")

# Menu Tabs
    menu_productLink = (By.XPATH,"//ul[@class='menu-list']//a[text()='Plans']")
    menu_planLink = (By.XPATH,"//ul[@class='menu-list']//a[text()='Plans']")
    menu_proceedToPay = (By.XPATH,"//button[@id='silver']")

    menu_HowItWorkLink = (By.XPATH,"//ul[@class='menu-list']//a[@data-scroll='#how-works']")
    desktop_AndroidPS = (By.XPATH,"//div[@class='appLinks_Zero desktopOnly']//img[@alt='Android Play Store']")
    desktop_ApplePS = (By.XPATH,"//div[@class='appLinks_Zero desktopOnly']//img[@alt='Apple Play Store']")

    menu_ReferEarnLink = (By.XPATH,"//ul[@class='menu-list']//a[text()='Refer & Earn']")
    menu_invitenow = (By.XPATH,"//h2[text()='Refer Friends & Earn']//following-sibling::a[text()='Invite Now']")

    menu_profileLink = (By.XPATH,"//ul[@class='menu-list']//a[text()='Profile']")

# upload KYC page
    uploadkycBtn = (By.XPATH,"//a[contains(.,'Upload Ekyc')]")
    verifyBtn = (By.XPATH,"//button[@id='verify']")








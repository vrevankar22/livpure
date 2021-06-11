import pytest

from Pages.smartWaterSubscriptionPage import smartWaterSubscriptionPage
from utilities.XLUtils import *

class TestSmartWaterSubscription(smartWaterSubscriptionPage):

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_menu_link
    def test_verify_menu_link(self):
        self.verify_menu_link()

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_signUp
    def test_signUp(self):
        self.SignUp(readData(excel,'SignUp',2,1),readData(excel,'SignUp',2,2),
                    readData(excel,'SignUp',2,3),readData(excel,'SignUp',2,5))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verifyMandatoryField
    @pytest.mark.depends(on=['test_signUp'])
    def test_verifyMandatoryField(self):
        self.verifyMandatoryField(readData(excel,'SignUp',2,1),readData(excel,'SignUp',2,2),
                                  readData(excel,'SignUp',2,3),readData(excel,'SignUp',2,5))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_invalid_details
    def test_verify_invalid_details(self):
        self.verify_invalid_details()

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::verify_processTillkycPage
    @pytest.mark.depends(on=['test_signUp'])
    def test_verify_processTillkycPage(self):
        self.verify_processTillkycPage(readData(excel,'SignUp',2,1),readData(excel,'SignUp',2,5),readData(excel,'SignUp',2,10),readData(excel,'SignUp',2,2),
                        readData(excel,'SignUp',2,3),readData(excel,'SignUp',2,16),readData(excel,'SignUp',3,16),readData(excel,'SignUp',4,16))

# upload_KYCDoc

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_login_invalidcredentials
    def test_login_invalidcredentials(self):
        self.login_invalidcredentials(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_ForgotPassword_Invalid
    def test_verify_ForgotPassword_Invalid(self):
       self.verify_ForgotPassword_Invalid()

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_ForgotPassword_valid
    def test_verify_ForgotPassword_valid(self):
        self.verify_ForgotPassword_valid(readData(excel,'SignUp',15,1))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_CustomerDashboard
    def test_verify_CustomerDashboard(self):
        self.verify_CustomerDashboard(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),readData(excel,'SignUp',15,4),
                                      readData(excel,'SignUp',15,2),readData(excel,'SignUp',15,5),readData(excel,'SignUp',15,6),
                                      readData(excel,'SignUp',15,7),readData(excel,'SignUp',15,8),readData(excel,'SignUp',21,1),readData(excel,'SignUp',21,2))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_ReferAndEarn
    def test_verify_ReferAndEarn(self):
        self.verify_ReferAndEarn(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),
                                 readData(excel,'SignUp',18,1),readData(excel,'SignUp',15,9))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_ReferralHistory
    def test_verify_ReferralHistory(self):
        self.verify_ReferralHistory(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_ReferralHistory
    def test_verify_LeaderBoard(self):
        self.verify_LeaderBoard(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_PlanDetails
    def test_verify_PlanDetails(self):
        self.verify_PlanDetails(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_SilverPlanPrice
    def test_verify_SilverPlanPrice(self):
        self.verify_SilverPlanPrice(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),
                                    readData(excel,'SignUp',3,9),readData(excel,'SignUp',4,9),readData(excel,'SignUp',5,9),
                                    readData(excel,'SignUp',3,10),readData(excel,'SignUp',4,10),readData(excel,'SignUp',5,10))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_GoldPlanPrice
    def test_verify_GoldPlanPrice(self):
        self.verify_GoldPlanPrice(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),
                                    readData(excel,'SignUp',3,9),readData(excel,'SignUp',4,9),readData(excel,'SignUp',5,9),
                                    readData(excel,'SignUp',3,11),readData(excel,'SignUp',4,11),readData(excel,'SignUp',5,11))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_PlatinumPlanPrice
    def test_verify_PlatinumPlanPrice(self):
        self.verify_PlatinumPlanPrice(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),
                                    readData(excel,'SignUp',3,9),readData(excel,'SignUp',4,9),readData(excel,'SignUp',5,9),
                                    readData(excel,'SignUp',3,12),readData(excel,'SignUp',4,12),readData(excel,'SignUp',5,12))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_TitaniumPlanPrice
    def test_verify_TitaniumPlanPrice(self):
        self.verify_TitaniumPlanPrice(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3),
                                    readData(excel,'SignUp',3,9),readData(excel,'SignUp',4,9),readData(excel,'SignUp',5,9),
                                    readData(excel,'SignUp',3,13),readData(excel,'SignUp',4,13),readData(excel,'SignUp',5,13))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_SilverChangePlan
    def test_verify_SilverChangePlan(self):
        self.verify_SilverChangePlan(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_GoldChangePlan
    def test_verify_GoldChangePlan(self):
        self.verify_GoldChangePlan(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_PlatinumChangePlan
    def test_verify_PlatinumChangePlan(self):
        self.verify_PlatinumChangePlan(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_TitaniumChangePlan
    def test_verify_TitaniumChangePlan(self):
        self.verify_TitaniumChangePlan(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_changePassword
    def test_verify_changePassword(self):
        self.verify_changePassword(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_diffPWD
    def test_verify_diffPWD(self):
        self.verify_diffPWD(readData(excel,'SignUp',15,1),readData(excel,'SignUp',15,3))

# py.test testcases/test_smartWaterSubscription.py::TestSmartWaterSubscription::test_verify_signupWithRefCode
    def test_verify_signupWithRefCode(self):
        self.verify_signupWithRefCode(readData(excel,'SignUp',15,9),readData(excel,'SignUp',15,4))






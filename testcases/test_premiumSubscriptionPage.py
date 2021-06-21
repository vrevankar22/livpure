from Pages.premiumSubscriptionPage import premiumSubscriptionPage
from utilities.XLUtils import *
from pytest import mark

class TestPremiumSubscription(premiumSubscriptionPage):

# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_verify_premiumLandingPage
    def test_verify_premiumLandingPage(self):
        self.verify_premiumLandingPage(readData(excel,'SignUp',30,3),readData(excel,'SignUp',30,2))

# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_verify_PremiumPlan
    def test_verify_PremiumPlan(self):
        self.verify_PremiumPlan(readData(excel,'SignUp',30,1),readData(excel,'SignUp',30,2),readData(excel,'SignUp',30,3))

# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_subsribe_premiumPlan
    @mark.depends(on=['test_verify_PremiumPlan'])
    def test_subsribe_premiumPlan(self):
        self.subsribe_premiumPlan(readData(excel,'SignUp',30,8),readData(excel,'SignUp',30,2), readData(excel,'SignUp',30,3),readData(excel,'SignUp',30,4))

# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_verify_SubcribedPremiumPlan
    def test_verify_SubcribedPremiumPlan(self):
        self.verify_SubcribedPremiumPlan(readData(excel,'SignUp',30,6),readData(excel,'SignUp',30,8),
                                         readData(excel,'SignUp',18,2),readData(excel,'SignUp',18,1),readData(excel,'SignUp',30,2))

# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_verify_renewPremiumPlan
    def test_verify_renewPremiumPlan(self):
        self.verify_renewPremiumPlan(readData(excel,'SignUp',30,6),readData(excel,'SignUp',30,8),readData(excel,'SignUp',30,2))


# py.test testcases/test_premiumSubscriptionPage.py::TestPremiumSubscription::test_verify_signupPremPlanWithRefCode
    def test_verify_signupPremPlanWithRefCode(self):
        self.verify_signupPremPlanWithRefCode(readData(excel,'SignUp',30,9),readData(excel,'SignUp',30,2),readData(excel,'SignUp',30,3))


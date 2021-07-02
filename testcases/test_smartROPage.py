from Pages.smartROPage import smartROPage
from utilities.XLUtils import *

class TestsmartRO(smartROPage):

# py.test testcases/test_smartROPage.py::TestsmartRO::test_verify_SmartROlandingPage
    def test_verify_SmartROlandingPage(self):
        self.verify_SmartROlandingPage()

# py.test testcases/test_smartROPage.py::TestsmartRO::test_signUp_smartRO
    def test_signUp_smartRO(self):
        self.signUp_smartRO(readData(excel,'SmartRO',2,5),readData(excel,'SmartRO',2,6))

# py.test testcases/test_smartROPage.py::TestsmartRO::test_verify_profileTabs
    def test_verify_profileTabs(self):
        self.verify_profileTabs(readData(excel,'SmartRO',2,2),readData(excel,'SmartRO',2,5),readData(excel,'SmartRO',2,1),
                                readData(excel,'SmartRO',2,3),readData(excel,'SmartRO',2,6))

# py.test testcases/test_smartROPage.py::TestsmartRO::test_verify_smartBuyplan
    def test_verify_smartBuyplan(self):
        self.verify_smartBuyplan(readData(excel,'SmartRO',2,2),readData(excel,'SmartRO',2,5),readData(excel,'SmartRO',2,7),
                                readData(excel,'SmartRO',2,8),readData(excel,'SmartRO',2,9),readData(excel,'SmartRO',2,10))
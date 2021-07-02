from Pages.smartACPage import smartACPage
from utilities.XLUtils import *


class TestsmartAC(smartACPage):

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_AClandingPage
    def test_verify_AClandingPage(self):
        self.verify_AClandingPage()

# py.test testcases/test_smartACPage.py::TestsmartAC::test_signUp_smartAC
    def test_signUp_smartAC(self):
        self.signUp_smartAC(readData(excel, 'SmartAC', 2, 5), readData(excel, 'SmartAC', 2, 6))

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_ACprofileTabs
    def test_verify_ACprofileTabs(self):
        self.verify_ACprofileTabs(readData(excel, 'SmartAC', 2, 2), readData(excel, 'SmartAC', 2, 5),readData(excel, 'SmartAC', 2, 1),
                                readData(excel, 'SmartAC', 2, 3), readData(excel, 'SmartAC', 2, 6))

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_ACsmartBuyplan
    def test_verify_ACsmartBuyplan(self):
        self.verify_ACsmartBuyplan(readData(excel, 'SmartAC', 2, 2), readData(excel, 'SmartAC', 2, 5),readData(excel, 'SmartAC', 2, 7),
                                 readData(excel, 'SmartAC', 2, 8), readData(excel, 'SmartAC', 2, 9), readData(excel, 'SmartAC', 2, 10))

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_AcinstallationAddress
    def test_verify_AcinstallationAddress(self):
        self.verify_AcinstallationAddress(readData(excel,'SmartAC',2,2),readData(excel,'SmartAC',2,5),readData(excel,'SmartAC',2,1),readData(excel,'SmartAC',2,3))

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_editAddress
    def test_verify_editAddress(self):
        self.verify_editAddress(readData(excel,'SmartAC',2,2),readData(excel,'SmartAC',2,5),readData(excel,'SmartAC',5,5))

# py.test testcases/test_smartACPage.py::TestsmartAC::test_verify_ReviewAndPay
    def test_verify_ReviewAndPay(self):
        self.verify_ReviewAndPay(readData(excel,'SmartAC',2,2),readData(excel,'SmartAC',2,5),readData(excel,'SmartAC',2,7),readData(excel,'SmartAC',2,6),
                                 readData(excel,'SmartAC',2,11),readData(excel,'SmartAC',2,12))




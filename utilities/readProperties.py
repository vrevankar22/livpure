import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','url')
        return url

    @staticmethod
    def getExcelsheet():
        excel = config.get('common info','excel')
        return excel

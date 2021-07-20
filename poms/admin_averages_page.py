from selenium.webdriver.chrome.webdriver import WebDriver


class AdminAveragesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def DevOpsStackTable(self):
        return self.driver.find_element_by_id('DevOpsStack')

    def AWSStackTable(self):
        return self.driver.find_element_by_id('AWSStack')

    def JavaStackTable(self):
        return self.driver.find_element_by_id('JavaStack')

    def averagesFromJavaStackTable(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"JavaStack\"]/tr/td[2]")

    def averagesFromAWSStackTable(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"JavaStack\"]/tr/td[2]")

    def averagesFromDevOpsStackTable(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"JavaStack\"]/tr/td[2]")
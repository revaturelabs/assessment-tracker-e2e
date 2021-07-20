from selenium.webdriver.chrome.webdriver import WebDriver


class AdminAveragesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def dev_ops_stack_table(self):
        return self.driver.find_element_by_id('DevOpsStack')

    def aws_stack_table(self):
        return self.driver.find_element_by_id('AWSStack')

    def java_stack_table(self):
        return self.driver.find_element_by_id('JavaStack')

    def averages_from_java_stack_table(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"JavaStack\"]/tr/td[2]")

    def averages_from_aws_stack_table(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"AWSStack\"]/tr/td[2]")

    def averages_from_dev_ops_stack_table(self):
        return self.driver.find_elements_by_xpath("//*[@id=\"DevOpsStack\"]/tr/td[2]")
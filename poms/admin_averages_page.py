from selenium.webdriver.chrome.webdriver import WebDriver


class AdminAveragesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_tables(self):
        return self.driver.find_elements_by_xpath("//*/table")

    def get_table_averages(self):
        return self.driver.find_elements_by_xpath("//*/tr/td[2]")
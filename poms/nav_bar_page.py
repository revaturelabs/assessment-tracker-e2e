from selenium.webdriver.chrome.webdriver import WebDriver

class NavBarPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search_bar(self):
        return self.driver.find_element_by_id("search")

    def search_row_one(self):
        return self.driver.find_element_by_xpath('//*[@id="searchSuggestion"]/div/a')
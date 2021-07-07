from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.assessments import AssessmentsPage
from poms.batch_home_page import BatchHomePage
from poms.home_page import HomePage


def before_all(context: Context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver: WebDriver = webdriver.Chrome('drivers/chromedriver.exe', options=options)
    context.driver = driver

    context.home_page = HomePage(context.driver)
    context.batch_home = BatchHomePage(context.driver)
    context.assessments_page = AssessmentsPage(context.driver)


def after_all(context: Context):
    context.driver.quit()

from poms.admin_page import AdminPage
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.assessments import AssessmentsPage
from poms.batch_home_page import BatchHomePage
from poms.home_page import HomePage
from poms.nav_bar_page import NavBarPage


def before_all(context: Context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome('drivers/chromedriver.exe', options=options)

    context.home_page = HomePage(context.driver)
    context.batch_home_page = BatchHomePage(context.driver)
    context.assessments_page = AssessmentsPage(context.driver)
    context.nav_bar_page = NavBarPage(context.driver)
    context.admin_page = AdminPage(context.driver)

    context.driver.implicitly_wait(2)
    context.driver.maximize_window()


def after_all(context: Context):
    context.driver.quit()

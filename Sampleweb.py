import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time 

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"login-credentials\"]").click()
    time.sleep(3)
    page.locator("#user-name").click()
    time.sleep(3)
    page.locator("[data-test=\"username\"]").type("standard_user")
    time.sleep(3)
    page.locator("[data-test=\"password\"]").click()
    time.sleep(3)
    page.locator("[name='password']").type("secret_sauce")
    time.sleep(5)
    page.locator("[data-test=\"login-button\"]").click()
    time.sleep(3)
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    time.sleep(3)
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"checkout\"]").click()
    time.sleep(3)
    page.get_by_placeholder("First Name").click()
    time.sleep(3)
    page.locator("[data-test=\"firstName\"]").type("xxxx")
    time.sleep(3)
    page.locator("[data-test=\"firstName\"]").press("Tab")
    time.sleep(3)
    page.locator("[data-test=\"lastName\"]").type("yyyy")
    time.sleep(3)
    page.locator("[data-test=\"lastName\"]").press("Tab")
    time.sleep(3)
    page.locator("[data-test=\"postalCode\"]").type("345")
    time.sleep(5)
    page.locator("[data-test=\"continue\"]").click()
    time.sleep(3)
    page.locator("[data-test=\"finish\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"back-to-products\"]").click()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

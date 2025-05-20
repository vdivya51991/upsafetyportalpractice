from playwright.sync_api import sync_playwright
import time


def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #Navigate to the login page
        page.goto("https://www.tocitestaging.net/cityofrockburg/portal/account/login")
        #wait for the email field to be visible
        page.get_by_placeholder("Email").wait_for()
        page.get_by_placeholder("Email").fill("divyavaith@gmail.com")
        page.get_by_placeholder("Password").fill("Divya@1991")
        # Click the Login button
        page.get_by_role("button", name = "Sign In").click()
        # get the box containing all the elements
        locator_elements = page.locator("//div[@class='dropdown ml-auto']//a//*[@id='user-greating']")
        locator_elements.wait_for()
        locator_elements.highlight()

        time.sleep(3)
        browser.close()

  #click on the sign in button
  # assert if it goes to main home page
def main():
    login()
    #print("Hello")

if __name__ == '__main__':
    main()

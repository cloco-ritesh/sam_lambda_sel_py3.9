import logging
import sys

from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, \
    NoSuchWindowException

language_list = ['en']


class Toreta:

    @staticmethod
    def new_reservation(event, context, driver):
        try:
            print("I am new_reservation")

            # Open browser
            browser = driver

            # Clean cookies
            browser.delete_all_cookies()
            browser.set_page_load_timeout(60)

            browser.get("https://www.google.com/")
            title = browser.title
            browser.close()
            browser.quit()
            print(f"[+] Title → {title}")

        except AssertionError as msg:
            logging.error(msg)
            browser.close()
            sys.exit()

        except TimeoutException:
            logging.error('Request Time Out')
            browser.close()
            sys.exit()
        except WebDriverException:
            logging.error('------------------------ WebDriver-Error! ---------------------', exc_info=True)
            logging.error('------------------------ WebDriver-Error! END ----------------')
            browser.close()
            sys.exit()
        except NoSuchWindowException:
            logging.error('Window is gone, somehow...- NoSuchWindowException')
            sys.exit()
        except NoSuchElementException:
            logging.error('------------------------ No such element on site. ------------------------', exc_info=True)
            logging.error('------------------------ No such element on site. END ------------------------')
            browser.close()
            sys.exit()

    @staticmethod
    def update_reservation(event, context):
        print("I am update_reservation")

    @staticmethod
    def cancel_reservation(event, context):
        print("I am cancel_reservation")

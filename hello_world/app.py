from tempfile import mkdtemp
import logging
import os
from faker import Faker
import random
from selenium import webdriver

from media.toreta import Toret

language_list = ['en']

# This part make logging work locally when testing and in lambda cloud watch
if logging.getLogger().hasHandlers():
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


# Function that setup the browser parameters and return browser object.
def open_browser():
    if 'RUN_IN_BACKGROUND' in os.environ and os.environ['RUN_IN_BACKGROUND']:
        fake_user_agent = Faker()
        options = webdriver.ChromeOptions()
        options.binary_location = '/opt/chrome/chrome'
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-first-run')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-client-side-phishing-detection')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-web-security')
        options.add_argument('--lang=' + random.choice(language_list))
        options.add_argument('--user-agent=' + fake_user_agent.user_agent())
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        options.add_argument("--remote-debugging-port=9222")
        chrome = webdriver.Chrome("/opt/chromedriver", options=options)
    else:
        chrome = webdriver.Chrome(r"chromedriver")

    return chrome


# Our main Lambda function
def lambda_handler(event, context):
    # this is from event.
    from_media = "book-at"
    want_media = "toreta"
    want_action = "new_reservation"

    clazz = {
        'toreta': {
            'new_reservation': Toreta.new_reservation,
            'update_reservation': Toreta.update_reservation,
            'cancel_reservation': Toreta.cancel_reservation,
        }
    }

    cntr = clazz[want_media][want_action]

    cntr(None, None, open_browser())


if __name__ == '__main__':
    lambda_handler(None, None)

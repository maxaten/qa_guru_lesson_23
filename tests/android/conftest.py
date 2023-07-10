import pytest
from allure_commons._allure import step
from appium import webdriver
from selene.support.shared import browser

import config
from lesson_5_23_mobile_autotests_with_Browserstack.helpers.allure.attach import attach_video, add_screenshot


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = config.settings.timeout

    yield

    with step('Test case resources: '):
        attach_video(browser)
        add_screenshot(browser)

    browser.quit()
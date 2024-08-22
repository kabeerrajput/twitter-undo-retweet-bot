from Selenium_Utils import *


class TwitterBot:
    def __init__(self):
        self._selenium = SeleniumUtils()
        self.execute_process()

    def execute_process(self):
        self.login_and_navigate()
        self.undo_retweets()

    def undo_retweets(self):
        retweets_xpath = '//article//div[@data-testid="unretweet"]'
        scroll_retweets_xpath = '//article//div[@data-testid="unretweet"]' + '//ancestor::article[@aria-labelledby]'
        click_on_undo_repost = retweets_xpath + '/div'
        undo_repost = '//div[@data-testid="Dropdown"]/div[@data-testid="unretweetConfirm"]'
        hover_xpath = '//header[@role="banner"]//div[@aria-label="Account menu"]'
        retried_attempt = 0

        while True:
            retweets_elements = self._selenium.get_elements(retweets_xpath)
            if retweets_elements is None:
                print("no retweets found scrolling")
                self._selenium.driver.execute_script("window.scrollBy(0, 500);")
                self._selenium.wait_for_loading_to_finish('//div[@role="progressbar"]/div')
                retried_attempt += 1
                print(f"retried attempt {retried_attempt}")
                if retried_attempt == 50:
                    print("no retweets found scrolling")
                    break
                continue

            if len(retweets_elements) > 0:
                retried_attempt = 0
                for i in range(len(retweets_elements)):
                    self._selenium.scroll_to_element(f'({scroll_retweets_xpath})[1]')
                    self._selenium.hover_over_element(hover_xpath)
                    self._selenium.click_element(f'({click_on_undo_repost})[1]')
                    time.sleep(0.2)
                    self._selenium.click_element(undo_repost)
                    time.sleep(0.3)
    def login_and_navigate(self, username="", password=""):
        link = "https://twitter.com/"
        sign_in_button = "(//span[@class and .='Sign in'])[1]"
        username_input = "//input[@type='text' and @autocomplete='username']"
        password_input = "//input[@type='password' and @autocomplete='current-password']"
        next_button = '(//div[@role="button"]//span[.= "Next"])[1]'
        login_button = '(//div[@role="button"]//span[.= "Log in"])[1]'
        startup_loading = '//div[contains(@aria-label, "Loading")]'
        common_loading = '//div[@role="progressbar"]/div'
        after_navigate_check = "//h1[@role='heading']//a[@aria-label='X']"
        after_navigate_profile = f'//main[@role="main"]//span[.= "@{username}"]'

        self._selenium.go_to_url(link)
        self._selenium.wait_for_loading_to_finish(startup_loading)
        self._selenium.wait_for_element_intractable(sign_in_button)
        self._selenium.click_element(sign_in_button)
        self._selenium.wait_for_loading_to_finish(common_loading)
        time.sleep(3)
        self._selenium.wait_for_loading_to_finish(common_loading)
        self._selenium.switch_to_iframe()

        self._selenium.click_element(username_input)
        self._selenium.fill_keys_value(username_input, username)
        self._selenium.click_element(next_button)
        self._selenium.wait_for_loading_to_finish(common_loading)
        self._selenium.fill_keys_value(password_input, password)
        self._selenium.click_element(login_button)
        self._selenium.wait_for_loading_to_finish(common_loading)
        time.sleep(3)
        self._selenium.wait_for_loading_to_finish(startup_loading)
        self._selenium.wait_for_loading_to_finish(common_loading)
        self._selenium.wait_for_loading_to_finish(common_loading)

        self._selenium.wait_for_element_presence(after_navigate_check)
        self._selenium.go_to_url(link+username)
        self._selenium.wait_for_loading_to_finish(startup_loading)
        self._selenium.wait_for_loading_to_finish(common_loading)
        self._selenium.wait_for_element_presence(after_navigate_profile)
        self._selenium.wait_for_element_presence('//main[@role="main"]//section[@role="region"]//article')

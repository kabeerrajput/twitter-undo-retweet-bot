import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumUtils:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_url(self, url):
        try:
            print("navigating_to_URL start")
            self.driver.get(url)
            print("navigating_to_URL end")
        except Exception as e:
            print("URL not found error: ", url)

    def wait_for_element_presence(self, xpath, wait_secs=60, By=By.XPATH):
        try:
            print("wait_for_element_presence start")
            WebDriverWait(self.driver, wait_secs).until(EC.presence_of_element_located((By, xpath)))
            print("wait_for_element_presence end")
        except Exception as e:
            print(f"wait_for_element_presence Failed {e} XPath :: {xpath}")

    def wait_for_loading_to_finish(self, xpath, wait_secs=60, By=By.XPATH):
        try:
            print("wait_for_loading_to_finish start")
            element = WebDriverWait(self.driver, wait_secs).until(EC.invisibility_of_element_located((By, xpath)))
            print(f"wait_for_loading_to_finish end")
        except Exception as e:
            print(f"wait_for_loading_to_finish Failed {e} XPath :: {xpath}")

    def wait_for_element_intractable(self, xpath, wait_secs="", By=By.XPATH):
        if wait_secs == "":
            wait_secs = 60
        try:
            print("wait_for_element_intractable start")
            element = WebDriverWait(self.driver, wait_secs).until(EC.visibility_of_element_located((By, xpath)))
            print(f"wait_for_element_intractable end")
        except Exception as e:
            print(f"wait_for_element_intractable Failed {e} XPath :: {xpath}")

    def click_element(self, xpath, By=By.XPATH):
        try:
            element = self.get_element(xpath)
            if element is not False:
                element.click()
        except Exception as e:
            print(f"Click Failed:: Error {e} XPath :: {xpath}")

    def switch_to_iframe(self, iframe_path="", By=By.XPATH):
        try:
            print("switch_to_iframe start")
            wait_secs = 60
            if iframe_path == "":
                self.driver.switch_to.parent_frame()
            else:
                element = WebDriverWait(self.driver, wait_secs).until(EC.frame_to_be_available_and_switch_to_it((By, iframe_path)))
            # else:
            #     iframe_element = self.driver.find_element(iframe_path)
            #     if iframe_element is not False:
            #         self.driver.switch_to.frame(iframe_element)
            print("switch_to_iframe end")
        except Exception as e:
            print(f"switch_to_iframe Failed:: Error {e} XPath:: {iframe_path}")

    def get_element(self, xpath, By=By.XPATH):
        try:
            element = self.driver.find_element(By, xpath)
            if element not in [False, None]:
                return element
        except Exception as e:
            print(f"get_element Failed:: Error {e} XPath:: {xpath}")
            return False

    def get_elements(self, xpath, By=By.XPATH):
        try:
            elements = self.driver.find_elements(By, xpath)
            if len(elements) > 0 and elements not in [None, False]:
                return elements
        except Exception as e:
            print(f"get_elements Failed:: Error {e} XPath:: {xpath}")

    def get_element_text(self, xpath, By=By.XPATH):
        try:
            element_text = self.get_element(xpath).text
            if element_text not in ["", None, False]:
                return element_text
        except Exception as e:
            print(f"get_element_text Failed:: Error {e} XPath:: {xpath}")

    def fill_keys_value(self, xpath, keys_value, By=By.XPATH):
        try:
            element = self.get_element(xpath)
            element.send_keys(keys_value)
            time.sleep(0.5)
        except Exception as e:
            print(f"fill_keys_value Failed:: Error {e} XPath:: {xpath}")

    def scroll_to_element(self, xpath, By=By.XPATH):
        try:
            element = self.get_element(xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)
        except Exception as e:
            print(f"scroll_to_element Failed:: Error {e} XPath:: {xpath}")

    def hover_over_element(self, xpath, By=By.XPATH):
        try:
            element = self.get_element(xpath, By)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(0.2)
            print("hovered on a element")
        except Exception as e:
            print(f"hover_over_element Failed:: Error {e} XPath:: {xpath}")


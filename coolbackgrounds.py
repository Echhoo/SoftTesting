# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest10():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test10(self):
    self.driver.get("https://coolbackgrounds.io/")
    self.driver.set_window_size(1550, 838)
    self.driver.find_element(By.CSS_SELECTOR, ".particles > img").click()
    self.driver.execute_script("window.scrollTo(0,48)")
    self.driver.find_element(By.CSS_SELECTOR, ".gradient").click()
    self.driver.find_element(By.CSS_SELECTOR, ".topography > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".unsplash").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .app-nav__list-item img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".app-option__symbol > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".app-option:nth-child(2) .app-option__color:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".app-option:nth-child(3) .app-option__color:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .nav-list__name").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .nav-list__image").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .nav-list__image").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) .nav-list__image").click()
    self.driver.find_element(By.CSS_SELECTOR, ".app-download > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".app-option__symbol > svg").click()
    element = self.driver.find_element(By.LINK_TEXT, "Trianglify →")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Trianglify →").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Trianglify →").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(3) > input").send_keys("0.72")
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(4) > input").send_keys("0.26")
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(4) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(5) > input").send_keys("0.06")
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(5) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(3) > input").send_keys("0.57")
    self.driver.find_element(By.CSS_SELECTOR, ".FormControl_FormControl__2zw2M:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".Palette_random__3jaxC").click()
    self.driver.find_element(By.CSS_SELECTOR, ".Palette_random__3jaxC").click()
  

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class ZisoftTests(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://0.0.0.0:8000/")
        # make sure website opened
        self.assertEquals("Zisoft Login", self.driver.find_element_by_xpath("//h1").text)

    def test_login(self):
        # get the user name textbox
        self.usrname_field = self.driver.find_element_by_name("username")
        self.usrname_field.clear()
        # enter user name keyword and submit
        self.usrname_field.send_keys("zisoft")
        self.usrname_field.submit()
        # get the password textbox
        self.password_field = self.driver.find_element_by_name("password")
        self.password_field.clear()
        # enter password keyword and submit
        self.password_field.send_keys("Zisoft123@")
        self.password_field.submit()
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        # make sure website opened
        self.assertEquals("Home", self.driver.find_element_by_xpath("//h1").text)
        self.assertEquals("zisoft", self.driver.find_element_by_xpath("//a/span").text)

        self.driver.find_element_by_xpath("//button[@type='button']").click()
        self.driver.find_element_by_link_text("Users").click()
        self.assertEquals("Create/Edit User",
                          self.driver.find_element_by_xpath("//div[@id='portlet_add_user']/div/div").text)
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys("islam")
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id("lastName").send_keys("taha")
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("islam")
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("ghadarizk2012@gmail.com")
        self.driver.find_element_by_id("user_role_select").click()
        Select(self.driver.find_element_by_id("user_role_select")).select_by_visible_text("User")
        self.driver.find_element_by_id("user_status_select").click()
        Select(self.driver.find_element_by_id("user_status_select")).select_by_visible_text("Enabled")
        self.driver.find_element_by_id("user_language_select").click()
        Select(self.driver.find_element_by_id("user_language_select")).select_by_visible_text("English")
        self.driver.find_element_by_id("reset").click()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("Zisoft123@")
        self.driver.find_element_by_id("password_confirmation").clear()
        self.driver.find_element_by_id("password_confirmation").send_keys("Zisoft123@")
        self.driver.find_element_by_id("submit_user_form").click()
        message = self.driver.find_element_by_id("alert_container").message
        print(message)

        # def test_create_new_user(self):

        def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

    def tearDown(self):
        # logout
        # self.assertEquals("zisoft", self.driver.find_element_by_xpath("//a/span").text)
        # self.driver.find_element_by_xpath("//a/span").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # self.assertEquals("Zisoft Login", self.driver.find_element_by_xpath("//h1").text)
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver

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


    def tearDown(self):
        # logout
        self.assertEquals("zisoft", self.driver.find_element_by_xpath("//a/span").text)
        self.driver.find_element_by_xpath("//a/span").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.assertEquals("Zisoft Login", self.driver.find_element_by_xpath("//h1").text)
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

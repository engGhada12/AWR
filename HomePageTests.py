from TestCases.BaseTest import BaseTest

class HomePageTests(BaseTest):

    def test001_view_home_page(self):
        """ HPT-01
                *Test view home page*
                **Test Scenario:**
                #. Login as admin, select Home.
                """
        self.login(username=self.username, password=self.password)
        self.driver.find_element_by_link_text("Home").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='alert_container']/h1").text, "Home")

        self.driver.find_element_by_xpath("//div[@id='alert_container']/div[2]/div/a/div/div/div/small").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='show_result_user_online']/div").text,"Users Online")

        self.driver.find_element_by_xpath("//div[@id='alert_container']/div[2]/div[2]/a/div").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='show_result_successquiz']/div").text,"Success Quiz")

        self.driver.find_element_by_xpath("//div[@id='alert_container']/div[2]/div[3]/a/div/div/div/small").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='show_result']/div").text,"Watched Lessons")

        self.driver.find_element_by_xpath("//div[@id='alert_container']/div[2]/div[4]/a/div/div/div/small").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='show_result_successexam']/div/div[2]").text,"Success Exam")

        self.driver.find_element_by_xpath("//ul[2]/li/a/span").click()
        self.driver.find_element_by_link_text(u"العربيه").click()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@id='alert_container']/h1").text,"الرئيسيه")

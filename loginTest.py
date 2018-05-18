from TestCases.BaseTest import BaseTest
import uuid


class ZisoftTests(BaseTest):
    def test01_login_as_admin(self):
        """ ZST-001
        *Test login as admin*
        **Test Scenario:**
        #. Login as admin, should get home page of admin
        """
        self.login(username=self.username,password=self.password)
        # make sure website opened
        self.assertEquals("Home", self.driver.find_element_by_xpath(self.elements['page_title_path']).text)
        self.assertEquals(self.username, self.driver.find_element_by_xpath(self.elements['user_title']).text)


    def test02_login_with_wrong_username(self):
        """ ZST-002
        *Test login with wrong username*
        **Test Scenario:**
        #. Login using wrong username, should fail
        """
        self.login(username=str(uuid.uuid4()), password=self.password)
        self.assertTrue("Wrong username and/or password",self.driver.find_element_by_class_name("help-block").text)

    def test03_login_with_wrong_password(self):
        """ ZST-003
        *Test login with wrong password*
        **Test Scenario:**
        #. Login using wrong password, should fail
        """
        self.login(username=self.username,password=str(uuid.uuid4()))
        self.assertTrue("Wrong username and/or password",self.driver.find_element_by_class_name("help-block").text)


    def test04_login_with_wrong_username_wrong_password(self):
        """ ZST-04
        *Test login with wrong username and wrong password*
        **Test Scenario:**
        #. Login using wrong username and wrong password, should fail
        """
        self.login(username=str(uuid.uuid4()),password=str(uuid.uuid4()))
        self.assertTrue("Wrong username and/or password",self.driver.find_element_by_class_name("help-block").text)


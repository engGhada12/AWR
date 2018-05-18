from TestCases.BaseTest import BaseTest

class ZisoftTests(BaseTest):

    def create_new_campaign(self,CampName,Camp_failAttemp,Camp_SP):
        """ ZST-01
                *Test create new campaign with valid data*
                **Test Scenario:**
                #. Login as admin, from +new select campaign, write valid data
                save.
                """
        self.login(username=self.username, password=self.password)
        self.driver.find_element_by_xpath(self.elements['New_button']).click()
        self.driver.find_element_by_link_text("Campaigns").click()
        self.assertTrue(self.driver.find_element_by_xpath(self.elements["Create_Campaign_portlet"]).text,"Create / Edit Campaign ")
        self.driver.find_element_by_id("title").clear()
        self.driver.find_element_by_id("title").send_keys(CampName)
        self.driver.find_element_by_id("fail_attempts").clear()
        if Camp_failAttemp is not None:
            self.driver.find_element_by_id("fail_attempts").send_keys(Camp_failAttemp)
        self.driver.find_element_by_id("success_percent").clear()
        if Camp_SP is not None :
            self.driver.find_element_by_id("success_percent").send_keys(Camp_SP)
        self.driver.find_element_by_name("hide_exam").click()
        self.driver.find_element_by_xpath(self.elements["submit_button"]).click()

    def test001_create_new_campaign(self):
        """ ZST-01
                *Test create new campaign with valid data*
                **Test Scenario:**
                #. Login as admin, from +new select campaign, write valid data
                save.
                """
        self.create_new_campaign(self.CampName,self.Camp_failAttemp,self.Camp_SP)
        self.assertTrue(self.driver.find_element_by_id("alert_container").text,"Add Campaign Successfully")

    def test002_create_campaign_duplicateName(self):
        """ ZST-02
                *Test create new campaign with duplicate name*
                **Test Scenario:**
                #. Login as admin, from +new select campaign, write valid data
                save.
                """
        self.create_new_campaign(self.CampName, self.Camp_failAttemp, self.Camp_SP)
        self.assertTrue(self.driver.find_element_by_id("alert_container").text,"Error! Check the logs")

    def test003_create_campaign_with_missing_FailAttempts(self):
        """ ZST-03
                *Test create new campaign with duplicate name*
                **Test Scenario:**
                #. Login as admin, from +new select campaign, write valid data
                save.
                """
        self.create_new_campaign(self.CampName,None,self.Camp_SP)
        self.assertTrue(self.driver.find_element_by_id("fail_attempts-error").text,"This field is required.")

    def test004_create_campaign_with_missing_successPercent(self):
        """ ZST-04
                *Test create new campaign with no success percent*
                **Test Scenario:**
                #. Login as admin, from +new select campaign, write valid data
                save.
                """
        self.create_new_campaign(self.CampName,self.Camp_failAttemp,None)
        self.assertTrue(self.driver.find_element_by_id("success_percent-error").text,"This field is required.")

import unittest, random
from selenium import webdriver
from testconfig import config
from TestCases.elements import elements

class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = config['main']['url']
        self.username = config['main']['username']
        self.password = config['main']['password']
        self.elements = elements
        self.CampName = config['main']['new_camp_name_1']
        self.Camp_failAttemp = config['main']['fail_attempts']
        self.Camp_SP = config['main']['success_percent']


    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get(self.url)
        # make sure website opened
        self.assertEquals("Zisoft Login", self.driver.find_element_by_xpath(self.elements['page_title_path']).text)

    def tearDown(self):
        self.driver.quit()
    #
    # @staticmethod
    # def set_browser():
    #     if not BaseTest.DRIVER:
    #         if CONFIG['browser'] == 'chrome':
    #             BaseTest.DRIVER = webdriver.Chrome()
    #         elif CONFIG['browser'] == 'firefox':
    #             BaseTest.DRIVER = webdriver.Firefox()
    #         elif CONFIG['browser'] == 'ie':
    #             BaseTest.DRIVER = webdriver.Ie()
    #         elif CONFIG['browser'] == 'opera':
    #             BaseTest.DRIVER = webdriver.Opera()
    #         elif CONFIG['browser'] == 'safari':
    #             BaseTest.DRIVER = webdriver.Safari
    #         else:
    #             print("Invalid browser configuration [%s]" % CONFIG['browser'])
    #     return BaseTest.DRIVER

    def generate_random_string(self):
        result = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(random.randint(0, len(chars))):
            result += random.choice(chars)
        return result

    def login(self,username,password):
        # get the user name textbox
        self.usrname_field = self.driver.find_element_by_name(self.elements['username_1'])
        self.usrname_field.clear()
        # enter user name keyword and submit
        self.usrname_field.send_keys(username)
        # get the password textbox
        self.password_field = self.driver.find_element_by_name(self.elements['password_1'])
        self.password_field.clear()
        # enter password keyword and submit
        self.password_field.send_keys(password)
        self.driver.find_element_by_xpath(self.elements['submit_button']).click()


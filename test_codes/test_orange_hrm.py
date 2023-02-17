from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep
from test_locators import locators
from test_data import data
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Test_Orange_hrm:
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver =webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.fixture
    def login(self,booting_function):
        self.driver.get(data.Orange_hrm_Data().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,locators.Orange_hrm_Locators().username_inputBox))).send_keys(data.Orange_hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators().username_inputBox)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators.password_InputBox).send_keys(data.Orange_hrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.LoginButton).click()

    # Test Login
    def test_Login(self,booting_function):
        self.driver.get(data.Orange_hrm_Data().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,locators.Orange_hrm_Locators().username_inputBox))).send_keys(data.Orange_hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators.password_InputBox).send_keys(data.Orange_hrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.LoginButton).click()
        print("SUCCESS : Logged in with Username {a} and Password {b}".format(a=data.Orange_hrm_Data.username, b = data.Orange_hrm_Data.password))
        sleep(5)

    # Logging in with invalid credentials
    def test_invalid_login(self,booting_function):
        self.driver.get(data.Orange_hrm_Data().url)
        # sleep(5)
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.Orange_hrm_Locators().username_inputBox))).send_keys(data.Orange_hrm_Data().invalid_username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators.password_InputBox).send_keys(data.Orange_hrm_Data.invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.LoginButton).click()
        sleep(3)
        result = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().invalid_alert)))
        error_message=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators().invalid_alert)
        if result:
            print("Error_message: " + error_message.text)
            print("Success: Cannot login with invalid credentials Username {a} and Password {b}".format(a=data.Orange_hrm_Data.invalid_username,b=data.Orange_hrm_Data.invalid_password))
        else:
            print("Failed : Can login with invalid credentials Username {a} and Password {b} ".format(a=data.Orange_hrm_Data.username,b=data.Orange_hrm_Data.password))
            sleep(5)

    # adding a new employee
    def test_add_new_user(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_tab))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().add_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().middlename_textbox).send_keys(data.Orange_hrm_Data.test_middle_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().lastname_textbox).send_keys(data.Orange_hrm_Data.test_last_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().save_button).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().added_user_toast)))
        result=EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().added_user_toast))
        if result:
            print("success: user created and add with firstname {a},middlename {b},lastname {c}".format(
                a=data.Orange_hrm_Data.test_first_name,b=data.Orange_hrm_Data.test_middle_name,
                c=data.Orange_hrm_Data.test_last_name))
        else:
            print("failure: Cannot able to create and add user with firstname {a},middlename {b},lastname {c}".format(
                a=data.Orange_hrm_Data.test_first_name,b=data.Orange_hrm_Data.test_middle_name,
                c=data.Orange_hrm_Data.test_last_name))

    # editing an existing current employee details
    def test_edit_employee_details(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_tab))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().edit_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().edit_firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().edit_middlename_textbox).send_keys(data.Orange_hrm_Data.test_middle_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().edit_lastname_textbox).send_keys(data.Orange_hrm_Data.test_last_name)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().edit_employee_id_textbox).send_keys(data.Orange_hrm_Data.test_employee_id)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators().edit_employee_details_save).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().edit_employee_toast)))
        result = EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().edit_employee_toast))
        if result:
            print("success: user details edit and saved with firstname {a},middlename {b},lastname {c}, employee_id {d}".format(
                a=data.Orange_hrm_Data.test_first_name, b=data.Orange_hrm_Data.test_middle_name,
                c=data.Orange_hrm_Data.test_last_name,d=data.Orange_hrm_Data.test_employee_id))
            # assert True
        else:
            print("failure: Cannot edit and save user details with firstname {a},middlename {b},lastname {c}, employee_id {d}".format(
                    a=data.Orange_hrm_Data.test_first_name, b=data.Orange_hrm_Data.test_middle_name,
                    c=data.Orange_hrm_Data.test_last_name, d=data.Orange_hrm_Data.test_employee_id))

    # deleting an existing current employee
    def test_delete_employee(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_tab))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().delete_user_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().confirm_delete_button))).click()
        result=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().deleted_user_toast)))
        if result:
            print("success: employee deleted successfully")
        else:
            print("failure: Cannot able to delete employee")

    
#########comment for reference


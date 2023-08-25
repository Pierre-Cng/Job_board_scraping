import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import time

# Loading .env variables 
load_dotenv()
url = os.getenv('URL')
cv_path = os.getenv('CV')
name = os.getenv('NAME')
email = os.getenv('EMAIL')
phone = os.getenv('PHONE')
company = os.getenv('ORG')
linkedIn = os.getenv('LINKEDIN')
portfolio = os.getenv('GITHUB')
website = os.getenv('WEBSITE')

class Job_board_page:
    '''
    Class that create a webdriver, go to a specific page and perform a serie of actions.
    '''
    driver = None

    def page_loader(self, url):
        '''
        Function setting options and launching detached Edge selenium webdriver at the given url.
        '''
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=edge_options)
        self.driver.get(url)
        return self.driver
    
    def reject_cookies(self, driver, id_handle):
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id_handle)))
            driver.find_element(By.ID, id_handle).click()
            WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, id_handle)))
    
    def goto_apply(self, driver=None):
        if driver is None:
             driver = self.driver
        try:                 
            self.reject_cookies(driver, TBD)
        except:
            pass
        
        apply_xpath = TBD
        driver.find_element(By.XPATH, apply_xpath).click()
        driver.switch_to.window(driver.window_handles[1])
    
    def upload_file(self, cv_path, driver=None):
        if driver is None:
             driver = self.driver 
        upload_input_xpath = TBD
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, upload_input_xpath)))
        driver.find_element(By.XPATH, upload_input_xpath).send_keys(cv_path)
    
    def fil_up_field(self, name, value, driver = None):
        if driver is None:
             driver = self.driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, name)))
        driver.find_element(By.NAME, name).send_keys(value)

    def select_choice(self, name, option, driver = None):
        if driver is None:
            driver = self.driver
        select_element = driver.find_element(By.NAME, name)
        select = Select(select_element)
        select.select_by_visible_text(option)
        '''https://www.selenium.dev/documentation/webdriver/support_features/select_lists/'''
    
    def radio_click(self, driver=None):
        if driver is None:
            driver = self.driver
        choices = driver.find_elements(By.NAME, TBD)
        choices[0].click()
        

    
    def full_application(self, url, cv_path):
        self.page_loader(url)
        self.goto_apply()

        # SUBMIT YOUR APPLICATION section
        self.upload_cv(cv_path)
        self.fil_up_field('name', TBD)
        self.fil_up_field('email', TBD)
        self.fil_up_field('phone', TBD)
        self.fil_up_field('org', TBD)

        # LINKS section
        self.fil_up_field('urls[LinkedIn]', TBD)
        self.fil_up_field('urls[Portfolio]', TBD)
        self.fil_up_field('urls[Other]', TBD)

        # LUCID STANDARD QUESTIONS section
        for i in range(5):
            answer = ['Yes', 'No', 'No', 'No', 'Masters Degree'][i]
            self.select_choice(f'TBD{i}]', answer)
        self.radio_click()

        # NEWARK RELOCATION section
        self.short_answer()
        

jb = Job_board_page()
url = TBD
path = TBD
jb.full_application(url, path)

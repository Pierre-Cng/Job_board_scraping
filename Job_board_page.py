from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from environs import Env

# Loading .env variables 
env = Env()
env.read_env() 
app_website = env.dict("APPLICATION_SITE", subcast_values=str)  
candidate_info = env.dict("CANDIDATE_INFO", subcast_values=str)  

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
    
    def click(self, driver, By_type, name):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By_type, name)))
        driver.find_element(By_type, name).click()

    def send_keys(self, driver, By_type, name, keys):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By_type, name)))
        driver.find_element(By_type, name).send_keys(keys)

    def select_choice(self, driver, By_type, name, option):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By_type, name)))
        Select(driver.find_element(By_type, name)).select_by_visible_text(option)
    
    def reject_cookies(self, driver, By_type, name):
            self.click(driver, By_type, name)
            WebDriverWait(driver, 5).until(EC.invisibility_of_element((By_type, name)))

    def goto_apply(self, driver, app_dict):
        try:                 
            self.reject_cookies(driver, By.ID, app_dict.get('reject_id'))
        except:
            pass  
        self.click(driver, By.XPATH, app_dict.get('apply_xpath')) 
        driver.switch_to.window(driver.window_handles[1])
    
    def upload_file(self, driver, app_dict, candidate_dict):
        self.send_keys(driver, By.XPATH, app_dict.get('upload_input_xpath'), candidate_dict.get('cv_path'))
        
    def radio_click(self, driver, By_type, name, choice):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By_type, name)))
        driver.find_element(By.CSS_SELECTOR, f'[name="{name}"][value={choice}]').click()
    
    def full_application(self, app_dict, candidate_dict):
        self.page_loader(app_dict.get('url'))
        self.goto_apply(self.driver, app_dict)

        self.upload_file(self.driver, app_dict, candidate_dict)

        for field in ['name', 'email', 'phone', 'org']:
            self.send_keys(self.driver, By.NAME, field, candidate_dict.get(field))
        
        for field in ['LinkedIn', 'Portfolio', 'Other']:
            self.send_keys(self.driver, By.NAME, f'urls[{field}]', candidate_dict.get(field))
    
        for i in range(5):
            answer = ['Yes', 'No', 'No', 'No', 'Masters Degree'][i]
            self.select_choice(self.driver, By.NAME, app_dict.get('field_name') % i, answer)
        
        self.reject_cookies(self.driver, By.XPATH, app_dict.get('dismiss_xpath'))
        self.radio_click(self.driver, By.NAME, app_dict.get('field_name') % 5, 'Yes')

        # NEWARK RELOCATION section
        self.send_keys(self.driver, By.NAME, app_dict.get('short_answer_name') % 0, candidate_dict.get('relocation'))
        self.send_keys(self.driver, By.NAME, 'comments', candidate_dict.get('comment'))
        for field in ['gender', 'race', 'veteran']:
            self.select_choice(self.driver, By.NAME, f'eeo[{field}]', candidate_dict.get(field))
        self.click(self.driver, By.XPATH, app_dict.get('checkbox_xpath'))
        self.click(self.driver, By.XPATH, app_dict.get('submit_xpath'))

jb = Job_board_page()
jb.full_application(app_website, candidate_info)

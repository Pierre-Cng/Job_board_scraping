from environs import Env

env = Env()
env.read_env() 

# required variables
#gh_user = env("GITHUB_USER")  # => 'sloria'

dico = env.dict("CANDIDATE_INFO", subcast_values=str)  

print(dico.get('name', 'not existing'))

'''
, subcast_values=int


#apply_xpath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/main/div/article/div[1]/section/a'
apply_xpath = '//*[@id="main"]/astro-island/div/article/div[1]/section/a'
upload_input_xpath = '//*[@id="resume-upload-input"]'
choices = driver.find_elements(By.NAME, 'cards[4e305699-44b1-4cc7-9d31-bab18b811eca][field5]')

self.select_choice(f'cards[4e305699-44b1-4cc7-9d31-bab18b811eca][field{i}]', answer)
jobs = soup.find_all("a", {"class": 'SearchResults-module--jobLink--d8113'})
'''
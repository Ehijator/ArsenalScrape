import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas


chrome_options = Options()
S = Service("C:\Python310\chromedriver.exe")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--s")
driver = webdriver.Chrome(service= S, options= chrome_options)
starturl = r"https://fbref.com/en/squads/18bb7c10/history/Arsenal-Stats-and-History#all_comps_fa_club_league"

driver.get(starturl)
season = []
def Nav():
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()
    vals = driver.find_elements(By.XPATH,"//*[@id='comps_fa_club_league']/tbody/tr/*[@_data-stat = 'season']" )
    for s in range(len(vals)):
        season.append()

    print(season)
    

Nav()
#driver.quit()
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
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service= S, options= chrome_options)
starturl = r"https://fbref.com/en/squads/18bb7c10/history/Arsenal-Stats-and-History#all_comps_fa_club_league"

driver.get(starturl)

def Nav():
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()
    dg = driver.find_elements(By.XPATH,"//*[@id='comps_fa_club_league']/tbody/tr")
    for tr in dg:
        Season = tr.find_element(By.XPATH,"./th[1]").text
        Competition = tr.find_element(By.XPATH,"./td[3]/a").text
        LeagueRank = tr.find_element(By.XPATH,"./td[4]").text
        Games =
        Wins=
        Draws=
        Losses=
        GoalsFor=
        GoalsAgainst=
        GoalDiff=
        Points=
        AttendancePerG=

        print(Season,Competition,LeagueRank)

#//*[@id="comps_fa_club_league"]/tbody/tr[1]/td[5]

#dg = driver.find_elements(By.XPATH,"//*[@id='comps_fa_club_league']/tbody/tr/th" )   
#     for tr in dg:
#         print(tr.text)
#         season.append(tr.text)
# print(season)
    
    
    

Nav()
#driver.quit()
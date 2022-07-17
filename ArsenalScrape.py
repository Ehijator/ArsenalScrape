import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


chrome_options = Options()
S = Service("C:\Python310\chromedriver.exe")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(service= S, options= chrome_options)
starturl = r"https://fbref.com/en/squads/18bb7c10/history/Arsenal-Stats-and-History#all_comps_fa_club_league"

driver.get(starturl)
list = []
id = ["//*[@id='comps_fa_club_league']/tbody/tr","//*[@id='comps_intl_club_cup']/tbody/tr","//*[@id='comps_fa_club_cup']/tbody/tr","//*[@id='comps_fa_club_supercup']/tbody/tr"]

def Nav():
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()


def scrape(idname):
    dg = driver.find_elements(By.XPATH,idname)
    for tr in dg:
        try:
            Season = tr.find_element(By.XPATH,"./th[1]").text
            Competition = tr.find_element(By.XPATH,"./td[3]/a").text
            LeagueRank = tr.find_element(By.XPATH,"./td[4]").text
            Games = tr.find_element(By.XPATH,"./td[5]").text
            Wins = tr.find_element(By.XPATH,"./td[6]").text
            Draws = tr.find_element(By.XPATH,"./td[7]").text
            Losses = tr.find_element(By.XPATH,"./td[8]").text
            GoalsFor = tr.find_element(By.XPATH,"./td[9]").text
            GoalsAgainst = tr.find_element(By.XPATH,"./td[10]").text
            GoalDiff = tr.find_element(By.XPATH,"./td[11]").text
            Points = tr.find_element(By.XPATH,"./td[12]").text
            AttendancePerG = tr.find_element(By.XPATH,"./td[13]").text
            TopTeamScorers = tr.find_element(By.XPATH,"./td[14]").text
            TopKeeper = tr.find_element(By.XPATH,"./td[15]").text
        

            Competition = {
                "Season": Season,
                "Competition":Competition,
                "LeagueRank":LeagueRank,
                "Games":Games,
                "Wins":Wins,
                "Draws":Draws,
                "Losses":Losses,
                "GoalsFor":GoalsFor,
                "GoalsAgainst":GoalsAgainst,
                "GoalDiff":GoalDiff,
                "Points":Points,
                "AttendancePerG":AttendancePerG,
                "TopTeamScorers":TopTeamScorers,
                "TopKeeper":TopKeeper
            }
            
            list.append(Competition)
        except NoSuchElementException:
            continue
    
    df = pd.DataFrame(list)
    print(df)
    df.to_csv(r"C:\Python310\Scripts\ArsenalScrape\Arsenal.csv")
    

def main():  
    print("Now Scraping...Go Gunners!") 
    for x in id:
        scrape(x)
    
    print("Completed Sucessfully")
    driver.quit()


if __name__ == "__main__":
    main()
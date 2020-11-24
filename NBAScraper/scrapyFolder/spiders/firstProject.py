from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def find_stats():
    table = driver.find_element_by_xpath("//div[@class='table_outer_container']//div[@id='div_per_minute']//table[@id='per_minute']/tbody")

    allRows = table.find_elements_by_tag_name("tr")

    for row in allRows:
        seasons = row.find_elements_by_xpath("//div[@class='table_outer_container']//div[@id='div_per_minute']//table[@id='per_minute']/tbody/tr/th")
        allPointAvg = row.find_elements_by_xpath("//div[@class='table_outer_container']//div[@id='div_per_minute']//table[@id='per_minute']/tbody/tr/td[@data-stat='fg3a_per_mp']")

    print(userPlayerName)

    for pointAvg, season in zip(allPointAvg, seasons):
        print(season.text + " " + pointAvg.text)

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

if (len(sys.argv) >= 2):
    userPlayerName = ""
    for i in sys.argv[1:]:
        
        userPlayerName = userPlayerName + i + " "

    driver.get("https://www.basketball-reference.com/leagues/NBA_2020_per_game.html")

    search = driver.find_element_by_name("search")
    search.send_keys(userPlayerName)
    search.send_keys(Keys.RETURN)

    #if(driver.find_element_by_class_name("search_results")):
    try:
        player_link = driver.find_element_by_partial_link_text(userPlayerName)
        player_link.click()
        find_stats()
    except:
        find_stats()

    

    driver.quit()
else:
    print("Enter a player name")
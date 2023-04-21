from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# import time
# import bs4 as bs
# import pandas as pd

def SearchDancers(dancernum=13758):
    url = 'https://points.worldsdc.com/lookup2020'
    # url2 = 'https://www.worldsdc.com/registry-points/'
    dancers = []
    searchlist = []
    for n in range(3):
        searchlist.append(n + dancernum)
    print(searchlist)
        

    s = Service('/wsdc/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    # Wait for the search box to be clickable
    for danceID in searchlist:    
        
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q"]')))
        element.clear()
        element.send_keys(danceID)
        element.send_keys(Keys.ENTER)

        h1name = driver.find_elements(By.XPATH, '//*[@id="lookup_results"]/h1')
        if h1name == "Found 0 matching names:":
            continue
        # if WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lookup_results"]/h1'))).text == "Found 0 matching names:":
        #     continue

        dancelvl = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="lookup_results"]/p/span'))).text
        name = driver.find_element(By.XPATH,'//*[@id="lookup_results"]/h1').text
        points = driver.find_element(By.XPATH,'//*[@id="lookup_results"]/h3[1]/small').text
        dict_name = str(danceID)
        dict_name = {
            "name": name,
            "dance lvl": dancelvl,
            "points": points
        }
        dancers.append(dict_name)

    input("Press Enter to close the browser window")  # Wait for user input
    driver.quit()  # Close the browser window
    printDics(dancers)



SearchDancers(420)
# SearchDancers()

list1 = [{'name': 'JD Nafziger (13758)', 'dance lvl': 'ADV', 'points': '27 points'}, {'name': 'Malory Beritsky (13759)', 'dance lvl': 'NEW', 'points': '6 points'}, {'name': 'Dan Kozar (13760)', 'dance lvl': 'NEW', 'points': '4 points'}]
def printDics(dics):
    for item in dics:
        print(item)

# printDics(list1)


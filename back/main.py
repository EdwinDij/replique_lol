import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://universe.leagueoflegends.com/fr_fr/'

driver = webdriver.Chrome(executable_path='c:\\Users\\narut\\Documents\\Workflow\\FrontEnd\\Lol\\back\\chromedriver.exe')
driver.get(url)

go_to_champion = driver.find_element(By.XPATH, '//*[@id="riotbar-center-content"]/div[2]/div[1]')
time.sleep(10)
go_to_champion.click()

time.sleep(100)
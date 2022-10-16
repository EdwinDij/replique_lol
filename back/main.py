
import time
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
url ='https://overwatch.blizzard.com/fr-fr/heroes/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
PATH = 'c:\\Users\\narut\\Documents\\Workflow\\FrontEnd\\Lol\\back\\chromedriver.exe'
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)


heroes_name = []
heroes_role = []
heroes_img = []
hero = soup.find_all('span')
role = soup.find_all('img', class_="heroCardRole")

def get_name():
    for name in hero:
        heroes_name.append(name.string)
    return heroes_name
get_name()


def get_role ():
    for herorole in role:
        hero_link = herorole.attrs.get("src")
        heroes_role.append(hero_link)
    return heroes_role
get_role()



##suppression des span non désiré
del heroes_name [0 : 4]
del heroes_name [35 : 40]

print(heroes_role)

time.sleep(100)
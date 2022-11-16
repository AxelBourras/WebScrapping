from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input JSON file with URLs', required=True)
parser.add_argument('--output', help='Output JSON file with data', required=True)
args = parser.parse_args()
argdict = vars(args)
input_file = argdict['input']
output_file = argdict['output']

N = 10
def titreVideo(soup):
    return soup.find("meta", itemprop="name")['content']

def auteur(soup):
    return soup.find("yt-formatted-string", class_="style-scope ytd-channel-name complex-string").text

def like(soup):
    raw_like = soup.find('button', class_="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start")
    like = raw_like['aria-label']
    if like[0] == 'C':
        nb_like = like.split("Cliquez sur \"J'aime\" pour cette vidéo comme ")[1].split("autres internautes.")[0]
    else:
        nb_like = like.split("like this video along with ")[1].split("other people")[0]
    return nb_like

def description(soup,driver):
    element = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
    element.click()
    element = driver.find_element(By.XPATH, "//html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]")
    element.click()
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return(soup.find("yt-formatted-string", {"class": "style-scope ytd-text-inline-expander"}))
    #eturn soup.find("meta", itemprop="description")['content']

def liens(description):
    listeLiens = []
    liens = description.find_all("a")
    for lien in liens :
        if lien['href'][0] == "/":
            listeLiens.append("https://www.youtube.com"+lien['href'])
        else:
            listeLiens.append(lien['href'])
    return(listeLiens)

def idVideo(soup):
    return soup.find("ytd-watch-flexy", class_="style-scope ytd-page-manager hide-skeleton")['video-id']

def commentaires(soup,driver):
    commentaires = []
    element = driver.find_element(By.XPATH, "//*[@id=\"comments\"]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    commentsList = soup.find_all("ytd-comment-thread-renderer", {"class": "style-scope ytd-item-section-renderer"}, limit = N)
    while commentsList == []:
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        commentsList = soup.find_all("ytd-comment-thread-renderer", {"class": "style-scope ytd-item-section-renderer"}, limit = N)
    for comment in commentsList:
        commentaires.append(comment.find("yt-formatted-string", {"id": "content-text"}).text)
    return commentaires

def init(url):
    s=Service(ChromeDriverManager().install())
    options = Options()
    driver = webdriver.Chrome(service=s, chrome_options=options)
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup, driver
    
def recupData(url,res):
    soup, driver =init(url)
    res['title'].append(titreVideo(soup))
    res['author'].append(auteur(soup))
    res['nbLike'].append(like(soup))

    res['description'].append(description(soup,driver).text)
    res['idVideo'].append(idVideo(soup))
    res['commentaires'].append(commentaires(soup,driver))
    driver.quit()
    return res

with open(input_file) as mon_fichier:
    data = json.load(mon_fichier)

res = {'title':[], 'author':[], 'nbLike':[],'description':[],'liens':[],'idVideo':[],'commentaires':[]}
for url in data:
    for video in data[url]:
        url = "https://www.youtube.com/watch?v="+video
        res = recupData(url,res)

print(res)

with open(output_file, 'w') as mon_fichier:
    json.dump(res, mon_fichier)


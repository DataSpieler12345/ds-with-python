#Import the libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import pandas as pd 
import time 

#show the path of chromedriver
path = 'E:/ChromeDriver'

#begin the services
service = Service(executable_path=path)
#create a driver 
driver = webdriver.Chrome(service=service)
#store the web into a variable 
web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'

driver.get(web)
#scrapping 
matches = driver.find_elements(by='xpath', value = '//th[@class="fhome"]//.. | //tr[@itemprop="name"]//..')

#Create a list of to store the data
home = []
score = [] 
away = []

#boocle to collect all elements 
for  match in matches:
     home.append(match.find_element(by ='xpath', value='//th[@class="fhome"]').text)
     score.append(match.find_element(by ='xpath', value='//th[@class="fscore"]').text)
     away.append(match.find_element(by ='xpath', value='//th[@class="faway"]').text)
 
#Create a dictionary 
dict_football = {'home': home, 'score': score, 'away': away}
df_football = pd.DataFrame(dict_football) 
df_football['year'] = 1982
time.sleep(2)
#store the data into a csv file
df_football.to_csv('test_1982.csv')
#close the driver of Selenium    
driver.quit()

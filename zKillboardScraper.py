# Ethan Kalika
# Finished on April 30, 2023

# This script scrapes data from the evonline site and loads it into a textfile called monthlyTableFinal.txt

# Library Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from pathlib import Path

# This number determines how often the file storing the monthly tables will be updated
fileUpdateRate = 500

# Create list of pages to scrape and stores a file with the alliance ID's being studied
direcPath = Path(__file__).parent
iDsAliveLoc = os.path.join(direcPath, "alliances_all_corporations.csv")
iDsDeadLoc = os.path.join(direcPath, "alliances_dead_corporations.csv")
dataAlive = pd.read_csv(iDsAliveLoc)
dataDead = pd.read_csv(iDsDeadLoc)
iDdf = pd.concat([dataAlive["AllianceID"], dataDead["AllianceID"]], ignore_index = True).drop_duplicates()
iDList = []
for element in iDdf.values.tolist():
    try:
        iDList += [str(int(element))]
    except:
        iDList += [element]
with open("iDList.txt", "w") as f:
    f.write(str(iDList))

# Reading of URL and creation of monthly tables variable to hold html file and stores all errors that occure during the running of the code for later analysis
dataDict = {}
errorDict = {}
iDnum = 1
for alliance in iDList:
    monthlyData = []
    try:
        uRLString1 = "https://zkillboard.com/alliance/"
        uRLString2 = "/stats/"
        currentURL = uRLString1 + alliance + uRLString2
        pagesToScrape = requests.get(currentURL)
        soup = BeautifulSoup(pagesToScrape.text, "html.parser")
        monthlyTables = soup.find_all("table")[-1]
        monthlyData = monthlyTables.find_all("td")
        dataDict[str(alliance)] = []
        print(str(iDnum) + ": " + str(alliance))
    except Exception as err:
        print(err)
        errorDict[currentURL] = str(err)

    # Creation of list to store scrapped data an writing it to a file
    counter = -1
    for i in range(len(monthlyData) // 9):
        counter = counter + 1
        currentDataList = []
        for j in range(9):
            currentDataList.append(monthlyData[9 * counter + j].text.replace("\n", ""))
        dataDict[str(alliance)] += [currentDataList]
    if (iDnum % fileUpdateRate == 0 or iDnum == len(iDList)):
        f = open("monthlyTableFinal.txt", "w")
        f.write(str(dataDict))
        f.close()
    iDnum += 1
with open("errors.txt", "w") as f:
    f.write(str(errorDict))
print("Data Scraped!")

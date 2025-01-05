# EVEonline Data Scraper
This is the work that I did for one of the projects I worked on in college. The goal is to scrape information from the EVEonline site, convert that information into a table, and the merge that table with the data collected by the rest of the team. These instructions first explain what each file in this directory does and then gives instructions on how to use them to recreate the results of the research project.

# File Descriptions
## SampleRuns:
A folder which stores the output files I obtained when I was writing the code so that any user who pulled this repository and is recreating the results may check their outputs.

## SampleRuns/iDListFinal.txt:
This is a file created by zKillboardScraper.py, it stores a list of all of the alliance ID's. This text file is used mostly for debugging and testing purposes as it allows the user to sample random alliances and see if the output of any given script for that file is correct. Note that zKillboardScraper.py creates a file called iDList.txt, and in this directory I manually change the name to iDListFinal.txt.

## SampleRuns/mainAndMonthlyTable.zip:
This is a zip file of the final product. This zip file stores the table resulting from the merging of tables stored in monthlyTable.csv and monthly_variables_total.csv

## SampleRuns/monthlyTable.csv:
This is created by toCSV.py and is a csv file which stores the data scraped by zKillboardScraper.py.

## SampleRuns/monthlyTableFinal.txt:
This is a text file created by zKillboardScraper.py, this file stores a string which encapsulates all the information scrapped by zKillboardScraper.py. Note that zKillboardScraper.py creates a file called monthlyTable.txt, and in this directory I manually change the name to monthlyTableFinal.txt.

## alliances_all_corporations.csv:
This is a csv file created by other members of the team and it stores information about all the living alliances in the game at the time when the project was conducted. In particular this file was used to store the alliance ID's of all the living alliances so that we can generate the necessary URL's and read the remainder of the necessary data from the website.

## alliances_dead_corporations.csv:
This is a csv file created by other members of the team and it stores information about dead the living alliances in the game at the time when the project was conducted. In particular this file was used to store the alliance ID's of all the living alliances so that we can generate the necessary URL's and read the remainder of the necessary data from the website.

## merger.py:
This is the python script used to merge the tables stored in monthlyTable.csv and monthly_variables_total.csv to create the mainAndMonthlyTable.csv file which is stored in mainAndMonthlyTable.zip.

## monthly_variables_total.zip:
This is a zip file which stores a csv file of the main table created by the rest of the team. This is the table to which I have to merge the monthly data that I collected.

## toCSV.py:
This is the python script used to convert text file outputted by zKillboardScraper.py into a csv file.

## zKillboardScraper.py:
This is the python script used to scrape the data from the EVEonline website and organize it into a dictionary which is then printed to a text file.

Steps to using the directory:
Step 1: Note the the directory should start with only 8 files (alliances_all_corporations.csv, alliances_dead_corporations.csv, monthly_variables_total.zip, merger.py, toCSV.py, zKillboardScraper.py, INSTRUCTIONS, and sampleRuns)
Step 2: Unzip all zipped files
Step 3: Run zKillboardScraper.py. This should create two files, iDListFinal.txt and monthlyTable.txt
Step 4: Run toCSV.py. This should create a file called monthlyTable.csv.
Step 5: Run merger.py. This should create a file called mainAndMonthlyTable.csv

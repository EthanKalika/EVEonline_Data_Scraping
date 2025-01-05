# Author: Ethan Kalika
# Date: August 1, 2023

# This script converts the monthly table stored in monthlyTableFinal.txt into a csv file ####

# Library Imports
import os
from pathlib import Path
import pandas as pd

# These are the helper functions for the program
def dateTransformer(date1):
    return date1[-4:] + "-" + str(int(date1[:2]))

def monthID1(data):
    return 12 * (int(data[8][-4:]) - 2007) + int(data[8][:2]) - 12

# Global Variables
endMonthID = 180

# Creates a dictionary representing the text file
filePath = os.path.join(Path(__file__).parent, "monthlyTableFinal.txt")
with open(filePath, 'r') as f:
    text = f.read()
    counterbrak  = 0  # A counter which counts the number of brakcets needed to close the string at its current position
    counterquote = 0  # A counter which counts the number of apposterfies in the string up until the current point
    innernums = ''
    nums = ''         
    prevNums = ''     
    currElement = ''  
    emptyValue = False
    currList = []     # A list which stores the current value
    currValue = []      
    prevValue = []
    pprevValue = []
    fileDict = {}     # A dictionary object which is to store the contents of the file as a dictionary
    for i in range(len(text)):
        if text[i].__eq__('['):
            counterbrak += 1
        elif text[i].__eq__(']'):
            counterbrak -= 1
        elif text[i].__eq__("\'"):
            counterquote += 1
        if i >= 1 and text[i].__eq__(']') and text[i - 1].__eq__('['):
            emptyValue = True
        if counterbrak == 0 and counterquote % 2 == 1:
            nums += text[i]
        if counterbrak == 2 and counterquote % 2 == 1:
            currElement += text[i]
        elif counterbrak == 2 and counterquote % 2 == 0:
            if not currElement.__eq__(''):
                currList.append(currElement[1:])
            currElement = ''
        elif counterbrak == 1:
            if not len(currList) == 0:
                currValue.append(currList)
            currList = []
        elif counterbrak == 0:
            if emptyValue:
                nums = ''
                emptyValue = False
            elif not len(currValue) == 0:
                fileDict[str(nums)[1:]] = []
                currValue.reverse()
                fileDict[str(nums)[1:]] = currValue
                prevNums = nums
                nums = ''
            pprevValue = prevValue
            prevValue = currValue
            currValue = []
    fileDict[str(prevNums)[1:]] = pprevValue
print("Dictionary created")

# Turns the dictionary into a dataframe and writes the dataframe to a new file
savePath = os.path.join(Path(__file__).parent, "monthlyTable.csv")
fileDf = pd.DataFrame(columns = ["ID's", "Date", "Kills", "Points", "ISK(Green)", "Losses", "Points", "ISK(Red)", "Efficiency"])
for key in fileDict.keys():
    for element in fileDict[key]:
        if monthID1(element) <= endMonthID:
            fileDf.loc[len(fileDf)] = [key] + [dateTransformer(element[8])] + element[1:8]
    print("key: ", key)
    fileDf.to_csv(savePath)
print("Monthly csv exported to file")
print("done")

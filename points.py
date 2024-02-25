# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# cl
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from webscraper import WebScraper
from discord.ext import commands
import discord



# Leetcompletion = False
# LtimeSpent = ""
# class acesssVariables (WebScraper):
#     def __init__(self, difficultyLevel, completion, timeSpent ):
#         # self.difficulty = difficultyLevel
#         # self.Leetcompletion = completion
#         # self.LtimeSpent = timeSpent
#         super().__init__(difficultyLevel, completion, timeSpent)

import datetime
from datetime import datetime
from webscraper import Webscraper
class pointSystem(Webscraper):
    # def __init__(self):
    #     super().__init__( Webscraper.questionArray)
    # def calculatePoints(self, points):
    #     if tier.user_tier <= 3 and tier.user_tier >= 0 and self.completionB == True:
    #         points = points + 10
    #     if tier.user_tier > 3 and tier.user_tier <= 6 and self.completedB == True:
    #         points = points + 20
    #     if tier.user_tier > 6 and tier.user_tier <=8 and self.completedB == True:
    #         points = points + 30
    #     return points
    newArray = Webscraper.createArray()
    points = 0
    def sendReminder(self, newArray):
        timeStamp = newArray[0].returnTime()
        dt_object = datetime.datetime.fromtimesamp(timeStamp)
        currentTime = datetime.now()
        time_difference = currentTime- dt_object
        days_difference = time_difference.days
        reminder = "Its been 24 hours. Why not practice some LeetCode?"
        if(days_difference >= 1):
            return reminder

    #After a day call this method
    count = 0
    def pointsOnTime(self, points, count, newArray):
        timeStamp = newArray[0].returnTime()
        dt_object = datetime.datetime.fromtimesamp(timeStamp)
        currentTime = datetime.now()
        time_difference = currentTime - dt_object
        days_difference = time_difference.days
        if(days_difference <= 1 ):
            count = count + 1
            if(count == 3):
                count = 0
                points = points + 1
        return points


    print(sendReminder(newArray))
    print(pointsOnTime(points, count, newArray))










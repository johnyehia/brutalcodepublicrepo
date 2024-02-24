import datetime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd



    

class Question:
    def __init__(self,name,timegiven):
        self.questionName = name
        self.time = timegiven
    def returnName(self):
        return self.questionName
    def returnTime(self):
        return self.time
        


class webscraper:

    def createArray():
        LeetUser = input("Input your LeetCode Username ")
        my_url = "https://leetcode-api-faisalshohag.vercel.app/" + LeetUser

        client = uReq(my_url)

        page_html = client.read()

        page_html

        page_soup = soup(page_html, features= "html.parser")

        page_soup.getText

        text = page_soup.getText() + ""

        completedNum= int(text[15:text.index(",")])
    
        finish=0
        questionArray=list()
        while completedNum > finish:


            AllQuestion = ""

            indexStart = text.index("\"title\":")+9
            text = text[indexStart:]
            indexEnd = text.index(",")-1
            name=text[0:indexEnd]
            text = text[indexEnd:]

    
            try:
                AllQuestion.index(name)
       
     
            except:
                finish = finish+1
                indexStartTime = text.index("timestamp")+12
                text = text[indexStart:]
                endtext = text.index(",")-1
                date = text[0:indexEnd]
                AllQuestion=AllQuestion+name
                questionArray.append(Question(name,date))
            return questionArray
       
  








    
    




















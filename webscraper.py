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
        



LeetUser = input("Input your LeetCode Username ")
my_url = "https://leetcode-api-faisalshohag.vercel.app/" + LeetUser

client = uReq(my_url)

page_html = client.read()

page_html

page_soup = soup(page_html, features= "html.parser")

page_soup.getText

text = page_soup.getText() + ""

completedNum= int(text[15:text.index(",")])
print(completedNum)
print(completedNum)

questionArray = list()
while text.index("\"title\":")+9  != text.rindex("\"title\":")+9:

    #print("times")
    
    indexStart = text.index("\"title\":")+9
    text = text[indexStart:]
    indexEnd = text.index(",")-1
    name=text[0:indexEnd]
    text = text[indexEnd:]
    
    indexStartTime = text.index("timestamp")+12
    text = text[indexStartTime:]
    endtext = text.index(",")-1
    date = text[0:endtext]
    text = text[endtext:]

    indexStartAccepted = text.index("statusDisplay")+16
    text = text[indexStartAccepted:]
    endtext = text.index(",")-1
    value = text[0:endtext]
    
    text = text[endtext:]
    
    Add = True
    for i in questionArray:
        if(i.returnName()==name):
            Add = False
        if(value != "Accepted"):
            Add = False

    if Add == True:
        
        questionArray.append(Question(name,date))


for j in questionArray:
    print(j.returnName())
        

    

       



  








    
    




















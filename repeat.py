import urllib
from rishabh import lst1,lst2
import schedule
import time
from BeautifulSoup import *
count=0
def resolve(count1):
    while(lst2[count1] and lst1[count1]):
        while(count1< count1+5):
            print(lst1[count1])
            html2 = urllib.urlopen(lst2[count1]).read()
            soup2 = BeautifulSoup(html2)
            meaning2 = soup2.findAll('span',{'class':'def'})
            for mean2 in meaning2:
                if mean2.string is not None:
                    print(mean2.string)
            count1=count1+1

schedule.every().day.at("19:40").do(resolve,count)

while True:
    schedule.run_pending()
    count=count+5
    time.sleep(60)

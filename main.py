import requests
import json
import datetime
from notify_run import Notify
from time import sleep

notify = Notify()

def task():
    f=open("extracted.txt","r")
    rdln=f.readline()
    tot=1
    hits=0
    hitlist=[]
    while rdln:
        date = str(datetime.date.today())
        link="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+rdln.strip()+"&date="+date[8]+date[9]+"-"+date[5]+date[6]+"-"+"2021
        x = requests.get(link)
        # print(link)
        data = json.loads(x.text)
        f_list=data["sessions"]
        count=1
        for i in f_list:
            if(i['min_age_limit']==18):
                hits+=1
                print(tot,".",count,":")
                print("\tname of hospital :",i['name'])
                hitlist.append(i['name'])
                print("\tpincode of hospital :",i['pincode'])
                print("\tAvailable doses :",i['available_capacity'])
                print("\tAge limit :",i['min_age_limit'])
            count+=1
        tot+=1
        rdln=f.readline()

    if(hits==0):
        notify.send('Nope! ran through db and no centers found for <45')
        notify.send('Nope! ran through db and no centers found for <45')
    elif(hits==1):
        strin="Yes! ran through db and found one. schedule it in "+str(hitlist[0])
        notify.send(strin)
        notify.send(strin)
    else:
        strin="Yes! multiple centers found when ran through db first being"+str(hitlist[0])
        notify.send(strin)
        notify.send(strin)

while True:
    if datetime.datetime.now().minute in {0,15,20,30,40,45,50}:
        print(datetime.datetime.now().minute)
        task()
    else:
        sleep(7)

# f=open("pincode.txt",'r')
# fs=open("extracted.txt",'w+')
# rdln=f.readline()
# while rdln:
#     rd=rdln.split("	")
#     fs.write(rd[len(rd)-1])
#     rdln=f.readline()
# f.close()
# fs.close()

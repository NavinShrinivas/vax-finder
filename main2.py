import requests
import json
import datetime
# from notify_run import Notify
from time import sleep
# s

# notify = Notify()



def task():
    f=open("extracted.txt","r")
    rdln=f.readline()
    tot=1
    hits=0
    hitlist=[]
    while rdln:
        try:
            date = str(datetime.date.today())
            link="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+rdln.strip()+"&date="+date[8]+date[9]+"-"+date[5]+date[6]+"-"+"2021"
            x = requests.get(link)
            # print(x.text)
            data = json.loads(x.text)
            f_list=data["centers"]
            count=1
            for i in f_list:
                for j in i["sessions"]:
                    if(j['min_age_limit']==18 and j['available_capacity']>0):
                        hits+=1
                        print(tot,".",count,":")
                        print("\tname of hospital :",i['name'])
                        if i['name'] not in hitlist:
                            hitlist.append(i['name'])
                        print("\tpincode of hospital :",i['pincode'])
                        print("\tAvailable doses :",j['available_capacity'])
                        print("\tAge limit :",j['min_age_limit'])
                        print("\tOn date :",j["date"])
                        # phone_obj=open("jsonformat.json")
                        # y=requests.post('https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP',data=phone_obj)
                        # print(y.text)
                        # otp=int(input("enter otp :"))
                        

                count+=1
            tot+=1
            rdln=f.readline()
        except json.decoder.JSONDecodeError :
            pass
    f.close()
    # f=open("extracted.txt","r")
    # rdln=f.readline()
    # while rdln:
    #     date = str(datetime.date.today())
    #     link="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+rdln.strip()+"&date="+str(int(date[8]+date[9])+1)+"-"+date[5]+date[6]+"-"+"2021"
    #     x = requests.get(link)
    #     # print(link)
    #     data = json.loads(x.text)
    #     f_list=data["sessions"]
    #     count=1
    #     for i in f_list:
    #         if(i['min_age_limit']==18 and i['available_capacity']>0):
    #             hits+=1
    #             print(tot,".",count,":")
    #             print("\tname of hospital :",i['name'])
    #             if i['name'] not in hitlist:
    #                     hitlist.append(i['name'])
    #             print("\tpincode of hospital :",i['pincode'])
    #             print("\tAvailable doses :",i['available_capacity'])
    #             print("\tAge limit :",i['min_age_limit'])
    #         count+=1
    #     tot+=1
    #     rdln=f.readline()
    print(hitlist)
    # with WhatsApp() as bot:
    #     bot.send('Kaveri',hitlist)

    # if(hits==0):
    #     notify.send('Nope! ran through db and no centers found for <45')
    #     notify.send('Nope! ran through db and no centers found for <45')
    # else:
    #     strin="Yes! centers found when ran through db first being : "+str(hitlist[0])
    #     notify.send(strin)
    #     notify.send(strin)

while True:
        task()
        
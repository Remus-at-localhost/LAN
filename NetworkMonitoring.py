import json
import requests
import os
import time
import pyautogui as auto

inp=[]
x=3
loc = os.getcwd()

with open(loc+'/Credentials') as T:
    inp=T.readlines()
    Gid = inp[3][:-1]
    Token = inp[1][:-1]
    username = inp[5][:-1]
    password = inp[7][:-1]     
        
def retrive():
    stacks =[]
    headers = {
        'authorization': Token
    }
    r = requests.get(
        Gid,headers=headers)
    
    jobj= json.loads(r.text)
    for value in jobj:
        #print(value['content'], '\n')
        stacks.append(value['content'])

    print(stacks[0])
    if stacks[0] == 'LAN':
        del jobj
        del value
        del stacks
        Automate()
        Transmit()
    elif stacks[0]=='STOP':
        exit

    else:
        del jobj
        del value
        del stacks
        time.sleep(5)
        retrive()  

def Transmit():
    for file in os.listdir():        			
        if file.__contains__(".pdf"):                   

            headers = {"Authorization": Token}
 
            files = {
                #'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open("./"+file, "rb")
            }
            
            
            r = requests.post(
                Gid,				#posts to this Group
                headers=headers,		#using this Access token(Header)
                files=files
            )
            print(r.text)			#Upload Log
            os.remove(file)			#Deleting the pdf
            #time.sleep(5)
            #ScreenShot()			
        else:
            pass
    retrive()

def Automate():
    auto.press('win')
    time.sleep(x)
    auto.write('Brave')
    time.sleep(x)
    auto.press('enter')
    time.sleep(13)
    auto.write('192.168.1.1')
    time.sleep(5)
    auto.press('enter')
    time.sleep(10)
    auto.write(username)
    time.sleep(x)
    auto.press('tab')
    time.sleep(x)
    auto.write(password)
    time.sleep(x)
    auto.press('enter')
    time.sleep(x)
    auto.press('tab')
    auto.press('tab')
    auto.press('tab')
    time.sleep(x)
    auto.press('enter')
    time.sleep(x)
    auto.press('end')
    time.sleep(x)
    auto.moveTo(500,555)
    time.sleep(x)
    auto.click()
    time.sleep(x)
    auto.hotkey('ctrl','p')
    time.sleep(5)
    auto.press('enter')
    time.sleep(7)
    auto.click()
    time.sleep(3)
    auto.press('enter')
    time.sleep(7)
    auto.hotkey('alt','f4')

def start():
    print("I'll be sending you the LAN details.. ")
    time.sleep(x)
    print("\n Now just open a newtab on your browser and close other programs..")
    time.sleep(x)
    print("\nSend me 'LAN' command on the channel and I'll start the process and share with you the pdf containing our LAN details")
    l = input('Type Y to start me!')
    if l=='Y':
        retrive()
    else:
        exit()
start() #Initial variables

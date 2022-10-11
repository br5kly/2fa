import pyotp
import time
import os
import sys
os.system('touch 2fa.txt')
B="\[\033[1;35m\]"
def z_d():
  note = B + "THIS TOOL CODED BY ZEYAD ALABANY GRETZ TO ALL MY FRIEND [WANIS] [AHMED XR] [OMAR]  "
  for letter in note:
     time.sleep(0.04)
     sys.stdout.write(letter)
     sys.stdout.flush()
     
  def fa():
   zd = input("COPY 2FA AND PAST HERE:  ")
   zd= zd.replace(" " ,"")
   sr = pyotp.TOTP(zd)
   print("Current OTP:", sr.now())
def show():
    with open ("myFile1.txt") as f:
         lines = f.readlines()
         for line in lines:
              words = line.split()
              for word in words:
                print(words)
                 
def main():
 print("""██████╗ ███████╗ █████╗ 
╚════██╗██╔════╝██╔══██╗
 █████╔╝█████╗  ███████║
██╔═══╝ ██╔══╝  ██╔══██║
███████╗██║     ██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝
                     BY ZEYAD ALABANY   """)
 print("[01]SHOW MY ACCOUNTS ")
 print("[02]ADD NEW 2FA ")
 print("[03]ABOUT")
 zeyad = input("CHOOSE :")
 if zeyad in["1","01"]:
    with open('2fa.txt') as f:
     lines = f.readlines()
     for line in lines:
      words = line.split()
      for word in words:
       aw = word
       aw = word.partition("|")[0]
       print(aw)
       word = word.partition("|")[2]      
       sr = pyotp.TOTP(word)
       print(sr.now()+"\n")   
 if zeyad in["2","02"]:
    zx= input("any name (ﻪﺑﺎﺸﺗ ﺮﻴﺼﻳ ﻻ ﻰﺘﺣ ﺰﻴﻤﻣ ﻢﺳﺍ): ")
    check = open('2fa.txt','r').read()
    if zx in check:
      print("ﻡﺪﺨﺘﺴﻣ ﻢﺳﻻﺍ ﺍﺬﻫ ﺍﺭﺬﻋ")
      os.system('python test.py')
    zr=input("ENTER 2FA CODE : ")
    zr= zr.replace(" ","")
    myFile = open("2fa.txt","a")
    myFile.write(zx+"|"+zr+"\n")
    myFile.close()
    os.system('clear')
    time.sleep(1)
    main()
 if zeyad in["03","3"]:
     z_d()
def show():
 myFile = open("2fa.txt", "a")
 myFile.close()

 myFile = open("2fa.txt", "r")

 print(myFile.read())
def add():
    zx= input("any name: ")
    zr=input("ENTER 2FA CODE : ")
    myFile.write(str.zx+"|"+zr)
    myFile.close()
main()

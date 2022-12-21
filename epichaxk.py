#!/usr/bin/python3

import requests
import json
import sys
import colorama
import os
from colorama import Fore
from datetime import datetime
from requests.exceptions import ConnectTimeout

#requests settings
requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES=5
session = requests.Session()
session.max_redirects = 5


#params
#param_file = sys.argv[1]

logo = """
___________.__           .____          ___.        .___       
\__    ___/|  |__   ____ |    |   _____ \_ |__    __| _/____   
  |    |   |  |  \_/ __ \|    |   \__  \ | __ \  / __ |\__  \  
  |    |   |   Y  \  ___/|    |___ / __ \| \_\ \/ /_/ | / __ \_
  |____|   |___|  /\___  >_______ (____  /___  /\____ |(____  /
                \/     \/        \/    \/    \/      \/     \/ \n SUPER EPIC HAXOR TOOL"""


def save_to_file(stringtowrite):
    with open(file_name, "a") as out:
        out.write(stringtowrite + '\n')


#functions
def funct_hostheader():
    save_to_file("\nHost Header successfully injected:")
    if global_set == 1:
        global target_global
        global inject_global
        param_file = target_global
        param_host = inject_global
        os.system("clear")
        print("Global targets set to: " + param_file + " with injecting " +param_host)
    else:
        global target_file
        global inject_string
        param_file = target_file
        param_host = inject_string
    
    headers = {'Host': param_host}
    list=[]
    f = open(param_file,'r')
    for x in f:
        target = 'https://' + x.replace('\n','')
        try:
                req = session.get(target, headers=headers, verify=False, timeout=5, allow_redirects=True)
                #RESPONSE BODY INJECTED +
                if param_host in str(req.content):
                            print("\n" + Fore.GREEN +  "|" + param_host + "| Injected on host: " + target + " --> Injected HOST reflected in BODY! Response:" + str(req.status_code))
                            save_to_file("\n" + target)
                #RESPONSE HEADER INJECTED +
                elif param_host in str(req.headers):
                            print("\n" + Fore.GREEN +  "|" + param_host + "| Injected on host: " + target + " --> Injected HOST reflected in HEADER! Response:" + str(req.status_code))
                            save_to_file("\n" + target)
                #INJECTION FAILED - 
                elif param_host not in str(req.content) and param_host not in str(req.headers):
                            print("\n" +  "|" + param_host + "|" + Fore.RED + "| Injection failed on: " + target + Fore.RESET + " --> Response:" + str(req.status_code))
        
        except ConnectTimeout:
            pass
        except (requests.exceptions.TooManyRedirects) as e:
            pass
        except requests.exceptions.ConnectionError as e:
            pass

def funct_cors():
    global menu
    save_to_file("\nCORS Header Successfully Injected:")

    if global_set == 1:
            global target_global
            global inject_global
            param_file = target_global
            param_origin = inject_global
            os.system("clear")
            print(Fore.RESET + "Global targets set to: " + param_file + " with injecting " + param_origin)
    else:
            global target_file
            global inject_string
            param_file = target_file
            param_origin = inject_string

    headers = {'Origin': param_origin}
    list=[]
    f = open(param_file,'r')
    for x in f:
        target = 'https://' + x.replace('\n','')
        try:
                req = session.get(target, headers=headers, verify=False, timeout=5, allow_redirects=True)
                #RESPONSE BODY INJECTED +
                if param_origin in str(req.content):
                            print("\n" + Fore.GREEN +  "|" + param_origin + "| Injected on host: " + target + " --> Injected Origin reflected in BODY! Response:" + str(req.status_code))
                            save_to_file("\n" + target)
                #RESPONSE HEADER INJECTED +
                elif param_origin in str(req.headers):
                            print("\n" + Fore.GREEN +  "|" + param_origin + "| Injected on host: " + target + " --> Injected Origin reflected in HEADER! Response:" + str(req.status_code))
                            save_to_file("\n" + target)
                #INJECTION FAILED
                elif param_origin not in str(req.content) and param_origin not in str(req.headers):
                            print("\n" +  "|" + param_origin + "|" + Fore.RED + " Injection failed on: " + target + Fore.RESET + " --> Response:" + str(req.status_code))
        
        
        except ConnectTimeout:
            pass
        except (requests.exceptions.TooManyRedirects) as e:
            pass
        except requests.exceptions.ConnectionError as e:
            pass
    save_to_file("\nFinished CORS Header Injection")

def funct_clickjacking():
    global menu
    save_to_file("\nClickJacking vulnerability Detected:")

    if global_set == 1:
            global target_global
            param_file = target_global
            os.system("clear")
            print(Fore.RESET + "Global targets set to: " + param_file + "To test for ClickJacking vulnerability")
    else:
            global target_file
            param_file = target_file

    list=[]
    f = open(param_file,'r')
    for x in f:
        target = 'https://' + x.replace('\n','')
        try:
                req = session.get(target, verify=False, timeout=5, allow_redirects=True)
                #RESPONSE HEADER INJECTED +
                if "X-Frame-Options: DENY" in str(req.headers) or "X-Frame-Options: SAMEORIGIN" in str(req.headers):
                            print("\n" + Fore.GREEN +  "| Vulnerable host: " + target + " Response:" + str(req.status_code))
                            save_to_file("\n" + target)
                #INJECTION FAILED
                elif "X-Frame-Options:" not in str(req.headers):
                            print("\n" + Fore.RED +  "|" + target + " is not vulnerable | Response:" + str(req.status_code))
        
        
        except ConnectTimeout:
            pass
        except (requests.exceptions.TooManyRedirects) as e:
            pass
        except requests.exceptions.ConnectionError as e:
            pass
    save_to_file("\nFinished test for ClickJacking")
    
    menu=True
    funct_main_menu()


def funct_magicHax():
    funct_hostheader()
    funct_cors()
    funct_clickjacking()



def funct_main_menu():
    global target_file
    global inject_string
    global global_set
    global target_global
    global inject_global
    global menu
    global_set = 0
    isExist = False
    while menu:
        print(Fore.RESET+"""
        1.Host header injection
        2.CORS
        3.ClickJacking
        4.HACK.exe (collect all the shit)
        5.Set GLOBAL targets
        6.Exit/Quit
        """)
    #INVOKE HOSTHEADER
        menu = input("Select a test to run! ")
        if menu == "1":
            if global_set == 0:
                while isExist != True:
                    target_file = input("provide the full path of txt containing targets: ")
                    inject_string = input("provide the injectable Domain: ")
                    isExist = os.path.exists(target_file)
                    if isExist == False:
                        os.system("clear")
                        print("Target file invalid!")
                        input("Press Enter to continue...")
                        os.system("clear")
                    else:
                        funct_hostheader()
            else:
                funct_hostheader()
                    
    #INVOKE ORIGIN
        elif menu == "2":
            if global_set == 0:
                while isExist != True:
                    target_file = input("provide the full path of txt containing targets: ")
                    inject_string = input("provide the injectable Origin: ")
                    isExist = os.path.exists(target_file)
                    if isExist == False:
                        os.system("clear")
                        print("Target file invalid!")
                        input("Press Enter to continue...")
                        os.system("clear")
                    else:
                        funct_cors()
            else:
                funct_cors()


    #INVOKE ClickJacking
        elif menu == "3":
            if global_set == 0:
                while isExist != True:
                    target_file = input("provide the full path of txt containing targets: ")
                    isExist = os.path.exists(target_file)
                    if isExist == False:
                        os.system("clear")
                        print("Target file invalid!")
                        input("Press Enter to continue...")
                        os.system("clear")
                    else:
                        funct_clickjacking()
            else:
                funct_clickjacking()

    #INVOKE HAXMAGIC
        elif menu == "4":
            if global_set == 0:
                while isExist != True:
                    target_file = input("provide the full path of txt containing targets: ")
                    inject_string = input("provide the injectable string: ")
                    isExist = os.path.exists(target_file)
                    if isExist == False:
                        os.system("clear")
                        print("Target file invalid!")
                        input("Press Enter to continue...")
                        os.system("clear")
                    else:
                        funct_magicHax()
            else:
                funct_magicHax()

    #SET GLOBAL TARGETS
        elif menu == "5":
           
            while isExist != True:
                
                target_global = input("provide the full path of txt containing targets: ")
                inject_global = input("provide the injectable string: ")
                isExist = os.path.exists(target_global)
                if isExist == False:
                    os.system("clear")
                    print("Target file invalid!")
                    input("Press Enter to continue...")
                    os.system("clear")
                else:
                    global_set = 1
        
                

        else:
            print ("Invalid choice!")
            menu = None



#MAIN
global_set = 0
inject_global = ""
target_file = ""
inject_string = ""
isExist = ""
now = ""
file_name = ""
isExists = False
menu=True
now = str(datetime.now())
file_name = now + ".txt"
os.system("clear")
print(Fore.BLUE + logo)
funct_main_menu()

import time,os,random, json, sys, platform
from colorama import Fore, Back, Style, init
from valclient.client import Client

debug = True

init(autoreset=True)

version = 0
title = Fore.RED+"Valo"+Fore.WHITE+"Lock | Version: "+Fore.RED+str(version)
delay = 0.5

regions = ['BR','EU','KR','LATAM','NA','AP']
regionnames = {
    "BR":"Brazil",
    "EU":"Europe",
    "KR":"Korea",
    "LATAM":"Latin America",
    "NA":"North America",
    "AP":"Southeast Asia / Asia-Pacific",
}

agents = {}
with open('data.json','r') as f:
    agents = json.load(f)

maps = ['Lotus','Pearl','Fracture','Breeze','Icebox','Bind','Haven','Split','Ascent','Universal']


def region_select():
    """
    Select a users region
    """
    selecting = True
    selected = 0
    while selecting:
        os.system("CLS")
        print(title)
        print(Fore.CYAN+"Select a region using W, S, and ENTER keys\n")
        for i in range(len(regions)):
            if i == selected:
                print(Back.RED+regionnames[regions[i]])
            else:
                print(regions[i])
        print("")
        key = input("> ")
        if key == "w":
            if selected < 1:
                pass
            else:
                selected-=1
        elif key == "s":
            if selected>len(regions)-2:
                pass
            else:
                selected+=1
        elif key == "":
            selecting = False
    os.system("CLS")
    print(title)
    print("You selected "+regions[selected]+" ("+regionnames[regions[selected]]+")")
    input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
    return regions[selected].lower()
def agent_select():
    """
    Select an agent
    """
    selecting = True
    while selecting:
        os.system("CLS")
        print(title)
        agent = input("Enter an angent name (like KAYO or Jett)"+Fore.RED+"\nLeave blank to cancle"+Fore.RESET+"\n\n> ").lower()
        if agent.lower() in agents['agents'].keys():
            selecting = False
        elif agent == "":
            selecting = False
    if agent == "":
        pass
    else:
        os.system("CLS")
        print(title)
        print("You selected "+agent)
        input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
        return agent.lower()
def map_select():
    """
    Select a map
    """
    selecting = True
    selected = 0
    while selecting:
        os.system("CLS")
        print(title)
        print(Fore.CYAN+"Select a map using W, S, and ENTER keys\n")
        for i in range(len(maps)):
            if i == selected:
                print(Back.RED+maps[i])
            else:
                print(maps[i])
        print("")
        key = input("")
        if key == "w":
            if selected < 1:
                pass
            else:
                selected-=1
        elif key == "s":
            if selected>len(maps)-2:
                pass
            else:
                selected+=1
        elif key == "":
            selecting = False
    os.system("CLS")
    print(title)
    print("You selected "+maps[selected])
    input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
    return maps[selected].lower()

if platform.system() == 'Windows':
    os.system('cls & title ValoLock')
elif platform.system() != 'Windows':
    os.system("CLS")
    print(title)
    print(Fore.CYAN+"It looks like you are on "+platform.system()+". ValoLock works best on Windows.")
    input(Fore.BLACK+"\nPress ENTER to exit")
    exit()

client = Client(region=region_select())
client.activate()

lotus = []
pearl = []
fracture = []
breeze = []
icebox = []
bind = []
haven = []
split = []
ascent = []

valolock_history = []

while True:
    os.system("CLS")
    print(title)
    print(Back.RED+"\n  Menu  ")
    print("[1] - Set Agent Pool\n[2] - Start Instalock\n[3] - Change Delay | Current Delay: "+str(delay))
    key = input()
    if key == "1":
        location = map_select()
        selecting = True
        pool = []
        while selecting:
            agent = agent_select()
            if agent in pool:
                pass
            elif agent == None:
                pass
            else:
                pool.append(agent)
            if agent != None:
                if input("\nWould you like to add another agent? (Y/n)").lower() != "y":
                    selecting = False
            else:
                selecting = False
        if location == "lotus":
            lotus = []
            for i in range(len(pool)):
                lotus.append(pool[i])
        elif location == "pearl":
            pearl = []
            for i in range(len(pool)):
                pearl.append(pool[i])
        elif location == "fracture":
            fracture = []
            for i in range(len(pool)):
                fracture.append(pool[i])
        elif location == "breeze":
            breeze = []
            for i in range(len(pool)):
                breeze.append(pool[i])
        elif location == "icebox":
            icebox = []
            for i in range(len(pool)):
                icebox.append(pool[i])
        elif location == "bind":
            bind = []
            for i in range(len(pool)):
                bind.append(pool[i])
        elif location == "haven":
            haven = []
            for i in range(len(pool)):
                haven.append(pool[i])
        elif location == "split":
            split = []
            for i in range(len(split)):
                split.append(pool[i])
        elif location == "ascent":
            ascent = []
            for i in range(len(pool)):
                ascent.append(pool[i])
        elif location == "universal":
            universal = []
            for i in range(len(pool)):
                universal.append(pool[i])
        else:
            print("Error: No location")
    elif key == "2":
        locking = True
        while locking:
            try:
                os.system("CLS")
                print(title)
                sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                matchID = client.pregame_fetch_match()['ID']
                print("Waiting for match")
                if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in valolock_history)):
                    print("Match found")
                    matchInfo = client.pregame_fetch_match(matchID)
                    mapName = matchInfo["MapID"].split('/')[-1].lower()
                    if debug == True:
                        print(matchInfo)
                        print(mapName)
                    if len(universal)!= 0:
                        selagent = random.choice(universal)
                    elif mapName == "lotus":
                        selagent = random.choice(lotus)
                    elif mapName == "pearl":
                        selagent = random.choice(pearl)
                    elif mapName == "fracture":
                        selagent = random.choice(fracture)
                    elif mapName == "breeze":
                        selagent = random.choice(breeze)
                    elif mapName == "icebox":
                        selagent = random.choice(icebox)
                    elif mapName == "bind":
                        selagent = random.choice(bind)
                    elif mapName == "haven":
                        selagent = random.choice(haven)
                    elif mapName == "split":
                        selagent = random.choice(split)
                    elif mapName == "ascent":
                        selagent = random.choice(ascent)
                    print("Selecting agent: "+Fore.GREEN+selagent)
                    time.sleep(delay/2)
                    client.pregame_select_character(agents['agents'][selagent])
                    time.sleep(delay/2)
                    client.pregame_lock_character(agents['agents'][selagent])
                    print("Agent Locked!")
                    time.sleep(5)
                    locking = False
                    valolock_history.append(matchID)
            except Exception as e:
                print("", end="")
    elif key == "3":
        os.system("CLS")
        print(title)
        print(Back.BLUE+"\n  Change Delay  ")
        print(Fore.RED+"0"+Style.RESET_ALL+" - [0 seccond]\n"+Fore.YELLOW+"1"+Style.RESET_ALL+" - [0.2 secconds]\n"+Fore.YELLOW+"2"+Style.RESET_ALL+" - [0.5 secconds]\n"+Fore.GREEN+"3"+Style.RESET_ALL+" - [0.8 secconds]\n"+Fore.GREEN+"4"+Style.RESET_ALL+" - [1 seccond]")
        print("")
        key = input("")
        if key == "0":
            delay = 0
        elif key == "1":
            delay = 0.2
        elif key == "2":
            delay = 0.5
        elif key == "3":
            delay = 0.8
        elif key == "4":
            delay = 1
    elif key == "0":
        os.system("CLS")
        print(title)
        print(Back.GREEN+"\n  DEBUG  ")
        print(Style.BRIGHT+Fore.GREEN+"\nMAP POOLS")
        print("Universal:",universal)
        print("Lotus:",lotus)
        print("Pearl:",pearl)
        print("Fracture:",fracture)
        print("Breeze:",breeze)
        print("Icebox",icebox)
        print("Bind:",bind)
        print("Haven:",haven)
        print("Split:",split)
        print("Ascent:",ascent)
        print("\nPress ENTER to continue...")
        input()


input()
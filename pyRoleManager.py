## Text menu in Python
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import os
import json
import sys
import re
import cfgData
import charMenu
import rl

# Setup character data list
char={}

# Read Professions into List
plist = {}
pi=1
with open("cfg/pro.csv") as pf:
    for pline in pf:
        plist[pi]=pline.rstrip('\n').split(",")
        #print plist[pi]
        pi+=1


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Create New Character"
    print "2. Show Character"
    print "3. Add Misc Bonus to Character"
    print "4. Assign Weapon Costs"
    print "5. Raise Character Level"
    #print "6. Delete Character"
    #print "7. Skills"
    print ""
    print "X. Exit"
    print 67 * "-"

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)

# Create a menu of characters
def create_char_menu():
    # Run menu
    p=char_menu()
    print p
    menu_len=len(p)

    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the character file
    file=open(char_dir+"/"+p+"/"+p+".json","r")
    char_data=file.read()
    char_dict=[]
    counter=0

    for words in char_data.split(":"):
        #print counter,"-",words
        char_dict.insert(counter,words)
        counter+=1

# Create a menu of characters
'''
def char_menu():
    # Clear list before function is ran
    menu_items=[]
    i=1
    print 5 * "-", "Characters", 5 * "-"
    for file in os.listdir(char_dir):
        menu_items.insert(i,file)
        print "{:<2}.) {:15}".format(i,file)
        i+=1
    print 25 * "-"
    return menu_items
'''

# Print prime requisite error
def pr_text():
    print "This is a Prime requisite and must be 90 or higher"

# Calcalute Potential stats based on current stats
poten=0
def pot_calc(current,pot_roll):
    # Under 25
    if current<25:
        if pot_roll<11:
            poten=25
        elif pot_roll>=11 and pot_roll<=20:
            poten=30
        elif pot_roll>=21 and pot_roll<=30:
            poten=35
        elif pot_roll>=31 and pot_roll<=35:
            poten=38
        elif pot_roll>=36 and pot_roll<=40:
            poten=40
        elif pot_roll>=41 and pot_roll<=45:
            poten=42
        elif pot_roll>=46 and pot_roll<=49:
            poten=44
        elif pot_roll>=50 and pot_roll<=51:
            poten=46
        elif pot_roll>=52 and pot_roll<=53:
            poten=48
        elif pot_roll>=54 and pot_roll<=55:
            poten=50
        elif pot_roll>=56 and pot_roll<=57:
            poten=52
        elif pot_roll>=58 and pot_roll<=59:
            poten=54
        elif pot_roll>=60 and pot_roll<=61:
            poten=56
        elif pot_roll>=62 and pot_roll<=63:
            poten=58
        elif pot_roll>=64 and pot_roll<=65:
            poten=60
        elif pot_roll>=66 and pot_roll<=67:
            poten=62
        elif pot_roll>=68 and pot_roll<=69:
            poten=64
        elif pot_roll>=70 and pot_roll<=71:
            poten=66
        elif pot_roll>=72 and pot_roll<=73:
            poten=68
        elif pot_roll>=74 and pot_roll<=75:
            poten=70
        elif pot_roll>=76 and pot_roll<=77:
            poten=72
        elif pot_roll>=78 and pot_roll<=79:
            poten=74
        elif pot_roll>=80 and pot_roll<=81:
            poten=76
        elif pot_roll>=82 and pot_roll<=83:
            poten=78
        elif pot_roll>=84 and pot_roll<=85:
            poten=80
        elif pot_roll>=86 and pot_roll<=87:
            poten=82
        elif pot_roll>=88 and pot_roll<=89:
            poten=84
        elif pot_roll==90:
            poten=86
        elif pot_roll==91:
            poten=88
        elif pot_roll==92:
            poten=90
        elif pot_roll==93:
            poten=91
        elif pot_roll==94:
            poten=92
        elif pot_roll==95:
            poten=93
        elif pot_roll==96:
            poten=94
        elif pot_roll==97:
            poten=95
        elif pot_roll==98:
            poten=96
        elif pot_roll==99:
            poten=97
        elif pot_roll==100:
            poten=98
    # 25-39
    elif current>=25 and current<=39:
        if pot_roll<21:
            poten=current
        elif pot_roll>=21 and pot_roll<=30:
            poten=39
        elif pot_roll>=31 and pot_roll<=35:
            poten=42
        elif pot_roll>=36 and pot_roll<=40:
            poten=45
        elif pot_roll>=41 and pot_roll<=45:
            poten=47
        elif pot_roll>=46 and pot_roll<=49:
            poten=49
        elif pot_roll>=50 and pot_roll<=51:
            poten=51
        elif pot_roll>=52 and pot_roll<=53:
            poten=53
        elif pot_roll>=54 and pot_roll<=55:
            poten=55
        elif pot_roll>=56 and pot_roll<=57:
            poten=57
        elif pot_roll>=58 and pot_roll<=59:
            poten=59
        elif pot_roll>=60 and pot_roll<=61:
            poten=61
        elif pot_roll>=62 and pot_roll<=63:
            poten=63
        elif pot_roll>=64 and pot_roll<=65:
            poten=65
        elif pot_roll>=66 and pot_roll<=67:
            poten=67
        elif pot_roll>=68 and pot_roll<=69:
            poten=69
        elif pot_roll>=70 and pot_roll<=71:
            poten=71
        elif pot_roll>=72 and pot_roll<=73:
            poten=73
        elif pot_roll>=74 and pot_roll<=75:
            poten=75
        elif pot_roll>=76 and pot_roll<=77:
            poten=77
        elif pot_roll>=78 and pot_roll<=79:
            poten=79
        elif pot_roll>=80 and pot_roll<=81:
            poten=81
        elif pot_roll>=82 and pot_roll<=83:
            poten=83
        elif pot_roll>=84 and pot_roll<=85:
            poten=85
        elif pot_roll>=86 and pot_roll<=87:
            poten=86
        elif pot_roll>=88 and pot_roll<=89:
            poten=87
        elif pot_roll==90:
            poten=88
        elif pot_roll==91:
            poten=89
        elif pot_roll==92:
            poten=90
        elif pot_roll==93:
            poten=91
        elif pot_roll==94:
            poten=92
        elif pot_roll==95:
            poten=93
        elif pot_roll==96:
            poten=94
        elif pot_roll==97:
            poten=95
        elif pot_roll==98:
            poten=96
        elif pot_roll==99:
            poten=97
        elif pot_roll==100:
            poten=98
    # 40-59
    elif current>=40 and current<=59:
        if pot_roll<31:
            poten=current
        elif pot_roll>=31 and pot_roll<=35:
            poten=59
        elif pot_roll>=36 and pot_roll<=40:
            poten=62
        elif pot_roll>=41 and pot_roll<=45:
            poten=64
        elif pot_roll>=46 and pot_roll<=49:
            poten=66
        elif pot_roll>=50 and pot_roll<=51:
            poten=68
        elif pot_roll>=52 and pot_roll<=53:
            poten=70
        elif pot_roll>=54 and pot_roll<=55:
            poten=71
        elif pot_roll>=56 and pot_roll<=57:
            poten=72
        elif pot_roll>=58 and pot_roll<=59:
            poten=73
        elif pot_roll>=60 and pot_roll<=61:
            poten=74
        elif pot_roll>=62 and pot_roll<=63:
            poten=75
        elif pot_roll>=64 and pot_roll<=65:
            poten=76
        elif pot_roll>=66 and pot_roll<=67:
            poten=77
        elif pot_roll>=68 and pot_roll<=69:
            poten=78
        elif pot_roll>=70 and pot_roll<=71:
            poten=79
        elif pot_roll>=72 and pot_roll<=73:
            poten=80
        elif pot_roll>=74 and pot_roll<=75:
            poten=81
        elif pot_roll>=76 and pot_roll<=77:
            poten=82
        elif pot_roll>=78 and pot_roll<=79:
            poten=83
        elif pot_roll>=80 and pot_roll<=81:
            poten=84
        elif pot_roll>=82 and pot_roll<=83:
            poten=85
        elif pot_roll>=84 and pot_roll<=85:
            poten=86
        elif pot_roll>=86 and pot_roll<=87:
            poten=87
        elif pot_roll>=88 and pot_roll<=89:
            poten=88
        elif pot_roll==90:
            poten=89
        elif pot_roll==91:
            poten=90
        elif pot_roll==92:
            poten=91
        elif pot_roll==93:
            poten=92
        elif pot_roll==94:
            poten=93
        elif pot_roll==95:
            poten=94
        elif pot_roll==96:
            poten=95
        elif pot_roll==97:
            poten=96
        elif pot_roll==98:
            poten=97
        elif pot_roll==99:
            poten=98
        elif pot_roll==100:
            poten=99
    # 60-74
    elif current>=60 and current<=74:
        if pot_roll<56:
            poten=current
        elif pot_roll>=56 and pot_roll<=57:
            poten=74
        elif pot_roll>=58 and pot_roll<=59:
            poten=75
        elif pot_roll>=60 and pot_roll<=61:
            poten=76
        elif pot_roll>=62 and pot_roll<=63:
            poten=77
        elif pot_roll>=64 and pot_roll<=65:
            poten=78
        elif pot_roll>=66 and pot_roll<=67:
            poten=79
        elif pot_roll>=68 and pot_roll<=69:
            poten=80
        elif pot_roll>=70 and pot_roll<=71:
            poten=81
        elif pot_roll>=72 and pot_roll<=73:
            poten=82
        elif pot_roll>=74 and pot_roll<=75:
            poten=83
        elif pot_roll>=76 and pot_roll<=77:
            poten=84
        elif pot_roll>=78 and pot_roll<=79:
            poten=85
        elif pot_roll>=80 and pot_roll<=81:
            poten=86
        elif pot_roll>=82 and pot_roll<=83:
            poten=87
        elif pot_roll>=84 and pot_roll<=85:
            poten=88
        elif pot_roll>=86 and pot_roll<=87:
            poten=89
        elif pot_roll>=88 and pot_roll<=89:
            poten=90
        elif pot_roll==90:
            poten=91
        elif pot_roll==91:
            poten=92
        elif pot_roll==92:
            poten=93
        elif pot_roll==93:
            poten=94
        elif pot_roll==94:
            poten=95
        elif pot_roll==95:
            poten=96
        elif pot_roll==96:
            poten=97
        elif pot_roll==97:
            poten=97
        elif pot_roll==98:
            poten=98
        elif pot_roll==99:
            poten=98
        elif pot_roll==100:
            poten=99
    # 75-84
    elif current>=75 and current<=84:
        if pot_roll<56:
            poten=current
        elif pot_roll>=56 and pot_roll<=57:
            poten=84
        elif pot_roll>=58 and pot_roll<=59:
            poten=85
        elif pot_roll>=60 and pot_roll<=61:
            poten=86
        elif pot_roll>=62 and pot_roll<=63:
            poten=87
        elif pot_roll>=64 and pot_roll<=65:
            poten=88
        elif pot_roll>=66 and pot_roll<=67:
            poten=88
        elif pot_roll>=68 and pot_roll<=69:
            poten=89
        elif pot_roll>=70 and pot_roll<=71:
            poten=89
        elif pot_roll>=72 and pot_roll<=73:
            poten=90
        elif pot_roll>=74 and pot_roll<=75:
            poten=90
        elif pot_roll>=76 and pot_roll<=77:
            poten=91
        elif pot_roll>=78 and pot_roll<=79:
            poten=91
        elif pot_roll>=80 and pot_roll<=81:
            poten=92
        elif pot_roll>=82 and pot_roll<=83:
            poten=92
        elif pot_roll>=84 and pot_roll<=85:
            poten=93
        elif pot_roll>=86 and pot_roll<=87:
            poten=93
        elif pot_roll>=88 and pot_roll<=89:
            poten=94
        elif pot_roll==90:
            poten=94
        elif pot_roll==91:
            poten=95
        elif pot_roll==92:
            poten=95
        elif pot_roll==93:
            poten=96
        elif pot_roll==94:
            poten=96
        elif pot_roll==95:
            poten=97
        elif pot_roll==96:
            poten=97
        elif pot_roll==97:
            poten=98
        elif pot_roll==98:
            poten=98
        elif pot_roll==99:
            poten=99
        elif pot_roll==100:
            poten=99
    # 85-89
    elif current>=85 and current<=89:
        if pot_roll<66:
            poten=current
        elif pot_roll>=66 and pot_roll<=67:
            poten=89
        elif pot_roll>=68 and pot_roll<=69:
            poten=89
        elif pot_roll>=70 and pot_roll<=71:
            poten=90
        elif pot_roll>=72 and pot_roll<=73:
            poten=90
        elif pot_roll>=74 and pot_roll<=75:
            poten=91
        elif pot_roll>=76 and pot_roll<=77:
            poten=91
        elif pot_roll>=78 and pot_roll<=79:
            poten=92
        elif pot_roll>=80 and pot_roll<=81:
            poten=92
        elif pot_roll>=82 and pot_roll<=83:
            poten=93
        elif pot_roll>=84 and pot_roll<=85:
            poten=93
        elif pot_roll>=86 and pot_roll<=87:
            poten=94
        elif pot_roll>=88 and pot_roll<=89:
            poten=94
        elif pot_roll==90:
            poten=95
        elif pot_roll==91:
            poten=95
        elif pot_roll==92:
            poten=96
        elif pot_roll==93:
            poten=96
        elif pot_roll==94:
            poten=97
        elif pot_roll==95:
            poten=97
        elif pot_roll==96:
            poten=98
        elif pot_roll==97:
            poten=98
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=99
        elif pot_roll==100:
            poten=100
    # 90-94
    elif current>=90 and current<=94:
        if pot_roll<84:
            poten=current
        elif pot_roll>=84 and pot_roll<=85:
            poten=94
        elif pot_roll>=86 and pot_roll<=87:
            poten=94
        elif pot_roll>=88 and pot_roll<=89:
            poten=95
        elif pot_roll==90:
            poten=95
        elif pot_roll==91:
            poten=96
        elif pot_roll==92:
            poten=96
        elif pot_roll==93:
            poten=97
        elif pot_roll==94:
            poten=97
        elif pot_roll==95:
            poten=98
        elif pot_roll==96:
            poten=98
        elif pot_roll==97:
            poten=99
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 95-97
    elif current>=95 and current<=97:
        if pot_roll<90:
            poten=current
        elif pot_roll==90:
            poten=97
        elif pot_roll==91:
            poten=97
        elif pot_roll==92:
            poten=97
        elif pot_roll==93:
            poten=98
        elif pot_roll==94:
            poten=98
        elif pot_roll==95:
            poten=98
        elif pot_roll==96:
            poten=99
        elif pot_roll==97:
            poten=99
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 98-99
    elif current>=98 and current<=99:
        if pot_roll<94:
            poten=current
        elif pot_roll==94:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==95:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==96:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==97:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==98:
            poten=100
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 100
    elif current>=100:
        if pot_roll<100:
            poten=current
        elif pot_roll==100:
            poten=101
    return poten

# Check if the profession's prime requisites are 90+
# prompt for a new value if less than 90
num=""
def prime_req(pro,char_stat,num):
    if pro==1:
        # Assassin
        if char_stat.upper()=="QU" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==2:
        # Bounty Hunter
        if char_stat.upper()=="AG" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==3:
        # Barbarian
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==4:
        # Burglar
        if char_stat.upper()=="IN" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==5:
        # Dancer
        if char_stat.upper()=="QU" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==6:
        # Fighter
        if char_stat.upper()=="ST" or char_stat.upper()=="CP":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==7:
        # High Warrior Monk
        if char_stat.upper()=="AG" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==8:
        # Rogue
        if char_stat.upper()=="ST" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==9:
        # Scholar
        if char_stat.upper()=="IN" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==10:
        # Theif
        if char_stat.upper()=="QU" or char_stat.upper()=="SG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==11:
        # Trader
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==12:
        # Warrior
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==13:
        # Warrior Monk
        if char_stat.upper()=="QU" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==14:
        # Alchemist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==15:
        # Animist
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==16:
        # Cleric
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==17:
        # Conjuror
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==18:
        # Druid
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==19:
        # Healer
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==20:
        # Illusionist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==21:
        # Lay Healer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==22:
        # Magician
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==23:
        # Mentalist
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==24:
        # Runemaster
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==25:
        # Sage
        if char_stat.upper()=="PR" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==26:
        # Seer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==27:
        # Shaman
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==28:
        # Bard
        if char_stat.upper()=="PR" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==29:
        # Beastmaster
        if char_stat.upper()=="PR" or char_stat.upper()=="ST":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==30:
        # Delver
        if char_stat.upper()=="EM" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==31:
        # Dervish
        if char_stat.upper()=="AG" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==32:
        # Monk
        if char_stat.upper()=="EM" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==33:
        # Montebanc
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==34:
        # Nightblade
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==35:
        # Noble Warrior
        if char_stat.upper()=="ST" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==36:
        # Paladin
        if char_stat.upper()=="IN" or char_stat.upper()=="ST":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==37:
        # Ranger
        if char_stat.upper()=="CO" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==38:
        # Sleuth
        if char_stat.upper()=="IN" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==39:
        # Warrior Mage
        if char_stat.upper()=="ST" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==40:
        # Archmage
        if char_stat.upper()=="IN" or char_stat.upper()=="EM" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==41:
        # Astrologer
        if char_stat.upper()=="IN" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==42:
        # Crystal Mage
        if char_stat.upper()=="PR" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==43:
        # Magus
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==44:
        # Mystic
        if char_stat.upper()=="PR" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==45:
        # Necromancer
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==46:
        # Sorceror
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==47:
        # Warlock
        if char_stat.upper()=="IN" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==48:
        # Witch
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    return num

st_pot_in,qu_pot_in,pr_pot_in,in_pot_in,em_pot_in=0,0,0,0,0
co_pot_in,ag_pot_in,sd_pot_in,me_pot_in,re_pot_in=0,0,0,0,0

# Start of the basic character creation, Name, Profession, Race and Stats
def create_char():
    user_name=str(raw_input('Please enter your first name: '))
    char_path=cfgData.char_dir+"/"+user_name
    print char_path
    if not os.path.exists(char_path):
        os.makedirs(char_path)
    if os.path.exists(char_path+"/"+user_name+".json") == True:
        print "Character exists"
        sys.exit()
    else:
        # Write character name to list
        char['name']=user_name

    print 25 * "-" , "Professions", 25 * "-"
    print ""
    print 15 * "-" , "Non" , 15 * "-"
    print "1.) {:20} 2.) {:19}".format(plist[1][0],plist[2][0])
    print "3.) {:20} 4.) {:19}".format(plist[3][0],plist[4][0])
    print "5.) {:20} 6.) {:19}".format(plist[5][0],plist[6][0])
    print "7.) {:20} 8.) {:19}".format(plist[7][0],plist[8][0])
    print "9.) {:20} 10.) {:19}".format(plist[9][0],plist[10][0])
    print "11.) {:19} 12.) {:19}".format(plist[11][0],plist[12][0])
    print "13.) {:19}".format(plist[13][0])
    print ""
    print 15 * "-", "Pure", 15 * "-"
    print "14.) {:19} 15.) {:19}".format(plist[14][0],plist[15][0])
    print "16.) {:19} 17.) {:19}".format(plist[16][0],plist[17][0])
    print "18.) {:19} 19.) {:19}".format(plist[18][0],plist[19][0])
    print "20.) {:19} 21.) {:19}".format(plist[20][0],plist[21][0])
    print "22.) {:19} 23.) {:19}".format(plist[22][0],plist[23][0])
    print "24.) {:19} 25.) {:19}".format(plist[24][0],plist[25][0])
    print "26.) {:19} 27.) {:19}".format(plist[26][0],plist[27][0])
    print ""
    print 15 * "-", "Semi", 15 * "-"
    print "28.) {:19} 29.) {:19}".format(plist[28][0],plist[29][0])
    print "30.) {:19} 31.) {:19}".format(plist[30][0],plist[31][0])
    print "32.) {:19} 33.) {:19}".format(plist[32][0],plist[33][0])
    print "34.) {:19} 35.) {:19}".format(plist[34][0],plist[35][0])
    print "36.) {:19} 38.) {:19}".format(plist[36][0],plist[37][0])
    print "39.) {:19}".format(plist[39][0])
    print ""
    print 15 * "-", "Hybrid", 15 * "-"
    print "40.) {:19} 41.) {:19}".format(plist[40][0],plist[41][0])
    print "42.) {:19} 43.) {:19}".format(plist[42][0],plist[43][0])
    print "44.) {:19} 45.) {:19}".format(plist[44][0],plist[45][0])
    print "46.) {:19} 47.) {:19}".format(plist[46][0],plist[47][0])
    print "48.) {:19}".format(plist[48][0])
    print 63 * "-"
    pro_ch=int(raw_input('Select Profession: '))
    if pro_ch==1:
        pro_name=plist[pro_ch][0]
    elif pro_ch==2:
        pro_name=plist[pro_ch][0]
    elif pro_ch==3:
        pro_name=plist[pro_ch][0]
    elif pro_ch==4:
        pro_name=plist[pro_ch][0]
    elif pro_ch==5:
        pro_name=plist[pro_ch][0]
    elif pro_ch==6:
        pro_name=plist[pro_ch][0]
    elif pro_ch==7:
        pro_name=plist[pro_ch][0]
    elif pro_ch==8:
        pro_name=plist[pro_ch][0]
    elif pro_ch==9:
        pro_name=plist[pro_ch][0]
    elif pro_ch==10:
        pro_name=plist[pro_ch][0]
    elif pro_ch==11:
        pro_name=plist[pro_ch][0]
    elif pro_ch==12:
        pro_name=plist[pro_ch][0]
    elif pro_ch==13:
        pro_name=plist[pro_ch][0]
    elif pro_ch==14:
        pro_name=plist[pro_ch][0]
    elif pro_ch==15:
        pro_name=plist[pro_ch][0]
    elif pro_ch==16:
        pro_name=plist[pro_ch][0]
    elif pro_ch==17:
        pro_name=plist[pro_ch][0]
    elif pro_ch==18:
        pro_name=plist[pro_ch][0]
    elif pro_ch==19:
        pro_name=plist[pro_ch][0]
    elif pro_ch==20:
        pro_name=plist[pro_ch][0]
    elif pro_ch==21:
        pro_name=plist[pro_ch][0]
    elif pro_ch==22:
        pro_name=plist[pro_ch][0]
    elif pro_ch==23:
        pro_name=plist[pro_ch][0]
    elif pro_ch==24:
        pro_name=plist[pro_ch][0]
    elif pro_ch==25:
        pro_name=plist[pro_ch][0]
    elif pro_ch==26:
        pro_name=plist[pro_ch][0]
    elif pro_ch==27:
        pro_name=plist[pro_ch][0]
    elif pro_ch==28:
        pro_name=plist[pro_ch][0]
    elif pro_ch==29:
        pro_name=plist[pro_ch][0]
    elif pro_ch==30:
        pro_name=plist[pro_ch][0]
    elif pro_ch==31:
        pro_name=plist[pro_ch][0]
    elif pro_ch==32:
        pro_name=plist[pro_ch][0]
    elif pro_ch==33:
        pro_name=plist[pro_ch][0]
    elif pro_ch==34:
        pro_name=plist[pro_ch][0]
    elif pro_ch==35:
        pro_name=plist[pro_ch][0]
    elif pro_ch==36:
        pro_name=plist[pro_ch][0]
    elif pro_ch==37:
        pro_name=plist[pro_ch][0]
    elif pro_ch==38:
        pro_name=plist[pro_ch][0]
    elif pro_ch==39:
        pro_name=plist[pro_ch][0]
    elif pro_ch==40:
        pro_name=plist[pro_ch][0]
    elif pro_ch==41:
        pro_name=plist[pro_ch][0]
    elif pro_ch==42:
        pro_name=plist[pro_ch][0]
    elif pro_ch==43:
        pro_name=plist[pro_ch][0]
    elif pro_ch==44:
        pro_name=plist[pro_ch][0]
    elif pro_ch==45:
        pro_name=plist[pro_ch][0]
    elif pro_ch==46:
        pro_name=plist[pro_ch][0]
    elif pro_ch==47:
        pro_name=plist[pro_ch][0]
    elif pro_ch==48:
        pro_name=plist[pro_ch][0]

    # write Profession to list
    char['pro_name']=pro_name
    print 10 * "-"

    # Select Race
    print ""
    print 10 * "-", "Race", 10 * "-"
    print ""
    print "1. Common Man"
    print "2. Wood Elf      3. High Elf      4. Half-elf"
    print "5. Grey Elf      6. Aquatic Elf   7. Dark Elf"
    print ""
    print "8. Tallfellow Halfling      9. Stout Halfling"
    print ""
    print "10. Dwarf        11. Half-Dwarf"
    print "12. Half-Orc   13. Half-Ogre    14. Half-Troll"
    print ""
    print "15. Gnomes     16. Hira'razhir (Avians)"
    print "17. Idiyva (Felines)   18. Vulfen (Wolfmen)"
    print "19. Sstoi'isslythi (Reptilies)"
    print 25 * "-"

    race_input=int(raw_input('Select a Race: '))
    if race_input==1:
        char['race']="Common Man"
    elif race_input==2:
        char['race']="Wood Elf"
    elif race_input==3:
        char['race']="High Elf"
    elif race_input==4:
        char['race']="Half-elf"
    elif race_input==5:
        char['race']="Grey Elf"
    elif race_input==6:
        char['race']="Aquatic Elf"
    elif race_input==7:
        char['race']="Dark Elf"
    elif race_input==8:
        char['race']="Tallfellow Halfling"
    elif race_input==9:
        char['race']="Stout Halfling"
    elif race_input==10:
        char['race']="Dwarf"
    elif race_input==11:
        char['race']="Half-Dwarf"
    elif race_input==12:
        char['race']="Half-Orc"
    elif race_input==13:
        char['race']="Half-Ogre"
    elif race_input==14:
        char['race']="Half-Troll"
    elif race_input==15:
        char['race']="Gnomes"
    elif race_input==16:
        char['race']="Hira'razhir"
    elif race_input==17:
        char['race']="Idiyva"
    elif race_input==18:
        char['race']="Vulfen"
    elif race_input==19:
        char['race']="Sstoi'isslythi"

    ### Enter current statistic values

    st_stat_input=int(raw_input('Strength: '))
    st_stat=prime_req(pro_ch,"st",st_stat_input)

    qu_stat_input=int(raw_input('Quickness: '))
    qu_stat=prime_req(pro_ch,"qu",qu_stat_input)

    pr_stat_input=int(raw_input('Presence: '))
    pr_stat=prime_req(pro_ch,"pr",pr_stat_input)

    in_stat_input=int(raw_input('Intuition: '))
    in_stat=prime_req(pro_ch,"in",in_stat_input)

    em_stat_input=int(raw_input('Empathy: '))
    em_stat=prime_req(pro_ch,"em",em_stat_input)

    co_stat_input=int(raw_input('Constitution: '))
    co_stat=prime_req(pro_ch,"co",co_stat_input)

    ag_stat_input=int(raw_input('Agility: '))
    ag_stat=prime_req(pro_ch,"ag",ag_stat_input)

    sd_stat_input=int(raw_input('Self-Discipline: '))
    sd_stat=prime_req(pro_ch,"sd",sd_stat_input)

    me_stat_input=int(raw_input('Memory: '))
    me_stat=prime_req(pro_ch,"me",me_stat_input)

    re_stat_input=int(raw_input('Reasoning: '))
    re_stat=prime_req(pro_ch,"re",re_stat_input)

    ### Calculate Potential Value using pot_calc function
    st_pot_in=int(raw_input('Potential Roll (ST): '))
    st_pot=pot_calc(st_stat,st_pot_in)

    qu_pot_in=int(raw_input('Potential Roll (QU): '))
    qu_pot=pot_calc(qu_stat,qu_pot_in)

    pr_pot_in=int(raw_input('Potential Roll (PR): '))
    pr_pot=pot_calc(pr_stat,pr_pot_in)

    in_pot_in=int(raw_input('Potential Roll (IN): '))
    in_pot=pot_calc(in_stat,in_pot_in)

    em_pot_in=int(raw_input('Potential Roll (EM): '))
    em_pot=pot_calc(em_stat,em_pot_in)

    co_pot_in=int(raw_input('Potential Roll (CO): '))
    co_pot=pot_calc(co_stat,co_pot_in)

    ag_pot_in=int(raw_input('Potential Roll (AG): '))
    ag_pot=pot_calc(ag_stat,ag_pot_in)

    sd_pot_in=int(raw_input('Potential Roll (SD): '))
    sd_pot=pot_calc(sd_stat,sd_pot_in)

    me_pot_in=int(raw_input('Potential Roll (ME): '))
    me_pot=pot_calc(me_stat,me_pot_in)

    re_pot_in=int(raw_input('Potential Roll (RE): '))
    re_pot=pot_calc(re_stat,re_pot_in)
    #print "ST Pot: %s" % st_pot
    #print "QU Pot: %s" % qu_pot
    #print "PR Pot: %s" % pr_pot
    #print "IN Pot: %s" % in_pot
    #print "EM Pot: %s" % em_pot
    #print "CO Pot: %s" % co_pot
    #print "AG Pot: %s" % ag_pot
    #print "SD Pot: %s" % sd_pot
    #print "ME Pot: %s" % me_pot
    #print "RE Pot: %s" % re_pot

    print 10 * "-"

    char['st_stat']=st_stat
    char['st_pot']=st_pot
    char['qu_stat']=qu_stat
    char['qu_pot']=qu_pot
    char['pr_stat']=pr_stat
    char['pr_pot']=pr_pot
    char['in_stat']=in_stat
    char['in_pot']=in_pot
    char['em_stat']=em_stat
    char['em_pot']=em_pot
    char['co_stat']=co_stat
    char['co_pot']=co_pot
    char['ag_stat']=ag_stat
    char['ag_pot']=ag_pot
    char['sd_stat']=sd_stat
    char['sd_pot']=sd_pot
    char['me_stat']=me_stat
    char['me_pot']=me_pot
    char['re_stat']=re_stat
    char['re_pot']=re_pot
    char['lvl']=0
    char['realm']=plist[pro_ch][8]
    char['stmb'],char['qumb'],char['emmb'],char['inmb'],char['prmb']=0,0,0,0,0
    char['comb'],char['agmb'],char['sdmb'],char['remb'],char['memb']=0,0,0,0,0

    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    f.close()
    sc=[]

    for x in statchart:
        sc.append(x.split(","))

    # Loop through statistics to pull bonuses
    for x1 in sc:
        if int(x1[0]) == int(char['st_stat']):
            stb,stdp,stpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['qu_stat']):
            qub,qudp,qupp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['pr_stat']):
            prb,prdp,prpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['in_stat']):
            inb,indp,inpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['em_stat']):
            emb,emdp,empp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['co_stat']):
            cob,codp,copp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['ag_stat']):
            agb,agdp,agpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['sd_stat']):
            sdb,sddp,sdpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['me_stat']):
            meb,medp,mepp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['re_stat']):
            reb,redp,repp=x1[1],x1[2],x1[3]

    ###################
    # Lookup Race Bonus
    ###################
    with open(cfgData.cfg_dir+"/race.csv") as r:
        racechart =r.read().splitlines()
    r.close()
    rc=[]

    for x in racechart:
        rc.append(x.split(","))

    # Race Bonus
    for x2 in rc:
        if x2[0] == char['race']:
            raceb=x2

    #######################
    # Calcalute Total Bonus
    #######################

    sttb=(int(stb)+int(raceb[1])+int(char['stmb']))
    qutb=(int(qub)+int(raceb[2])+int(char['qumb']))
    prtb=(int(prb)+int(raceb[3])+int(char['prmb']))
    intb=(int(inb)+int(raceb[4])+int(char['inmb']))
    emtb=(int(emb)+int(raceb[5])+int(char['emmb']))
    cotb=(int(cob)+int(raceb[6])+int(char['comb']))
    agtb=(int(agb)+int(raceb[7])+int(char['agmb']))
    sdtb=(int(sdb)+int(raceb[8])+int(char['sdmb']))
    metb=(int(meb)+int(raceb[9])+int(char['memb']))
    retb=(int(reb)+int(raceb[10])+int(char['remb']))
    tdp=float(codp)+float(agdp)+float(sddp)+float(medp)+float(redp)
    char['dp']=tdp

    # Power Point Math
    stpp,qupp,copp,agpp,sdpp,mepp,repp="-","-","-","-","-","-","-"
    if char['realm'] == "NULL":
        prpp,inpp,empp=0.0,0.0,0.0
        tpp=0.0
    if char['realm'] == "PR":
        inpp,empp=0.0,0.0
        tpp=prpp
    if char['realm'] == "IN":
        empp,prpp=0.0,0.0
        tpp=inpp
    if char['realm'] == "EM":
        inpp,prpp=0.0,0.0
        tpp=empp
    if char['realm'] == "IP":
        empp=0.0
        tpp=(float(inpp)+float(prpp))/2
    if char['realm'] == "PE":
        inpp=0.0
        tpp=(float(empp)+float(prpp))/2
    if char['realm'] == "IE":
        prpp=0.0
        tpp=(float(inpp)+float(empp))/2
    if char['realm'] == "AR":
        tpp=(float(inpp)+float(prpp)+float(empp))/3

    # Development Point Math
    stdp,qudp,emdp,indp,prdp="-","-","-","-","-"

    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    f.close()
    skill_list=[]
    for list in sl:
        skill_list.append(list.split(","))
        crt=1
        for outer_list in skill_list:
            index=int(plist[pro_ch][1])
            char[crt]=(outer_list[1],outer_list[5],outer_list[7],outer_list[index],outer_list[6],0,0,0,0)
            crt+=1

    # Write Character data to file
    with open(char_path+'/'+user_name+'.json', 'w') as f:
        f.write(json.dumps(char))

    # Open skill list file and to character skill file
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    f.close()
    skill_list=[]
    char_skill={}
    for list in sl:
        skill_list.append(list.split(","))
        crt=1
        for outer_list in skill_list:
            index=int(plist[pro_ch][1])
            char_skill[crt]=(outer_list[1],outer_list[5],outer_list[7],outer_list[index],outer_list[6],0,0,0,0)
            crt+=1

## End of create_char

def show_char():
    p=charMenu.char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the file
    char_data={}
    s-=1
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as cf:
        char_dict = json.load(cf)
    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    f.close()
    sc=[]

    for x in statchart:
        sc.append(x.split(","))

    # Loop through statistics to pull bonuses
    for x1 in sc:
        #print x1[0],":",x1[1],":",x1[2],":",x1[3]
        if int(x1[0]) == int(char_dict['st_stat']):
            stb,stdp,stpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['qu_stat']):
            qub,qudp,qupp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['pr_stat']):
            prb,prdp,prpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['in_stat']):
            inb,indp,inpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['em_stat']):
            emb,emdp,empp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['co_stat']):
            cob,codp,copp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['ag_stat']):
            agb,agdp,agpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['sd_stat']):
            sdb,sddp,sdpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['me_stat']):
            meb,medp,mepp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char_dict['re_stat']):
            reb,redp,repp=x1[1],x1[2],x1[3]

    ###################
    # Lookup Race Bonus
    ###################
    with open(cfgData.cfg_dir+"/race.csv") as r:
        racechart =r.read().splitlines()
    r.close()
    rc=[]

    for x in racechart:
        rc.append(x.split(","))

    # Race Bonus
    for x2 in rc:
        if x2[0] == char_dict['race']:
            raceb=x2

    #######################
    # Calcalute Total Bonus
    #######################

    sttb=(int(stb)+int(raceb[1])+int(char_dict['stmb']))
    qutb=(int(qub)+int(raceb[2])+int(char_dict['qumb']))
    prtb=(int(prb)+int(raceb[3])+int(char_dict['prmb']))
    intb=(int(inb)+int(raceb[4])+int(char_dict['inmb']))
    emtb=(int(emb)+int(raceb[5])+int(char_dict['emmb']))
    cotb=(int(cob)+int(raceb[6])+int(char_dict['comb']))
    agtb=(int(agb)+int(raceb[7])+int(char_dict['agmb']))
    sdtb=(int(sdb)+int(raceb[8])+int(char_dict['sdmb']))
    metb=(int(meb)+int(raceb[9])+int(char_dict['memb']))
    retb=(int(reb)+int(raceb[10])+int(char_dict['remb']))
    tdp=float(codp)+float(agdp)+float(sddp)+float(medp)+float(redp)

    # Power Point Math
    stpp,qupp,copp,agpp,sdpp,mepp,repp="-","-","-","-","-","-","-"
    if char_dict['realm'] == "NULL":
        prpp,inpp,empp=0.0,0.0,0.0
        tpp=0.0
    if char_dict['realm'] == "PR":
        inpp,empp=0.0,0.0
        tpp=prpp
    if char_dict['realm'] == "IN":
        empp,prpp=0.0,0.0
        tpp=inpp
    if char_dict['realm'] == "EM":
        inpp,prpp=0.0,0.0
        tpp=empp
    if char_dict['realm'] == "IP":
        empp=0.0
        tpp=(float(inpp)+float(prpp))/2
    if char_dict['realm'] == "PE":
        inpp=0.0
        tpp=(float(empp)+float(prpp))/2
    if char_dict['realm'] == "IE":
        prpp=0.0
        tpp=(float(inpp)+float(empp))/2
    if char_dict['realm'] == "AR":
        tpp=(float(inpp)+float(prpp)+float(empp))/3

    # Development Point Math
    stdp,qudp,emdp,indp,prdp="-","-","-","-","-"

    print ""
    print 89 * "-"
    print "| Name: %s" % char_dict['name'].title()
    print "| Profession: %s" % char_dict['pro_name'].title()
    print "| Race: %s" % char_dict['race'].title()
    print 89 * "-"
    print "|                                   Stats                                                |"
    print 89 * "-"
    print "|                      |         |           |  Stat |  Race | Dev | PP  | Misc  | Total |"
    print "|                      | Current |   Pot'l   | Bonus | Bonus | Pts | Pts | Bonus | Bonus |"
    print 89 * "-"
    print "| Strength (ST)        |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['st_stat'],char_dict['st_pot'],stb,raceb[1],stdp,stpp,char_dict['stmb'],sttb)
    print "| Quickness (QU)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['qu_stat'],char_dict['qu_pot'],qub,raceb[2],qudp,qupp,char_dict['qumb'],qutb)
    print "| Presence (PR)        |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['pr_stat'],char_dict['pr_pot'],prb,raceb[3],prdp,prpp,char_dict['prmb'],prtb)
    print "| Intuition (IN)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['in_stat'],char_dict['in_pot'],inb,raceb[4],indp,inpp,char_dict['inmb'],intb)
    print "| Empathy (EM)         |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['em_stat'],char_dict['em_pot'],emb,raceb[5],emdp,empp,char_dict['emmb'],emtb)
    print "| Constitution (CO)    |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['co_stat'],char_dict['co_pot'],cob,raceb[6],codp,copp,char_dict['comb'],cotb)
    print "| Agility (AG)         |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['ag_stat'],char_dict['ag_pot'],agb,raceb[7],agdp,agpp,char_dict['agmb'],agtb)
    print "| Self Discipline (SD) |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['sd_stat'],char_dict['sd_pot'],sdb,raceb[8],sddp,sdpp,char_dict['sdmb'],sdtb)
    print "| Memory (ME)          |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['me_stat'],char_dict['me_pot'],meb,raceb[9],medp,mepp,char_dict['memb'],metb)
    print "| Reasoning (RE)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['re_stat'],char_dict['re_pot'],reb,raceb[10],redp,repp,char_dict['remb'],retb)
    print 89 * "-"
    print "| Development Points:                                        | {:^4}| {:^4}|               |".format(tdp,tpp)
    print 89 * "-"
    print

mb=""
setstmb,setqumb,setprmb,setinmb,setemmb=0,0,0,0,0
setcomb,setagmb,setsdmb,setmemb,setremb=0,0,0,0,0
def mbset():
    global mb
    mb=int(raw_input("Bonus: "))
    return mb

def mbbonus():
    global setstmb
    global setcomb
    global setagmb
    global setqumb
    global setprmb
    global setinmb
    global setemmb
    global setsdmb
    global setmemb
    global setremb

    p=char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the file
    s-=1
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as cf:
        char_dict = json.load(cf)
        setstmb=char_dict['stmb']
        setqumb=char_dict['qumb']
        setprmb=char_dict['prmb']
        setinmb=char_dict['inmb']
        setemmb=char_dict['emmb']
        setcomb=char_dict['comb']
        setagmb=char_dict['agmb']
        setsdmb=char_dict['sdmb']
        setmemb=char_dict['memb']
        setremb=char_dict['remb']
    mbloop=True
    while mbloop:
        print 58 * "-"
        print "| 1.) Strength  ({:^4})        6.) Constitution    ({:^4}) |".format(setstmb,setcomb)
        print "| 2.) Quickness ({:^4})        7.) Agility         ({:^4}) |".format(setqumb,setagmb)
        print "| 3.) Presence  ({:^4})        8.) Self Discipline ({:^4}) |".format(setprmb,setsdmb)
        print "| 4.) Intuition ({:^4})        9.) Memory          ({:^4}) |".format(setinmb,setmemb)
        print "| 5.) Empathy   ({:^4})       10.) Reasoning       ({:^4}) |".format(setemmb,setremb)
        print "|                                                        |"
        print "| X.) Exit                                               |"
        print 58 * "-"
        print
        mbch=raw_input('Select Stat to add a bonus: ')
        if mbch == "1":
            mbset()
            setstmb=mb
        if mbch == "2":
            mbset()
            setqumb=mb
        if mbch == "3":
            mbset()
            setprmb=mb
        if mbch == "4":
            mbset()
            setinmb=mb
        if mbch == "5":
            mbset()
            setemmb=mb
        if mbch == "6":
            mbset()
            setcomb=mb
        if mbch == "7":
            mbset()
            setagmb=mb
        if mbch == "8":
            mbset()
            setsdmb=mb
        if mbch == "9":
            mbset()
            setmemb=mb
        if mbch == "10":
            mbset()
            setremb=mb
        if mbch.upper() == "X":
            print "Exiting.."
            print
            mbloop=False

        user_name=char_dict['name']
        # Physical stats
        char_dict['stmb']=setstmb
        char_dict['qumb']=setqumb
        char_dict['prmb']=setprmb
        char_dict['inmb']=setinmb
        char_dict['emmb']=setemmb
        # Development stats
        char_dict['comb']=setcomb
        char_dict['agmb']=setagmb
        char_dict['sdmb']=setsdmb
        char_dict['memb']=setmemb
        char_dict['remb']=setremb

        # Open character file to write out data
        with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json", 'w') as f:
            f.write(json.dumps(char_dict))

def weapon_costs():
    # Create character list to work with
    p=charMenu.char_menu()
    menu_len=len(p)
    cloop=True
    while cloop:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            cloop=False
        else:
            print "Invalid Selection! Select a character from the list"

    s-=1
    if len(os.listdir(cfgData.char_dir+"/"+p[s]))==2 and os.listdir(cfgData.char_dir+"/"+p[s])[0] == p[s]+"-0.json":
        print "Level 0 Character Found"
    elif len(os.listdir(cfgData.char_dir+"/"+p[s]))>2:
        print "extra levels"
    # Open the character file, read-only
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as cf:
        char_dict = json.load(cf)

    ## Read in list of professions and weapon costs, read-only
    with open(cfgData.cfg_dir+"/pro.csv","r") as procsv:
        plist=procsv.read()
    for profess in plist.splitlines():
        rt=profess.split(",")
        if rt[0] == char_dict['pro_name']:
            wclist=[rt[2],rt[3],rt[4],rt[5],rt[6],rt[7]]

    ### Initial display of Weapon Categories and costs for the profession
    print
    wlist=['1-HS','1-HC','2-H','Thrown','Missile','Polearm']
    wc,wmenu=0,1
    wea_assign={}

    print "List of weapon costs"
    print 25 * "-"
    for x1 in wlist:
        print "{:1}.){:^5}      {:1}.) {:10}".format(wmenu,wclist[wc],wmenu,x1)
        wc+=1
        wmenu+=1
    print
    print "Select a cost to assign to a weapon category"
    # Weapon Cost selection
    weapsel = int(raw_input('Select Weapon cost to assign: '))
    while weapsel<1 or weapsel>6: # Check that input is in the range
        print "You must select a number between (1 and 6)"
        weapsel=int(raw_input('Select weapon cost to assign: '))
    # Weapon category selection
    weapcat = int(raw_input('Select Weapon Category to assign cost: '))
    while weapcat<1 or weapcat>6: # Check that input is in the range
        print "You must select a number between (1 and 6)"
        weapcat=int(raw_input('Select Weapon Category to assign cost: '))

    weapsel-=1 # Subtract to match menu
    weapcat-=1 # Subtract to match menu

    weacat=wlist[weapcat]
    wea_assign[weacat]=wclist[weapsel]
    wlist.pop(weapcat)
    wclist.pop(weapsel)
    print

    # Weapon loop
    wea_loop=True
    while wea_loop:
        wc,wmenu=0,1
        print "List of weapon costs"
        print 25 * "-"
        for x1 in wlist:
            print "{:1}.){:^5}      {:1}.) {:10}".format(wmenu,wclist[wc],wmenu,x1)
            wc+=1
            wmenu+=1
        print
        print "Select a cost to assign to a weapon category"
        # Weapon Cost selection
        weapsel = int(raw_input('Select Weapon cost to assign: '))
        while weapsel<1 or weapsel>6: # Check that input is in the range
            print "You must select a number between (1 and 6)"
            weapsel=int(raw_input('Select weapon cost to assign: '))

        # Weapon category selection
        weapcat = int(raw_input('Select Weapon Category to assign cost: '))
        while weapcat<1 or weapcat>6: # Check that input is in the range
            print "You must select a number between (1 and 6)"
            weapcat=int(raw_input('Select Weapon Category to assign cost: '))

        # Weapon select
        weapsel-=1 # Subtract to match menu
        weapcat-=1 # Subtract to match menu

        weacat=wlist[weapcat]
        wea_assign[weacat]=wclist[weapsel]

        # Remove weapon cost and category
        wlist.pop(weapcat)
        wclist.pop(weapsel)
        print
        if len(wlist)==1:
            weacat=wlist[0]
            wea_assign[weacat]=wclist[0]
            wea_loop=False

    ## Open character skill file
    skill_dict={}
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as sf:
        skill_dict = json.load(sf)
    # Open ds.csv for count of skills
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    skcnt=1
    # Loop through skills and update costs of weapons
    while skcnt <= len(sl):
        if skill_dict[`skcnt`][2]=='Thrown':
            skill_dict[`skcnt`][3]=wea_assign['Thrown']
        if skill_dict[`skcnt`][2]=='1-HS':
            skill_dict[`skcnt`][3]=wea_assign['1-HS']
        if skill_dict[`skcnt`][2]=='1-HC':
            skill_dict[`skcnt`][3]=wea_assign['1-HC']
        if skill_dict[`skcnt`][2]=='2-H':
            skill_dict[`skcnt`][3]=wea_assign['2-H']
        if skill_dict[`skcnt`][2]=='Missile':
            skill_dict[`skcnt`][3]=wea_assign['Missile']
        if skill_dict[`skcnt`][2]=='Polearm':
            skill_dict[`skcnt`][3]=wea_assign['Polearm']
        skcnt+=1
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","w") as sw:
        sw.write(json.dumps(skill_dict))

###########################
###   Start Menu Loop   ###
###########################

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = raw_input("Enter your choice [1-5]: ")
    print ""
    if choice=="1":
        clear_screen()
        create_char()
    elif choice=="2":
        clear_screen()
        show_char()
    elif choice=="3":
        clear_screen()
        mbbonus()
        clear_screen()
    elif choice=="4":
        clear_screen()
        weapon_costs()
    elif choice=="5":
        clear_screen()
        rl.select_skills()
    elif choice=="7":
        import skills
        clear_screen()
        skills.select_skills()
    elif choice=="x":
        print "Exiting Program"
        loop=False
    elif choice=="X":
        print "Exiting program"
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
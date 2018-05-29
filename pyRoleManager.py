## Text menu in Python
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
#from decimal import Decimal
#import os
#import json
#import sys
#import re
import cfgData
import charMenu
#import rl
import charData
#import exp
import export
#import level
import charCreate
import charImport

'''
# Update character records if a new skill is added
#charData.new_skill_check()

# Setup character data list
char_dict={}

# Read Professions into List
plist = {}
pi=1
with open(cfgData.cfg_dir+"/pro.csv") as pf:
    for pline in pf:
        plist[pi]=pline.rstrip('\n').split(",")
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
'''

def print_menu():       
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Create New Character"
    print "2. Show Character"
    print "3. Add Misc Stat Bonus"
    print "4. Add Misc Skill Bonus"
    print "5. Stat Gain Roll"
    print "6. Assign Armor Type to Character"
    print
    print "7. Add experience to character"
    print "8. Raise Character Level"
    print
    print "9. Export Character to Excel"
    print "10. Export All of Character Skills to Excel"
    print "11. Print list of all skills to screen"
    print ""
    print "X. Exit"
    print 67 * "-"


# Clear the clear_screen
cfgData.clear_screen()


###########################
###   Start Menu Loop   ###
###########################

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = raw_input("Enter your choice [1-9]: ")
    print ""
    if choice=="1":
        cfgData.clear_screen()
        charCreate.create_char()
    elif choice=="2":
        cfgData.clear_screen()
        charData.show_char()
    elif choice=="3":
        cfgData.clear_screen()
        mbbonus()
        cfgData.clear_screen()
    elif choice=="4":
        cfgData.clear_screen()
        rl.skill_mb_bonus()
    elif choice=="5":
        cfgData.clear_screen()
        stat_gain()
    elif choice=="6":
        cfgData.clear_screen()
        charData.assign_at()
    elif choice=="7":
        cfgData.clear_screen()
        exp.exp_check()
    elif choice=="8":
        cfgData.clear_screen()
        p=charMenu.char_menu()
        menu_len=len(p)
        while True:
            s=int(raw_input("Select Character: "))
            if s >=1 and s<=menu_len:
                break
            else:
                print "Invalid Selection! Select a character from the list"
        skill_list=[]
        s-=1
        rl.select_skills(p[s])
        cfgData.clear_screen()
    elif choice=="9":
        cfgData.clear_screen()
        export.export_to_excel()
        cfgData.clear_screen()
    elif choice=="10":
        cfgData.clear_screen()
        export.export_allskills_to_excel()
        cfgData.clear_screen()
    elif choice=="11":
        cfgData.clear_screen()
        charData.all_skill_list()
    elif choice=="12":
        cfgData.clear_screen()
        level.exp_check()
        cfgData.clear_screen()
    elif choice=="13":
        cfgData.clear_screen()
        charImport.char_import()
    elif choice=="x":
        print "Exiting Program"
        loop=False
    elif choice=="X":
        print "Exiting program"
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

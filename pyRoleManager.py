## Text menu in Python
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import cfgData
import charMenu
import charData
import export
import charCreate
import charImport
import skill

def print_menu():
    print 30 * "=" , "PyRoleManager" , 30 * "="
    print 30 * "=" , "  Main Menu  " , 30 * "="
    print "1. New Characters"
    print "2. Modify Characters"
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

def print_smenu1():
    print 30 * "=", "New Character" ,30 * "="
    print "1. Create new character"
    print "2. Import Character"
    print "3. Export Character Sheet"
    print "4. Export all skills"
    print "5. Add Misc Stat bonus"
    print "6. Add Misc Skill bonus"
    print "7. Assign Armor/Shield to character"
    print ""
    print "X. Exit"

def print_smenu2():
    print 30 * "=", "Character modifications", 30 * "="
    print
    print "1. Add experience to character"
    print "2. Add/Increase skills"
    print "3. Stat gain"
    print "4. Export Character Sheet"
    print "5. Add Misc Stat bonus"
    print "6. Add Misc Skill bonus"
    print "7. Assign Armor/Shield to character"
    print ""
    print "X. Exit"

# Clear the clear_screen
cfgData.clear_screen()

#####################
###   Sub Menu    ###
#####################
def sloop1():
    smloop=True
    while smloop:
        print_smenu1()
        choice = raw_input("Enter you choice: ")
        print
        if choice=="1":
            cfgData.clear_screen()
            charCreate.create_char()
        if choice=="2":
            cfgData.clear_screen()
            charImport.char_import()
        if choice=="3":
            cfgData.clear_screen()
            export.export_to_excel()
            cfgData.clear_screen()
        if choice=="4":
            cfgData.clear_screen()
            export.export_allskills_to_excel()
            cfgData.clear_screen()
        if choice=="5":
            cfgData.clear_screen()
            charData.mbbonus()
            cfgData.clear_screen()
        elif choice.upper()=="X":
            print "Exiting program"
            smloop=False
        else:
            raw_input("Wrong option selection. Enter any key to try again..")

def sloop2():
    smloop=True
    while smloop:
        print_smenu2()
        choice = raw_input("Enter you choice: ")
        print
        if choice=="1":
            print "1-S2"
        if choice=="2":
            print "Add skills"
            skill.add_skill()
        if choice=="4":
            cfgData.clear_screen()
            export.export_to_excel()
            cfgData.clear_screen()
        elif choice.upper()=="X":
            print "Exiting program"
            smloop=False
        else:
            raw_input("Wrong option selection2. Enter any key to try again..")

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
        sloop1()
    elif choice=="2":
        cfgData.clear_screen()
        sloop2()
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
    elif choice=="14":
        p=charMenu.char_menu()
        menu_len=len(p)
        while True:
            s=int(raw_input("Select Character: "))
            if s >=1 and s<=menu_len:
                break
            else:
                print "Invalid Selection! Select a character from the list"

        # Open the file
        char_dict={}
        s-=1
        char = p[s]
        skill.import_skill(char)
        cfgData.clear_screen()
    elif choice=="x":
        print "Exiting Program"
        loop=False
    elif choice=="X":
        print "Exiting program"
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

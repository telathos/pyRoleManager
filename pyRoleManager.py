## Text menu in Python
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
from decimal import Decimal
import os
import json
import sys
import re
import cfgData
import charMenu
import rl
import charData
import exp
import export
import level
import charCreate
import charImport

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

def print_menu():       ## Your menu design here
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
        char_dict.insert(counter,words)
        counter+=1

def lang_set(char):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","r") as cf:
        char_dict = json.load(cf)

    # Pull number of languages from race.csv
    with open(cfgData.cfg_dir+"/lang.csv","r") as la:
        lan = la.read().splitlines()

    #clear_screen()
    num_of_lang=0
    with open(cfgData.cfg_dir+"/race.csv","r") as rf:
        racelist = rf.read().splitlines()
    # loop thru race list to find a matching race
    f=0
    while f < len(racelist):
        x = racelist[f].split(',')
        f+=1
        if x[0] == char_dict['race']:
            num_of_lang = x[16]
    # Check if character's languages are set
    check=1
    lcheck=[]
    while check <= int(num_of_lang):
        lanSearch = "lang"+`check`
        if lanSearch in char_dict:
            lcheck.append(check)
        check+=1
    if len(lcheck) == int(num_of_lang):
        print "Base languages are already set."
        print "Returning to Main Menu"
        print
    else:
        with open(cfgData.cfg_dir+"/lc.csv","r") as r:
            lc=r.read().splitlines()

        lanlist=[]
        lcnt=1
        while len(lanlist)< int(num_of_lang):
            num=1
            j=0
            print "+",87 * "=","+"
            for x in lc:
                j=x.split(';')
                print "| {:<2} | {:40}| {:40} |".format(j[0],j[1],j[2])
            print "+",87 * "=","+"
            print
            # Create menu of languages
            for y in lan:
                print "{:<2}.) {:20}".format(num,y)
                num+=1
            lanch=""
            while lanch<1 or lanch>len(lan):
                try:
                    lanch = int(raw_input("Select Language: "))
                except:
                    print "Enter a number between 1 and {:2}..".format(len(lan))

            lanspoke=""
            while lanspoke<1 or lanspoke>10:
                try:
                    lanspoke = int(raw_input("Enter Spoken rank: "))
                except:
                    print "Enter a number between 1 and 10.."
            lanwritten=""
            while lanwritten<1 or lanwritten>10:
                try:
                    lanwritten = int(raw_input("Enter Written rank: "))
                except:
                    print "Enter a number between 1 and 10.."

            lanlist.append(lan[lanch-1])
            lan.pop(lanch-1)
            y="lang"+`lcnt`
            char_dict[y] = [lanlist[lcnt-1],lanspoke,lanwritten]
            lcnt+=1

        # Add languages to dictionary
        # Open character file to write out data
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", 'w') as f:
            f.write(json.dumps(char_dict))
        cfgData.clear_screen()
#################
# End of lang_set
#################

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

    p=charMenu.char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the file
    s-=1
    char=p[s]
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","r") as cf:
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
        mbch=""
        while mbch<1 or mbch>10:
            try:
                mbch=raw_input('Select Stat to add a bonus: ')
            except:
                print "Enter a number between 1 and 10.."
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
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", 'w') as f:
            f.write(json.dumps(char_dict))
    # End of Misc Bonus function

def stat_gain_lookup(diff,roll):
    global change
    if diff == 0:
        if roll <= 4:
            change = roll * -2
        else:
            change =0
    elif diff == 1:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 50:
            change =0
        else:
            change = 1
    elif diff == 2:
        if roll <=4:
            change = roll * -2
        elif roll <= 30:
            change = 0
        elif roll >= 31 and roll <= 65:
            change = 1
        else:
            change = 2
    elif diff == 3:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 25:
            change = 0
        elif roll >= 26 and roll <= 50:
            change = 1
        elif roll >= 51 and roll <= 75:
            change = 2
        else:
            change = 3
    elif diff >= 4 and diff <= 5:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 20:
            change = 0
        elif roll >= 21 and roll <= 40:
            change = 1
        elif roll >= 41 and roll <= 60:
            change = 2
        elif roll >= 61 and roll <= 80:
            change = 3
        else:
            change = 4
    elif diff >= 6 and diff <= 7:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 15:
            change = 0
        elif roll >= 16 and roll <= 25:
            change = 1
        elif roll >= 26 and roll <= 40:
            change = 2
        elif roll >= 41 and roll <= 55:
            change =3
        elif roll >= 56 and roll <= 70:
            change = 4
        elif roll >= 71 and roll <= 85:
            change = 5
        else:
            change = 6
    elif diff >= 8 and diff <= 9:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 10:
            change = 0
        elif roll >= 11 and roll <= 20:
            change = 1
        elif roll >= 21 and roll <= 35:
            change = 2
        elif roll >= 36 and roll <= 50:
            change = 3
        elif roll >= 51 and roll <= 65:
            change = 4
        elif roll >= 66 and roll <= 75:
            change = 5
        elif roll >= 76 and roll <= 85:
            change = 6
        elif roll >= 86 and roll <= 95:
            change = 7
        else:
            change = 8
    elif diff >=10 and diff <= 11:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 15:
            change = 1
        elif roll >= 16 and roll <= 25:
            change = 2
        elif roll >= 26 and roll <= 35:
            change = 3
        elif roll >= 36 and roll <= 45:
            change = 4
        elif roll >= 46 and roll <= 55:
            change = 5
        elif roll >= 56 and roll <= 65:
            change = 6
        elif roll >= 66 and roll <= 75:
            change = 7
        elif roll >= 76 and roll <= 85:
            change = 8
        elif roll >= 86 and roll <= 95:
            change = 9
        else:
            change = 10
    elif diff >= 12 and diff <= 14:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 10:
            change = 1
        elif roll >= 11 and roll <= 15:
            change = 2
        elif roll >= 16 and roll <= 20:
            change = 3
        elif roll >= 21 and roll <= 25:
            change = 4
        elif roll >= 26 and roll <= 35:
            change = 5
        elif roll >= 36 and roll <= 45:
            change = 6
        elif roll >= 46 and roll <= 55:
            change = 7
        elif roll >= 56 and roll <= 65:
            change = 8
        elif roll >= 66 and roll <= 75:
            change = 9
        elif roll >= 76 and roll <= 85:
            change = 10
        elif roll >= 86 and roll <= 95:
            change = 11
        else:
            change = 12
    else:
        if roll <= 4:
            change = roll * -2
        elif roll >= 5 and roll <= 10:
            change = 1
        elif roll >= 11 and roll <= 15:
            change = 2
        elif roll >= 16 and roll <= 20:
            change = 3
        elif roll >= 21 and roll <= 25:
            change = 4
        elif roll >= 26 and roll <= 30:
            change = 5
        elif roll >= 31 and roll <= 35:
            change = 6
        elif roll >= 36 and roll <= 40:
            change = 7
        elif roll >= 41 and roll <= 45:
            change = 8
        elif roll >= 46 and roll <= 50:
            change = 9
        elif roll >= 51 and roll <= 55:
            change = 10
        elif roll >= 56 and roll <= 65:
            change = 11
        elif roll >= 66 and roll <= 75:
            change = 12
        elif roll >= 76 and roll <= 85:
            change = 13
        elif roll >= 86 and roll <= 95:
            change = 14
        else:
            change = 15
    return change

def stat_gain():
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
    user_name = p[s]
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+".json","r") as cf:
        char_dict = json.load(cf)
    st_diff = char_dict['st_pot'] - char_dict['st_stat']
    qu_diff = char_dict['qu_pot'] - char_dict['qu_stat']
    pr_diff = char_dict['pr_pot'] - char_dict['pr_stat']
    em_diff = char_dict['em_pot'] - char_dict['em_stat']
    in_diff = char_dict['in_pot'] - char_dict['in_stat']
    co_diff = char_dict['co_pot'] - char_dict['co_stat']
    sd_diff = char_dict['sd_pot'] - char_dict['sd_stat']
    ag_diff = char_dict['ag_pot'] - char_dict['ag_stat']
    me_diff = char_dict['me_pot'] - char_dict['me_stat']
    re_diff = char_dict['re_pot'] - char_dict['re_stat']
    st_stat, qu_stat, pr_stat, em_stat, in_stat = char_dict['st_stat'], char_dict['qu_stat'],char_dict['pr_stat'],char_dict['em_stat'],char_dict['in_stat']
    co_stat, sd_stat, ag_stat, me_stat, re_stat = char_dict['co_stat'], char_dict['sd_stat'],char_dict['ag_stat'],char_dict['me_stat'],char_dict['re_stat']

    difflist = [[st_stat,st_diff,"ST","st_stat"], [qu_stat,qu_diff,"QU","qu_stat"], [pr_stat,pr_diff,"PR","pr_stat"],
    [in_stat,in_diff,"IN","in_stat"], [em_stat,em_diff,"EM","em_stat"], [co_stat,co_diff,"CO","co_stat"],
    [ag_stat,ag_diff,"AG","ag_stat"], [sd_stat,sd_diff,"SD","sd_stat"], [me_stat, me_diff,"ME","me_stat"],
    [re_stat,re_diff,"RE","re_stat"]]
    change=0

    #print difflist
    for x in difflist:
        print
        print "Stat: {:2}".format(x[2])
        roll = int(raw_input("Enter roll: "))
        change = stat_gain_lookup(x[1], roll)
        newStat = x[0]+change
        print "Stat: {:2} had a change of {:<2}".format(x[2],change)
        print "Prev: {:<3}".format(x[0])
        print "Cur:  {:<3}".format(newStat)
        char_dict[x[3]]=newStat
        #print char_dict[x[3]]

    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    sc=[]

    for x in statchart:
        sc.append(x.split(","))

    # Loop through statistics to pull bonuses
    for x1 in sc:
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
    tdp=char_dict['dp']
    # Updaet character file
    char_dict['sttb'],char_dict['qutb']= sttb,qutb
    char_dict['prtb'],char_dict['intb']= prtb,intb
    char_dict['emtb'],char_dict['cotb']= emtb,cotb
    char_dict['agtb'],char_dict['sdtb']= agtb,sdtb
    char_dict['metb'],char_dict['retb']= metb,retb

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

    # Write Character data to file
    with open(cfgData.char_dir+'/'+user_name+'/'+user_name+'.json', 'w') as f:
        f.write(json.dumps(char_dict))

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

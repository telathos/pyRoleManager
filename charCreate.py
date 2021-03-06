import cfgData
import re
from decimal import Decimal
import sys
import os
import json

# Setup character data dictionaries
char_dict={}
char_skill={}
# Read Professions into dictionaries
plist = {}
rlist = {}
pi,ri=1,1

# Open Profession and Race files
with open(cfgData.cfg_dir+"/profession.csv") as pf:
    for pline in pf:
        plist[pi]=pline.rstrip('\n').split(",")
        pi+=1
with open(cfgData.cfg_dir+"/race.csv") as rf:
    for rline in rf:
        rlist[ri]=rline.rstrip('\n').split(",")
        ri+=1

#st_pot_in,qu_pot_in,pr_pot_in,in_pot_in,em_pot_in=0,0,0,0,0
#co_pot_in,ag_pot_in,sd_pot_in,me_pot_in,re_pot_in=0,0,0,0,0

# Start of the basic character creation, Name, Profession, Race and Stats
def create_char():
    # Set base Experience
    char_dict['exp'] = 10000
    char_dict['next_lvl'] = 20000

    print 30 * "-" , "Professions", 30 * "-"
    print ""
    #Skip header
    ln=1
    menu=1
    while ln <= len(plist):
        # Create Section Headers
        if plist[ln][8] == "NON" and menu == 1:
            print 25 * "-" , "Non", 25 * "-"
            menu=2
        if plist[ln][8] == "SEMI" and menu == 2:
            print ""
            print 25 * "-" ,"Semi", 25 * "-"
            menu=3
        if plist[ln][8] == "PURE" and menu == 3:
            print ""
            print 25 * "-" , "Pure", 25 * "-"
            menu=4
        if plist[ln][8] == "HYB" and menu == 4:
            print ""
            print 25 * "-" , "Hybrid", 25 * "-"
            menu=5
        if plist[ln+1][8] == plist[ln][8]:
            print "{:2}.) {:20} {:2}.) {:20}".format(plist[ln][0],plist[ln][1],plist[ln+1][0],plist[ln+1][1])
            ln+=1
        else:
            print "{:2}.) {:20}".format(plist[ln][0],plist[ln][1])
        ln+=1
    print ""
    print 63 * "-"
    pro_ch =""
    while pro_ch<1 or pro_ch>len(plist):
        try:
            pro_ch=int(raw_input('Select Profession: '))
            if pro_ch<1 or pro_ch>len(plist):
                print "You must enter a number between 1 and {:2}".format(len(plist))
        except:
            print "You must enter a number between 1 and {:2}".format(len(plist))
    # Set Profession name
    char_dict['proname'] = plist[pro_ch][1]
    print char_dict['proname']
    char_dict['pro_pr1'] = plist[pro_ch][2]
    char_dict['pro_pr2'] = plist[pro_ch][3]
    char_dict['pro_pr3'] = plist[pro_ch][4]
    char_dict['mrealm'] = plist[pro_ch][7]
    proID = int(plist[pro_ch][0])
    proID += 7
    print ""

    # Race Selection
    print len(rlist),":len(rlist)"
    ln=1
    print 30 * "-", "Races", 30 * "-"
    print ""
    while ln <= len(rlist):
        if (len(rlist) - ln) == 0:
            print "{:2}.) {:20}".format(rlist[ln][0],rlist[ln][1])
            ln+=1
        else:
            print "{:2}.) {:20} {:2}.) {:20}".format(rlist[ln][0],rlist[ln][1],rlist[ln+1][0],rlist[ln+1][1])
            ln+=2
    print ""
    print 63 * "-"
    race_input =""
    while race_input<1 or race_input>len(rlist):
        try:
            race_input=int(raw_input('Select a Race: '))
            if race_input<1 or race_input>len(rlist):
                print "You must enter a number between 1 and {:2}".format(len(rlist))
        except:
            print "You must enter a number between 1 and {:2}".format(len(rlist))
    char_dict['race'] = rlist[race_input][1]
    print char_dict['race']

    ### Enter current statistic values
    curlist=[]
    statlist=[]
    stat_temp_list=[]
    print "Roll for Current stats"
    print ""

    cnt=1
    for i in range(12):
        while i<20 or i>100:
            try:
                i=int(raw_input('Current Stat Roll {:<2} :'.format(cnt)))
                if i<20 or i>100:
                    print "You must enter a number between 20 and 100"
            except:
                print "You must enter a number between 20 and 100"
        curlist.append(i)
        cnt+=1

    # Reset the counter
    cnt=1
    curlist.sort()

    # Test the number of 90 or higher rolls
    if curlist[-3]>89:
        ninty=3
    elif curlist[-2]>89:
        ninty=2
    elif curlist[-1]>89:
        ninty=1
    elif curlist[-1]<90:
        ninty=0

    # Test if enough 90+ rolls for profession and replace lowest value with 90
    if char_dict['proname'] == 'Archmage':
        if ninty==2:
            curlist[0]=90
        if ninty==1:
            curlist[0],curlist[1]=90,90
        if ninty==0:
            curlist[0],curlist[1],curlist[2]=90,90,90
    else:
        if ninty==1:
            curlist[0]=90
        if ninty==0:
            curlist[0],curlist[1]=90,90

    # Enter Potential stat rolls
    for i in curlist:
        try:
            p=int(raw_input('Potential Roll {:<2} :'.format(cnt)))
            if p<1 or p>100:
                print "You must enter a number between 1 and 100"
        except:
            print "You must enter a number between 1 and 100"
        pot=cfgData.pot_calc(i,p)
        statlist.append([i,pot])
        cnt+=1
    # Clear screen
    cfgData.clear_screen()

    # Reset counter
    cnt=1
    print 65 * "-"
    print ""
    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    f.close()
    sc=[]
    cnt=1
    for x in statchart:
        sc.append(x.split(","))
    u=0
    while u< len(statlist):
        for x1 in sc:
            if int(x1[0]) == statlist[u][0]:
                stat_temp_list.append([statlist[u][0],statlist[u][1],x1[1],x1[2],x1[3]])
        u+=1
    cnt=1

    print "+", 48 * "=", "+"
    print "|{:5}| {:7} | {:9} | {:5} | {:4} | {:5} |".format("","","","Stat","Dev","Power")
    print "|{:5}| {:6} | {:9} | {:5} | {:4} | {:5} |".format("","Current","Potential","Bonus","Pts","Pts")
    print "+", 48 * "=", "+"

    while cnt<=len(statlist):
        print "| {:>2}.) | {:^6} | {:^9} | {:^5} | {:4} | {:^5} |".format(cnt,stat_temp_list[cnt-1][0],stat_temp_list[cnt-1][1],stat_temp_list[cnt-1][2],stat_temp_list[cnt-1][3],stat_temp_list[cnt-1][4])
        cnt+=1
    print "+", 48 * "=", "+"
    print ""
    print "Remove (2) stats"
    cnt=1

    while cnt<len(stat_temp_list)>10:
        cnt,r=1,0
        while r<1 or r>(len(stat_temp_list)):
            try:
                r=int(raw_input("Enter Stat to remove:"))
                if r<1 or r>len(stat_temp_list):
                      print "Please enter a number between 1 and {:2}".format(len(stat_temp_list))
            except:
                print "Please enter a number between 1 and {:2}".format(len(stat_temp_list))
        stat_temp_list.pop(r-1)

        print "+", 48 * "=", "+"
        print "|{:5}| {:7} | {:9} | {:5} | {:4} | {:5} |".format("","","","Stat","Dev","Power")
        print "|{:5}| {:6} | {:9} | {:5} | {:4} | {:5} |".format("","Current","Potential","Bonus","Pts","Pts")
        print "+", 48 * "=", "+"
        while cnt<=len(stat_temp_list):
            print "| {:>2}.) | {:^6} | {:^9} | {:^5} | {:4} | {:^5} |".format(cnt,stat_temp_list[cnt-1][0],stat_temp_list[cnt-1][1],stat_temp_list[cnt-1][2],stat_temp_list[cnt-1][3],stat_temp_list[cnt-1][4])
            cnt+=1
        print "+", 48 * "=", "+"
        print ""
        cnt=0

    stat=[
    ['Strength','ST','st_stat','st_pot','stb','stdp','stpp'],
    ['Quickness','QU','qu_stat','qu_pot','qub','qudp','qupp'],
    ['Empathy','EM','em_stat','em_pot','emb','emdp','empp'],
    ['Presence','PR','pr_stat','pr_pot','prb','prdp','prpp'],
    ['Intuition','IN','in_stat','in_pot','inb','indp','inpp'],
    ['Constitution','CO','co_stat','co_pot','cob','codp','copp'],
    ['Agility','AG','ag_stat','ag_pot','agb','agdp','agpp'],
    ['Self Discipline','SD','sd_stat','sd_pot','sdb','sddp','sdpp'],
    ['Memory','ME','me_stat','me_pot','meb','medp','mepp'],
    ['Reasoning','RE','re_stat','re_pot','reb','redp','repp']
    ]
    # Clear screen
    cfgData.clear_screen()
    # Redraw table
    cnt=1
    print "+", 81 * "=", "+"
    print "|{:5}| {:7} | {:9} | {:5} | {:4} | {:5} || {:2}    | {:<16} | {:2} |".format("","","","Stat","Dev","Power","","","")
    print "|{:5}| {:6} | {:9} | {:5} | {:4} | {:5} || {:^2}    | {:<16} | {:2} |".format("","Current","Potential","Bonus","Pts","Pts","","Stat","")
    print "+", 81 * "=", "+"
    while cnt<=len(stat_temp_list):
        print "| {:>2}.) | {:^6} | {:^9} | {:^5} | {:4} | {:^5} || {:>2} .) | {:<16} | {:2} |".format(cnt,stat_temp_list[cnt-1][0],stat_temp_list[cnt-1][1],stat_temp_list[cnt-1][2],stat_temp_list[cnt-1][3],stat_temp_list[cnt-1][4],cnt,stat[cnt-1][0],stat[cnt-1][1])
        cnt+=1
    print "+", 81 * "=", "+"
    print ""
    print "Assign rolls to the stat"
    print "You must assign a 90 or higher to your professions prime requisites stats"
    print ""
    print " Your Profession is a {:35}".format(char_dict['proname'])
    if char_dict['pro_pr3']=="":
        print " Your Prime Requisites are {:2}/{:2}".format(char_dict['pro_pr1'],char_dict['pro_pr2'])
    else:
        print " Your Prime Requisites are {:2}/{:2}/{:3}".format(char_dict['pro_pr1'],char_dict['pro_pr2'],char_dict['pro_pr3'])
    print ""
    while len(stat)>0:
        colx,coly=0,0
        # Select last stat to roll
        if len(stat)==1:
            colx,coly=1,1
            y01,y02,y03=stat[coly-1][2],stat[coly-1][3],stat[coly-1][4]
            y04,y05=stat[coly-1][5],stat[coly-1][6]
            char_dict[y01]=stat_temp_list[colx-1][0]
            char_dict[y02]=stat_temp_list[colx-1][1]
            char_dict[y03]=stat_temp_list[colx-1][2]
            char_dict[y04]=stat_temp_list[colx-1][3]
            char_dict[y05]=stat_temp_list[colx-1][4]
        # Select current value to assign to a stat
        while colx<1 or colx>len(stat):
            try:
                colx=int(raw_input('Select a Current Roll: '))
                if colx<1 or colx>len(stat):
                    print "You must enter a number between 1 and {:<2}".format(len(stat))
            except:
                print "You must enter number between and {:<2}".format(len(stat))
        # Select stat that current value will be assigned to
        while coly<1 or coly>len(stat):
            pr = 0
            while pr == 0:
                try:
                    coly=int(raw_input('Select a Stat to assign: '))
                    #print pr,":pr"
                    if stat_temp_list[colx-1][0] < 90:
                        '''print stat_temp_list[colx-1][0]
                        print stat[coly-1][1]
                        print char_dict['pro_pr1']
                        print char_dict['pro_pr2']
                        print char_dict['pro_pr3']'''
                        if stat[coly-1][1] == char_dict['pro_pr1'] or \
                           stat[coly-1][1] == char_dict['pro_pr2'] or stat[coly-1][1] == char_dict['pro_pr3']:
                            print "This is a prime requisite for your profession and must be assigned a value of 90 or higher!"
                            print "Please enter a higher value.."
                            print ""
                        else:
                            # Break loop
                            pr = 1
                    else:
                        pr = 1
                    if coly<1 or coly>len(stat):
                        print "You must enter a number between 1 and {:<2}".format(len(stat))
                        pr = 1
                except:
                    print "You must enter number between and {:<2}".format(len(stat))

        y01,y02,y03=stat[coly-1][2],stat[coly-1][3],stat[coly-1][4]
        y04,y05=stat[coly-1][5],stat[coly-1][6]

        char_dict[y01]=stat_temp_list[colx-1][0]
        char_dict[y02]=stat_temp_list[colx-1][1]
        char_dict[y03]=stat_temp_list[colx-1][2]
        char_dict[y04]=stat_temp_list[colx-1][3]
        char_dict[y05]=stat_temp_list[colx-1][4]

        # Remove assigned stat and roll
        stat.pop(coly-1)
        stat_temp_list.pop(colx-1)
        if len(stat)>1:
            cnt=1
            print "+", 81 * "=", "+"
            print "|{:5}| {:7} | {:9} | {:5} | {:4} | {:5} || {:2}    | {:<16} | {:2} |".format("","","","Stat","Dev","Power","","","")
            print "|{:5}| {:6} | {:9} | {:5} | {:4} | {:5} || {:2}    | {:<16} | {:2} |".format("","Current","Potential","Bonus","Pts","Pts","","Stat","")
            print "+", 81 * "=", "+"
            while cnt<=len(stat_temp_list):
                print "| {:>2}.) | {:^6} | {:^9} | {:^5} | {:4} | {:^5} || {:>2} .) | {:<16} | {:2} |".format(cnt,stat_temp_list[cnt-1][0],stat_temp_list[cnt-1][1],stat_temp_list[cnt-1][2],stat_temp_list[cnt-1][3],stat_temp_list[cnt-1][4],cnt,stat[cnt-1][0],stat[cnt-1][1])
                cnt+=1
            print "+", 81 * "=", "+"


    print ""
    print "+", 38 * "=","+"
    print "| {:^38} |".format('Suggested Chooses')
    print "+", 38 * "=","+"
    print "| {:^8} | {:^16} | {:^8} |".format('Gender','Hair','Eye')
    print "+", 38 * "=","+"
    print "| {:^8} | {:^8} {:^8}| {:^8} |".format('Male','Black','Grey','Brown')
    print "| {:^8} | {:^8} {:^8}| {:^8} |".format('Female','Brown','Yellow','Blue')
    print "| {:^8} | {:^8} {:^8}| {:^8} |".format('','Blonde','White','Grey')
    print "| {:^8} | {:^8} {:^8}| {:^8} |".format('','Red','Calico','Red')
    print "| {:^8} | {:^8} {:^8}| {:^8} |".format('','Purple','None','Black')
    print "+", 38 * "=","+"
    print ""

    # Enter character's gender
    le=1
    while le==1:
        try:
            sexch = raw_input("Enter a Gender: ")
            if re.match("^[A-Za-z]*$",sexch):
                le=0
            else:
                print "Enter a gender for your character"
        except:
            print "Enter a gender for your character"
    char_dict['gender'] = sexch

    # Enter character's Hair Color
    le=1
    while le==1:
        try:
            hairch = raw_input("Enter a Hair color: ")
            if re.match("^[A-Za-z]*$",hairch):
                le=0
            else:
                print "Enter a hair color for your character"
        except:
            print "Enter a hair color for your character"
    char_dict['hair'] = hairch

    # Enter character's Eye Color
    le=1
    while le==1:
        try:
            eyech = raw_input("Enter a Eye color: ")
            if re.match("^[A-Za-z]*$",eyech):
                le=0
            else:
                print "Enter a eye color for your character"
        except:
            print "Enter a eye color for your character"
    char_dict['eye'] = eyech

    # Enter characters age
    age=""
    while age<1 or age>1000:
        try:
            age = int(raw_input("Character's Age: "))
        except:
            print "You must enter a number.."
    char_dict['age'] = age

    ht=""
    while ht == "":
        try:
            ht = str(raw_input("Enter Height: "))
        except:
            print "You must enter a height in ft' in\" format"
    # Enter weight
    wt=""
    while wt<1 or wt>1000:
        try:
            wt = int(raw_input("Enter Weight: "))
        except:
            print "Enter a number between 1 and 1000.."
    char_dict['height'],char_dict['weight'] = ht,wt

    # Load data into dictionary for saving of the character
    char_dict['lvl']=0
    char_dict['realm']=plist[pro_ch][8]
    char_dict['stmb'],char_dict['qumb'],char_dict['emmb'],char_dict['inmb'],char_dict['prmb']=0,0,0,0,0
    char_dict['comb'],char_dict['agmb'],char_dict['sdmb'],char_dict['remb'],char_dict['memb']=0,0,0,0,0
    hp_math=Decimal(char_dict['co_stat'])/Decimal(10)
    hp=Decimal(hp_math).quantize(Decimal('1e-3'))
    char_dict['hp_base']=int(round(hp,0))

    #######################
    # Calcalute Total Bonus
    #######################
    raclist=[]
    with open(cfgData.cfg_dir+"/race.csv") as rf:
        rline = rf.readlines()
    raclist = [x.strip() for x in rline]
    for x in raclist:
    #print x.split(",")
        if x.split(",")[1] == char_dict['race']:
            char_dict['strb'] = x.split(",")[2]
            char_dict['qurb'] = x.split(",")[3]
            char_dict['prrb'] = x.split(",")[4]
            char_dict['inrb'] = x.split(",")[5]
            char_dict['emrb'] = x.split(",")[6]
            char_dict['corb'] = x.split(",")[7]
            char_dict['agrb'] = x.split(",")[8]
            char_dict['sdrb'] = x.split(",")[9]
            char_dict['merb'] = x.split(",")[10]
            char_dict['rerb'] = x.split(",")[11]
            char_dict['Essmod'] = x.split(",")[12]
            char_dict['Chanmod'] = x.split(",")[13]
            char_dict['Mentmod'] = x.split(",")[14]
            char_dict['Poimod'] = x.split(",")[15]
            char_dict['Dismod'] = x.split(",")[16]
            char_dict['HitDie'] = x.split(",")[19]

    # Add Total Bonus of skills to character data
    char_dict['sttb']=(int(char_dict['stb'])+int(char_dict['strb'])+int(char_dict['stmb']))
    char_dict['qutb']=(int(char_dict['qub'])+int(char_dict['qurb'])+int(char_dict['qumb']))
    char_dict['prtb']=(int(char_dict['prb'])+int(char_dict['prrb'])+int(char_dict['prmb']))
    char_dict['intb']=(int(char_dict['inb'])+int(char_dict['inrb'])+int(char_dict['inmb']))
    char_dict['emtb']=(int(char_dict['emb'])+int(char_dict['emrb'])+int(char_dict['emmb']))
    char_dict['cotb']=(int(char_dict['cob'])+int(char_dict['corb'])+int(char_dict['comb']))
    char_dict['agtb']=(int(char_dict['agb'])+int(char_dict['agrb'])+int(char_dict['agmb']))
    char_dict['sdtb']=(int(char_dict['sdb'])+int(char_dict['sdrb'])+int(char_dict['sdmb']))
    char_dict['metb']=(int(char_dict['meb'])+int(char_dict['merb'])+int(char_dict['memb']))
    char_dict['retb']=(int(char_dict['reb'])+int(char_dict['rerb'])+int(char_dict['remb']))

    # Set Armor defaults
    char_dict['armorType'] = 1
    char_dict['armorTypeDesc'] = "Skin"
    char_dict['at_min_mod'] = 0
    char_dict['at_max_mod'] = 0
    char_dict['at_miss_pen'] = 0
    char_dict['at_qu_pen'] = 0
    char_dict['shieldType'] = "None"
    char_dict['shieldMeDB'] = 0
    char_dict['shieldMiDB'] = 0
    char_dict['shieldMaDB'] = 0
    char_dict['helm'] = "None"
    char_dict['helmMaDB'] = -5
    char_dict['armGrea'] = "None"
    char_dict['legGrea'] = "None"
    char_dict['at_qu_pen'] = 0

    # Development Points
    tdp=(float(char_dict['codp'])+float(char_dict['agdp'])+float(char_dict['sddp'])+float(char_dict['medp'])+float(char_dict['redp']))*float(cfgData.dp_multipler)
    char_dict['dp']=round(tdp,1)
    dp_math=Decimal(char_dict['dp'])
    dp=Decimal(dp_math).quantize(Decimal('1e-3'))
    char_dict['tempdp'] = int(round(dp,0))

    # Set Resistance Roll Modifiers
    char_dict['Essmod'] = int(char_dict['Essmod'])+int(char_dict['emtb'])
    char_dict['Chanmod'] = int(char_dict['Chanmod'])+int(char_dict['intb'])
    char_dict['Mentmod'] = int(char_dict['Mentmod'])+int(char_dict['prtb'])
    char_dict['Poimod'] = int(char_dict['Poimod'])+int(char_dict['cotb'])
    char_dict['Dismod'] = int(char_dict['Dismod'])+int(char_dict['cotb'])

    # Power Point Math
    char_dict['stpp'],char_dict['qupp'],char_dict['copp'],char_dict['agpp'],char_dict['sdpp'],char_dict['mepp'],char_dict['repp']="-","-","-","-","-","-","-"
    if char_dict['mrealm'] == "NON":
        char['prpp'],char_dict['inpp'],char_dict['empp']=0.0,0.0,0.0
        char_dict['tpp']=0.0
    if char_dict['mrealm'] == "PR":
        char_dict['inpp'],char_dict['empp']=0.0,0.0
        char_dict['tpp']=char_dict['prpp']
    if char_dict['mrealm'] == "IN":
        char_dict['empp'],char_dict['prpp']=0.0,0.0
        char_dict['tpp']=char_dict['inpp']
    if char_dict['mrealm'] == "EM":
        char_dict['inpp'],char_dict['prpp']=0.0,0.0
        char_dict['tpp']=char_dict['empp']
    if char_dict['mrealm'] == "IP":
        char_dict['empp']=0.0
        char_dict['tpp']=(float(char_dict['inpp'])+float(char_dict['prpp']))/2
    if char_dict['mrealm'] == "PE":
        char_dict['inpp']=0.0
        char_dict['tpp']=(float(char_dict['empp'])+float(char_dict['prpp']))/2
    if char_dict['mrealm'] == "IE":
        char_dict['prpp']=0.0
        char_dict['tpp']=(float(char_dict['inpp'])+float(char_dict['empp']))/2
    if char_dict['mrealm'] == "AR":
        char_dict['tpp']=(float(char_dict['inpp'])+float(char_dict['prpp'])+float(char_dict['empp']))/3

    # Development Point Math
    stdp,qudp,emdp,indp,prdp="-","-","-","-","-"

    # Set Character's First Name
    le=1
    while le==1:
        try:
            first_name=raw_input('Enter the Character\'s First Name: ')
            if re.match("^[A-Za-z]*$",first_name):
                le=0
            else:
                print "You must enter a First name for your character!"
        except:
            print "You must enter a First name for your character!"
    char_dict['name'] = first_name
    # Set Last Name
    last_name=""
    last_name=raw_input('Enter the Character\'s Last Name: ')
    if last_name == "":
        char_dict['Fullname'] = first_name
    else:
        char_dict['FullName'] = first_name +" "+ last_name
    char_path=cfgData.char_dir+"/"+first_name

    # Check if character exists
    path_check = os.path.exists(char_path+"/"+first_name+".json")
    while path_check == True:
        print "Character exists! Please enter a different name for your character"
        le=1
        try:
            first_name=raw_input('Enter the Character\'s First Name: ')
            if re.match("^[A-Za-z]*$",first_name):
                le=0
                char_path=cfgData.char_dir+"/"+first_name
                path_check = os.path.exists(char_path+"/"+first_name+".json")
            else:
                print "You must enter a First name for your character!"
        except:
            print "Character exists! Please enter a different name for your character"

        # If character and folder doesn't exist - create it
        char_dict['name']=first_name
    if not os.path.exists(char_path):
        os.makedirs(char_path)

    # Write out file
    with open(char_path+"/"+first_name+".json", 'w') as f:
        f.write(json.dumps(char_dict))

    # Open Skill file
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    skill_list=[]
    for list in sl:
        skill_list.append(list.split(","))
        crt=1

    # Loop through skills and add to dictionary
    for i in skill_list:
        #print i[1]
        stat_tb2,stat_tb3,stat_tb4 = i[2].lower()+"tb",i[3].lower()+"tb",i[4].lower()+"tb"
        if i[2] == "NA" or i[3] == "NA":
            char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
        elif i[2] == "":
            if i[1].startswith("Spell") or i[1].startswith("Transcend") or i[1].startswith("Power"):
                if char_dict['mrealm'] == "NA":
                    i[2],i[5] = "NA","NA"
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "EM":
                    stat_tb2,i[5] = "em",char_dict['mrealm']
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "IN":
                    stat_tb2,i[5] = "in",char_dict['mrealm']
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "PR":
                    stat_tb2,i[5] = "pr",char_dict['mrealm']
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "IP":
                    stat_tb2,stat_tb3,i[5] = "in","pr",i[6]
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "PE":
                    stat_tb2,stat_tb3,i[5] = "em","pr",i[6]
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "IE":
                    stat_tb2,stat_tb3,i[5] = "in","em",i[6]
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
                if char_dict['mrealm'] == "AR":
                    stat_tb2,stat_tb3,stat_tb4,i[5] = "em","in","pr",i[6]
                    char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
        elif i[3] == "":
            char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
        else:
            char_skill[i[0]]=(i[1],i[5],i[7],i[proID],i[6],0,0,0,0,0,0,0,0,0,0)
    # Write Character data to file
    with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name'].capitalize()+"_Skills.json", 'w') as f:
        f.write(json.dumps(char_skill))

    # Set Weapon costs using function
    weapon_costs(first_name)

def weapon_costs(user_name):
    # Open the character and skill file, read-only
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+"_Skills.json","r") as cf:
        skill_dict = json.load(cf)
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+".json","r") as cf:
        char_dict = json.load(cf)

    ## Read in list of professions and weapon costs, read-only
    with open(cfgData.cfg_dir+"/profession.csv","r") as procsv:
        plist=procsv.read()

    for profess in plist.splitlines():
        rt=profess.split(",")
        if rt[1] == char_dict['proname']:
            wclist=[rt[9],rt[10],rt[11],rt[12],rt[13],rt[14]]

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
    weapsel=""
    while weapsel<1 or weapsel>6: # Check that input is in the range
        try:
            weapsel = int(raw_input('Select Weapon cost to assign: '))
        except:
            print "You must select a number between (1 and 6)"

    # Weapon category selection
    weapcat=""
    while weapcat<1 or weapcat>6: # Check that input is in the range
        try:
            weapcat = int(raw_input('Select Weapon Category to assign cost: '))
        except:
            print "You must select a number between (1 and 6)"

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
        weapsel = ""
        while weapsel<1 or weapsel>len(wlist): # Check that input is in the range
            try:
                weapsel=int(raw_input('Select weapon cost to assign: '))
            except:
                print "You must select a number between (1 and {:1})".format(len(wlist))

        # Weapon category selection
        weapcat = ""
        while weapcat<1 or weapcat>len(wclist): # Check that input is in the range
            try:
                weapcat=int(raw_input('Select Weapon Category to assign cost: '))
            except:
                print "You must select a number between (1 and {:1})".format(len(wclist))


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
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+"_Skills.json","r") as sf:
        skill_dict = json.load(sf)
    # Open ds.csv for count of skills
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    skcnt=1
    # Loop through skills and update costs of weapons
    while skcnt <= len(sl)-6:
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
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+"_Skills.json","w") as sw:
        sw.write(json.dumps(skill_dict))

    # Open character's skill file to update Two-weapon Combos
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+"_Skills.json","r") as sl:
        skill_dict = json.load(sl)

    cnt=1
    while cnt <= len(skill_dict):
        if skill_dict[`cnt`][0].startswith("TWC:") and '/' in skill_dict[`cnt`][3]:
            cost=skill_dict[`cnt`][3]
            ecost=cost.split("/")
            twc=str(int(cost[0])*2)+"/"+str(int(cost[2])*2)
            i=cnt-1
            skill_dict[`cnt`][3]=twc
        cnt+=1

    with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name'].capitalize()+"_Skills.json", 'w') as f:
        f.write(json.dumps(skill_dict))

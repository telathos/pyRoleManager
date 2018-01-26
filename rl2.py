import json
import re
import os.path
from natsort import natsorted, ns
import cfgData
import charMenu
from colorama import init
from colorama import Fore, Back, Style
import decimal
import sys
init()

dp_used=0
limit=1
def skill_rank_qty_check(srnk,cost,lvl,old):
    global dp_used
    global limit
    if len(cost) > 2:
        #print len(cost),":len(cost)"
        ecost=cost.split('/')
        if ecost[1] == "*":
            limit=3
        else:
            limit=2
    else:
        ecost=cost
        limit=1

    nlimit = (limit - old)
    #print limit,":limit"
    #print nlimit,":nlimit"

    while srnk > limit or srnk > nlimit:
        print "You can not purchase that number of ranks."
        print "Enter {} or less ranks".format(nlimit)
        srnk=int(raw_input('Number of Ranks: '))
        if srnk == 0:
            break
    else:
        if len(cost) <= 2: # 9 or 10
            dp_used=int(cost)
        elif len(cost) > 2:
            if srnk <=3 and ecost[1] == "*": #1/*
                if old >= 1:
                    #print "*1*if"
                    #print ecost[0],":ecost[0]"
                    #print old,":old 1"
                    dp_used=int(ecost[0]) * int(srnk)
                else:
                    #print "*1*else"
                    dp_used=int(ecost[0]) * int(srnk)
            elif srnk == 2: # 1/3 2 ranks
                dp_used=int(ecost[0])+int(ecost[1])
            else: # 1/3 1 rank
                new = old + srnk
                if old == 1:
                    dp_used=int(ecost[1])
                    srnk=1
                else:
                    dp_used=int(ecost[0])
    return dp_used,srnk

skill_menu_list=[]
def create_skill_menu(arg1):
    i=1
    # Clear list for rebuilding
    del skill_menu_list[:]
    for skills in arg1:
        print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
        skill_menu_list.insert(i,skills[8])
        i+=1
    print "{:6}|{:72}|".format("","")
    print "{:>3}.) | Back{:67}|".format(i,"")
    print 80 * "-"
    print
    return arg1,skill_menu_list

def iround(x):
    # Rounds floating point number to nearest interger
    return int(round(x) - .5) + (x > 0)

def skill_added_display(char,skill):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as f:
        char_dict=json.load(f)
    stats=[]
    cnt=0
    for stat in char_dict[skill][1].split("/"):
        stats.insert(cnt,stat)
    if len(stats)==2:
        one=stats[0].lower()+"tb"
        two=stats[1].lower()+"tb"
        avg=(float(char_dict[one])+float(char_dict[two]))/2
    elif len(stats)==3:
        one=stats[0].lower()+"tb"
        two=stats[1].lower()+"tb"
        three=stats[2].lower()+"tb"
        avg=(float(char_dict[one])+float(char_dict[two])+float(char_dict[three]))/3
    else:
        if stats[0] == "NA":
            avg=0.0
        else:
            one=stats[0].lower()+"tb"
            avg=float(char_dict[one])

    rank_total=char_dict[skill][5]+char_dict[skill][6]+char_dict[skill][7]+char_dict[skill][8]
    if rank_total>=30:
        skill_bonus=iround(((rank_total-20)*0.5)+80)
    elif rank_total>=20 and rank_total<30:
        skill_bonus=((rank_total-20)*1)+70
    elif rank_total>=10 and rank_total<20:
        skill_bonus=((rank_total-10)*2)+50
    else:
        skill_bonus=rank_total*5
    ravg=iround(avg)

    # Create list of the level bonus
    lblist=[]
    with open(cfgData.cfg_dir+"/pro.csv") as f:
        llbonus=f.read()
    for lb in llbonus.splitlines():
        rt=lb.split(",")
        if rt[0]==char_dict['pro_name']:
            lblist=[rt[9],rt[10],rt[11],rt[12],rt[13],rt[14],rt[15],rt[16],rt[17],rt[18],rt[19],rt[20],rt[21],rt[22],rt[23],rt[24]]

    # Lookup category and Calcalute lvl Bonus
    if char_dict[skill][4] == "academic":
        lvl_bonus = int(lblist[0])
    if char_dict[skill][4] == "arms":
        lvl_bonus = int(lblist[1])
    if char_dict[skill][4] == "athletic":
        lvl_bonus = int(lblist[2])
    if char_dict[skill][4] == "base":
        lvl_bonus = int(lblist[3])
    if char_dict[skill][4] == "body development":
        lvl_bonus = int(lblist[4])
    if char_dict[skill][4] == "concentration":
        lvl_bonus = int(lblist[5])
    if char_dict[skill][4] == "deadly":
        lvl_bonus = int(lblist[6])
    if char_dict[skill][4] == "directed spells":
        lvl_bonus = int(lblist[7])
    if char_dict[skill][4] == "general":
        lvl_bonus = int(lblist[8])
    if char_dict[skill][4] == "linguistic":
        lvl_bonus = int(lblist[9])
    if char_dict[skill][4] == "magical":
        lvl_bonus = int(lblist[10])
    if char_dict[skill][4] == "medical":
        lvl_bonus = int(lblist[11])
    if char_dict[skill][4] == "outdoor":
        lvl_bonus = int(lblist[12])
    if char_dict[skill][4] == "perception":
        lvl_bonus = int(lblist[13])
    if char_dict[skill][4] == "social":
        lvl_bonus = int(lblist[14])
    if char_dict[skill][4] == "subterfuge":
        lvl_bonus = int(lblist[15])
    if char_dict['lvl']<= 1:
        lvl_mult =1
    else:
        lvl_mult=int(char_dict['lvl'])

    lvl_bonus = lvl_bonus * lvl_mult

    #if skmb_bonus
    skmb_bonus=0
    total_bonus=(ravg+lvl_bonus+skill_bonus+skmb_bonus)

    print
    cfgData.skill_header_added_skill()
    print "| {:32} |{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(char_dict[skill][0],char_dict[skill][1],char_dict[skill][3],char_dict[skill][5],char_dict[skill][6],char_dict[skill][7],char_dict[skill][8],ravg,skill_bonus,skmb_bonus,lvl_bonus,total_bonus)
    print 104 * "-"

    char_dict[skill][10]=ravg
    char_dict[skill][11]=skill_bonus
    char_dict[skill][12]=skmb_bonus
    char_dict[skill][13]=lvl_bonus
    char_dict[skill][14]=total_bonus

    with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
        f.write(json.dumps(char_dict))
    char_dict.clear()

def skill_mb_bonus():
    p=charMenu.char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"
    s-=1
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json") as f:
        char_dict=json.load(f)
    sklist=[]
    sklst=[]

    for words in char_dict:
        if words.isdigit():
            index=words
            sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])
            sklst=sorted(sklist, key=lambda skill: skill[0])
    menu_loop=True
    while menu_loop:
        search=str(raw_input("Select Skill to add Misc bonus: "))
        # Takes inputed search and adds regex matching code
        regex = re.compile('^%s.+'%search,re.I)

        # Create header
        print "| {:5} | {:32} | {:5} |".format("","","Misc")
        print "| {:>5} | {:32} | {:5} |".format("","Skill Name","Bonus")
        print 52 * "-"
        # Loop through skills
        skill_menu=[]
        for y in sklst:
            if re.search(regex,y[0]):
                print "| {:>3}.) | {:32} | {:^5} |".format(y[13],y[0],y[11])
                # Create list of skills in menu
                skill_menu.append(int(y[13]))
        while skill_menu:
            m=int(raw_input("Select skill: "))
            if m in skill_menu:
                msb=int(raw_input("Bonus: "))
                char_dict[`m`][13]=int(msb)

                # Open character file to write update
                with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json",'w') as f:
                    f.write(json.dumps(char_dict))
                skill_menu=False
                menu_loop=False
            else:
                print "Select a skill on the list"
                print

def select_skills(char):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as f:
        char_dict=json.load(f)

    # load for skill list count
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    sklist=[]
    sklst=[]

    for words in char_dict:
        if words.isdigit():
            index=words
            sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])
            sklst=sorted(sklist, key=lambda skill: skill[0])
    #print sklst
    for y in sklst:
        if y[0] == "Jumping":
            print y[4] # Hobby
            print y[5] # AD
            print y[6] # AP
            print y[7] # Std
        if y[4] == 0:
            pass


    # Set Base dp
    if char_dict['tempdp']< char_dict['dp']:
        current_dp=iround(char_dict['tempdp'])
    else:
        current_dp=iround(char_dict['dp'])
        char_dict['tempdp']=current_dp

    # Start loop
    skloop=True
    if char_dict['lvl'] == 0 and char_dict['tempdp'] >= iround(char_dict['dp']):
        print
        print "Are you ready to assign skill ranks for your Adolescence Level?"
        print
        while True:
            y=str(raw_input('[Y/N]: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                break
            else:
                print "Invalid Selection! Enter Y or N"

    elif char_dict['lvl'] == 0.5 and char_dict['tempdp'] >= iround(char_dict['dp']):
        print
        print "Are you ready to assign skill ranks for your Appenticeship Level?"
        print
        while True:
            y=str(raw_input('[Y/N]: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                break
            else:
                print "Invalid Selection! Enter Y or N"

    elif char_dict['lvl'] >= 1 and char_dict['tempdp'] >= iround(char_dict['dp']):
        print
        print "Are you ready to assign skill ranks for level {}?".format(char_dict['lvl'])
        print
        while True:
            y=str(raw_input('[Y/N]: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                break
            else:
                print "Invalid Selection! Enter Y or N"

    while skloop:
        if char_dict['tempdp']<1.0:
            if char_dict['lvl']==0:
                next_lvl="Appenticeship"
                print next_lvl
            elif char_dict['lvl']==0.5:
                next_lvl=1
            else:
                next_lvl=int(char_dict['lvl']+1)
                # Clear temp column
                for words in char_dict:
                    if words.isdigit():
                        char_dict[words][9] = 0
        # Reload Character file
        char_dict.clear()
        with open(cfgData.char_dir+"/"+char+"/"+char+".json") as f:
            char_dict=json.load(f)
        #print char_dict['lvl']
        #print char_dict['tempdp']
        print
        if char_dict['lvl']==0:
            # Call suggested adolescence skills module
            cfgData.adolescence_skills()
            print
        print "Enter the start of the Skill to increase:"
        print 'Example: entering b will list all skills that start with "B"'
        print
        print "Enter 'Exit' to return the previous menu"
        search=str(raw_input(": "))
        # Takes inputed search and adds regex matching code
        regex = re.compile('^%s.+'%search,re.I)

        if search.upper() == "EXIT":
            skloop=False
        else:
            # Create header
            print "*",78 * "=","*"
            print "| {:5} | {:32} | {:^3} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
            print "| {:>5} | {:32} | {:^3}| {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
            print "*",78 * "-","*"
            # Loop through skills
            skill_menu=[]
            for y in sklst:
                if re.search(regex,y[0]):
                    print "| {:>3}.) | {:32} | {:^3} | {:^5} | {:^5} | {:^5} | {:^5} |".format(y[13],y[0],y[3],y[4],y[5],y[6],y[7])
                    # Create list of skills in menu
                    skill_menu.append(int(y[13]))
            print "*",78 * "-","*"

            while skill_menu:
                cfgData.running_dp(current_dp)
                print "Enter the skill number or 'Exit' to return to the previous menu"
                m=raw_input("Skill: ")
                if m.upper() == "EXIT":
                    skill_menu = False
                else:
                    print char_dict[`m`]
                    if char_dict['lvl'] == 0:
                        col = char_dict[`m`][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[`m`][7]
                    else:
                        col = char_dict[`m`][9]

                    print col
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[`m`][3]
                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)

                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[`m`][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[`m`][7] += rnk
                        else:
                            char_dict[`m`][9] += rnk
                            char_dict[`m`][8] += char_dict[`m`][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char+"/"+char+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        # Display newly added skill
                        print "*"
                        print "| {:32} | {:^3} | {:^3} | {:^3} | {:^3} |".format(char_dict[`m`][0],char_dict[`m`][5],char_dict[`m`][6],char_dict[`m`][7],char_dict[`m`][8])
                        print "*"
                        #skill_added_display(char_dict['name'],skill_menu_list[`m`])
            '''
            if m in skill_menu:
                skill=int(raw_input("Bonus: "))
                char_dict[`m`][13]=int(skill)
            print char_dict[`m`][13]

        print "| 1.) A      10.) J      19.) U"
        print "| 2.) B      11.) L      20.) V"
        print "| 3.) C      12.) M      21.) W"
        print "| 4.) D      13.) N      22.) Y"
        print "| 5.) E      14.) P"
        print "| 6.) F      15.) Q"
        print "| 7.) G      16.) R"
        print "| 8.) H      17.) S"
        print "| 9.) I      18.) T"
        print
        print "| X.) Back"
        print
        if char_dict['lvl']==0:
            print "Suggested Adolescence skills:"
            print
            print "Basic Math"
            print "Climbing"
            print "Cookery"
            print "First Aid"
            print "General Perception"
            print "Body Development"
            print "Hygiene"
            print "Stalk & Hide"
            print "Swimming"
            print "Dagger"
            print
        ska=raw_input('Select First Letter of Skill: ')

        def skill_to_list(g):
            sklist=[]
            sklst={}
            for words in char_dict:
                if words.isdigit():
                    if char_dict[words][0].startswith(g):
                        index=words
                        sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],index])
                        sklst=sorted(sklist, key=lambda skill: skill[0])
            return sklst

        sksubloop=True
        skill_menu_list=[]

        sys.exit()
        if ska=="1":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("A")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]

                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)

                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        # Display newly added skill
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="2":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("B")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False

        if ska=="3":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("C")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="4":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("D")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    #print col,":col before function"
                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    #print dpu,":dpu"
                    #print rnk,":ranks added"
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="5":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("E")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="6":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("F")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="7":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("G")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="8":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("H")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="9":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("I")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="10":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("J")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="11":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("L")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="12":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("M")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="13":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("N")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="14":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("P")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="15":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("Q")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="16":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("R")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="17":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("S")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    print dpu,":dpu"
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="18":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("T")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="19":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("U")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="20":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("V")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="21":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("W")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False
        if ska=="22":
            cfgData.running_dp(current_dp)
            sx=skill_to_list("Y")
            while sksubloop:
                cfgData.skill_header()
                sx,skill_menu_list=create_skill_menu(sx)
                length=len(sx)+1
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=length:
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                if sr == length:
                    sksubloop=False
                else:
                    # substrat one from menu select to line up with list
                    sr-=1
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[skill_menu_list[sr]][3]
                    # Define which column to update
                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][9]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[skill_menu_list[sr]][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[skill_menu_list[sr]][7] += rnk
                        else:
                            char_dict[skill_menu_list[sr]][9] += rnk
                            char_dict[skill_menu_list[sr]][8] += char_dict[skill_menu_list[sr]][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        skill_added_display(char_dict['name'],skill_menu_list[sr])
                    sksubloop=False

        if ska.upper() == "X":
            skloop=False
            print "Back to main menu"
    # Clear dictionary
    char_dict.clear()
'''

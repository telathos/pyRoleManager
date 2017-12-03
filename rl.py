import json
import re
import os.path
from natsort import natsorted, ns
import cfgData
import charMenu
from colorama import init
from colorama import Fore, Back, Style
import decimal
init()

dp_used=0
limit=1
def skill_rank_qty_check(srnk,cost,lvl,old):
    global dp_used
    global limit
    print old,":old"
    if len(cost) > 2:
        ecost=cost.split('/')
        if ecost[1] == "*":
            limit=3
        else:
            limit=2
    else:
        ecost=cost
        limit=1

    nlimit = (limit - old)
    print limit,":limit"
    print nlimit,":nlimit"

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
                    dp_used=int(ecost[0]) * (3 - srnk)
                    srnk-=old
                else:
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
    if srnk < 1:
        dp_used=0
        print dp_used
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

def select_skills():
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
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json") as f:
        char_dict=json.load(f)
    # Create snapshot of the data before starting
    char_dict_orig=char_dict

    # load for skill list count
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    # Set Base dp
    current_dp=char_dict['dp']
    char_dict['tempdp']=current_dp

    # Start loop
    skloop=True
    if char_dict['lvl'] == 0 and char_dict['tempdp'] <= char_dict['dp']:
        print
        print "Are you ready to assign skill ranks for your Adolescence Level?"
        print "[Yes/No]"
        print
        while True:
            y=str(raw_input('Y/N: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                break
            else:
                print "Invalid Selection! Enter Y or N"

    elif char_dict['lvl'] == 0.5 and char_dict['tempdp'] <= char_dict['dp']:
        print
        print "Are you ready to assign skill ranks for your Appenticeship Level?"
        print "[Yes/No]"
        print
        while True:
            y=str(raw_input('Y/N: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                break
            else:
                print "Invalid Selection! Enter Y or N"

    elif char_dict['lvl'] == 1 and char_dict['tempdp'] <= char_dict['dp']:
        print
        print "Are you ready to assign skill ranks for level {}?".format(char_dict['lvl'])
        print "[Yes/No]"
        print
        while True:
            y=str(raw_input('Y/N: '))
            if y.upper() =="N":
                skloop=False
                break
            elif y.upper() == "Y":
                lvl="ap"
                char_dict['lvl_raise']= "ap"
                break
            else:
                print "Invalid Selection! Enter Y or N"

    while skloop:
        print
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
        ska=raw_input('Select First Letter of Skill: ')
        print

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
                    # Define which column to update

                    if char_dict['lvl'] == 0:
                        col = char_dict[skill_menu_list[sr]][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[skill_menu_list[sr]][7]
                    else:
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
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
                        col = char_dict[skill_menu_list[sr]][8]

                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)
                    current_dp-=float(dp_used)
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
                            char_dict[skill_menu_list[sr]][8] += rnk
                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                            f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska.upper() == "X":
            skloop=False
            print "Back to main menu"

#select_skills()

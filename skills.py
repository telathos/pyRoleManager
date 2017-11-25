import json
import re
import os.path
from natsort import natsorted, ns
import cfgData
import charMenu

dp_used=0
limit=1
def skill_rank_qty_check(srnk,cost):
    global dp_used
    global limit
    if len(cost) > 2:
        ecost=cost.split('/')
        if ecost[1] == "*":
            limit=3
        else:
            limit=2
    else:
        ecost=cost
        limit=1
    while srnk > limit:
        print "You can not purchase that number of ranks."
        print "Enter a different number of ranks"
        srnk=int(raw_input('Number of Ranks: '))
    else:
        if len(cost) <= 2:
            dp_used=int(cost)
        elif len(cost) > 2:
            if srnk <=3 and ecost[1] == "*":
                dp_used=int(ecost[0]) * int(srnk)
            elif srnk == 2:
                dp_used=int(ecost[0])+int(ecost[1])
            else:
                dp_used=int(ecost[0])

        return dp_used

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

    # load for skill list count
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    # Start loop
    skloop=True
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
            i=1
            sx=skill_to_list("A")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="2":
            i=1
            sx=skill_to_list("B")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="3":
            i=1
            sx=skill_to_list("C")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="4":
            i=1
            sx=skill_to_list("D")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="5":
            i=1
            sx=skill_to_list("E")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="6":
            i=1
            sx=skill_to_list("F")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="7":
            i=1
            sx=skill_to_list("G")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="8":
            i=1
            sx=skill_to_list("H")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="8":
            i=1
            sx=skill_to_list("I")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="10":
            i=1
            sx=skill_to_list("J")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="11":
            i=1
            sx=skill_to_list("L")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="12":
            i=1
            sx=skill_to_list("M")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="13":
            i=1
            sx=skill_to_list("N")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="14":
            i=1
            sx=skill_to_list("P")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="15":
            i=1
            sx=skill_to_list("Q")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="16":
            i=1
            sx=skill_to_list("R")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="17":
            i=1
            sx=skill_to_list("S")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="18":
            i=1
            sx=skill_to_list("T")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="19":
            i=1
            sx=skill_to_list("U")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="20":
            i=1
            sx=skill_to_list("V")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="21":
            i=1
            sx=skill_to_list("W")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska=="22":
            i=1
            sx=skill_to_list("Y")
            while sksubloop:
                print 80 * "-"
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
                print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
                print 80 * "-"
                for skills in sx:
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print "{:6}|{:72}|".format("","")
                print "{:>3}.) | Back{:67}|".format(i,"")
                print
                print 80 * "-"
                print
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
                    skill_rank_qty_check(srnk,cost)
                    print dp_used

                    # Update dictionary
                    char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                    # Write Character data to file
                    with open(char_dir+"/"+char_dict['name']+"/"+char_dict['name']+".json","w") as f:
                        f.write(json.dumps(char_dict))
                    sksubloop=False
        if ska == "X" or ska == "x":
            skloop=False

#select_skills()

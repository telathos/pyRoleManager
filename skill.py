import json
import re
from decimal import Decimal
import charMenu
import cfgData

###### dictionaries ###########
char_dict={}
skill_dict={}
###### Lists ###########
skill_menu=[]
temp_skill_list=[]
###############
def import_skill(char):
    print char
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as cf:
        char_dict=json.load(cf)
    with open(cfgData.char_dir+"/"+char+"/"+char+"_skills.json") as sf:
        skill_dict=json.load(sf)

    tempdp=char_dict['tempdp']
    select=0
    while select == 0:
        print ""
        print "Enter the start of the Skill to increase:"
        print 'Example: entering b will list all skills that start with "B"'
        print
        print "Enter 'Exit' to return the previous menu"
        search=str(raw_input(": "))
        print search
        # Takes inputed search and adds regex matching code
        regex = re.compile('^%s.+'%search,re.I)
        skill_menu=[]
        if search.upper() == "EXIT":
            select = 1
        else:
            # Create header
            print "*",79 * "=","*"
            print "| {:5} | {:32} | {:^4} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
            print "| {:>5} | {:32} | {:^4} | {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
            print "*",79 * "-","*"
            # Loop through skills
            for y in skill_dict:
                if re.search(regex,skill_dict[y][0]):
                    print "| {:>3}.) | {:32} | {:^4} | {:^5} | {:^5} | {:^5} | {:^5} |".format(y,skill_dict[y][0],skill_dict[y][3],
                                                                                               skill_dict[y][5],skill_dict[y][6],skill_dict[y][7],
                                                                                               skill_dict[y][8])
                    # Create list of skills in menu
                    skill_menu.append(int(y))
            print "*",79 * "-","*"
        skill_select = 0
        while skill_select == 0 and select == 0:
            try:
                rnkch=int(raw_input("Select skill: "))
            except:
                print "You must enter a number"
            if rnkch in skill_menu:
                print "Enter quantity of ranks for all skills types"
                print "Separate each type with a comma"
                print "Ex. 0,0,0,4"
                rnkhb, rnkad, rnkap, rnkstd = [int(x) for x in raw_input("Enter (4) numbers total: ").split(",")]
                # Exit while
                skill_select=1

                # Update bonuses
                stats=skill_dict[`rnkch`][1].split("/")
                if len(skill_dict[`rnkch`][1])==5:
                    stat_bonus_math=(float(char_dict[stats[0].lower()+"tb"])+float(char_dict[stats[1].lower()+"tb"]))/2
                    stat_bonus=Decimal(stat_bonus_math).quantize(Decimal('1e-3'))
                    stat_bonus=int(round(stat_bonus,0))
                    #print stat_bonus,":Stat"
                elif len(skill_dict[`rnkch`][1])==8:
                    stat_bonus_math=(float(char_dict[stats[0].lower()+"tb"])+float(char_dict[stats[1].lower()+"tb"])+float(char_dict[stats[2].lower()+"tb"]))/3
                    stat_bonus=Decimal(stat_bonus_math).quantize(Decimal('1e-3'))
                    stat_bonus=int(round(stat_bonus,0))
                    #print stat_bonus,":Stat"
                elif len(skill_dict[`rnkch`][1])==2 and skill_dict[`rnkch`][1].lower() != "na":
                    stat_bonus=char_dict[stats[0].lower()+"tb"]
                    #print stat_bonus,":Stat"
                elif skill_dict[`rnkch`][1].lower() == "na":
                    print "na"
                    stat_bonus=0

                # Update skill rank total
                skrnk = rnkhb + rnkad + rnkap + rnkstd
                print skrnk,": # of ranks"
                if skrnk <= 10:
                    skill_rank_total = skrnk * 5
                elif 10 < skrnk <= 20:
                    skill_rank_total = 50 + (skrnk - 10) * 2
                elif 20 < skrnk <=30:
                    skill_rank_total = 70 + (skrnk - 20) * 1
                elif skrnk > 30:
                    skill_rank_total_math = float(80 + (skrnk - 30) * 0.5)
                    skill_rank_total=Decimal(skill_rank_total_math).quantize(Decimal('1e-3'))
                    skill_rank_total=int(round(skill_rank_total,0))

                # Update level bonus
                lblist=[]
                with open(cfgData.cfg_dir+"/pro.csv") as f:
                    llbonus=f.read()
                for lb in llbonus.splitlines():
                    rt=lb.split(",")
                    if rt[0]==char_dict['proname']:
                        lblist=[rt[9],rt[10],rt[11],rt[12],rt[13],rt[14],rt[15],rt[16],rt[17],rt[18],rt[19],rt[20],rt[21],rt[22],rt[23],rt[24]]
                # Lookup category and Calcalute lvl Bonus
                if skill_dict[`rnkch`][4] == "academic":
                    lvl_bonus = int(lblist[0])
                if skill_dict[`rnkch`][4] == "arms":
                    lvl_bonus = int(lblist[1])
                if skill_dict[`rnkch`][4] == "athletic":
                    lvl_bonus = int(lblist[2])
                if skill_dict[`rnkch`][4] == "base":
                    lvl_bonus = int(lblist[3])
                if skill_dict[`rnkch`][4] == "body development":
                    lvl_bonus = int(lblist[4])
                if skill_dict[`rnkch`][4] == "concentration":
                    lvl_bonus = int(lblist[5])
                if skill_dict[`rnkch`][4] == "deadly":
                    lvl_bonus = int(lblist[6])
                if skill_dict[`rnkch`][4] == "directed spells":
                    lvl_bonus = int(lblist[7])
                if skill_dict[`rnkch`][4] == "general":
                    lvl_bonus = int(lblist[8])
                if skill_dict[`rnkch`][4] == "linguistic":
                    lvl_bonus = int(lblist[9])
                if skill_dict[`rnkch`][4] == "magical":
                    lvl_bonus = int(lblist[10])
                if skill_dict[`rnkch`][4] == "medical":
                    lvl_bonus = int(lblist[11])
                if skill_dict[`rnkch`][4] == "outdoor":
                    lvl_bonus = int(lblist[12])
                if skill_dict[`rnkch`][4] == "perception":
                    lvl_bonus = int(lblist[13])
                if skill_dict[`rnkch`][4] == "social":
                    lvl_bonus = int(lblist[14])
                if skill_dict[`rnkch`][4] == "subterfuge":
                    lvl_bonus = int(lblist[15])

                # Update Total skill bonus
                total_bonus = skill_dict[`rnkch`][10] + skill_dict[`rnkch`][11] + skill_dict[`rnkch`][12] + skill_dict[`rnkch`][13]
                # Update dictionary
                skill_dict[`rnkch`][11],skill_dict[`rnkch`][5],skill_dict[`rnkch`][6],skill_dict[`rnkch`][7],skill_dict[`rnkch`][8]=stat_bonus,rnkhb,rnkad,rnkap,rnkstd
                skill_dict[`rnkch`][10],skill_dict[`rnkch`][13],skill_dict[`rnkch`][14]=skill_rank_total,lvl_bonus,total_bonus

                # Create display
                print "*",79 * "=","*"
                print "| {:5} | {:32} | {:^4} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
                print "| {:>5} | {:32} | {:^4} | {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
                print "*",79 * "-","*"
                print "| {:>3}.) | {:32} | {:^4} | {:^5} | {:^5} | {:^5} | {:^5} |".format(rnkch,skill_dict[`rnkch`][0],skill_dict[`rnkch`][3],
                                                                                           skill_dict[`rnkch`][5],skill_dict[`rnkch`][6],skill_dict[`rnkch`][7],
                                                                                           skill_dict[`rnkch`][8])
                print "*",79 * "-","*"
            else:
                print "Not in list"
            with open(cfgData.char_dir+"/"+char+"/"+char+"_Skills.json","w") as f:
                f.write(json.dumps(skill_dict))

def update_skill_bonus(char):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as cf:
        char_dict=json.load(cf)
    with open(cfgData.char_dir+"/"+char+"/"+char+"_skills.json") as sf:
        skill_dict=json.load(sf)

    # Update bonuses
    for x in skill_dict:
        stats=skill_dict[x][1].split("/")
        if len(skill_dict[x][1])==5:
            stat_bonus_math=(float(char_dict[stats[0].lower()+"tb"])+float(char_dict[stats[1].lower()+"tb"]))/2
            stat_bonus=Decimal(stat_bonus_math).quantize(Decimal('1e-3'))
            stat_bonus=int(round(stat_bonus,0))
        elif len(skill_dict[x][1])==8:
            stat_bonus_math=(float(char_dict[stats[0].lower()+"tb"])+float(char_dict[stats[1].lower()+"tb"])+float(char_dict[stats[2].lower()+"tb"]))/3
            stat_bonus=Decimal(stat_bonus_math).quantize(Decimal('1e-3'))
            stat_bonus=int(round(stat_bonus,0))
        elif len(skill_dict[x][1])==2 and skill_dict[x][1].lower() != "na":
            stat_bonus=char_dict[stats[0].lower()+"tb"]
        elif skill_dict[x][1].lower() == "na":
            stat_bonus=0

        # Update skill rank total
        skrnk = int(skill_dict[x][5]) + int(skill_dict[x][6]) + int(skill_dict[x][7]) + int(skill_dict[x][8])
        if 1 <= skrnk <= 10:
            skill_rank_total = skrnk * 5
        elif 10 < skrnk <= 20:
            skill_rank_total = 50 + (skrnk - 10) * 2
        elif 20 < skrnk <=30:
            skill_rank_total = 70 + (skrnk - 20) * 1
        elif skrnk > 30:
            skill_rank_total_math = float(80 + (skrnk - 30) * 0.5)
            skill_rank_total=Decimal(skill_rank_total_math).quantize(Decimal('1e-3'))
            skill_rank_total=int(round(skill_rank_total,0))
        else:
            skill_rank_total=-25

        # Update level bonus
        lblist=[]
        with open(cfgData.cfg_dir+"/pro.csv") as f:
            llbonus=f.read()
        for lb in llbonus.splitlines():
            rt=lb.split(",")
            if rt[0]==char_dict['proname']:
                lblist=[rt[9],rt[10],rt[11],rt[12],rt[13],rt[14],rt[15],rt[16],rt[17],rt[18],rt[19],rt[20],rt[21],rt[22],rt[23],rt[24]]
        # Lookup category and Calcalute lvl Bonus
        if skill_dict[x][4] == "academic":
            lvl_bonus = int(lblist[0])
        if skill_dict[x][4] == "arms":
            lvl_bonus = int(lblist[1])
        if skill_dict[x][4] == "athletic":
            lvl_bonus = int(lblist[2])
        if skill_dict[x][4] == "base":
            lvl_bonus = int(lblist[3])
        if skill_dict[x][4] == "body development":
            lvl_bonus = int(lblist[4])
        if skill_dict[x][4] == "concentration":
            lvl_bonus = int(lblist[5])
        if skill_dict[x][4] == "deadly":
            lvl_bonus = int(lblist[6])
        if skill_dict[x][4] == "directed spells":
            lvl_bonus = int(lblist[7])
        if skill_dict[x][4] == "general":
            lvl_bonus = int(lblist[8])
        if skill_dict[x][4] == "linguistic":
            lvl_bonus = int(lblist[9])
        if skill_dict[x][4] == "magical":
            lvl_bonus = int(lblist[10])
        if skill_dict[x][4] == "medical":
            lvl_bonus = int(lblist[11])
        if skill_dict[x][4] == "outdoor":
            lvl_bonus = int(lblist[12])
        if skill_dict[x][4] == "perception":
            lvl_bonus = int(lblist[13])
        if skill_dict[x][4] == "social":
            lvl_bonus = int(lblist[14])
        if skill_dict[x][4] == "subterfuge":
            lvl_bonus = int(lblist[15])

        # Update Total skill bonus
        total_bonus = skill_dict[x][10] + skill_dict[x][11] + skill_dict[x][12] + skill_dict[x][13]
        # Update dictionary
        skill_dict[x][11]=stat_bonus
        skill_dict[x][10],skill_dict[x][13],skill_dict[x][14]=skill_rank_total,lvl_bonus,total_bonus

    with open(cfgData.char_dir+"/"+char+"/"+char+"_Skills.json","w") as f:
        f.write(json.dumps(skill_dict))

def skill_add(char):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as cf:
        char_dict=json.load(cf)
    with open(cfgData.char_dir+"/"+char+"/"+char+"_skills.json") as sf:
        skill_dict=json.load(sf)

    #print char_dict['tempdp']
    tempdp=char_dict['tempdp']
    while tempdp>0:
        print tempdp
        print ""
        print "Enter the start of the Skill to increase:"
        print 'Example: entering b will list all skills that start with "B"'
        print
        print "Enter 'Exit' to return the previous menu"
        search=str(raw_input(": "))
        print search
        print search.upper()
        # Takes inputed search and adds regex matching code
        regex = re.compile('^%s.+'%search,re.I)
        skill_menu=[]
        # Check if exiting loop
        if search.upper() == "EXIT":
            break
        else:
            # Create header
            print "*",79 * "=","*"
            print "| {:5} | {:32} | {:^4} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
            print "| {:>5} | {:32} | {:^4} | {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
            print "*",79 * "-","*"
            # Loop through skills
            for y in skill_dict:
                if re.search(regex,skill_dict[y][0]):
                    print "| {:>3}.) | {:32} | {:^4} | {:^5} | {:^5} | {:^5} | {:^5} |".format(y,skill_dict[y][0],skill_dict[y][3],
                                                                                               skill_dict[y][5],skill_dict[y][6],skill_dict[y][7],
                                                                                               skill_dict[y][8])
                    # Create list of skills in menu
                    skill_menu.append(int(y))
            print "*",79 * "-","*"
            #print skill_menu
            select=0
            while select == 0:
                try:
                    rnkch=int(raw_input("Select skill: "))
                    if rnkch in skill_menu:
                        select=1
                        # Check number of ranks allowed
                        if re.match("^[1-9]\/.+",skill_dict[`rnkch`][3]):
                            #print skill_dict[`rnkch`][3]
                            cost=skill_dict[`rnkch`][3].split("/")
                            if cost[1] == "*":
                                skill_qty=3
                            else:
                                skill_qty=2
                        else:
                            cost=int(skill_dict[`rnkch`][3])
                            skill_qty=1
                        # Add ranks
                        rnkadd=0
                        if skill_qty==1:
                            try:
                                rnkadd=int(raw_input("Enter number of Ranks to assign: [1]"))
                                if rnkadd > 1:
                                    print "Only 1 rank can be assigned!"
                                else:
                                    chkdp=tempdp - int(cost)
                                    if chkdp < 0:
                                        print "You do not have enough Development Points"
                                        rnkadd=0
                                    else:
                                        rnkadd=1
                                        tempdp=tempdp - int(cost)
                                        #print tempdp,":tempdp -1"
                                        temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        #print temp_skill_list
                            except:
                                print "Enter a number of ranks to assign??"
                        elif skill_qty>1:
                            while rnkadd < 1 or rnkadd > skill_qty:
                                try:
                                    rnkadd=int(raw_input("Enter number of Ranks to assign: [1-{:<1}]: ".format(skill_qty)))
                                    if rnkadd > skill_qty:
                                        print "You must enter a number between 1 and {:<2}".format(skill_qty)
                                    else:
                                        #print rnkadd,"rnkadd"
                                        #print type(rnkadd)
                                        if rnkadd == 3:
                                            used=int(rnkadd)* int(cost[0])
                                            chkdp = tempdp - used
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=2
                                            else:
                                                tempdp = tempdp - used
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 2:
                                            #print cost[0]
                                            used=int(cost[0])+int(cost[1])
                                            #print used
                                            chkdp = tempdp - used
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=1
                                            else:
                                                tempdp = tempdp - used
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 1:
                                            chkdp = tempdp - int(cost[0])
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=0
                                            else:
                                                tempdp = tempdp - int(cost[0])
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 0:
                                            rnkadd=1
                                            #print "Exit skill"
                                except:
                                    print "Enter the number of ranks"
                    else:
                        print "Select a skill on the list"
                except:
                    print "Select a skill"
            #print temp_skill_list

def add_skill():
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
    skill_add(char)

    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as cf:
        char_dict=json.load(cf)
    if len(temp_skill_list) > 0:
        print "The following ranks will be assigned to"
        if char_dict['lvl'] == 0:
            print "the selected skills for your Adolescence Level"
        elif char_dict['lvl'] == 0.5:
            print "the selected skills for your Appenticeship Level"
        elif char_dict['lvl']>= 1:
            print "the selected skills for your level {:<2} ".format(char_dict['lvl'])
        print ""
        print "*",36 * "=","*"
        for j in temp_skill_list:
            print "| {:32} | {:1} |".format(j[0],j[1])
        print "*",36 * "=","*"
        print ""
        print "Do you want to assign these ranks? [Y/N]"
        print "Selecting No will restart the selection"
        print ""
        skasch=True
        while skasch:
            try:
                sch=raw_input("Do you want to assign these ranks? [Y/N]: ")
                if sch.upper()=="Y":
                    print "Assigned"
                    skasch=False
                    # Write to skill_dict and save
                elif sch.upper()=="N":
                    skasch=True
                    skill_add(char)
                    tempdp=char_dict['tempdp']
                else:
                    print "Enter Y or N to continue"
            except:
                print "Enter Y or N to continue"

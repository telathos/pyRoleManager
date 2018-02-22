import json
import charMenu
import cfgData
#import rl
import re

def exp_check():
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
    char=p[s]
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","r") as cf:
        char_dict = json.load(cf)

    # Enter experience
    print
    print "Current Experience:",char_dict['exp']
    print "Next level:",char_dict['next_lvl']
    print
    exp=int(raw_input("Enter experience to add: "))
    # Add experience to character's current experience
    char_dict['exp'] += int(exp)
    print "New experience:",char_dict['exp']
    print
    # Check if character raised level
    if char_dict['exp'] > char_dict['next_lvl']:
        lvlcheck = lvl_check(char_dict['lvl'])

        # Check if more than one level is gained
        y=1
        while char_dict['exp'] > lvlcheck:
            lvlcheck = lvl_check(char_dict['lvl'] + y)
            y += 1

        # Set new character level
        lvl_gain = y - char_dict['lvl']
        char_dict['lvl'] = y
        in_lvl = y
        print "Leveled Up!"
        print "You gained",lvl_gain,"level(s)"

        # Set next lvl
        char_dict['next_lvl'] = next_lvl
        char_dict['tempdp']=cfgData.iround(char_dict['dp'])

        # Open character file to write out data
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", 'w') as f:
            f.write(json.dumps(char_dict))
        # Clear dictionary from memory
        char_dict.clear()

        if in_lvl > 0:
            p=0
            while p < in_lvl:
                assign_skills(char)
                p += 1

def assign_skills(char):
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

    # Set Base dp
    if char_dict['tempdp']< char_dict['dp']:
        current_dp=cfgData.iround(char_dict['tempdp'])
    else:
        current_dp=cfgData.iround(char_dict['dp'])
        char_dict['tempdp']=current_dp


    # Start loop
    skloop=True
    '''
    if char_dict['lvl'] == 0 and char_dict['tempdp'] >= cfgData.iround(char_dict['dp']):
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

    elif char_dict['lvl'] == 0.5 and char_dict['tempdp'] >= cfgData.iround(char_dict['dp']):
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

    elif char_dict['lvl'] >= 1 and char_dict['tempdp'] >= cfgData.iround(char_dict['dp']):
    '''
    if char_dict['lvl'] > 1 and char_dict['tempdp'] >= cfgData.iround(char_dict['dp']):
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
                char_dict['lvl']=0.5
                char_dict['tempdp'] = cfgData.iround(char_dict['dp'])
            elif char_dict['lvl']==0.5:
                next_lvl=1
                char_dict['lvl']=1
                char_dict['tempdp'] = cfgData.iround(char_dict['dp'])
            else:
                next_lvl=int(char_dict['lvl']+1)
                char_dict['lvl']=next_lvl
                current_dp = cfgData.iround(char_dict['dp'])
                # Clear temp column
                for words in char_dict:
                    if words.isdigit():
                        char_dict[words][9] = 0
        # Reload Character file
        char_dict.clear()
        with open(cfgData.char_dir+"/"+char+"/"+char+".json") as f:
            char_dict=json.load(f)
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

        # Check if exiting loop
        if search.upper() == "EXIT":
            skloop=False
        else:
            # Create header
            print "*",79 * "=","*"
            print "| {:5} | {:32} | {:^4} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
            print "| {:>5} | {:32} | {:^4} | {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
            print "*",79 * "-","*"
            # Loop through skills
            skill_menu=[]
            for y in sklst:
                if re.search(regex,y[0]):
                    print "| {:>3}.) | {:32} | {:^4} | {:^5} | {:^5} | {:^5} | {:^5} |".format(y[13],y[0],y[3],y[4],y[5],y[6],y[7])
                    # Create list of skills in menu
                    skill_menu.append(int(y[13]))
            print "*",79 * "-","*"

            while skill_menu:
                cfgData.running_dp(current_dp)
                print "Enter the skill number or 'Exit' to return to the previous menu"
                m = ""
                while m == "":
                    m=raw_input("Skill: ")
                    try:
                        y = int(m)
                    except:
                        print "You must enter a number"
                        print
                        print "Enter the skill number or 'Exit' to return to the previous menu"
                        m=raw_input("Skill: ")

                # Check if exiting loop
                if m.upper() == "EXIT":
                    skill_menu = False
                else:
                    print char_dict[`int(m)`][0]
                    if char_dict['lvl'] == 0:
                        col = char_dict[`int(m)`][6]
                    elif char_dict['lvl'] == 0.5:
                        col = char_dict[`int(m)`][7]
                    else:
                        col = char_dict[`int(m)`][9]

                    #print col
                    srnk=int(raw_input('Number of Ranks: '))
                    cost=char_dict[`int(m)`][3]
                    dpu,rnk = skill_rank_qty_check(srnk,cost,char_dict['lvl'],col)

                    print dpu,":dpu"
                    print rnk,":rnk"
                    print dp_used,":dp_used"
                    if rnk > 0:
                        current_dp-=int(dp_used)

                    #current_dp-=int(dp_used)
                    if current_dp < 0:
                        print "You do not have enough development points for this skill"
                        current_dp+=dp_used
                        cfgData.running_dp(current_dp)
                    else:
                        # Current DP update
                        char_dict['tempdp']=current_dp

                        # Update dictionary
                        if char_dict['lvl'] == 0:
                            char_dict[`int(m)`][6] += rnk
                        elif char_dict['lvl'] == 0.5:
                            char_dict[`int(m)`][7] += rnk
                        else:
                            char_dict[`int(m)`][9] += rnk
                            char_dict[`int(m)`][8] += char_dict[`int(m)`][9]

                        # Write Character data to file
                        with open(cfgData.char_dir+"/"+char+"/"+char+".json","w") as f:
                            f.write(json.dumps(char_dict))
                        # Display newly added skill
                        print "*",64 * "=","*"
                        print "| {:32} | {:5} | {:^5} | {:^5} | {:^5} |".format("","Hobby","AD","AP","Std")
                        print "| {:32} | {:5} | {:5} | {:5} | {:5} |".format("Skill Name","Bonus","Bonus","Bonus","Bonus")
                        print "*",64 * "-","*"
                        print "| {:32} | {:^5} | {:^5} | {:^5} | {:^5} |".format(char_dict[`int(m)`][0],char_dict[`int(m)`][5],char_dict[`int(m)`][6],char_dict[`int(m)`][7],char_dict[`int(m)`][8])
                        print "*",64 * "-","*"

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

next_lvl=0
def lvl_check(lvl):
    global next_lvl
    if lvl <= 4:
        next_lvl = (int(lvl * 10000) + 10000)
    elif lvl >= 5 and lvl <= 9:
        next_lvl = ((int(lvl - 4 ) * 20000) + 50000)
    elif lvl >=10 and lvl <= 14:
        next_lvl = ((int(lvl - 9 ) * 30000) + 150000)
    elif lvl >=15 and lvl <= 19:
        next_lvl = ((int(lvl - 14 ) * 40000) + 300000)
    else:
        next_lvl = ((int(lvl - 19 ) * 50000) + 500000)
    print "Experience for lvl",lvl+1,":",next_lvl
    return next_lvl

exp_check()

import cfgData
import charMenu
import json
import os

# function to check if any new skills have been added
def new_skill_check():
    char_dict={}
    dirlist=[]
    skills=[]
    skill_len={}
    char_list=[]
    with open(cfgData.cfg_dir+"/ds.csv","r") as r:
        skills=r.read().splitlines()
    l=len(skills)
    i=0
    col=0
    for file in os.listdir(cfgData.char_dir):
        dirlist.insert(i,file)
    for c in dirlist:
        char_dict.clear()
        '''
        Check if folder exists, but not character json file and remove folder
        This is clean up if a character creation fails in the build process
        '''
        if os.path.exists(cfgData.char_dir+"/"+dirlist[i]+"/"+dirlist[i]+".json") == False:
            os.rmdir(cfgData.char_dir+"/"+dirlist[i])
        else:
            with open(cfgData.char_dir+"/"+dirlist[i]+"/"+dirlist[i]+".json","r") as fl:
                char_dict = json.load(fl)
            x=0
            cl=0
            for words in char_dict:
                if words.isdigit():
                    char_list.insert(x,words)
                    x+=1
                    cl=len(char_list)
            del char_list[:]
            ld=l-cl
            with open(cfgData.cfg_dir+"/pro.csv","r") as rp:
                pro=rp.read().splitlines()

            for p in pro:
                if char_dict['pro_name'] == p.split(',')[0]:
                    col=int(p.split(',')[1])
            while ld>0:
                index=cl+1
                char_dict[`index`]=(skills[cl].split(',')[1],skills[cl].split(',')[5],skills[cl].split(',')[7],skills[cl].split(',')[col],skills[cl].split(',')[6],0,0,0,0,0,0,0,0,0,0)
                cl+=1
                ld-=1

            # Write Character data to file
            with open(cfgData.char_dir+"/"+dirlist[i]+"/"+dirlist[i]+".json", 'w') as f:
                f.write(json.dumps(char_dict))
            i+=1

def assign_at():
    p=charMenu.char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the character file
    char_dict={}
    s-=1
    char=p[s]
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","r") as cf:
        char_dict = json.load(cf)

    # Open Armor Type file
    with open(cfgData.cfg_dir+"/at.csv","r") as atl:
        atlist = atl.read().splitlines()

    print 85 * "="
    print "|    |                                     | Minimum  | Maximum  | Missile|          |"
    print "|    |                                     | Maneuver | Maneuver | Attack | Quickness|"
    print "| AT | Description                         |   Mod.   |   Mod.   | Penalty| Penalty  |"
    print 85 * "-"
    for a in range(0,20,1):
        t = atlist[a].split(',')
        print "| {:<2} | {:35} | {:^8} | {:^8} | {:^6} | {:^8} |".format(t[0],t[2],t[3],t[4],t[5],t[6])
    print 85 * "-"
    print

    atloop = True
    while atloop:
        at = int(raw_input("Armor Type [1-20]: "))
        if not at>=1 or not at<=20:
            print "Wrong Armor Type Selection. Please try again.. "
        else:
            for var in atlist:
                at_check = var.split(',')
                if int(at_check[0]) == int(at):
                    char_dict['armorType'] = at
                    char_dict['armorTypeDesc'] = at_check[2]
                    char_dict['at_min_mod'] = at_check[3]
                    char_dict['at_max_mod'] = at_check[4]
                    char_dict['at_miss_pen'] = at_check[5]
                    char_dict['at_qu_pen'] = at_check[6]
                    char_dict['armGrea'] = at_check[7]
                    char_dict['legGrea'] = at_check[8]

            atloop=False

    # Helmet selection
    helmloop = True
    hsubloop = True
    hl=[]
    with open(cfgData.cfg_dir+"/helm.csv") as hf:
        p = hf.read().splitlines()

    while helmloop:
        print 43 * "="
        print "|     |                         |    DB    |"
        print "|     | Helm                    | vs Magic |"
        print 43 * "-"
        for h in p:
            hl.append(h.split(','))
        for h in hl:
            print "| {:1}.) | {:23} | {:^8} |".format(h[0],h[1],h[2])
        print 43 * "="
        print
        while hsubloop:
            helm = int(raw_input("Select Helm: "))
            if helm < 1 or helm > len(p):
                print "Wrong Helm selected. Please try again.."
            else:
                for var in p:
                    helm_check = var.split(',')
                    if int(helm_check[0]) == int(helm):
                        char_dict['helm'] = helm_check[1]
                        char_dict['helmMaDB'] = helm_check[2]
                helmloop = False
                hsubloop = False

    # Shield
    shloop = True
    shsubloop = True
    tl=[]
    with open(cfgData.cfg_dir+"/shield.csv") as sh:
        t = sh.read().splitlines()

    while shloop:
        print 55 * "="
        print "|     | Shield               | Melee | Missile | Magic |"
        print 55 * "-"
        for var in t:
            tl.append(var.split(','))

        for var in tl:
            print "| {:1}.) | {:20} | {:^5} | {:^7} | {:^5} |".format(var[0],var[1],var[2],var[3],var[4])
        print 55 * "="
        print
        while shsubloop:
            sh = int(raw_input("Select Shield: "))
            if sh < 1 or sh > len(t):
                print "Wrong Shield selected. Please try again.."
            else:
                for var in t:
                        sh_check = var.split(',')
                        if int(sh_check[0]) == int(sh):
                            print sh_check[1]
                            char_dict['shieldType'] = sh_check[1]
                            char_dict['shieldMeDB'] = sh_check[2]
                            char_dict['shieldMiDB'] = sh_check[3]
                            char_dict['shieldMaDB'] = sh_check[4]
                shloop = False
                shsubloop = False

    # Write character data to file
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","w") as sw:
        sw.write(json.dumps(char_dict))


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
    char_dict={}
    s-=1
    char=p[s]
    with open(cfgData.char_dir+"/"+char+"/"+char+".json","r") as cf:
        char_dict = json.load(cf)
    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
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
    tdp=char_dict['dp']

    cfgData.clear_screen()
    print "Calculating totals..."
    print

    # Create list of the level bonus
    lblist=[]
    with open(cfgData.cfg_dir+"/pro.csv") as f:
        llbonus=f.read()
    for lb in llbonus.splitlines():
        rt=lb.split(",")
        if rt[0]==char_dict['pro_name']:
            lblist=[rt[9],rt[10],rt[11],rt[12],rt[13],rt[14],rt[15],rt[16],rt[17],rt[18],rt[19],rt[20],rt[21],rt[22],rt[23],rt[24]]

    # Pull previously assigned weapon cost for normal weapon costs
    for v in char_dict:
        if v.isdigit():
            index=v
            if char_dict[v][0] == 'Dagger':
                hs1=char_dict[v][3]
            if char_dict[v][0] == 'Mace':
                hc1=char_dict[v][3]
            if char_dict[v][0] == 'Bola':
                thr=char_dict[v][3]
            if char_dict[v][0] == 'Quarterstaff':
                h2=char_dict[v][3]
            if char_dict[v][0] == 'Short Bow':
                msl=char_dict[v][3]
            if char_dict[v][0] == 'Polearm':
                pa=char_dict[v][3]

    # Check if is a skill
    sklist=[]
    for words in char_dict:
        if words.isdigit():
            index=words
            sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])

            # Lookup category and Calcalute lvl Bonus
            if char_dict[words][4] == "academic":
                lvl_bonus = int(lblist[0])
            if char_dict[words][4] == "arms":
                lvl_bonus = int(lblist[1])
            if char_dict[words][4] == "athletic":
                lvl_bonus = int(lblist[2])
            if char_dict[words][4] == "base":
                lvl_bonus = int(lblist[3])
            if char_dict[words][4] == "body development":
                lvl_bonus = int(lblist[4])
            if char_dict[words][4] == "concentration":
                lvl_bonus = int(lblist[5])
            if char_dict[words][4] == "deadly":
                lvl_bonus = int(lblist[6])
            if char_dict[words][4] == "directed spells":
                lvl_bonus = int(lblist[7])
            if char_dict[words][4] == "general":
                lvl_bonus = int(lblist[8])
            if char_dict[words][4] == "linguistic":
                lvl_bonus = int(lblist[9])
            if char_dict[words][4] == "magical":
                lvl_bonus = int(lblist[10])
            if char_dict[words][4] == "medical":
                lvl_bonus = int(lblist[11])
            if char_dict[words][4] == "outdoor":
                lvl_bonus = int(lblist[12])
            if char_dict[words][4] == "perception":
                lvl_bonus = int(lblist[13])
            if char_dict[words][4] == "social":
                lvl_bonus = int(lblist[14])
            if char_dict[words][4] == "subterfuge":
                lvl_bonus = int(lblist[15])

            if char_dict['lvl']<= 1:
                lvl_mult = 1
            elif char_dict['lvl'] >= 1 and char_dict['lvl'] <= 20:
                lvl_mult = int(char_dict['lvl'])
            else:
                lvl_mult = 20

            if char_dict['pro_name'] == "Fighter" and char_dict[words][4] == "arms" and char_dict['lvl'] > 20:
                lvl_bonus = 60 + (char_dict['lvl'] - 20 )
            else:
                lvl_bonus = lvl_bonus * lvl_mult
            char_dict[words][13] = lvl_bonus

            # Update weapon costs
            if not char_dict[words][2] == 'Polearm' or not char_dict[words][2] == 'Missile':
                if char_dict[words][0].startswith('TWC'):
                    if char_dict[words][2] == '1-HS':
                        weatype=hs1
                    elif char_dict[words][2] == 'Thrown':
                        weatype=thr
                    elif char_dict[words][2] == '1-HC':
                        weatype=hc1
                    elif char_dict[words][2] == '2-H':
                        weatype=h2
                    if len(weatype) == 1:
                        twc_wea=int(weatype)*2
                    elif len(weatype) == 2:
                        twc_wea=int(weatype)*2
                    elif len(weatype) == 3:
                        temp=weatype.split('/')
                        twc_wea=`int(temp[0])*2` + "/" + `int(temp[1])*2`
                    char_dict[words][3]=twc_wea
                #print char_dict[words][0],":",char_dict[words][3]

                # Set weapon cost if NULL
            if char_dict[words][3] == 'NULL':
                if char_dict[words][2] == '1-HS':
                    char_dict[words][3] = hs1
                elif char_dict[words][2] == 'Thrown':
                    char_dict[words][3] = thr
                elif char_dict[words][2] == '1-HC':
                    char_dict[words][3] = hc1
                elif char_dict[words][2] == '2-H':
                    char_dict[words][3] = h2
                elif char_dict[words][2] == 'Polearm':
                    char_dict[words][3] = pa
                elif char_dict[words][2] == 'Missile':
                    char_dict[words][3] = msl

                # Write Character data to file
                with open(cfgData.char_dir+"/"+char+"/"+char+".json", "w") as f:
                    f.write(json.dumps(char_dict))

            # Get stat total bonuses
            stat=char_dict[words][1]
            if len(stat)==2:
                if stat.upper() == "NA":
                    stat_bonus = 0
                else:
                    if stat == "ST":
                        stat_bonus = sttb
                    elif stat == "QU":
                        stat_bonus = qutb
                    elif stat == "PR":
                        stat_bonus = prtb
                    elif stat == "IN":
                        stat_bonus = intb
                    elif stat == "EM":
                        stat_bonus = emtb
                    elif stat == "CO":
                        stat_bonus = cotb
                    elif stat == "AG":
                        stat_bonus = agtb
                    elif stat == "SD":
                        stat_bonus = sdtb
                    elif stat == "ME":
                        stat_bonus = metb
                    elif stat == "RE":
                        stat_bonus = retb
                    char_dict[words][11] = stat_bonus
            elif len(stat)==5:
                stats=stat.split('/')
                # Stat 1
                if stats[0] == "ST":
                    stat_bonus1 = sttb
                elif stats[0] == "QU":
                    stat_bonus1 = qutb
                elif stats[0] == "PR":
                    stat_bonus1 = prtb
                elif stats[0] == "IN":
                    stat_bonus1 = intb
                elif stats[0] == "EM":
                    stat_bonus1 = emtb
                elif stats[0] == "CO":
                    stat_bonus1 = cotb
                elif stats[0] == "AG":
                    stat_bonus1 = agtb
                elif stats[0] == "SD":
                    stat_bonus1 = sdtb
                elif stats[0] == "ME":
                    stat_bonus1 = metb
                elif stats[0] == "RE":
                    stat_bonus1 = retb
                # Stat 2
                if stats[1] == "ST":
                    stat_bonus2 = sttb
                elif stats[1] == "QU":
                    stat_bonus2 = qutb
                elif stats[1] == "PR":
                    stat_bonus2 = prtb
                elif stats[1] == "IN":
                    stat_bonus2 = intb
                elif stats[1] == "EM":
                    stat_bonus2 = emtb
                elif stats[1] == "CO":
                    stat_bonus2 = cotb
                elif stats[1] == "AG":
                    stat_bonus2 = agtb
                elif stats[1] == "SD":
                    stat_bonus2 = sdtb
                elif stats[1] == "ME":
                    stat_bonus2 = metb
                elif stats[1] == "RE":
                    stat_bonus2 = retb
                stat_bonus = (stat_bonus1 + stat_bonus2)/2
                char_dict[words][11] = cfgData.iround(stat_bonus)
            elif len(stat)==8:
                stats=stat.split('/')
                # Stat 1
                if stats[0] == "ST":
                    stat_bonus1 = sttb
                elif stats[0] == "QU":
                    stat_bonus1 = qutb
                elif stats[0] == "PR":
                    stat_bonus1 = prtb
                elif stats[0] == "IN":
                    stat_bonus1 = intb
                elif stats[0] == "EM":
                    stat_bonus1 = emtb
                elif stats[0] == "CO":
                    stat_bonus1 = cotb
                elif stats[0] == "AG":
                    stat_bonus1 = agtb
                elif stats[0] == "SD":
                    stat_bonus1 = sdtb
                elif stats[0] == "ME":
                    stat_bonus1 = metb
                elif stats[0] == "RE":
                    stat_bonus1 = retb
                # Stat 2
                if stats[1] == "ST":
                    stat_bonus2 = sttb
                elif stats[1] == "QU":
                    stat_bonus2 = qutb
                elif stats[1] == "PR":
                    stat_bonus2 = prtb
                elif stats[1] == "IN":
                    stat_bonus2 = intb
                elif stats[1] == "EM":
                    stat_bonus2 = emtb
                elif stats[1] == "CO":
                    stat_bonus2 = cotb
                elif stats[1] == "AG":
                    stat_bonus2 = agtb
                elif stats[1] == "SD":
                    stat_bonus2 = sdtb
                elif stats[1] == "ME":
                    stat_bonus2 = metb
                elif stats[1] == "RE":
                    stat_bonus2 = retb
                # Stat 3
                if stats[2] == "ST":
                    stat_bonus3 = sttb
                elif stats[2] == "QU":
                    stat_bonus3 = qutb
                elif stats[2] == "PR":
                    stat_bonus3 = prtb
                elif stats[2] == "IN":
                    stat_bonus3 = intb
                elif stats[2] == "EM":
                    stat_bonus3 = emtb
                elif stats[2] == "CO":
                    stat_bonus3 = cotb
                elif stats[2] == "AG":
                    stat_bonus3 = agtb
                elif stats[2] == "SD":
                    stat_bonus3 = sdtb
                elif stats[2] == "ME":
                    stat_bonus3 = metb
                elif stats[2] == "RE":
                    stat_bonus3 = retb
                stat_bonus = (stat_bonus1 + stat_bonus2 + stat_bonus3)/3

            # Update dictionary
            char_dict[words][11] = cfgData.iround(stat_bonus)

            # Calcalute skill bonus
            skill_rank_total = char_dict[words][5] + char_dict[words][6] + char_dict[words][7] + char_dict[words][8]

            if char_dict[words][0] == 'Maneuvering in Soft Leather':
                skill_bonus = skill_rank_total * 5
            elif char_dict[words][0] == 'Maneuvering in Rigid Leather':
                skill_bonus = skill_rank_total * 5
            elif char_dict[words][0] == 'Maneuvering in Chain':
                skill_bonus = skill_rank_total * 5
            elif char_dict[words][0] == 'Maneuvering in Plate':
                skill_bonus = skill_rank_total * 5
            elif skill_rank_total <= 10:
                skill_bonus = skill_rank_total * 5
            elif skill_rank_total >=11 and skill_rank_total <= 20:
                skill_bonus = 50 + ((skill_rank_total-10) * 2)
            elif skill_rank_total >= 21 and skill_rank_total <= 30:
                skill_bonus = 70 + ((skill_rank_total-20) * 1)
            else:
                skill_bonus = 80 + ((skill_rank_total-30) * 0.5)
            # Update dictionary
            char_dict[words][10] = cfgData.iround(skill_bonus)

            # Calcalute Total Skill Bonus
            total_skill_bonus = char_dict[words][10] + char_dict[words][11] + char_dict[words][12] + char_dict[words][13]
            # Update dictionary
            char_dict[words][14] = total_skill_bonus
        # Write Character data to file
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", "w") as f:
            f.write(json.dumps(char_dict))

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

    if char_dict['lvl']==0:
        lvl="AD"
    elif char_dict['lvl']==0.5:
        lvl="AP"
    else:
        lvl=char_dict['lvl']

    cfgData.clear_screen()
    print
    print "*", 93 * "-","*"
    print "| Name: {:<23} Level: {:2}{:13}Race: {:20}{:16}|".format(char_dict['FullName'].title(),lvl,"",char_dict['race'],"")
    print "| Profession: {:<18}Exp: {:<8}{:5}Next Level: {:<33} |".format(char_dict['pro_name'].title(),char_dict['exp'],"",char_dict['next_lvl'])
    print "| Sex: {:<7}{:10}Age: {:<4}{:63}|".format(char_dict['gender'].title(),"",char_dict['age'],"")
    print "| Height: {:<7}{:4}Weight: {:<4}{:63}|".format(char_dict['height']," ",char_dict['weight'],"")
    print "| Hair: {:<8}{:7}Eyes: {:<8}{:59}|".format(char_dict['hair'],"",char_dict['eye'],"")
    print "*", 93 * "-","*"
    print "|                                          Stats                                                |"
    print "*", 93 * "-","*"
    print "|                             |         |           |  Stat |  Race | Dev | PP  | Misc  | Total |"
    print "|                             | Current |   Pot'l   | Bonus | Bonus | Pts | Pts | Bonus | Bonus |"
    print "*", 93 * "-","*"
    print "| Strength (ST)               |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['st_stat'],char_dict['st_pot'],stb,raceb[1],stdp,stpp,char_dict['stmb'],sttb)
    print "| Quickness (QU)              |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['qu_stat'],char_dict['qu_pot'],qub,raceb[2],qudp,qupp,char_dict['qumb'],qutb)
    print "| Presence (PR)               |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['pr_stat'],char_dict['pr_pot'],prb,raceb[3],prdp,prpp,char_dict['prmb'],prtb)
    print "| Intuition (IN)              |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['in_stat'],char_dict['in_pot'],inb,raceb[4],indp,inpp,char_dict['inmb'],intb)
    print "| Empathy (EM)                |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['em_stat'],char_dict['em_pot'],emb,raceb[5],emdp,empp,char_dict['emmb'],emtb)
    print "| Constitution (CO)           |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['co_stat'],char_dict['co_pot'],cob,raceb[6],codp,copp,char_dict['comb'],cotb)
    print "| Agility (AG)                |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['ag_stat'],char_dict['ag_pot'],agb,raceb[7],agdp,agpp,char_dict['agmb'],agtb)
    print "| Self Discipline (SD)        |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['sd_stat'],char_dict['sd_pot'],sdb,raceb[8],sddp,sdpp,char_dict['sdmb'],sdtb)
    print "| Memory (ME)                 |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['me_stat'],char_dict['me_pot'],meb,raceb[9],medp,mepp,char_dict['memb'],metb)
    print "| Reasoning (RE)              |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['re_stat'],char_dict['re_pot'],reb,raceb[10],redp,repp,char_dict['remb'],retb)
    print "*", 93 * "-","*"
    print "| Development/Power Points:{:41}| {:^4}| {:^4}|               |".format(" ",tdp,tpp)
    print "*", 93 * "-","*"
    print "| {:32} | Hobby | AD  | AP  |     | Skill| Stat |Level| Misc | Total |".format(" ")
    print "| {:32} | Ranks |Ranks|Ranks|Ranks| Bonus| Bonus|Bonus| Bonus| Bonus |".format("Skill Name")
    print "*", 93 * "-","*"
    sklist=[]
    for words in char_dict:
        if words.isdigit():
            if char_dict[words][5]>0 or char_dict[words][6]>0 or char_dict[words][7]>0 or char_dict[words][8]>0:
                print "| {:32} | {:^5} |{:^5}|{:^5}|{:^5}|{:^6}|{:^6}|{:^5}|{:^6}|{:^7}|".format(char_dict[words][0],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][13],char_dict[words][12],char_dict[words][14])
    print "*", 93 * "-","*"
    print
    print

def all_skill_list():
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
    print
    print "*", 93 * "-","*"
    print "| {:32} | Hobby | AD  | AP  |     | Skill| Stat |Level| Misc | Total |".format(" ")
    print "| {:32} | Ranks |Ranks|Ranks|Ranks| Bonus| Bonus|Bonus| Bonus| Bonus |".format("Skill Name")
    print "*", 93 * "-","*"
    sklist=[]
    for words in char_dict:
        if words.isdigit():
            index=words
            sklist.append([char_dict[words][0],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][13],char_dict[words][12],char_dict[words][14],index])
            sklst=sorted(sklist, key=lambda skill: skill[0])
    for y in sklst:
        print "| {:32} | {:^5} |{:^5}|{:^5}|{:^5}|{:^6}|{:^6}|{:^5}|{:^6}|{:^7}|".format(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9])
    print "*", 93 * "-","*"

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

def mbset(stat):
    x=1
    while x==1:
        try:
            mbi=int(raw_input("Bonus: "))
            if mbi<0 or mbi > 30:
                print "Enter a number between 1 and 30"
            else:
                x=0
        except:
            print "Enter a number"
    return mbi

def mbbonus():
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

    stat_name=[
        ["Strength", "stmb","stb","strb","sttb"],
        ["Quickness", "qumb","qub","qurb","qutb"],
        ["Presence", "prmb","prb","prrb","prtb"],
        ["Intuition", "inmb","inb","inrb","intb"],
        ["Empathy", "emmb","emb","emrb","emtb"],
        ["Constitution", "comb","cob","corb","cotb"],
        ["Agility", "agmb","agb","agrb","agtb"], ["Self Discipline", "sdmb","sdb","sdrb","sdtb"],
        ["Memory", "memb","meb","merb","metb"], ["Reasoning", "remb","reb","rerb","retb"]
    ]
    mb=""

    cfgData.clear_screen()
    mbloop=True
    while mbloop:
        cnt,menu=1,0
        print ""
        print "+", 47 * "=", "+"
        while cnt <= len(stat_name):
            print "|  {:>2}.) {:9}({:2})   {:>2}.) {:16}({:2}) |".format(cnt,stat_name[menu][0],char_dict[stat_name[menu][1]],cnt+1,stat_name[menu+1][0],char_dict[stat_name[menu+1][1]])
            cnt+=2
            menu+=2
        print "|", 47 * " ","|"
        print "|  {:>2}.) {:42}|".format("X","Exit")
        print "+", 47 * "=", "+"
        print ""
        le=1
        while le==1:
            try:
                mbch=raw_input("Select a stat to increase: ")
                if re.match("^[1-9xX]$",mbch):
                    le=0
                elif re.match("^10$",mbch):
                    le=0
                else:
                    print "Enter a number between 1 and 10!"
            except:
                print "Enter a number or X to exit"

            # Run Misc Bonus function
            if mbch.upper() == "X":
                le=0
                mbloop=False
            else:
                j=int(mbch)
                if 0<j<11:
                    mb=mbset(stat_name[int(mbch)-1][1])
                    stat_total_bonus = int(char_dict[stat_name[int(mbch)-1][1]]) + int(char_dict[stat_name[int(mbch)-1][2]]) + int(char_dict[stat_name[int(mbch)-1][3]])
                    char_dict[stat_name[int(mbch)-1][1]]=mb
                    char_dict[stat_name[int(mbch)-1][4]]=stat_total_bonus

        # Open character file to write out data
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", 'w') as f:
            f.write(json.dumps(char_dict))
    # End of Misc Bonus function

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

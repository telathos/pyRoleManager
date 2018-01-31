import cfgData
import charMenu
import json
import os
import skill_math


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
                char_dict[`index`]=(skills[cl].split(',')[1],skills[cl].split(',')[5],skills[cl].split(',')[7],skills[cl].split(',')[col],skills[cl].split(',')[6],0,0,0,0)
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
    with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as cf:
        char_dict = json.load(cf)

    # Open Armor Type file
    with open(cfgData.cfg_dir+"/at.csv","r") as atl:
        atlist = atl.read().splitlines()

    print 85 * "="
    print "|    |                                     | Minimum  | Maximum  | Missile|          |"
    print "|    |                                     | Maneuver | Maneuver | Attack | Quickness|"
    print "| AT | Description                         |   Mod.   |   Mod.   | Penalty| Penalty  |"
    print 85 * "-"
    for a in range(1,21,1):
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
            atloop=False

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

    skill_math.skill_totals(char,"hi")

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
    print ""
    print " ",86 * "-"," "
    print "/",86 * " ","\\"
    print "| Name: {:<23} Level: {:2}{:13}Race: {:12}{:17}|".format(char_dict['FullName'].title(),lvl,"",char_dict['race'],"")
    print "| Profession: {:<18}Exp: {:<8}{:5}Next Level: {:26} |".format(char_dict['pro_name'].title(),char_dict['exp'],"","")
    print "| Sex: {:<7}{:10}Age: {:<4}{:53}|".format(char_dict['race'].title(),"",char_dict['age'],"")
    print "| Height: {:<7}{:4}Weight: {:<4}{:56}|".format(char_dict['height']," ",char_dict['weight'],"")
    print "| Hair: {:<8}{:7}Eyes: {:<8}{:52}|".format(char_dict['hair'],"",char_dict['eye'],"")
    print "*", 86 * "-","*"
    print "|                                   Stats                                                |"
    print "*", 86 * "-","*"
    print "|                      |         |           |  Stat |  Race | Dev | PP  | Misc  | Total |"
    print "|                      | Current |   Pot'l   | Bonus | Bonus | Pts | Pts | Bonus | Bonus |"
    print "*", 86 * "-","*"
    print "| Strength (ST)        |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['st_stat'],char_dict['st_pot'],stb,raceb[1],stdp,stpp,char_dict['stmb'],sttb)
    print "| Quickness (QU)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['qu_stat'],char_dict['qu_pot'],qub,raceb[2],qudp,qupp,char_dict['qumb'],qutb)
    print "| Presence (PR)        |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['pr_stat'],char_dict['pr_pot'],prb,raceb[3],prdp,prpp,char_dict['prmb'],prtb)
    print "| Intuition (IN)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['in_stat'],char_dict['in_pot'],inb,raceb[4],indp,inpp,char_dict['inmb'],intb)
    print "| Empathy (EM)         |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['em_stat'],char_dict['em_pot'],emb,raceb[5],emdp,empp,char_dict['emmb'],emtb)
    print "| Constitution (CO)    |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['co_stat'],char_dict['co_pot'],cob,raceb[6],codp,copp,char_dict['comb'],cotb)
    print "| Agility (AG)         |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['ag_stat'],char_dict['ag_pot'],agb,raceb[7],agdp,agpp,char_dict['agmb'],agtb)
    print "| Self Discipline (SD) |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['sd_stat'],char_dict['sd_pot'],sdb,raceb[8],sddp,sdpp,char_dict['sdmb'],sdtb)
    print "| Memory (ME)          |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['me_stat'],char_dict['me_pot'],meb,raceb[9],medp,mepp,char_dict['memb'],metb)
    print "| Reasoning (RE)       |{:^9}|{:^11}|{:^7}|{:^7}|{:^5}|{:^5}|{:^7}|{:^7}|".format(char_dict['re_stat'],char_dict['re_pot'],reb,raceb[10],redp,repp,char_dict['remb'],retb)
    print "*", 86 * "-","*"
    print "| Development/Power Points:                                  | {:^4}| {:^4}|               |".format(tdp,tpp)
    print "*", 86 * "-","*"
    print
    print 96 * "-"
    print "| {:32} | Hobby | AD  | AP  |     | Skill| Stat |Level| Misc | Total |".format(" ")
    print "| {:32} | Ranks |Ranks|Ranks|Ranks| Bonus| Bonus|Bonus| Bonus| Bonus |".format("Skill Name")
    print 96 * "-"
    sklist=[]
    for words in char_dict:
        if words.isdigit():
            if char_dict[words][5]>0 or char_dict[words][6]>0 or char_dict[words][7]>0 or char_dict[words][8]>0:
                print "| {:32} | {:^5} |{:^5}|{:^5}|{:^5}|{:^6}|{:^6}|{:^5}|{:^6}|{:^7}|".format(char_dict[words][0],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][13],char_dict[words][12],char_dict[words][14])
    print 96 * "-"
    print
    print

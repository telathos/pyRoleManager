import cfgData

# Setup character data list
char_dict={}

# Read Professions into List
plist = {}
rlist = {}
pi,ri=1,1
with open(cfgData.cfg_dir+"/profession.csv") as pf:
    for pline in pf:
        plist[pi]=pline.rstrip('\n').split(",")
        pi+=1
with open(cfgData.cfg_dir+"/race.csv") as rf:
    for rline in rf:
        rlist[ri]=rline.rstrip('\n').split(",")
        ri+=1

st_pot_in,qu_pot_in,pr_pot_in,in_pot_in,em_pot_in=0,0,0,0,0
co_pot_in,ag_pot_in,sd_pot_in,me_pot_in,re_pot_in=0,0,0,0,0

# Start of the basic character creation, Name, Profession, Race and Stats
def create_char():
    '''
    user_name=str(raw_input('Please enter your first name: '))
    last_name = str(raw_input('Pleae enter last name: '))
    char_path=cfgData.char_dir+"/"+user_name
    fullName = user_name +" "+ last_name
    char_dict['FullName'] = fullName
    if not os.path.exists(char_path):
        os.makedirs(char_path)
    if os.path.exists(char_path+"/"+user_name+".json") == True:
        print "Character exists"
        sys.exit()
    else:
        # Write character name to list
        char_dict['name']=user_name
    '''
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
    print ""

    # Race Selection
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
                #print "Matched"
                stat_temp_list.append([statlist[u][0],statlist[u][1],x1[1],x1[2],x1[3]])
        #print stat_temp_list
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
        cnt=1
        try:
            r=int(raw_input("Enter Stat to remove:"))
            if r<1 or r>12:
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

    # Clear screen
    cfgData.clear_screen()
    # Redraw table
    cnt=1
    print "+", 48 * "=", "+"
    print "|{:5}| {:7} | {:9} | {:5} | {:4} | {:5} |".format("","","","Stat","Dev","Power")
    print "|{:5}| {:6} | {:9} | {:5} | {:4} | {:5} |".format("","Current","Potential","Bonus","Pts","Pts")
    print "+", 48 * "=", "+"
    while cnt<=len(stat_temp_list):
        print "| {:>2}.) | {:^6} | {:^9} | {:^5} | {:4} | {:^5} |".format(cnt,stat_temp_list[cnt-1][0],stat_temp_list[cnt-1][1],stat_temp_list[cnt-1][2],stat_temp_list[cnt-1][3],stat_temp_list[cnt-1][4])
        cnt+=1
    print "+", 48 * "=", "+"

    # Strength
    stat_error="You must enter a number between 1 and 100.."
    st_stat_input=""
    while st_stat_input<1 or st_stat_input>100:
        try:
            st_stat_input=int(raw_input('Strength: '))
        except:
            print stat_error
    st_stat=cfgData.prime_req(pro_ch,"st",st_stat_input)

    # Quickness
    qu_stat_input=""
    while qu_stat_input<1 or qu_stat_input>100:
        try:
            qu_stat_input=int(raw_input('Quickness: '))
        except:
            print stat_error
    qu_stat=cfgData.prime_req(pro_ch,"qu",qu_stat_input)

    #Presence
    pr_stat_input=""
    while pr_stat_input<1 or pr_stat_input>100:
        try:
            pr_stat_input=int(raw_input('Presence: '))
        except:
            print stat_error
    pr_stat=cfgData.prime_req(pro_ch,"pr",pr_stat_input)

    # Intuition
    in_stat_input=""
    while in_stat_input<1 or in_stat_input>100:
        try:
            in_stat_input=int(raw_input('Intuition: '))
        except:
            print stat_error
    in_stat=cfgData.prime_req(pro_ch,"in",in_stat_input)

    # Essence
    em_stat_input=""
    try:
        em_stat_input=int(raw_input('Empathy: '))
    except:
        print stat_error
    em_stat=cfgData.prime_req(pro_ch,"em",em_stat_input)

    # Constitution
    co_stat_input=""
    while co_stat_input<1 or co_stat_input>100:
        try:
            co_stat_input=int(raw_input('Constitution: '))
        except:
            print stat_error
    co_stat=cfgData.prime_req(pro_ch,"co",co_stat_input)

    # Agility
    ag_stat_input=""
    while ag_stat_input<1 or ag_stat_input>100:
        try:
            ag_stat_input=int(raw_input('Agility: '))
        except:
            print stat_error
    ag_stat=cfgData.prime_req(pro_ch,"ag",ag_stat_input)

    # Self-Discipline
    sd_stat_input=""
    while sd_stat_input<1 or sd_stat_input>100:
        try:
            sd_stat_input=int(raw_input('Self-Discipline: '))
        except:
            print stat_error
    sd_stat=cfgData.prime_req(pro_ch,"sd",sd_stat_input)

    # Memory
    me_stat_input=""
    while me_stat_input<1 or me_stat_input>100:
        try:
            me_stat_input=int(raw_input('Memory: '))
        except:
            print stat_error
    me_stat=cfgData.prime_req(pro_ch,"me",me_stat_input)

    # Reasoning
    re_stat_input=""
    while re_stat_input<1 or re_stat_input>100:
        try:
            re_stat_input=int(raw_input('Reasoning: '))
        except:
            print stat_error
    re_stat=cfgData.prime_req(pro_ch,"re",re_stat_input)

    ### Calculate Potential Value using pot_calc function
    # Strength
    st_pot_in=""
    while st_pot_in<1 or st_pot_in>100:
        try:
            st_pot_in=int(raw_input('Potential Roll (ST): '))
        except:
            print stat_error
    st_pot=cfgData.pot_calc(st_stat,st_pot_in)

    # Quickness
    qu_pot_in=""
    while qu_pot_in<1 or qu_pot_in>100:
        try:
            qu_pot_in=int(raw_input('Potential Roll (QU): '))
        except:
            print stat_error
    qu_pot=cfgData.pot_calc(qu_stat,qu_pot_in)

    # Presence
    pr_pot_in=""
    while pr_pot_in<1 or pr_pot_in>100:
        try:
            pr_pot_in=int(raw_input('Potential Roll (PR): '))
        except:
            print stat_error
    pr_pot=cfgData.pot_calc(pr_stat,pr_pot_in)

    # Intuition
    in_pot_in=""
    while in_pot_in<1 or in_pot_in>100:
        try:
            in_pot_in=int(raw_input('Potential Roll (IN): '))
        except:
            print stat_error
    in_pot=cfgData.pot_calc(in_stat,in_pot_in)

    # Essence
    em_pot_in=""
    while em_pot_in<1 or em_pot_in>100:
        try:
            em_pot_in=int(raw_input('Potential Roll (EM): '))
        except:
            print stat_error
    em_pot=cfgData.pot_calc(em_stat,em_pot_in)

    # Constitution
    co_pot_in=""
    while co_pot_in<1 or co_pot_in>100:
        try:
            co_pot_in=int(raw_input('Potential Roll (CO): '))
        except:
            print stat_error
    co_pot=cfgData.pot_calc(co_stat,co_pot_in)

    # Agility
    ag_pot_in=""
    while ag_pot_in<1 or ag_pot_in>100:
        try:
            ag_pot_in=int(raw_input('Potential Roll (AG): '))
        except:
            print stat_error
    ag_pot=cfgData.pot_calc(ag_stat,ag_pot_in)

    # Self-Discipline
    sd_pot_in=""
    while sd_pot_in<1 or sd_pot_in>100:
        try:
            sd_pot_in=int(raw_input('Potential Roll (SD): '))
        except:
            print stat_error
    sd_pot=cfgData.pot_calc(sd_stat,sd_pot_in)

    # Memory
    me_pot_in=""
    while me_pot_in<1 or me_pot_in>100:
        try:
            me_pot_in=int(raw_input('Potential Roll (ME): '))
        except:
            print stat_error
    me_pot=cfgData.pot_calc(me_stat,me_pot_in)

    # Reasoning
    re_pot_in=""
    while re_pot_in<1 or re_pot_in>100:
        try:
            re_pot_in=int(raw_input('Potential Roll (RE): '))
        except:
            print stat_error
    re_pot=cfgData.pot_calc(re_stat,re_pot_in)

    print 10 * "-"
    print
    print 20 * "="
    print "| Gender"
    print "|"
    x,s=0,1
    while x<len(cfgData.sexlist):
        print "|{:<2}.) {:10}".format(s,cfgData.sexlist[x])
        x+=1
        s+=1
    print 20 * "="
    print "| Hair Color"
    print "|"
    x,s=0,1
    while x<len(cfgData.hairlist):
        print "|{:<2}.) {:10}".format(s,cfgData.hairlist[x])
        x+=1
        s+=1
    print 20 * "="
    print "| Eye Color"
    print "|"
    x,s=0,1
    while x<len(cfgData.eyelist):
        print "|{:<2}.) {:10}".format(s,cfgData.eyelist[x])
        x+=1
        s+=1
    print 20 * "="

    # Enter characters gender
    sexch=""
    while sexch<1 or sexch>len(cfgData.sexlist):
        try:
            sexch = int(raw_input("Select Sex: "))
        except:
            print "Enter a number between 1 and {:2}..".format(len(cfgData.sexlist))
    sex = cfgData.sexlist[sexch-1]
    char_dict['gender'] = sex

    # Enter hair color
    hairch=""
    while hairch<1 or hairch>len(cfgData.hairlist):
        try:
            hairch = int(raw_input("Select Hair color: "))
        except:
            print "Enter a number between 1 and {:2}..".format(len(cfgData.hairlist))
    hair = cfgData.hairlist[hairch-1]
    char_dict['hair'] = hair

    # Enter eye color
    eyech=""
    while eyech<1 or eyech>len(cfgData.eyelist):
        try:
            eyech = int(raw_input("Select Eye color: "))
        except:
            print "Enter a number between 1 and {:2}..".format(len(cfgData.eyelist))
    eye = cfgData.eyelist[eyech-1]
    char_dict['eye'] = eye

    # Enter characters age
    age=""
    while age=="":
        try:
            age = int(raw_input("Character's Age: "))
        except:
            print "You must enter a number.."
    char_dict['age'] = age
    print

    ht = str(raw_input("Enter Height: "))

    # Enter weight
    wt=""
    while wt<1 or wt>1000:
        try:
            wt = int(raw_input("Enter Weight: "))
        except:
            print "Enter a number between 1 and 1000.."
    char_dict['height'],char_dict['weight'] = ht,wt

    # Load data into dictionary for saving of the character
    char_dict['st_stat'],char_dict['st_pot']=st_stat,st_pot
    char_dict['qu_stat'],char_dict['qu_pot']=qu_stat,qu_pot
    char_dict['pr_stat'],char_dict['pr_pot']=pr_stat,pr_pot
    char_dict['in_stat'],char_dict['in_pot']=in_stat,in_pot
    char_dict['em_stat'],char_dict['em_pot']=em_stat,em_pot
    char_dict['co_stat'],char_dict['co_pot']=co_stat,co_pot
    char_dict['ag_stat'],char_dict['ag_pot']=ag_stat,ag_pot
    char_dict['sd_stat'],char_dict['sd_pot']=sd_stat,sd_pot
    char_dict['me_stat'],char_dict['me_pot']=me_stat,me_pot
    char_dict['re_stat'],char_dict['re_pot']=re_stat,re_pot
    char_dict['lvl']=0
    char_dict['realm']=plist[pro_ch][8]
    char_dict['stmb'],char_dict['qumb'],char_dict['emmb'],char_dict['inmb'],char_dict['prmb']=0,0,0,0,0
    char_dict['comb'],char_dict['agmb'],char_dict['sdmb'],char_dict['remb'],char_dict['memb']=0,0,0,0,0
    hp_math=Decimal(char_dict['co_stat'])/Decimal(10)
    hp=Decimal(hp_math).quantize(Decimal('1e-3'))
    char_dict['hp_base']=int(round(hp,0))

    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    f.close()
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
    rc=[]

    for x in racechart:
        rc.append(x.split(","))

    f=0
    while f < len(racechart):
        x3 = racechart[f].split(',')
        f+=1
        if x3[0] == char_dict['race']:
            essModBase = x3[11]
            chanModBase = x3[12]
            mentModBase = x3[13]
            poiModBase = x3[14]
            disModBase = x3[15]
            HitDie = x3[17]
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
    tdp=(float(codp)+float(agdp)+float(sddp)+float(medp)+float(redp))*float(cfgData.dp_multipler)
    char_dict['dp']=round(tdp,1)
    dp_math=Decimal(char_dict['dp'])
    dp=Decimal(dp_math).quantize(Decimal('1e-3'))
    char_dict['tempdp'] = int(round(dp,0))

    # Add Total Bonus of skills to character data
    char_dict['sttb']=sttb
    char_dict['qutb']=qutb
    char_dict['prtb']=prtb
    char_dict['intb']=intb
    char_dict['emtb']=emtb
    char_dict['cotb']=cotb
    char_dict['agtb']=agtb
    char_dict['sdtb']=sdtb
    char_dict['metb']=metb
    char_dict['retb']=retb

    # Set Resistance Roll Modifiers
    char_dict['essmod'] = int(essModBase)+int(emtb)
    char_dict['chanmod'] = int(chanModBase)+int(intb)
    char_dict['mentmod'] = int(mentModBase)+int(prtb)
    char_dict['poimod'] = int(poiModBase)+int(cotb)
    char_dict['dismod'] = int(disModBase)+int(cotb)
    char_dict['hitdie'] = HitDie

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

    # Open skill list file and write to character skill file. Set number of ranks for Hobby, AD, AP,
    # normal to 0
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    skill_list=[]
    for list in sl:
        skill_list.append(list.split(","))
        crt=1
        for outer_list in skill_list:
            index=int(plist[pro_ch][1])

            # Set Spell Lists and Spell Mastery based on realm
            if outer_list[1].startswith("Spell"):
                if char_dict['realm'] == "EM":
                    outer_list[5]="EM"
                elif char_dict['realm'] == "PR":
                    outer_list[5]="PR"
                elif char_dict['realm'] == "IN":
                    outer_list[5]=="IN"
                elif char_dict['realm'] == "IP":
                    outer_list[5]=="IN/PR"
                elif char_dict['realm'] == "PE":
                    outer_list[5]=="PR/EM"
                elif char_dict['realm'] == "IE":
                    outer_list[5]=="IN/EM"
                elif char_dict['realm'] == "AR":
                    outer_list[5]=="IN/PR/EM"
                elif char_dict['realm'] == "NULL":
                    outer_list[5]=="NA"
            char_dict[crt]=(outer_list[1],outer_list[5],outer_list[7],outer_list[index],outer_list[6],0,0,0,0,0,0,0,0,0,0)
            crt+=1

    # Write Character data to file
    with open(char_path+'/'+user_name+'.json', 'w') as f:
        f.write(json.dumps(char_dict))

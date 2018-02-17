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

# Update character records if a new skill is added
charData.new_skill_check()

# Setup character data list
char={}

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
    print "7. Add experience to character"
    print "8. Raise Character Level"
    print "9. Export Character to Excel"
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

st_pot_in,qu_pot_in,pr_pot_in,in_pot_in,em_pot_in=0,0,0,0,0
co_pot_in,ag_pot_in,sd_pot_in,me_pot_in,re_pot_in=0,0,0,0,0

# Start of the basic character creation, Name, Profession, Race and Stats
def create_char():
    user_name=str(raw_input('Please enter your first name: '))
    last_name = str(raw_input('Pleae enter last name: '))
    char_path=cfgData.char_dir+"/"+user_name
    fullName = user_name +" "+ last_name
    char['FullName'] = fullName
    if not os.path.exists(char_path):
        os.makedirs(char_path)
    if os.path.exists(char_path+"/"+user_name+".json") == True:
        print "Character exists"
        sys.exit()
    else:
        # Write character name to list
        char['name']=user_name

    # Set base Experience
    char['exp'] = 10000

    print 25 * "-" , "Professions", 25 * "-"
    print ""
    print 15 * "-" , "Non" , 15 * "-"
    print "1.) {:20} 2.) {:19}".format(plist[1][0],plist[2][0])
    print "3.) {:20} 4.) {:19}".format(plist[3][0],plist[4][0])
    print "5.) {:20} 6.) {:19}".format(plist[5][0],plist[6][0])
    print "7.) {:20} 8.) {:19}".format(plist[7][0],plist[8][0])
    print "9.) {:20} 10.) {:19}".format(plist[9][0],plist[10][0])
    print "11.) {:19} 12.) {:19}".format(plist[11][0],plist[12][0])
    print "13.) {:19}".format(plist[13][0])
    print ""
    print 15 * "-", "Pure", 15 * "-"
    print "14.) {:19} 15.) {:19}".format(plist[14][0],plist[15][0])
    print "16.) {:19} 17.) {:19}".format(plist[16][0],plist[17][0])
    print "18.) {:19} 19.) {:19}".format(plist[18][0],plist[19][0])
    print "20.) {:19} 21.) {:19}".format(plist[20][0],plist[21][0])
    print "22.) {:19} 23.) {:19}".format(plist[22][0],plist[23][0])
    print "24.) {:19} 25.) {:19}".format(plist[24][0],plist[25][0])
    print "26.) {:19} 27.) {:19}".format(plist[26][0],plist[27][0])
    print ""
    print 15 * "-", "Semi", 15 * "-"
    print "28.) {:19} 29.) {:19}".format(plist[28][0],plist[29][0])
    print "30.) {:19} 31.) {:19}".format(plist[30][0],plist[31][0])
    print "32.) {:19} 33.) {:19}".format(plist[32][0],plist[33][0])
    print "34.) {:19} 35.) {:19}".format(plist[34][0],plist[35][0])
    print "36.) {:19} 37.) {:19}".format(plist[36][0],plist[37][0])
    print "38.) {:19} 39.) {:19}".format(plist[38][0],plist[39][0])
    print ""
    print 15 * "-", "Hybrid", 15 * "-"
    print "40.) {:19} 41.) {:19}".format(plist[40][0],plist[41][0])
    print "42.) {:19} 43.) {:19}".format(plist[42][0],plist[43][0])
    print "44.) {:19} 45.) {:19}".format(plist[44][0],plist[45][0])
    print "46.) {:19} 47.) {:19}".format(plist[46][0],plist[47][0])
    print "48.) {:19}".format(plist[48][0])
    print 63 * "-"
    pro_ch=int(raw_input('Select Profession: '))
    if pro_ch==1:
        pro_name=plist[pro_ch][0]
    elif pro_ch==2:
        pro_name=plist[pro_ch][0]
    elif pro_ch==3:
        pro_name=plist[pro_ch][0]
    elif pro_ch==4:
        pro_name=plist[pro_ch][0]
    elif pro_ch==5:
        pro_name=plist[pro_ch][0]
    elif pro_ch==6:
        pro_name=plist[pro_ch][0]
    elif pro_ch==7:
        pro_name=plist[pro_ch][0]
    elif pro_ch==8:
        pro_name=plist[pro_ch][0]
    elif pro_ch==9:
        pro_name=plist[pro_ch][0]
    elif pro_ch==10:
        pro_name=plist[pro_ch][0]
    elif pro_ch==11:
        pro_name=plist[pro_ch][0]
    elif pro_ch==12:
        pro_name=plist[pro_ch][0]
    elif pro_ch==13:
        pro_name=plist[pro_ch][0]
    elif pro_ch==14:
        pro_name=plist[pro_ch][0]
    elif pro_ch==15:
        pro_name=plist[pro_ch][0]
    elif pro_ch==16:
        pro_name=plist[pro_ch][0]
    elif pro_ch==17:
        pro_name=plist[pro_ch][0]
    elif pro_ch==18:
        pro_name=plist[pro_ch][0]
    elif pro_ch==19:
        pro_name=plist[pro_ch][0]
    elif pro_ch==20:
        pro_name=plist[pro_ch][0]
    elif pro_ch==21:
        pro_name=plist[pro_ch][0]
    elif pro_ch==22:
        pro_name=plist[pro_ch][0]
    elif pro_ch==23:
        pro_name=plist[pro_ch][0]
    elif pro_ch==24:
        pro_name=plist[pro_ch][0]
    elif pro_ch==25:
        pro_name=plist[pro_ch][0]
    elif pro_ch==26:
        pro_name=plist[pro_ch][0]
    elif pro_ch==27:
        pro_name=plist[pro_ch][0]
    elif pro_ch==28:
        pro_name=plist[pro_ch][0]
    elif pro_ch==29:
        pro_name=plist[pro_ch][0]
    elif pro_ch==30:
        pro_name=plist[pro_ch][0]
    elif pro_ch==31:
        pro_name=plist[pro_ch][0]
    elif pro_ch==32:
        pro_name=plist[pro_ch][0]
    elif pro_ch==33:
        pro_name=plist[pro_ch][0]
    elif pro_ch==34:
        pro_name=plist[pro_ch][0]
    elif pro_ch==35:
        pro_name=plist[pro_ch][0]
    elif pro_ch==36:
        pro_name=plist[pro_ch][0]
    elif pro_ch==37:
        pro_name=plist[pro_ch][0]
    elif pro_ch==38:
        pro_name=plist[pro_ch][0]
    elif pro_ch==39:
        pro_name=plist[pro_ch][0]
    elif pro_ch==40:
        pro_name=plist[pro_ch][0]
    elif pro_ch==41:
        pro_name=plist[pro_ch][0]
    elif pro_ch==42:
        pro_name=plist[pro_ch][0]
    elif pro_ch==43:
        pro_name=plist[pro_ch][0]
    elif pro_ch==44:
        pro_name=plist[pro_ch][0]
    elif pro_ch==45:
        pro_name=plist[pro_ch][0]
    elif pro_ch==46:
        pro_name=plist[pro_ch][0]
    elif pro_ch==47:
        pro_name=plist[pro_ch][0]
    elif pro_ch==48:
        pro_name=plist[pro_ch][0]

    # write Profession to list
    char['pro_name']=pro_name
    print 10 * "-"

    # Select Race
    print ""
    print 10 * "-", "Race", 10 * "-"
    print ""
    print "1. Common Man"
    print "2. Wood Elf      3. High Elf      4. Half-elf"
    print "5. Grey Elf      6. Aquatic Elf   7. Dark Elf"
    print ""
    print "8. Tallfellow Halfling      9. Stout Halfling"
    print ""
    print "10. Dwarf        11. Half-Dwarf"
    print "12. Half-Orc   13. Half-Ogre    14. Half-Troll"
    print ""
    print "15. Gnomes     16. Hira'razhir (Avians)"
    print "17. Idiyva (Felines)   18. Vulfen (Wolfmen)"
    print "19. Sstoi'isslythi (Reptilies)"
    print 25 * "-"

    race_input=int(raw_input('Select a Race: '))
    if race_input==1:
        char['race']="Common Man"
    elif race_input==2:
        char['race']="Wood Elf"
    elif race_input==3:
        char['race']="High Elf"
    elif race_input==4:
        char['race']="Half-elf"
    elif race_input==5:
        char['race']="Grey Elf"
    elif race_input==6:
        char['race']="Aquatic Elf"
    elif race_input==7:
        char['race']="Dark Elf"
    elif race_input==8:
        char['race']="Tallfellow Halfling"
    elif race_input==9:
        char['race']="Stout Halfling"
    elif race_input==10:
        char['race']="Dwarf"
    elif race_input==11:
        char['race']="Half-Dwarf"
    elif race_input==12:
        char['race']="Half-Orc"
    elif race_input==13:
        char['race']="Half-Ogre"
    elif race_input==14:
        char['race']="Half-Troll"
    elif race_input==15:
        char['race']="Gnomes"
    elif race_input==16:
        char['race']="Hira'razhir"
    elif race_input==17:
        char['race']="Idiyva"
    elif race_input==18:
        char['race']="Vulfen"
    elif race_input==19:
        char['race']="Sstoi'isslythi"

    ### Enter current statistic values

    st_stat_input=int(raw_input('Strength: '))
    st_stat=cfgData.prime_req(pro_ch,"st",st_stat_input)

    qu_stat_input=int(raw_input('Quickness: '))
    qu_stat=cfgData.prime_req(pro_ch,"qu",qu_stat_input)

    pr_stat_input=int(raw_input('Presence: '))
    pr_stat=cfgData.prime_req(pro_ch,"pr",pr_stat_input)

    in_stat_input=int(raw_input('Intuition: '))
    in_stat=cfgData.prime_req(pro_ch,"in",in_stat_input)

    em_stat_input=int(raw_input('Empathy: '))
    em_stat=cfgData.prime_req(pro_ch,"em",em_stat_input)

    co_stat_input=int(raw_input('Constitution: '))
    co_stat=cfgData.prime_req(pro_ch,"co",co_stat_input)

    ag_stat_input=int(raw_input('Agility: '))
    ag_stat=cfgData.prime_req(pro_ch,"ag",ag_stat_input)

    sd_stat_input=int(raw_input('Self-Discipline: '))
    sd_stat=cfgData.prime_req(pro_ch,"sd",sd_stat_input)

    me_stat_input=int(raw_input('Memory: '))
    me_stat=cfgData.prime_req(pro_ch,"me",me_stat_input)

    re_stat_input=int(raw_input('Reasoning: '))
    re_stat=cfgData.prime_req(pro_ch,"re",re_stat_input)

    ### Calculate Potential Value using pot_calc function
    st_pot_in=int(raw_input('Potential Roll (ST): '))
    st_pot=cfgData.pot_calc(st_stat,st_pot_in)

    qu_pot_in=int(raw_input('Potential Roll (QU): '))
    qu_pot=cfgData.pot_calc(qu_stat,qu_pot_in)

    pr_pot_in=int(raw_input('Potential Roll (PR): '))
    pr_pot=cfgData.pot_calc(pr_stat,pr_pot_in)

    in_pot_in=int(raw_input('Potential Roll (IN): '))
    in_pot=cfgData.pot_calc(in_stat,in_pot_in)

    em_pot_in=int(raw_input('Potential Roll (EM): '))
    em_pot=cfgData.pot_calc(em_stat,em_pot_in)

    co_pot_in=int(raw_input('Potential Roll (CO): '))
    co_pot=cfgData.pot_calc(co_stat,co_pot_in)

    ag_pot_in=int(raw_input('Potential Roll (AG): '))
    ag_pot=cfgData.pot_calc(ag_stat,ag_pot_in)

    sd_pot_in=int(raw_input('Potential Roll (SD): '))
    sd_pot=cfgData.pot_calc(sd_stat,sd_pot_in)

    me_pot_in=int(raw_input('Potential Roll (ME): '))
    me_pot=cfgData.pot_calc(me_stat,me_pot_in)

    re_pot_in=int(raw_input('Potential Roll (RE): '))
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
    sexch = int(raw_input("Select Sex: "))
    sex = cfgData.sexlist[sexch-1]
    char['gender'] = sex
    hairch = int(raw_input("Select Hair color: "))
    hair = cfgData.hairlist[hairch-1]
    char['hair'] = hair
    eyech = int(raw_input("Select Eye color: "))
    eye = cfgData.eyelist[eyech-1]
    char['eye'] = eye
    age = int(raw_input("Character's Age: "))
    char['age'] = age
    print

    ht = str(raw_input("Enter Height: "))
    wt = str(raw_input("Enter Weight: "))
    char['height'],char['weight'] = ht,wt

    # Load data into dictionary for saving of the character
    char['st_stat'],char['st_pot']=st_stat,st_pot
    char['qu_stat'],char['qu_pot']=qu_stat,qu_pot
    char['pr_stat'],char['pr_pot']=pr_stat,pr_pot
    char['in_stat'],char['in_pot']=in_stat,in_pot
    char['em_stat'],char['em_pot']=em_stat,em_pot
    char['co_stat'],char['co_pot']=co_stat,co_pot
    char['ag_stat'],char['ag_pot']=ag_stat,ag_pot
    char['sd_stat'],char['sd_pot']=sd_stat,sd_pot
    char['me_stat'],char['me_pot']=me_stat,me_pot
    char['re_stat'],char['re_pot']=re_stat,re_pot
    char['lvl']=0
    char['realm']=plist[pro_ch][8]
    char['stmb'],char['qumb'],char['emmb'],char['inmb'],char['prmb']=0,0,0,0,0
    char['comb'],char['agmb'],char['sdmb'],char['remb'],char['memb']=0,0,0,0,0
    hp_math=Decimal(char['co_stat'])/Decimal(10)
    hp=Decimal(hp_math).quantize(Decimal('1e-3'))
    char['hp_base']=int(round(hp,0))

    # Open chart of stat values
    with open(cfgData.cfg_dir+"/sttchart.csv") as f:
        statchart =f.read().splitlines()
    f.close()
    sc=[]

    for x in statchart:
        sc.append(x.split(","))

    # Loop through statistics to pull bonuses
    for x1 in sc:
        if int(x1[0]) == int(char['st_stat']):
            stb,stdp,stpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['qu_stat']):
            qub,qudp,qupp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['pr_stat']):
            prb,prdp,prpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['in_stat']):
            inb,indp,inpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['em_stat']):
            emb,emdp,empp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['co_stat']):
            cob,codp,copp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['ag_stat']):
            agb,agdp,agpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['sd_stat']):
            sdb,sddp,sdpp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['me_stat']):
            meb,medp,mepp=x1[1],x1[2],x1[3]
        if int(x1[0]) == int(char['re_stat']):
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
        if x3[0] == char['race']:
            '''
            print x3[0]
            print x3[11],":Essence"
            print x3[12],":Channeling"
            print x3[13],":Mentalism"
            print x3[14],":Poison"
            print x3[15],":Disease"
            print x3[17]
            '''
            essModBase = x3[11]
            chanModBase = x3[12]
            mentModBase = x3[13]
            poiModBase = x3[14]
            disModBase = x3[15]
            HitDie = x3[17]
    # Race Bonus
    for x2 in rc:
        if x2[0] == char['race']:
            raceb=x2

    #######################
    # Calcalute Total Bonus
    #######################

    sttb=(int(stb)+int(raceb[1])+int(char['stmb']))
    qutb=(int(qub)+int(raceb[2])+int(char['qumb']))
    prtb=(int(prb)+int(raceb[3])+int(char['prmb']))
    intb=(int(inb)+int(raceb[4])+int(char['inmb']))
    emtb=(int(emb)+int(raceb[5])+int(char['emmb']))
    cotb=(int(cob)+int(raceb[6])+int(char['comb']))
    agtb=(int(agb)+int(raceb[7])+int(char['agmb']))
    sdtb=(int(sdb)+int(raceb[8])+int(char['sdmb']))
    metb=(int(meb)+int(raceb[9])+int(char['memb']))
    retb=(int(reb)+int(raceb[10])+int(char['remb']))
    tdp=(float(codp)+float(agdp)+float(sddp)+float(medp)+float(redp))*float(cfgData.dp_multipler)
    char['dp']=round(tdp,1)
    dp_math=Decimal(char['dp'])
    dp=Decimal(dp_math).quantize(Decimal('1e-3'))
    char['tempdp'] = int(round(dp,0))

    # Add Total Bonus of skills to character data
    char['sttb']=sttb
    char['qutb']=qutb
    char['prtb']=prtb
    char['intb']=intb
    char['emtb']=emtb
    char['cotb']=cotb
    char['agtb']=agtb
    char['sdtb']=sdtb
    char['metb']=metb
    char['retb']=retb

    # Set Resistance Roll Modifiers
    char['essmod'] = int(essModBase)+int(emtb)
    char['chanmod'] = int(chanModBase)+int(intb)
    char['mentmod'] = int(mentModBase)+int(prtb)
    char['poimod'] = int(poiModBase)+int(cotb)
    char['dismod'] = int(disModBase)+int(cotb)
    char['hitdie'] = HitDie

    # Power Point Math
    stpp,qupp,copp,agpp,sdpp,mepp,repp="-","-","-","-","-","-","-"
    if char['realm'] == "NULL":
        prpp,inpp,empp=0.0,0.0,0.0
        tpp=0.0
    if char['realm'] == "PR":
        inpp,empp=0.0,0.0
        tpp=prpp
    if char['realm'] == "IN":
        empp,prpp=0.0,0.0
        tpp=inpp
    if char['realm'] == "EM":
        inpp,prpp=0.0,0.0
        tpp=empp
    if char['realm'] == "IP":
        empp=0.0
        tpp=(float(inpp)+float(prpp))/2
    if char['realm'] == "PE":
        inpp=0.0
        tpp=(float(empp)+float(prpp))/2
    if char['realm'] == "IE":
        prpp=0.0
        tpp=(float(inpp)+float(empp))/2
    if char['realm'] == "AR":
        tpp=(float(inpp)+float(prpp)+float(empp))/3

    # Development Point Math
    stdp,qudp,emdp,indp,prdp="-","-","-","-","-"

    # Open skills csv based on magic realm of the character
    if char['realm'] == "EM":
        skill_file="ds_em.csv"
    if char['realm'] == "PR":
        skill_file="ds_pr.csv"
    if char['realm'] == "IN":
        skill_file="ds_in.csv"
    if char['realm'] == "IP":
        skill_file="ds_ip.csv"
    if char['realm'] == "PE":
        skill_file="ds_pe.csv"
    if char['realm'] == "IE":
        skill_file="ds_ie.csv"
    if char['realm'] == "AR":
        skill_file="ds_ar.csv"
    if char['realm'] == "NULL":
        skill_file="ds_na.csv"


    # Open skill list file and write to character skill file. Set number of ranks for Hobby, AD, AP,
    # normal to 0
    with open(cfgData.cfg_dir+"/"+skill_file) as f:
        sl=f.read().splitlines()
    f.close()
    skill_list=[]
    for list in sl:
        skill_list.append(list.split(","))
        crt=1
        for outer_list in skill_list:
            index=int(plist[pro_ch][1])
            char[crt]=(outer_list[1],outer_list[5],outer_list[7],outer_list[index],outer_list[6],0,0,0,0,0,0,0,0,0,0)
            crt+=1

    # Write Character data to file
    with open(char_path+'/'+user_name+'.json', 'w') as f:
        f.write(json.dumps(char))

    # Set Languages
    lang_set(user_name)
    # Set Weapon costs using function
    weapon_costs(user_name)

#################################
## End of create_char function ##
#################################

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
            lanch = int(raw_input("Select Language: "))
            lanspoke = int(raw_input("Enter Spoken rank: "))
            lanwritten = int(raw_input("Enter Written rank: "))

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
        mbch=raw_input('Select Stat to add a bonus: ')
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

def weapon_costs(user_name):
    # Open the character file, read-only
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+".json","r") as cf:
        char_dict = json.load(cf)

    ## Read in list of professions and weapon costs, read-only
    with open(cfgData.cfg_dir+"/pro.csv","r") as procsv:
        plist=procsv.read()
    for profess in plist.splitlines():
        rt=profess.split(",")
        if rt[0] == char_dict['pro_name']:
            wclist=[rt[2],rt[3],rt[4],rt[5],rt[6],rt[7]]

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
    weapsel = int(raw_input('Select Weapon cost to assign: '))
    while weapsel<1 or weapsel>6: # Check that input is in the range
        print "You must select a number between (1 and 6)"
        weapsel=int(raw_input('Select weapon cost to assign: '))
    # Weapon category selection
    weapcat = int(raw_input('Select Weapon Category to assign cost: '))
    while weapcat<1 or weapcat>6: # Check that input is in the range
        print "You must select a number between (1 and 6)"
        weapcat=int(raw_input('Select Weapon Category to assign cost: '))

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
        weapsel = int(raw_input('Select Weapon cost to assign: '))
        while weapsel<1 or weapsel>6: # Check that input is in the range
            print "You must select a number between (1 and 6)"
            weapsel=int(raw_input('Select weapon cost to assign: '))

        # Weapon category selection
        weapcat = int(raw_input('Select Weapon Category to assign cost: '))
        while weapcat<1 or weapcat>6: # Check that input is in the range
            print "You must select a number between (1 and 6)"
            weapcat=int(raw_input('Select Weapon Category to assign cost: '))

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
    #with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as sf:
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+".json","r") as sf:
        skill_dict = json.load(sf)
    # Open ds.csv for count of skills
    with open(cfgData.cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()

    skcnt=1
    # Loop through skills and update costs of weapons
    while skcnt <= len(sl):
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
    with open(cfgData.char_dir+"/"+user_name+"/"+user_name+".json","w") as sw:
        sw.write(json.dumps(skill_dict))

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
        create_char()
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
    elif choice=="x":
        print "Exiting Program"
        loop=False
    elif choice=="X":
        print "Exiting program"
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

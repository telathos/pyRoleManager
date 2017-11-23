import json
import re
import os.path
from natsort import natsorted, ns

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'

########
def char_menu():
    # Clear list before function is ran
    menu_items=[]
    i=1
    print 5 * "-", "Characters", 5 * "-"
    for file in os.listdir(char_dir):
        menu_items.insert(i,file)
        print "{:<2}.) {:15}".format(i,file)
        i+=1
    print 25 * "-"
    return menu_items

def char_menu_level(char_name):
    menu_items=[]
    menu_sort=[]
    i=1
    lvl=0
    print 5 * "-", "Level", 5 * "-"
    print
    char_dir_files=char_dir+"/"+char_name
    p=len(os.listdir(char_dir_files))
    for json in os.listdir(char_dir_files):
        if i < p:
            menu_items.insert(i,json)
            i+=1
            lvl+=1
    menu_sort.insert(i,natsorted(menu_items, key=lambda json: json))
    ml=len(menu_sort[0])

    print 25 * "-"
    ch_lvl=raw_input('Select Level: ')
    #char_lvl=char_dir_files+"/"+char_name+"-"+ch_lvl+".json"
    skill_dict={}
    with open(char_dir_files+"/"+char_name+".json","r") as rl:
        skill_dict = json.load(rl)
    print skill_dict

def select_skills():
    p=char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"
    #skill_dict={}
    skill_list=[]
    #print p
    s-=1
    with open(char_dir+"/"+p[s]+"/"+p[s]+".json") as f:
        char_dict=json.load(f)

    # load for skill list count
    with open(cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    print len(sl),":len"
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
            print sklst
            for words in char_dict:
                print words,":words"
                if words.isdigit():
                    if char_dict[words][0].startswith(g):
                        index=words
                        print char_dict[words][0]
                        sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],index])
                        sklst=sorted(sklist, key=lambda skill: skill[0])
                    print sklst,":sklst"
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
                    print "{:>3}.) | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:4}".format(i,skills[0],skills[1],skills[3],skills[4],skills[5],skills[6],skills[7],skills[8])
                    skill_menu_list.insert(i,skills[8])
                    i+=1
                print 80 * "-"
                print
                while True:
                    sr=int(raw_input("Select Skill: "))
                    if sr >=1 and sr<=len(sx):
                        break
                    else:
                        print "Invalid Selection! Select a skill from the list"
                # substrat one from menu select to line up with list
                sr-=1
                print "| {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|85".format(char_dict[skill_menu_list[sr]][0],char_dict[skill_menu_list[sr]][1],char_dict[skill_menu_list[sr]][3],char_dict[skill_menu_list[sr]][5],char_dict[skill_menu_list[sr]][6],char_dict[skill_menu_list[sr]][7],char_dict[skill_menu_list[sr]][8])
                srnk=int(raw_input('Number of Ranks: '))
                char_dict[skill_menu_list[sr]][8]=char_dict[skill_menu_list[sr]][8]+srnk
                #print skill_menu_list[sr]

                sksubloop=False
        if ska=="2":
            print "2"
            sx=skill_to_list("B")
            print sx
            while sksubloop:
                print "digit"
                sksubloop=False
        # Exit loop
        if ska == 'X' or ska=='x':
            skloop=False
select_skills()

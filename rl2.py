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
    i=1
    lvl=0
    while lvl<ml:
        # Testing
        #print "{}.) Level :{} - {:15}:{}".format(lvl,lvl,char_name,menu_sort[0][lvl])
        print "{}.) Level :{} - {:15}".format(lvl,lvl,char_name)
        lvl+=1
    print 25 * "-"
    ch_lvl=raw_input('Select Level: ')
    char_lvl=char_dir_files+"/"+char_name+"-"+ch_lvl+".json"
    skill_dict={}
    with open(char_dir_files+"/"+char_name+".json","r") as rl:
        skill_dict = json.load(rl)
    print skill_dict

def raise_level():
    p=char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"
    skill_dict={}

    print p
    s-=1
    with open(char_dir+"/"+p[s]+"/"+p[s]+".json") as f:
        char_dict=json.load(f)
    print char_dict['name']
    print char_dict['lvl']
    char_menu_level(char_dict['name'])


raise_level()

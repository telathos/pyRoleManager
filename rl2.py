import json
#import re
import os.path

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

def char_menu_level(lvl):
    cml=[]
    i=1
    print 5 * "-", Level, 5 * "-"
    print
    #char_dir_files=char_dir+"/-"+lvl"+".json"
    for json in os.listdir()

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
    lvl=char_menu_level()


raise_level()

import json
import charMenu
import cfgData
import rl

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

    next_lvl=0
    if char_dict['lvl']<=4:
        next_lvl = 10000 + int(char_dict['lvl'])*10000
    elif char_dict['lvl']>4 and char_dict['lvl']<=9:
        next_lvl = 50000+(int(char_dict['lvl'])-4)*20000
    elif char_dict['lvl']>9 and char_dict['lvl']<=14:
        next_lvl = 150000+(int(char_dict['lvl'])-9)*30000
    elif char_dict['lvl']>14 and char_dict['lvl']<=19:
        next_lvl = 300000+(int(char_dict['lvl'])-14)*40000
    else:
        next_lvl = 500000+(int(char_dict['lvl'])-19)*50000

    # Enter experience
    exp=int(raw_input("Add experience: "))
    # Add experience to character's current experience
    char_dict['exp'] += int(exp)
    print char_dict['exp']
    if char_dict['exp']>next_lvl:
        print "Leveled up!"
        rl.select_skills(p[s])

    # Open character file to write out data
    with open(cfgData.char_dir+"/"+char+"/"+char+".json", 'w') as f:
        f.write(json.dumps(char_dict))

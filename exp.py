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
        #print lvlcheck
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
    '''
    if in_lvl > 0:
        rl.select_skills
    '''
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

#exp_check()

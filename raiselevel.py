import json
import charMenu

#char_dir='c:\pyRoleManager\char'
#cfg_dir='c:\pyRoleManager\cfg'

########
'''
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
'''

charMenu.char_menu()
ch=int(raw_input('Select a Character: '))

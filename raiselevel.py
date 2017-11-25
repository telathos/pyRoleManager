import json
import charMenu
import cfgData

p=charMenu.char_menu()
menu_len=len(p)
while True:
    s=int(raw_input("Select a Character: "))
    if s >=1 and s<=menu_len:
        break
    else:
        print "Invalid Selection! Select a character from the list"

# Open the file
s-=1
with open(cfgData.char_dir+"/"+p[s]+"/"+p[s]+".json","r") as cf:
    char_dict = json.load(cf)
#print char_dict

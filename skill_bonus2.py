import json
import re

with open('c:\pyrolemanager\char\kyle\kyle.json','r') as f:
    char_dict=json.load(f)
sklist=[]
sklst=[]

for words in char_dict:
    if words.isdigit():
        index=words
        sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])
        sklst=sorted(sklist, key=lambda skill: skill[0])
#print sklst
menu_loop=True
while menu_loop:
    search=str(raw_input("Select Skill to add Misc bonus: "))
    # Takes inputed search and adds regex matching code
    regex = re.compile('^%s.+'%search,re.I)

    # Create header
    print "| {:5} | {:32} | {:5} |".format("","","Misc")
    print "| {:>5} | {:32} | {:5} |".format("","Skill Name","Bonus")
    print 52 * "-"
    # Loop through skills
    skill_menu=[]
    for y in sklst:
        if re.search(regex,y[0]):
            print "| {:>3}.) | {:32} | {:^5} |".format(y[13],y[0],y[11])
            #print char_dict[y[13]]
            # Create list of skills in menu
            skill_menu.append(int(y[13]))
    #print
    #print "| {:>3}.) | {:32} | {:^5} |".format("X","Back","")
    print skill_menu
    while skill_menu:
        m=int(raw_input("Select skill: "))
        #print m
        if m in skill_menu:
            msb=int(raw_input("Bonus: "))
            char_dict[`m`][13]=int(msb)
            #print char_dict[`m`],":y"
            with open('c:\pyrolemanager\char\kyle\kyle.json','w') as f:
                f.write(json.dumps(char_dict))
            skill_menu=False
            menu_loop=False
        else:
            print "Select a skill on the list"
            print

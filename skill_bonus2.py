import json
import re

with open('c:\pyrolemanager\char\kyle\kyle.json','r') as f:
    char_dict=json.load(f)
sklist=[]
sklst=[]

for words in char_dict:
    if words.isdigit():
        #print char_dict[words][0]
        index=words
        sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])
        sklst=sorted(sklist, key=lambda skill: skill[0])
#print sklst
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
print
print "| {:>3}.) | {:32} | {:^5} |".format("X","Back","")
print skill_menu
while skill_menu:
    m=int(raw_input("Select skill: "))
    print m
    if m in skill_menu:
        msb=int(raw_input("Bonus: "))
        char_dict[y[13]]=int(msb)
        skill_menu=False
    else:
        print "Try again.."

#print skill_menu
'''
qnt=0
for q in sklst:
    qnt+=1
    if qnt == 31:
        ans=str(raw_input("Continue: "))
        if ans.upper()=="N":
            break
        else:
            print "| {:>3}.) | {:29}|{:7}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(qnt,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11],q[12])
            continue
    elif qnt == 61:
        ans=str(raw_input("Continue: "))
        if ans.upper()=="N":
            break
        else:
            print "| {:>3}.) | {:29}|{:7}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(qnt,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11],q[12])
            continue
    elif qnt == 91:
        ans=str(raw_input("Continue: "))
        if ans.upper()=="N":
            break
        else:
            print "| {:>3}.) | {:29}|{:7}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(qnt,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11],q[12])
            continue
    print "| {:>3}.) | {:29}|{:7}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(qnt,q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11],q[12])
skill_select=int(raw_input("Select Skill to add Misc bonus: "))

# Subtract one from skill_select to match item in list
skill_select-=1

print skill_select,":skill_select"
smb_bonus=int(raw_input("Add Misc Bonus: "))
char_dict[`skill_select`][12]=smb_bonus
print char_dict[`skill_select`]
#print char_dict

with open('c:\pyrolemanager\char\kyle\kyle.json','w') as fs:
    fs.write(json.dumps(char_dict))
'''

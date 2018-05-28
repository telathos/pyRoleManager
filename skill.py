import json
import re
###### dictionaries ###########
char_dict={}
skill_dict={}
###### Lists ###########
skill_menu=[]
temp_skill_list=[]
###############

def skill_add(char):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as cf:
        char_dict=json.load(cf)
    with open(cfgData.char_dir+"/"+char+"/"+char+"_skills.json") as sf:
        skill_dict=json.load(sf)

    #print char_dict['tempdp']
    tempdp=char_dict['tempdp']
    while tempdp>0:
        print ""
        print "Enter the start of the Skill to increase:"
        print 'Example: entering b will list all skills that start with "B"'
        print
        print "Enter 'Exit' to return the previous menu"
        search=str(raw_input(": "))
        # Takes inputed search and adds regex matching code
        regex = re.compile('^%s.+'%search,re.I)
        skill_menu=[]
        # Check if exiting loop
        if search.upper() == "EXIT":
            skloop=False
        else:
            # Create header
            print "*",79 * "=","*"
            print "| {:5} | {:32} | {:^4} | {:5} | {:^5} | {:^5} | {:^5} |".format("","","","Hobby","AD","AP","Std")
            print "| {:>5} | {:32} | {:^4} | {:5} | {:5} | {:5} | {:5} |".format("","Skill Name","Cost","Bonus","Bonus","Bonus","Bonus")
            print "*",79 * "-","*"
            # Loop through skills
            for y in skill_dict:
                if re.search(regex,skill_dict[y][0]):
                    print "| {:>3}.) | {:32} | {:^4} | {:^5} | {:^5} | {:^5} | {:^5} |".format(y,skill_dict[y][0],skill_dict[y][3],
                                                                                               skill_dict[y][5],skill_dict[y][6],skill_dict[y][7],
                                                                                               skill_dict[y][8])
                    # Create list of skills in menu
                    skill_menu.append(int(y))
            print "*",79 * "-","*"
            #print skill_menu
            select=0
            while select == 0:
                try:
                    rnkch=int(raw_input("Select skill: "))
                    if rnkch in skill_menu:
                        select=1
                        # Check number of ranks allowed
                        if re.match("^[1-9]\/.+",skill_dict[`rnkch`][3]):
                            #print skill_dict[`rnkch`][3]
                            cost=skill_dict[`rnkch`][3].split("/")
                            if cost[1] == "*":
                                skill_qty=3
                            else:
                                skill_qty=2
                        else:
                            cost=int(skill_dict[`rnkch`][3])
                            skill_qty=1
                        # Add ranks
                        rnkadd=0
                        if skill_qty==1:
                            try:
                                rnkadd=int(raw_input("Enter number of Ranks to assign: [1]"))
                                if rnkadd > 1:
                                    print "Only 1 rank can be assigned!"
                                else:
                                    chkdp=tempdp - int(cost)
                                    if chkdp < 0:
                                        print "You do not have enough Development Points"
                                        rnkadd=0
                                    else:
                                        rnkadd=1
                                        tempdp=tempdp - int(cost)
                                        #print tempdp,":tempdp -1"
                                        temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        #print temp_skill_list
                            except:
                                print "Enter a number of ranks to assign??"
                        elif skill_qty>1:
                            while rnkadd < 1 or rnkadd > skill_qty:
                                try:
                                    rnkadd=int(raw_input("Enter number of Ranks to assign: [1-{:<1}]: ".format(skill_qty)))
                                    if rnkadd > skill_qty:
                                        print "You must enter a number between 1 and {:<2}".format(skill_qty)
                                    else:
                                        #print rnkadd,"rnkadd"
                                        #print type(rnkadd)
                                        if rnkadd == 3:
                                            used=int(rnkadd)* int(cost[0])
                                            chkdp = tempdp - used
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=2
                                            else:
                                                tempdp = tempdp - used
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 2:
                                            #print cost[0]
                                            used=int(cost[0])+int(cost[1])
                                            #print used
                                            chkdp = tempdp - used
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=1
                                            else:
                                                tempdp = tempdp - used
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 1:
                                            chkdp = tempdp - int(cost[0])
                                            if chkdp < 0:
                                                print "You do not have enough Development Points"
                                                rnkadd=0
                                            else:
                                                tempdp = tempdp - int(cost[0])
                                                #print tempdp,":tempdp"
                                                temp_skill_list.append([skill_dict[`rnkch`][0],rnkadd])
                                        if rnkadd == 0:
                                            rnkadd=1
                                            #print "Exit skill"
                                except:
                                    print "Enter the number of ranks"
                    else:
                        print "Select a skill on the list"
                except:
                    print "Select a skill"
            #print temp_skill_list
skill_add(char)

with open(char_dir+"/"+char+"/"+char+".json") as cf:
    char_dict=json.load(cf)
print "The following ranks will be assigned to"
if char_dict['lvl'] == 0:
    print "the selected skills for your Adolescence Level"
elif char_dict['lvl'] == 0.5:
    print "the selected skills for your Appenticeship Level"
elif char_dict['lvl']>= 1:
    print "the selected skills for your level {:<2} ".format(char_dict['lvl'])
print ""
print "*",36 * "=","*"
for j in temp_skill_list:
    print "| {:32} | {:1} |".format(j[0],j[1])
print "*",36 * "=","*"
print ""
print "Do you want to assign these ranks? [Y/N]"
print "No will restart the selection"
skasch=True
while skasch:
    try:
        sch=raw_input("Do you want to assign these ranks? [Y/N]: ")
        if sch.upper()=="Y":
            print "Assigned"
            skasch=False
            # Write to skill_dict and save
        elif sch.upper()=="N":
            skasch=True
            skill_add(char)
            tempdp=char_dict['tempdp']
        else:
            print "Enter Y or N to continue"
    except:
        print "Enter Y or N to continue"

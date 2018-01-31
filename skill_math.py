import json
import cfgData
import charMenu

p=charMenu.char_menu()
menu_len=len(p)
while True:
    s=int(raw_input("Select Character: "))
    if s >=1 and s<=menu_len:
        break
    else:
        print "Invalid Selection! Select a character from the list"
skill_list=[]
s-=1
char=p[s]

def skill_totals(char,var1):
    with open(cfgData.char_dir+"/"+char+"/"+char+".json") as f:
        char_dict=json.load(f)
    sklist=[]

    for words in char_dict:
        if words.isdigit():
            index=words
            sklist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3],char_dict[words][5],char_dict[words][6],char_dict[words][7],char_dict[words][8],char_dict[words][10],char_dict[words][11],char_dict[words][12],char_dict[words][13],char_dict[words][14],index])

            # Get stat total bonuses
            stat=char_dict[words][1]
            if len(stat)==2:
                print stat
                if stat.upper() == "NA":
                    print "No Stat"
                else:
                    if stat == "ST":
                        stat_bonus = char_dict['sttb']
                        print stat_bonus
                    elif stat == "QU":
                        stat_bonus = char_dict['qutb']
                        print stat_bonus
                    elif stat == "PR":
                        stat_bonus = char_dict['prtb']
                        print stat_bonus
                    elif stat == "IN":
                        stat_bonus = char_dict['intb']
                        print stat_bonus
                    elif stat == "EM":
                        stat_bonus = char_dict['emtb']
                        print stat_bonus
                    elif stat == "CO":
                        stat_bonus = char_dict['cotb']
                        print stat_bonus
                    elif stat == "AG":
                        stat_bonus = char_dict['agtb']
                        print stat_bonus
                    elif stat == "SD":
                        stat_bonus = char_dict['sdtb']
                        print stat_bonus
                    elif stat == "ME":
                        stat_bonus = char_dict['metb']
                        print stat_bonus
                    elif stat == "RE":
                        stat_bonus = char_dict['retb']
                        print stat_bonus
                    char_dict[words][11] = stat_bonus
                    print char_dict[words][11],":stat bonus (Single)"
            elif len(stat)==5:
                stats=stat.split('/')
                # Stat 1
                print char_dict[words][0],stat
                if char_dict[words][0]=="Diving":
                    print "+++++++++++++"
                    print "+++++++++++++"
                if stats[0] == "ST":
                    stat_bonus1 = char_dict['sttb']
                elif stats[0] == "QU":
                    stat_bonus1 = char_dict['qutb']
                elif stats[0] == "PR":
                    stat_bonus1 = char_dict['prtb']
                elif stats[0] == "IN":
                    stat_bonus1 = char_dict['intb']
                elif stats[0] == "EM":
                    stat_bonus1 = char_dict['emtb']
                elif stats[0] == "CO":
                    stat_bonus1 = char_dict['cotb']
                elif stats[0] == "AG":
                    stat_bonus1 = char_dict['agtb']
                elif stats[0] == "SD":
                    stat_bonus1 = char_dict['sdtb']
                elif stats[0] == "ME":
                    stat_bonus1 = char_dict['metb']
                elif stats[0] == "RE":
                    stat_bonus1 = char_dict['retb']
                # Stat 2
                if stats[1] == "ST":
                    stat_bonus2 = char_dict['sttb']
                elif stats[1] == "QU":
                    stat_bonus2 = char_dict['qutb']
                elif stats[1] == "PR":
                    stat_bonus2 = char_dict['prtb']
                elif stats[1] == "IN":
                    stat_bonus2 = char_dict['intb']
                elif stats[1] == "EM":
                    stat_bonus2 = char_dict['emtb']
                elif stats[1] == "CO":
                    stat_bonus2 = char_dict['cotb']
                elif stats[1] == "AG":
                    stat_bonus2 = char_dict['agtb']
                elif stats[1] == "SD":
                    stat_bonus2 = char_dict['sdtb']
                elif stats[1] == "ME":
                    stat_bonus2 = char_dict['metb']
                elif stats[1] == "RE":
                    stat_bonus2 = char_dict['retb']
                print stats[0],"0"
                print stats[1],"1"
                stat_bonus = (stat_bonus1 + stat_bonus2)/2
                char_dict[words][11] = stat_bonus
                print stat_bonus,":stat bonus (Double)"
            elif len(stat)==8:
                stats=stat.split('/')
                # Stat 1
                if stats[0] == "ST":
                    stat_bonus1 = char_dict['sttb']
                elif stats[0] == "QU":
                    stat_bonus1 = char_dict['qutb']
                elif stats[0] == "PR":
                    stat_bonus1 = char_dict['prtb']
                elif stats[0] == "IN":
                    stat_bonus1 = char_dict['intb']
                elif stats[0] == "EM":
                    stat_bonus1 = char_dict['emtb']
                elif stats[0] == "CO":
                    stat_bonus1 = char_dict['cotb']
                elif stats[0] == "AG":
                    stat_bonus1 = char_dict['agtb']
                elif stats[0] == "SD":
                    stat_bonus1 = char_dict['sdtb']
                elif stats[0] == "ME":
                    stat_bonus1 = char_dict['metb']
                elif stats[0] == "RE":
                    stat_bonus1 = char_dict['retb']
                # Stat 2
                if stats[1] == "ST":
                    stat_bonus2 = char_dict['sttb']
                elif stats[1] == "QU":
                    stat_bonus2 = char_dict['qutb']
                elif stats[1] == "PR":
                    stat_bonus2 = char_dict['prtb']
                elif stats[1] == "IN":
                    stat_bonus2 = char_dict['intb']
                elif stats[1] == "EM":
                    stat_bonus2 = char_dict['emtb']
                elif stats[1] == "CO":
                    stat_bonus2 = char_dict['cotb']
                elif stats[1] == "AG":
                    stat_bonus2 = char_dict['agtb']
                elif stats[1] == "SD":
                    stat_bonus2 = char_dict['sdtb']
                elif stats[1] == "ME":
                    stat_bonus2 = char_dict['metb']
                elif stats[1] == "RE":
                    stat_bonus2 = char_dict['retb']
                # Stat 3
                if stats[2] == "ST":
                    stat_bonus3 = char_dict['sttb']
                elif stats[2] == "QU":
                    stat_bonus3 = char_dict['qutb']
                elif stats[2] == "PR":
                    stat_bonus3 = char_dict['prtb']
                elif stats[2] == "IN":
                    stat_bonus3 = char_dict['intb']
                elif stats[2] == "EM":
                    stat_bonus3 = char_dict['emtb']
                elif stats[2] == "CO":
                    stat_bonus3 = char_dict['cotb']
                elif stats[2] == "AG":
                    stat_bonus3 = char_dict['agtb']
                elif stats[2] == "SD":
                    stat_bonus3 = char_dict['sdtb']
                elif stats[2] == "ME":
                    stat_bonus3 = char_dict['metb']
                elif stats[2] == "RE":
                    stat_bonus3 = char_dict['retb']
                print stats[0],"0"
                print stats[1],"1"
                print stats[2],"2"
                stat_bonus = (stat_bonus1 + stat_bonus2 + stat_bonus3)/3
                print stat_bonus,":stat bonus (Triple)"
                char_dict[words][11] = stat_bonus

        # Write Character data to file
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", "w") as f:
            f.write(json.dumps(char_dict))

skill_totals(char,"hi")

import json
import cfgData
import charMenu

'''
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
'''
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
                if stat.upper() == "NA":
                    stat_bonus = 0
                else:
                    if stat == "ST":
                        stat_bonus = char_dict['sttb']
                    elif stat == "QU":
                        stat_bonus = char_dict['qutb']
                    elif stat == "PR":
                        stat_bonus = char_dict['prtb']
                    elif stat == "IN":
                        stat_bonus = char_dict['intb']
                    elif stat == "EM":
                        stat_bonus = char_dict['emtb']
                    elif stat == "CO":
                        stat_bonus = char_dict['cotb']
                    elif stat == "AG":
                        stat_bonus = char_dict['agtb']
                    elif stat == "SD":
                        stat_bonus = char_dict['sdtb']
                    elif stat == "ME":
                        stat_bonus = char_dict['metb']
                    elif stat == "RE":
                        stat_bonus = char_dict['retb']
                    char_dict[words][11] = stat_bonus
                    #print char_dict[words][11],":stat bonus (Single)"
            elif len(stat)==5:
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
                '''
                print stats[0],"0"
                print stats[1],"1"
                print stat_bonus,":stat bonus (Double)"
                '''
                stat_bonus = (stat_bonus1 + stat_bonus2)/2
                char_dict[words][11] = stat_bonus
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
                '''
                print stats[0],"0"
                print stats[1],"1"
                print stats[2],"2"
                print stat_bonus,":stat bonus (Triple)"
                '''
                stat_bonus = (stat_bonus1 + stat_bonus2 + stat_bonus3)/3
                char_dict[words][11] = stat_bonus
            # Calcalute skill bonus
            skill_rank_total = char_dict[words][5] + char_dict[words][6] + char_dict[words][7] + char_dict[words][8]

            if skill_rank_total <= 10:
                skill_bonus = skill_rank_total * 5
            elif skill_rank_total >=11 and skill_rank_total <= 20:
                skill_bonus = 50 + ((skill_rank_total-10) * 2)
            elif skill_rank_total >= 21 and skill_rank_total <= 30:
                skill_bonus = 70 + ((skill_rank_total-20) * 1)
            else:
                skill_bonus = 80 + ((skill_rank_total-30) * 0.5)
            # Update dictionary
            char_dict[words][10] = skill_bonus

            # Calcalute Total Skill Bonus
            total_skill_bonus = char_dict[words][10] + char_dict[words][11] + char_dict[words][12] + char_dict[words][13]
            # Update dictionary
            char_dict[words][14] = total_skill_bonus
        # Write Character data to file
        with open(cfgData.char_dir+"/"+char+"/"+char+".json", "w") as f:
            f.write(json.dumps(char_dict))

#skill_totals(char,"hi")

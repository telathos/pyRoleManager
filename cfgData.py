# Change the paths to where pyRoleManager is installed on your system_call

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'

'''
'dp_multipler' is used to increase the amount of Development Points
a character will get. Set the value to another other than 1.0 will
change the total Development Points a character recieves
'''
dp_multipler = 1.25

from colorama import Fore, Back, Style
import decimal

dp=0
dp_cur=0
space=' '
def running_dp(num):
    dp=decimal.Decimal(num)
    dp_cur=round(dp,0)
    print(72*space + Fore.RED + Back.WHITE + "DP:" + `dp_cur`)
    print (Style.RESET_ALL)

    return dp_cur

def skill_header():
    print 80 * "-"
    print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
    print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
    print 80 * "-"

def skill_header_added_skill():
    print 104 * "-"
    print "| {:32} |{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std","Stat","Skill","Misc","lvl","Total")
    print "| {:32} |{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank","Bonus","Bonus","Bonus","Bonus","Bonus")
    print 104 * "-"

# Calcalute Potential stats based on current stats
poten=0
def pot_calc(current,pot_roll):
    # Under 25
    if current<25:
        if pot_roll<11:
            poten=25
        elif pot_roll>=11 and pot_roll<=20:
            poten=30
        elif pot_roll>=21 and pot_roll<=30:
            poten=35
        elif pot_roll>=31 and pot_roll<=35:
            poten=38
        elif pot_roll>=36 and pot_roll<=40:
            poten=40
        elif pot_roll>=41 and pot_roll<=45:
            poten=42
        elif pot_roll>=46 and pot_roll<=49:
            poten=44
        elif pot_roll>=50 and pot_roll<=51:
            poten=46
        elif pot_roll>=52 and pot_roll<=53:
            poten=48
        elif pot_roll>=54 and pot_roll<=55:
            poten=50
        elif pot_roll>=56 and pot_roll<=57:
            poten=52
        elif pot_roll>=58 and pot_roll<=59:
            poten=54
        elif pot_roll>=60 and pot_roll<=61:
            poten=56
        elif pot_roll>=62 and pot_roll<=63:
            poten=58
        elif pot_roll>=64 and pot_roll<=65:
            poten=60
        elif pot_roll>=66 and pot_roll<=67:
            poten=62
        elif pot_roll>=68 and pot_roll<=69:
            poten=64
        elif pot_roll>=70 and pot_roll<=71:
            poten=66
        elif pot_roll>=72 and pot_roll<=73:
            poten=68
        elif pot_roll>=74 and pot_roll<=75:
            poten=70
        elif pot_roll>=76 and pot_roll<=77:
            poten=72
        elif pot_roll>=78 and pot_roll<=79:
            poten=74
        elif pot_roll>=80 and pot_roll<=81:
            poten=76
        elif pot_roll>=82 and pot_roll<=83:
            poten=78
        elif pot_roll>=84 and pot_roll<=85:
            poten=80
        elif pot_roll>=86 and pot_roll<=87:
            poten=82
        elif pot_roll>=88 and pot_roll<=89:
            poten=84
        elif pot_roll==90:
            poten=86
        elif pot_roll==91:
            poten=88
        elif pot_roll==92:
            poten=90
        elif pot_roll==93:
            poten=91
        elif pot_roll==94:
            poten=92
        elif pot_roll==95:
            poten=93
        elif pot_roll==96:
            poten=94
        elif pot_roll==97:
            poten=95
        elif pot_roll==98:
            poten=96
        elif pot_roll==99:
            poten=97
        elif pot_roll==100:
            poten=98
    # 25-39
    elif current>=25 and current<=39:
        if pot_roll<21:
            poten=current
        elif pot_roll>=21 and pot_roll<=30:
            poten=39
        elif pot_roll>=31 and pot_roll<=35:
            poten=42
        elif pot_roll>=36 and pot_roll<=40:
            poten=45
        elif pot_roll>=41 and pot_roll<=45:
            poten=47
        elif pot_roll>=46 and pot_roll<=49:
            poten=49
        elif pot_roll>=50 and pot_roll<=51:
            poten=51
        elif pot_roll>=52 and pot_roll<=53:
            poten=53
        elif pot_roll>=54 and pot_roll<=55:
            poten=55
        elif pot_roll>=56 and pot_roll<=57:
            poten=57
        elif pot_roll>=58 and pot_roll<=59:
            poten=59
        elif pot_roll>=60 and pot_roll<=61:
            poten=61
        elif pot_roll>=62 and pot_roll<=63:
            poten=63
        elif pot_roll>=64 and pot_roll<=65:
            poten=65
        elif pot_roll>=66 and pot_roll<=67:
            poten=67
        elif pot_roll>=68 and pot_roll<=69:
            poten=69
        elif pot_roll>=70 and pot_roll<=71:
            poten=71
        elif pot_roll>=72 and pot_roll<=73:
            poten=73
        elif pot_roll>=74 and pot_roll<=75:
            poten=75
        elif pot_roll>=76 and pot_roll<=77:
            poten=77
        elif pot_roll>=78 and pot_roll<=79:
            poten=79
        elif pot_roll>=80 and pot_roll<=81:
            poten=81
        elif pot_roll>=82 and pot_roll<=83:
            poten=83
        elif pot_roll>=84 and pot_roll<=85:
            poten=85
        elif pot_roll>=86 and pot_roll<=87:
            poten=86
        elif pot_roll>=88 and pot_roll<=89:
            poten=87
        elif pot_roll==90:
            poten=88
        elif pot_roll==91:
            poten=89
        elif pot_roll==92:
            poten=90
        elif pot_roll==93:
            poten=91
        elif pot_roll==94:
            poten=92
        elif pot_roll==95:
            poten=93
        elif pot_roll==96:
            poten=94
        elif pot_roll==97:
            poten=95
        elif pot_roll==98:
            poten=96
        elif pot_roll==99:
            poten=97
        elif pot_roll==100:
            poten=98
    # 40-59
    elif current>=40 and current<=59:
        if pot_roll<31:
            poten=current
        elif pot_roll>=31 and pot_roll<=35:
            poten=59
        elif pot_roll>=36 and pot_roll<=40:
            poten=62
        elif pot_roll>=41 and pot_roll<=45:
            poten=64
        elif pot_roll>=46 and pot_roll<=49:
            poten=66
        elif pot_roll>=50 and pot_roll<=51:
            poten=68
        elif pot_roll>=52 and pot_roll<=53:
            poten=70
        elif pot_roll>=54 and pot_roll<=55:
            poten=71
        elif pot_roll>=56 and pot_roll<=57:
            poten=72
        elif pot_roll>=58 and pot_roll<=59:
            poten=73
        elif pot_roll>=60 and pot_roll<=61:
            poten=74
        elif pot_roll>=62 and pot_roll<=63:
            poten=75
        elif pot_roll>=64 and pot_roll<=65:
            poten=76
        elif pot_roll>=66 and pot_roll<=67:
            poten=77
        elif pot_roll>=68 and pot_roll<=69:
            poten=78
        elif pot_roll>=70 and pot_roll<=71:
            poten=79
        elif pot_roll>=72 and pot_roll<=73:
            poten=80
        elif pot_roll>=74 and pot_roll<=75:
            poten=81
        elif pot_roll>=76 and pot_roll<=77:
            poten=82
        elif pot_roll>=78 and pot_roll<=79:
            poten=83
        elif pot_roll>=80 and pot_roll<=81:
            poten=84
        elif pot_roll>=82 and pot_roll<=83:
            poten=85
        elif pot_roll>=84 and pot_roll<=85:
            poten=86
        elif pot_roll>=86 and pot_roll<=87:
            poten=87
        elif pot_roll>=88 and pot_roll<=89:
            poten=88
        elif pot_roll==90:
            poten=89
        elif pot_roll==91:
            poten=90
        elif pot_roll==92:
            poten=91
        elif pot_roll==93:
            poten=92
        elif pot_roll==94:
            poten=93
        elif pot_roll==95:
            poten=94
        elif pot_roll==96:
            poten=95
        elif pot_roll==97:
            poten=96
        elif pot_roll==98:
            poten=97
        elif pot_roll==99:
            poten=98
        elif pot_roll==100:
            poten=99
    # 60-74
    elif current>=60 and current<=74:
        if pot_roll<56:
            poten=current
        elif pot_roll>=56 and pot_roll<=57:
            poten=74
        elif pot_roll>=58 and pot_roll<=59:
            poten=75
        elif pot_roll>=60 and pot_roll<=61:
            poten=76
        elif pot_roll>=62 and pot_roll<=63:
            poten=77
        elif pot_roll>=64 and pot_roll<=65:
            poten=78
        elif pot_roll>=66 and pot_roll<=67:
            poten=79
        elif pot_roll>=68 and pot_roll<=69:
            poten=80
        elif pot_roll>=70 and pot_roll<=71:
            poten=81
        elif pot_roll>=72 and pot_roll<=73:
            poten=82
        elif pot_roll>=74 and pot_roll<=75:
            poten=83
        elif pot_roll>=76 and pot_roll<=77:
            poten=84
        elif pot_roll>=78 and pot_roll<=79:
            poten=85
        elif pot_roll>=80 and pot_roll<=81:
            poten=86
        elif pot_roll>=82 and pot_roll<=83:
            poten=87
        elif pot_roll>=84 and pot_roll<=85:
            poten=88
        elif pot_roll>=86 and pot_roll<=87:
            poten=89
        elif pot_roll>=88 and pot_roll<=89:
            poten=90
        elif pot_roll==90:
            poten=91
        elif pot_roll==91:
            poten=92
        elif pot_roll==92:
            poten=93
        elif pot_roll==93:
            poten=94
        elif pot_roll==94:
            poten=95
        elif pot_roll==95:
            poten=96
        elif pot_roll==96:
            poten=97
        elif pot_roll==97:
            poten=97
        elif pot_roll==98:
            poten=98
        elif pot_roll==99:
            poten=98
        elif pot_roll==100:
            poten=99
    # 75-84
    elif current>=75 and current<=84:
        if pot_roll<56:
            poten=current
        elif pot_roll>=56 and pot_roll<=57:
            poten=84
        elif pot_roll>=58 and pot_roll<=59:
            poten=85
        elif pot_roll>=60 and pot_roll<=61:
            poten=86
        elif pot_roll>=62 and pot_roll<=63:
            poten=87
        elif pot_roll>=64 and pot_roll<=65:
            poten=88
        elif pot_roll>=66 and pot_roll<=67:
            poten=88
        elif pot_roll>=68 and pot_roll<=69:
            poten=89
        elif pot_roll>=70 and pot_roll<=71:
            poten=89
        elif pot_roll>=72 and pot_roll<=73:
            poten=90
        elif pot_roll>=74 and pot_roll<=75:
            poten=90
        elif pot_roll>=76 and pot_roll<=77:
            poten=91
        elif pot_roll>=78 and pot_roll<=79:
            poten=91
        elif pot_roll>=80 and pot_roll<=81:
            poten=92
        elif pot_roll>=82 and pot_roll<=83:
            poten=92
        elif pot_roll>=84 and pot_roll<=85:
            poten=93
        elif pot_roll>=86 and pot_roll<=87:
            poten=93
        elif pot_roll>=88 and pot_roll<=89:
            poten=94
        elif pot_roll==90:
            poten=94
        elif pot_roll==91:
            poten=95
        elif pot_roll==92:
            poten=95
        elif pot_roll==93:
            poten=96
        elif pot_roll==94:
            poten=96
        elif pot_roll==95:
            poten=97
        elif pot_roll==96:
            poten=97
        elif pot_roll==97:
            poten=98
        elif pot_roll==98:
            poten=98
        elif pot_roll==99:
            poten=99
        elif pot_roll==100:
            poten=99
    # 85-89
    elif current>=85 and current<=89:
        if pot_roll<66:
            poten=current
        elif pot_roll>=66 and pot_roll<=67:
            poten=89
        elif pot_roll>=68 and pot_roll<=69:
            poten=89
        elif pot_roll>=70 and pot_roll<=71:
            poten=90
        elif pot_roll>=72 and pot_roll<=73:
            poten=90
        elif pot_roll>=74 and pot_roll<=75:
            poten=91
        elif pot_roll>=76 and pot_roll<=77:
            poten=91
        elif pot_roll>=78 and pot_roll<=79:
            poten=92
        elif pot_roll>=80 and pot_roll<=81:
            poten=92
        elif pot_roll>=82 and pot_roll<=83:
            poten=93
        elif pot_roll>=84 and pot_roll<=85:
            poten=93
        elif pot_roll>=86 and pot_roll<=87:
            poten=94
        elif pot_roll>=88 and pot_roll<=89:
            poten=94
        elif pot_roll==90:
            poten=95
        elif pot_roll==91:
            poten=95
        elif pot_roll==92:
            poten=96
        elif pot_roll==93:
            poten=96
        elif pot_roll==94:
            poten=97
        elif pot_roll==95:
            poten=97
        elif pot_roll==96:
            poten=98
        elif pot_roll==97:
            poten=98
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=99
        elif pot_roll==100:
            poten=100
    # 90-94
    elif current>=90 and current<=94:
        if pot_roll<84:
            poten=current
        elif pot_roll>=84 and pot_roll<=85:
            poten=94
        elif pot_roll>=86 and pot_roll<=87:
            poten=94
        elif pot_roll>=88 and pot_roll<=89:
            poten=95
        elif pot_roll==90:
            poten=95
        elif pot_roll==91:
            poten=96
        elif pot_roll==92:
            poten=96
        elif pot_roll==93:
            poten=97
        elif pot_roll==94:
            poten=97
        elif pot_roll==95:
            poten=98
        elif pot_roll==96:
            poten=98
        elif pot_roll==97:
            poten=99
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 95-97
    elif current>=95 and current<=97:
        if pot_roll<90:
            poten=current
        elif pot_roll==90:
            poten=97
        elif pot_roll==91:
            poten=97
        elif pot_roll==92:
            poten=97
        elif pot_roll==93:
            poten=98
        elif pot_roll==94:
            poten=98
        elif pot_roll==95:
            poten=98
        elif pot_roll==96:
            poten=99
        elif pot_roll==97:
            poten=99
        elif pot_roll==98:
            poten=99
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 98-99
    elif current>=98 and current<=99:
        if pot_roll<94:
            poten=current
        elif pot_roll==94:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==95:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==96:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==97:
            poten=97
            if poten<current:
                poten=current
        elif pot_roll==98:
            poten=100
        elif pot_roll==99:
            poten=100
        elif pot_roll==100:
            poten=100
    # 100
    elif current>=100:
        if pot_roll<100:
            poten=current
        elif pot_roll==100:
            poten=101
    return poten

# Print prime requisite error
def pr_text():
    print "This is a Prime requisite and must be 90 or higher"

num=""
def prime_req(pro,char_stat,num):
    '''
    Check if the profession's prime requisites are 90+
    prompt for a new value if less than 90
    '''
    if pro==1:
        # Assassin
        if char_stat.upper()=="QU" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==2:
        # Bounty Hunter
        if char_stat.upper()=="AG" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==3:
        # Barbarian
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==4:
        # Burglar
        if char_stat.upper()=="IN" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==5:
        # Dancer
        if char_stat.upper()=="QU" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==6:
        # Fighter
        if char_stat.upper()=="ST" or char_stat.upper()=="CP":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==7:
        # High Warrior Monk
        if char_stat.upper()=="AG" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==8:
        # Rogue
        if char_stat.upper()=="ST" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==9:
        # Scholar
        if char_stat.upper()=="IN" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==10:
        # Theif
        if char_stat.upper()=="QU" or char_stat.upper()=="SG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==11:
        # Trader
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==12:
        # Warrior
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==13:
        # Warrior Monk
        if char_stat.upper()=="QU" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==14:
        # Alchemist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==15:
        # Animist
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==16:
        # Cleric
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==17:
        # Conjuror
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==18:
        # Druid
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==19:
        # Healer
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==20:
        # Illusionist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==21:
        # Lay Healer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==22:
        # Magician
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==23:
        # Mentalist
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==24:
        # Runemaster
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==25:
        # Sage
        if char_stat.upper()=="PR" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==26:
        # Seer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==27:
        # Shaman
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==28:
        # Bard
        if char_stat.upper()=="PR" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==29:
        # Beastmaster
        if char_stat.upper()=="PR" or char_stat.upper()=="ST":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==30:
        # Delver
        if char_stat.upper()=="EM" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==31:
        # Dervish
        if char_stat.upper()=="AG" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==32:
        # Monk
        if char_stat.upper()=="EM" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==33:
        # Montebanc
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==34:
        # Nightblade
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==35:
        # Noble Warrior
        if char_stat.upper()=="ST" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==36:
        # Paladin
        if char_stat.upper()=="IN" or char_stat.upper()=="ST":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==37:
        # Ranger
        if char_stat.upper()=="CO" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==38:
        # Sleuth
        if char_stat.upper()=="IN" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==39:
        # Warrior Mage
        if char_stat.upper()=="ST" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==40:
        # Archmage
        if char_stat.upper()=="IN" or char_stat.upper()=="EM" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==41:
        # Astrologer
        if char_stat.upper()=="IN" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==42:
        # Crystal Mage
        if char_stat.upper()=="PR" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==43:
        # Magus
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==44:
        # Mystic
        if char_stat.upper()=="PR" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==45:
        # Necromancer
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==46:
        # Sorceror
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==47:
        # Warlock
        if char_stat.upper()=="IN" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==48:
        # Witch
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    return num

import os.path

def pr_text():
    print "This is a Prime requisite and must be 90 or higher"

poten=2
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

num=""
print num
def prime_req(pro,char_stat,num):
    if pro==1:
        # Barbarian
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==2:
        # Burglar
        if char_stat.upper()=="AG" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==3:
        # Dancer
        if char_stat.upper()=="AG" or char_stat.upper()=="QU":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==4:
        # Fighter
        if char_stat.upper()=="ST" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==5:
        # High Warrior Monk
        if char_stat.upper()=="AG" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==6:
        # Rogue
        if char_stat.upper()=="ST" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==7:
        # Scholar
        if char_stat.upper()=="IN" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==8:
        # Theif
        if char_stat.upper()=="AG" or char_stat.upper()=="QU":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==9:
        # Trader
        if char_stat.upper()=="AG" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==10:
        # Warrior Monk
        if char_stat.upper()=="QU" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==11:
        # Alchemist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==12:
        # Animist
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==13:
        # Cleric
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==14:
        # Conjuror
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==15:
        # Druid
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==16:
        # Healer
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==17:
        # Illusionist
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==18:
        # Lay Healer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==19:
        # Magician
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==20:
        # Mentalist
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==21:
        # Runemaster
        if char_stat.upper()=="EM" or char_stat.upper()=="RE":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==22:
        # Sage
        if char_stat.upper()=="PR" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==23:
        # Seer
        if char_stat.upper()=="PR" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==24:
        # Shaman
        if char_stat.upper()=="IN" or char_stat.upper()=="ME":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==25:
        # Bard
        if char_stat.upper()=="PR" or char_stat.upper()=="MR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==26:
        # Beastmaster
        if char_stat.upper()=="ST" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==27:
        # Delver
        if char_stat.upper()=="EM" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==28:
        # Dervish
        if char_stat.upper()=="IN" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==29:
        # Monk
        if char_stat.upper()=="EM" or char_stat.upper()=="SD":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==30:
        # Nightblade
        if char_stat.upper()=="PR" or char_stat.upper()=="AG":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==31:
        # Paladin
        if char_stat.upper()=="ST" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==32:
        # Ranger
        if char_stat.upper()=="IN" or char_stat.upper()=="CO":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==33:
        # Warrior Mage
        if char_stat.upper()=="ST" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==34:
        # Astrologer
        if char_stat.upper()=="PR" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==35:
        # Mystic
        if char_stat.upper()=="PR" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==36:
        # Necromancer
        if char_stat.upper()=="EM" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==37:
        # Sorceror
        if char_stat.upper()=="EM" or char_stat.upper()=="IN":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==38:
        # Warlock
        if char_stat.upper()=="IN" or char_stat.upper()=="PR":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    elif pro==39:
        # Witch
        if char_stat.upper()=="IN" or char_stat.upper()=="EM":
            while num<90 or num>=102:
                pr_text()
                num=int(raw_input('Enter a new number: '))
    return num

st_pot_in,qu_pot_in,pr_pot_in,in_pot_in,em_pot_in=0,0,0,0,0
co_pot_in,ag_pot_in,sd_pot_in,me_pot_in,re_pot_in=0,0,0,0,0

def create_char():
    user_name=str(raw_input('Please enter your name: '))
    if os.path.exists(user_name+".txt") == True:
        print "Character exists"
        exit
    else:
        file = open(user_name+".txt","w")
        file.write(user_name)
        file.write(":")

    print 25 * "-" , "Professions", 25 * "-"
    print ""
    print 15 * "-" , "Non" , 15 * "-"
    print "1. Barbarian          2. Burglar"
    print "3. Dancer             4. Fighter"
    print "5. High Warrior Monk  6. Rogue"
    print "7. Scholar            8. Thief"
    print "9. Trader             10. Warrior Monk"
    print ""
    print 15 * "-", "Pure", 15 * "-"
    print "11. Alchemist        12. Animist"
    print "13. Cleric           14. Conjuror"
    print "15. Druid            16. Healer"
    print "17. Illusionist      18. Lay Healer"
    print "19. Magician         20. Mentalist"
    print "21. Runemaster       22. Sage"
    print "23. Seer             24. Shaman"
    print ""
    print 15 * "-", "Semi", 15 * "-"
    print "25. Bard             26. Beastmaster"
    print "27. Delver           28. Dervish"
    print "29. Monk             30. Nightblade"
    print "31. Paladin          32. Ranger"
    print "33. Warrior Mage"
    print ""
    print 15 * "-", "Hybrid", 15 * "-"
    print "34. Astrologer        35. Mystic"
    print "36. Necromancer       37. Sorcerer"
    print "38. Warlock           39. Witch"
    print 63 * "-"
    pro_ch=int(raw_input('Select Profession: '))
    if pro_ch==1:
        pro_name="Barbarian"
    elif pro_ch==2:
        pro_name="Burglar"
    elif pro_ch==3:
        pro_name="Dancer"
    elif pro_ch==4:
        pro_name="Fighter"
    elif pro_ch==5:
        pro_name="High Warrior Monk"
    elif pro_ch==6:
        pro_name="Rogue"
    elif pro_ch==7:
        pro_name="Scholar"
    elif pro_ch==8:
        pro_name="Thief"
    elif pro_ch==9:
        pro_name="Trader"
    elif pro_ch==10:
        pro_name="Warrior Monk"
    elif pro_ch==11:
        pro_name="Alchemist"
    elif pro_ch==12:
        pro_name="Animist"
    elif pro_ch==13:
        pro_name="Cleric"
    elif pro_ch==14:
        pro_name="Conjuror"
    elif pro_ch==15:
        pro_name="Druid"
    elif pro_ch==16:
        pro_name="Healer"
    elif pro_ch==17:
        pro_name="Illusionist"
    elif pro_ch==18:
        pro_name="Lay Healer"
    elif pro_ch==19:
        pro_name="Magician"
    elif pro_ch==20:
        pro_name="Mentalist"
    elif pro_ch==21:
        pro_name="Runemaster"
    elif pro_ch==22:
        pro_name="Sage"
    elif pro_ch==23:
        pro_name="Seer"
    elif pro_ch==24:
        pro_name="Shaman"
    elif pro_ch==25:
        pro_name="Bard"
    elif pro_ch==26:
        pro_name="Beastmaster"
    elif pro_ch==27:
        pro_name="Delver"
    elif pro_ch==28:
        pro_name="Dervish"
    elif pro_ch==29:
        pro_name="Monk"
    elif pro_ch==30:
        pro_name="Nightblade"
    elif pro_ch==31:
        pro_name="Paladin"
    elif pro_ch==32:
        pro_name="Ranger"
    elif pro_ch==33:
        pro_name="Warrior Mage"
    elif pro_ch==34:
        pro_name="Astrologer"
    elif pro_ch==35:
        pro_name="Mystic"
    elif pro_ch==36:
        pro_name="Necromancer"
    elif pro_ch==37:
        pro_name="Sorcerer"
    elif pro_ch==38:
        pro_name="Warlock"
    elif pro_ch==39:
        pro_name="Witch"

    file.write(pro_name)
    file.write(":")
    print 10 * "-"

    # Select Race
    print ""
    print 10 * "-", "Race", 10 * "-"
    print ""
    print "1. Common Man"
    print "2. Wood Elf      3. High Elf      4. Half-elf"
    print "5. Grey Elf      6. Aquatic Elf   7. Dark Elf"
    print ""
    print "8. Tallfellow Halfling      9. Stout Halfling"
    print ""
    print "10. Dwarf        11. Half-Dwarf"
    print "12. Half-Orc   13. Half-Ogre    14. Half-Troll"
    print ""
    print 25 * "-"

    race_input=int(raw_input('Select a Race: '))
    print race_input
    if race_input==1:
        file.write("Common Man")
        file.write(":")
    elif race_input==2:
        file.write("Wood Elf")
        file.write(":")
    elif race_input==3:
        file.write("High Elf")
        file.write(":")
    elif race_input==4:
        file.write("Half-elf")
        file.write(":")
    elif race_input==5:
        file.write("Grey Elf")
        file.write(":")
    elif race_input==6:
        file.write("Aquatic Elf")
        file.write(":")
    elif race_input==7:
        file.write("Dark Elf")
        file.write(":")
    elif race_input==8:
        file.write("Tallfellow Halfling")
        file.write(":")
    elif race_input==9:
        file.write("Stout Halfling")
        file.write(":")
    elif race_input==10:
        file.write("Dwarf")
        file.write(":")
    elif race_input==11:
        file.write("Half-Dwarf")
        file.write(":")
    elif race_input==12:
        file.write("Half-Orc")
        file.write(":")
    elif race_input==13:
        file.write("Half-Ogre")
        file.write(":")
    elif race_input==14:
        file.write("Half-Troll")
        file.write(":")

    # Enter statistic values
    st_stat_input=int(raw_input('Strength: '))
    st_stat=prime_req(pro_ch,"st",st_stat_input)
    #print "ST: %s" % st_stat
    file.write(str(st_stat))
    file.write(":")

    qu_stat_input=int(raw_input('Quickness: '))
    qu_stat=prime_req(pro_ch,"qu",qu_stat_input)
    #print "QU: %s" % qu_stat
    file.write(str(qu_stat))
    file.write(":")

    pr_stat_input=int(raw_input('Presence: '))
    pr_stat=prime_req(pro_ch,"pr",pr_stat_input)
    #print "PR: %s" % pr_stat
    file.write(str(pr_stat))
    file.write(":")

    in_stat_input=int(raw_input('Intuition: '))
    in_stat=prime_req(pro_ch,"in",in_stat_input)
    #print "IN: %s" % in_stat
    file.write(str(in_stat))
    file.write(":")

    em_stat_input=int(raw_input('Empathy: '))
    em_stat=prime_req(pro_ch,"em",em_stat_input)
    #print "EM: %s" % em_stat
    file.write(str(em_stat))
    file.write(":")

    co_stat_input=int(raw_input('Constitution: '))
    co_stat=prime_req(pro_ch,"co",co_stat_input)
    #print "CO: %s" % co_stat
    file.write(str(co_stat))
    file.write(":")

    ag_stat_input=int(raw_input('Agility: '))
    ag_stat=prime_req(pro_ch,"ag",ag_stat_input)
    #print "AG: %s" % ag_stat
    file.write(str(ag_stat))
    file.write(":")

    sd_stat_input=int(raw_input('Self-Discipline: '))
    sd_stat=prime_req(pro_ch,"sd",sd_stat_input)
    #print "SD: %s" % sd_stat
    file.write(str(sd_stat))
    file.write(":")

    me_stat_input=int(raw_input('Memory: '))
    me_stat=prime_req(pro_ch,"me",me_stat_input)
    #print "ME: %s" % me_stat
    file.write(str(me_stat))
    file.write(":")

    re_stat_input=int(raw_input('Reasoning: '))
    re_stat=prime_req(pro_ch,"re",re_stat_input)
    #print "RE: %s" % re_stat
    file.write(str(re_stat))
    file.write(":")

    # Calculate Potential Value
    st_pot_in=int(raw_input('Potential Roll (ST): '))
    st_pot=pot_calc(st_stat,st_pot_in)
    #print "ST Pot: %s" % st_pot
    file.write(str(st_pot))
    file.write(":")

    qu_pot_in=int(raw_input('Potential Roll (QU): '))
    qu_pot=pot_calc(qu_stat,qu_pot_in)
    #print "QU Pot: %s" % qu_pot
    file.write(str(qu_pot))
    file.write(":")

    pr_pot_in=int(raw_input('Potential Roll (PR): '))
    pr_pot=pot_calc(pr_stat,pr_pot_in)
    #print "PR Pot: %s" % pr_pot
    file.write(str(pr_pot))
    file.write(":")

    in_pot_in=int(raw_input('Potential Roll (IN): '))
    in_pot=pot_calc(in_stat,in_pot_in)
    #print "IN Pot: %s" % in_pot
    file.write(str(in_pot))
    file.write(":")

    em_pot_in=int(raw_input('Potential Roll (EM): '))
    em_pot=pot_calc(em_stat,em_pot_in)
    #print "EM Pot: %s" % em_pot
    file.write(str(em_pot))
    file.write(":")

    co_pot_in=int(raw_input('Potential Roll (CO): '))
    co_pot=pot_calc(co_stat,co_pot_in)
    #print "CO Pot: %s" % co_pot
    file.write(str(co_pot))
    file.write(":")

    ag_pot_in=int(raw_input('Potential Roll (AG): '))
    ag_pot=pot_calc(ag_stat,ag_pot_in)
    #print "AG Pot: %s" % ag_pot
    file.write(str(ag_pot))
    file.write(":")

    sd_pot_in=int(raw_input('Potential Roll (SD): '))
    sd_pot=pot_calc(sd_stat,sd_pot_in)
    #print "SD Pot: %s" % sd_pot
    file.write(str(sd_pot))
    file.write(":")

    me_pot_in=int(raw_input('Potential Roll (ME): '))
    me_pot=pot_calc(me_stat,me_pot_in)
    #print "ME Pot: %s" % me_pot
    file.write(str(me_pot))
    file.write(":")

    re_pot_in=int(raw_input('Potential Roll (RE): '))
    re_pot=pot_calc(re_stat,re_pot_in)
    #print "RE Pot: %s" % re_pot
    file.write(str(re_pot))
    file.write(":")

    print 10 * "-"

    file.close()
    file=open(user_name+".txt","r")
    print file.read()

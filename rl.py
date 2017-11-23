import json
import re
import os.path
from natsort import natsorted, ns

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'

########
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

def char_menu_level(char_name):
    menu_items=[]
    menu_sort=[]
    i=1
    lvl=0
    print 5 * "-", "Level", 5 * "-"
    print
    char_dir_files=char_dir+"/"+char_name
    p=len(os.listdir(char_dir_files))
    for json in os.listdir(char_dir_files):
        if i < p:
            menu_items.insert(i,json)
            i+=1
            lvl+=1
    menu_sort.insert(i,natsorted(menu_items, key=lambda json: json))
    ml=len(menu_sort[0])
    '''
    i=1
    lvl=0
    while lvl<ml:
        # Testing
        #print "{}.) Level :{} - {:15}:{}".format(lvl,lvl,char_name,menu_sort[0][lvl])
        print "{}.) Level :{} - {:15}".format(lvl,lvl,char_name)
        lvl+=1
    '''
    print 25 * "-"
    ch_lvl=raw_input('Select Level: ')
    #char_lvl=char_dir_files+"/"+char_name+"-"+ch_lvl+".json"
    skill_dict={}
    with open(char_dir_files+"/"+char_name+".json","r") as rl:
        skill_dict = json.load(rl)
    print skill_dict

def raise_level():
    p=char_menu()
    menu_len=len(p)
    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"
    #skill_dict={}
    skill_list=[]
    #print p
    s-=1
    with open(char_dir+"/"+p[s]+"/"+p[s]+".json") as f:
        char_dict=json.load(f)

    # load for skill list count
    with open(cfg_dir+"/ds.csv") as f:
        sl=f.read().splitlines()
    print len(sl),":len"
    s=1
    skill_dict={}
    pro_name=char_dict['pro_name']

    print
    print "| 1.) A      10.) J      19.) U"
    print "| 2.) B      11.) L      20.) V"
    print "| 3.) C      12.) M      21.) W"
    print "| 4.) D      13.) N      22.) Y"
    print "| 5.) E      14.) P"
    print "| 6.) F      15.) Q"
    print "| 7.) G      16.) R"
    print "| 8.) H      17.) S"
    print "| 9.) I      18.) T"
    print
    ska=int(raw_input('Select First Letter of Skill: '))
    print

    # Setup lists for skills
    alist,blist,clist,dlist,elist=([] for i1 in range(5))
    flist,glist,hlist,ilist,jlist=([] for i2 in range(5))
    llist,mlist,nlist,plist,qlist=([] for i3 in range(5))
    rlist,slist,tlist,ulist,vlist,wlist,ylist=([] for i4 in range(7))

    for words in char_dict:
        if words.isdigit():
            sk=1
            if ska == 1 and char_dict[words][0].startswith('A'):
                alist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                alst=sorted(alist, key=lambda skill: skill[1])

            if ska == 2 and char_dict[words][0].startswith('B'):
                blist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                blst=sorted(blist, key=lambda skill: skill[1])

            if ska == 3 and char_dict[words][0].startswith('C'):
                clist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                clst=sorted(clist, key=lambda skill: skill[1])

            if ska == 4 and char_dict[words][0].startswith('D'):
                dlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                dlst=sorted(dlist, key=lambda skill: skill[1])

            if ska == 5 and char_dict[words][0].startswith('E'):
                elist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                elst=sorted(elist, key=lambda skill: skill[1])

            if ska == 6 and char_dict[words][0].startswith('F'):
                flist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                flst=sorted(flist, key=lambda skill: skill[1])

            if ska == 7 and char_dict[words][0].startswith('G'):
                glist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                glst=sorted(glist, key=lambda skill: skill[1])

            if ska == 8 and char_dict[words][0].startswith('H'):
                hlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                hlst=sorted(hlist, key=lambda skill: skill[1])

            if ska == 9 and char_dict[words][0].startswith('I'):
                ilist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                ilst=sorted(ilist, key=lambda skill: skill[1])

            if ska == 10 and char_dict[words][0].startswith('J'):
                jlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                jlst=sorted(jlist, key=lambda skill: skill[1])

            if ska == 11 and char_dict[words][0].startswith('L'):
                llist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                llst=sorted(llist, key=lambda skill: skill[1])

            if ska == 12 and char_dict[words][0].startswith('M'):
                mlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                mlst=sorted(mlist, key=lambda skill: skill[1])

            if ska == 13 and char_dict[words][0].startswith('N'):
                nlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                nlst=sorted(nlist, key=lambda skill: skill[1])

            if ska == 14 and char_dict[words][0].startswith('P'):
                plist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                plst=sorted(plist, key=lambda skill: skill[1])

            if ska == 15 and char_dict[words][0].startswith('Q'):
                qlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                qlst=sorted(qlist, key=lambda skill: skill[1])

            if ska == 16 and char_dict[words][0].startswith('R'):
                rlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                rlst=sorted(rlist, key=lambda skill: skill[1])

            if ska == 17 and char_dict[words][0].startswith('S'):
                slist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                slst=sorted(slist, key=lambda skill: skill[1])

            if ska == 18 and char_dict[words][0].startswith('T'):
                tlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                tlst=sorted(tlist, key=lambda skill: skill[1])

            if ska == 19 and char_dict[words][0].startswith('U'):
                ulist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                ulst=sorted(ulist, key=lambda skill: skill[1])

            if ska == 20 and char_dict[words][0].startswith('V'):
                vlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                vlst=sorted(vlist, key=lambda skill: skill[1])

            if ska == 21 and char_dict[words][0].startswith('W'):
                wlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                wlst=sorted(wlist, key=lambda skill: skill[1])

            if ska == 22 and char_dict[words][0].startswith('Y'):
                ylist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                ylst=sorted(ylist, key=lambda skill: skill[1])

    skill_loop=True
    while skill_loop:
        print "      | {:32}|{:^8}|{:^5}|".format("Skill","Stats","Cost")
        print 56 * "-"
        if ska == 1:
            x=1
            for askills in alst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,askills[0],askills[1],askills[3])
                x+=1
        if ska == 2:
            x=1
            for bskills in blst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,bskills[0],bskills[1],bskills[3])
                x+=1
        if ska == 3:
            x=1
            for cskills in clst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,cskills[0],cskills[1],cskills[3])
                x+=1
        if ska == 4:
            x=1
            for dskills in dlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,dskills[0],dskills[1],dskills[3])
                x+=1
        if ska == 5:
            x=1
            for eskills in elst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,eskills[0],eskills[1],eskills[3])
                x+=1
        if ska == 6:
            x=1
            for fskills in flst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,fskills[0],fskills[1],fskills[3])
                x+=1
        if ska == 7:
            x=1
            for gskills in glst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,gskills[0],gskills[1],gskills[3])
                x+=1
        if ska == 8:
            x=1
            for hskills in hlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,hskills[0],hskills[1],hskills[3])
                x+=1
        if ska == 9:
            x=1
            for iskills in ilst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,iskills[0],iskills[1],iskills[3])
                x+=1
        if ska == 10:
            x=1
            for jskills in jlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,jskills[0],jskills[1],jskills[3])
                x+=1
        if ska == 11:
            x=1
            for lskills in llst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,lskills[0],lskills[1],lskills[3])
                x+=1
        if ska == 12:
            x=1
            for mskills in mlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,mskills[0],mskills[1],mskills[3])
                x+=1
        if ska == 13:
            x=1
            for nskills in nlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,nskills[0],nskills[1],nskills[3])
                x+=1
        if ska == 14:
            x=1
            for pskills in plst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,pskills[0],pskills[1],pskills[3])
                x+=1
        if ska == 15:
            x=1
            for qskills in qlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,qskills[0],qskills[1],qskills[3])
                x+=1
        if ska == 16:
            x=1
            for rskills in rlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,rskills[0],rskills[1],rskills[3])
                x+=1
        if ska == 17:
            x=1
            for sskills in slst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,sskills[0],sskills[1],sskills[3])
                x+=1
        if ska == 18:
            x=1
            for tskills in tlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,tskills[0],tskills[1],tskills[3])
                x+=1
        if ska == 19:
            x=1
            for uskills in ulst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,uskills[0],uskills[1],uskills[3])
                x+=1
        if ska == 20:
            x=1
            for vskills in vlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,vskills[0],vskills[1],vskills[3])
                x+=1
        if ska == 21:
            x=1
            for wskills in wlst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,wskills[0],wskills[1],wskills[3])
                x+=1
        if ska == 22:
            # 'Y'
            x=1
            for yskills in ylst:
                print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(x,yskills[0],yskills[1],yskills[3])
                x+=1
            y=loop_done()
            if y == "False":
                skill_loop=False

def loop_done():
    print
    print "  X.) Back"
    sub_skill=raw_input('Select a skill: ')
    # Exit skil loop
    if sub_skill == "X" or sub_skill == "x":
        loops=="False"
    return loops

raise_level()

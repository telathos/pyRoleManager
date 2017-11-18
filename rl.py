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
    print "| 1.) A      10.) J      19.) S"
    print "| 2.) B                  20.) T"
    print "| 3.) C      12.) L      21.) U"
    print "| 4.) D      13.) M      22.) V"
    print "| 5.) E      14.) N      23.) W"
    print "| 6.) F                        "
    print "| 7.) G      16.) P      25.) Y"
    print "| 8.) H      17.) Q            "
    print "| 9.) I      18.) R"
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
            if ska == 1 and char_dict[words][0].startswith('A'):
                alist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                alst=sorted(alist, key=lambda skill: skill[1])
                print alist
                print "----- A ------"

            if ska == 2 and char_dict[words][0].startswith('B'):
                blist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                blst=sorted(blist, key=lambda skill: skill[1])
                print blist
                print "----- B ------"

            if ska == 3 and char_dict[words][0].startswith('C'):
                clist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                clst=sorted(clist, key=lambda skill: skill[1])
                print clist
                print "----- C ------"

            if ska == 4 and char_dict[words][0].startswith('D'):
                dlist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                dlst=sorted(dlist, key=lambda skill: skill[1])
                print dlist
                print "----- D ------"

            if ska == 5 and char_dict[words][0].startswith('E'):
                elist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                elst=sorted(elist, key=lambda skill: skill[1])
                print elist
                print "----- E ------"

            if ska == 6 and char_dict[words][0].startswith('F'):
                flist.append([char_dict[words][0],char_dict[words][1],char_dict[words][2],char_dict[words][3]])
                flst=sorted(flist, key=lambda skill: skill[1])
                print flist
                print "----- F ------"

            if ska == 7 and skill_dict[words][0].startswith('G'):
                glist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                glst=sorted(glist, key=lambda skill: skill[1])

            if ska == 8 and skill_dict[words][0].startswith('H'):
                hlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                hlst=sorted(hlist, key=lambda skill: skill[1])

            if ska == 9 and skill_dict[words][0].startswith('I'):
                ilist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                ilst=sorted(ilist, key=lambda skill: skill[1])

            if ska == 10 and skill_dict[words][0].startswith('J'):
                jlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                jlst=sorted(jlist, key=lambda skill: skill[1])

            if ska == 12 and skill_dict[words][0].startswith('L'):
                llist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                llst=sorted(llist, key=lambda skill: skill[1])

            if ska == 13 and skill_dict[words][0].startswith('M'):
                mlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                mlst=sorted(mlist, key=lambda skill: skill[1])

            if ska == 14 and skill_dict[words][0].startswith('N'):
                nlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                nlst=sorted(nlist, key=lambda skill: skill[1])

            if ska == 16 and skill_dict[words][0].startswith('P'):
                plist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                plst=sorted(plist, key=lambda skill: skill[1])

            if ska == 17 and skill_dict[words][0].startswith('Q'):
                qlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                qlst=sorted(qlist, key=lambda skill: skill[1])

            if ska == 18 and skill_dict[words][0].startswith('R'):
                rlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                rlst=sorted(rlist, key=lambda skill: skill[1])

            if ska == 19 and skill_dict[words][0].startswith('S'):
                slist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                slst=sorted(slist, key=lambda skill: skill[1])

            if ska == 20 and skill_dict[words][0].startswith('T'):
                tlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                tlst=sorted(tlist, key=lambda skill: skill[1])

            if ska == 21 and skill_dict[words][0].startswith('U'):
                ulist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                ulst=sorted(ulist, key=lambda skill: skill[1])

            if ska == 22 and skill_dict[words][0].startswith('V'):
                vlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                vlst=sorted(vlist, key=lambda skill: skill[1])

            if ska == 23 and skill_dict[words][0].startswith('W'):
                wlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                wlst=sorted(wlist, key=lambda skill: skill[1])

            if ska == 25 and skill_dict[words][0].startswith('Y'):
                ylist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
                ylst=sorted(ylist, key=lambda skill: skill[1])

    x=1
    while x <= len(sl):
        #print char_dict[`x`]
        #print
        x+=1

raise_level()

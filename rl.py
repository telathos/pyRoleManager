import json
import re

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'
## Testing code ##
pro_name=17

##########

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

skill_dict={}


with open(cfg_dir+"/ds.csv") as f:
    sl=f.read().splitlines()
f.close()
skill_list=[]

for list in sl:
    skill_list.append(list.split(","))
y=len(skill_list)
s=1

for outer_list in skill_list:
    s=outer_list[0]
    skill_dict[s]=(outer_list[0],outer_list[1],outer_list[5],outer_list[pro_name])

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
rlist,slist,tlist,ulist,vlist=([] for i4 in range(5))
wlist,ylist=([] for i5 in range(2))

for words in skill_dict:
    if ska == 1 and skill_dict[words][1].startswith('A'):
        alist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        alst=sorted(alist, key=lambda skill: skill[1])

    if ska == 2 and skill_dict[words][1].startswith('B'):
        blist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        blst=sorted(blist, key=lambda skill: skill[1])

    if ska == 3 and skill_dict[words][1].startswith('C'):
        clist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        clst=sorted(clist, key=lambda skill: skill[1])

    if ska == 4 and skill_dict[words][1].startswith('D'):
        dlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        dlst=sorted(dlist, key=lambda skill: skill[1])

    if ska == 5 and skill_dict[words][1].startswith('E'):
        elist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        elst=sorted(elist, key=lambda skill: skill[1])

    if ska == 6 and skill_dict[words][1].startswith('F'):
        flist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        flst=sorted(flist, key=lambda skill: skill[1])

    if ska == 7 and skill_dict[words][1].startswith('G'):
        glist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        glst=sorted(glist, key=lambda skill: skill[1])

    if ska == 8 and skill_dict[words][1].startswith('H'):
        hlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        hlst=sorted(hlist, key=lambda skill: skill[1])

    if ska == 9 and skill_dict[words][1].startswith('I'):
        ilist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        ilst=sorted(ilist, key=lambda skill: skill[1])

    if ska == 10 and skill_dict[words][1].startswith('J'):
        jlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        jlst=sorted(jlist, key=lambda skill: skill[1])

    if ska == 12 and skill_dict[words][1].startswith('L'):
        llist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        llst=sorted(llist, key=lambda skill: skill[1])

    if ska == 13 and skill_dict[words][1].startswith('M'):
        mlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        mlst=sorted(mlist, key=lambda skill: skill[1])

    if ska == 14 and skill_dict[words][1].startswith('N'):
        nlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        nlst=sorted(nlist, key=lambda skill: skill[1])

    if ska == 16 and skill_dict[words][1].startswith('P'):
        plist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        plst=sorted(plist, key=lambda skill: skill[1])

    if ska == 17 and skill_dict[words][1].startswith('Q'):
        qlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        qlst=sorted(qlist, key=lambda skill: skill[1])

    if ska == 18 and skill_dict[words][1].startswith('R'):
        rlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        rlst=sorted(rlist, key=lambda skill: skill[1])

    if ska == 19 and skill_dict[words][1].startswith('S'):
        slist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        slst=sorted(slist, key=lambda skill: skill[1])

    if ska == 20 and skill_dict[words][1].startswith('T'):
        tlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        tlst=sorted(tlist, key=lambda skill: skill[1])

    if ska == 21 and skill_dict[words][1].startswith('U'):
        ulist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        ulst=sorted(ulist, key=lambda skill: skill[1])

    if ska == 22 and skill_dict[words][1].startswith('V'):
        vlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        vlst=sorted(vlist, key=lambda skill: skill[1])

    if ska == 23 and skill_dict[words][1].startswith('W'):
        wlist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        wlst=sorted(wlist, key=lambda skill: skill[1])

    if ska == 25 and skill_dict[words][1].startswith('Y'):
        ylist.append([skill_dict[words][0],skill_dict[words][1],skill_dict[words][2],skill_dict[words][3]])
        ylst=sorted(ylist, key=lambda skill: skill[1])

skill_loop=True
while skill_loop:
    print "      | {:32}|{:^8}|{:^5}|".format("Skill","Stats","Cost")
    print 56 * "-"
    if ska == 1:
        for askills in alst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(askills[0],askills[1],askills[2],askills[3])
    if ska == 2:
        for bskills in blst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(bskills[0],bskills[1],bskills[2],bskills[3])
    if ska == 3:
        for cskills in clst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(cskills[0],cskills[1],cskills[2],cskills[3])
    if ska == 4:
        for dskills in dlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(dskills[0],dskills[1],dskills[2],dskills[3])
    if ska == 5:
        for eskills in elst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(eskills[0],eskills[1],eskills[2],eskills[3])
    if ska == 6:
        for fskills in flst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(fskills[0],fskills[1],fskills[2],fskills[3])
    if ska == 7:
        for gskills in glst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(gskills[0],gskills[1],gskills[2],gskills[3])
    if ska == 8:
        for hskills in hlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(hskills[0],hskills[1],hskills[2],hskills[3])
    if ska == 9:
        for iskills in ilst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(iskills[0],iskills[1],iskills[2],iskills[3])
    if ska == 10:
        for jskills in jlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(jskills[0],jskills[1],jskills[2],jskills[3])
    if ska == 12:
        for lskills in llst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(lskills[0],lskills[1],lskills[2],lskills[3])
    if ska == 13:
        for mskills in mlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(mskills[0],mskills[1],mskills[2],mskills[3])
    if ska == 14:
        for nskills in nlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(nskills[0],nskills[1],nskills[2],nskills[3])
    if ska == 16:
        for pskills in plst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(pskills[0],pskills[1],pskills[2],pskills[3])
    if ska == 17:
        for qskills in qlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(qskills[0],qskills[1],qskills[2],qskills[3])
    if ska == 18:
        for rskills in rlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(rskills[0],rskills[1],rskills[2],rskills[3])
    if ska == 19:
        for sskills in slst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(sskills[0],sskills[1],sskills[2],sskills[3])
    if ska == 20:
        for tskills in tlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(tskills[0],tskills[1],tskills[2],tskills[3])
    if ska == 21:
        for uskills in ulst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(uskills[0],uskills[1],uskills[2],uskills[3])
    if ska == 22:
        for vskills in vlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(vskills[0],vskills[1],vskills[2],vskills[3])
    if ska == 23:
        for wskills in wlst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(wskills[0],wskills[1],wskills[2],wskills[3])
    if ska == 25:
        for yskills in ylst:
            print "{:>3}.) | {:32}|{:^8}|{:^5}|".format(yskills[0],yskills[1],yskills[2],yskills[3])

    print
    print "  X.) Back"
    sub_skill=raw_input('Select a skill: ')
    print sub_skill
    if sub_skill == "X" or sub_skill == "x":
        print "quit"
        skill_loop=False
print

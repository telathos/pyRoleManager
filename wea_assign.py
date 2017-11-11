### Initial display of Weapon Categories and costs for the profession
print
wlist=['1-HS','1-HC','2-H','Thrown','Missile','Polearm']
wc,wmenu=2,1
wea_asign={}
print "List of weapon costs"

for x1 in wlist:
    print "{:1}.){:^5}      {:1}.) {:10}".format(wmenu,plist[pro_ch][wc],wmenu,x1)
    wc+=1
    wmenu+=1
print
print "Select a cost to assign to a weapon category"

# Select the weapon cost within range
wea=int(raw_input('Select weapon cost: '))
while 0<=wea>7: # Check that input is in the range
    print "You must select a number between (1 and 6)"
    wea=int(raw_input('Select weapon cost: '))

# Select the weapon category
wclist=int(raw_input('Select weapon category: '))

### Loop through categories and cost until all costs are assigned
wea_loop=True
# Add selections to dictionary
x2=wlist[wclist-1]
print x2
wea_asign[x2]=plist[pro_ch][wea+1]
print wea_asign,":wea_asign"
# Categories remove from lists
wlist.pop(wclist-1)
plist[pro_ch].pop(wea+1)

while wea_loop:
# Reset counters
    wc,wmenu=2,1
    # Create menu
    for x1 in wlist:
        print "{:1}.){:^5}      {:1}.) {:10}".format(wmenu,plist[pro_ch][wc],wmenu,x1)
        wc+=1
        wmenu+=1
    wea=int(raw_input('Select weapon cost: '))
    while 0<=wea>len(wlist): # Check that input is in the range
        print "You must select a number between (1 and %i)" % len(wlist)
        wea=int(raw_input('Select weapon cost: '))

    # Select the weapon category
    wclist=int(raw_input('Select weapon category: '))

    # Add to Dictionary
    x2=wlist[wclist-1]
    wea_asign[x2]=plist[pro_ch][wea+1]
    print wea_asign,":wea_asign2"
    print wclist,":wclist category"
    print wlist,":wlist"
    # Remove selections from lists
    wlist.pop(wclist-1)
    plist[pro_ch].pop(wea+1)
    if len(wlist)==0:
        wea_loop=False

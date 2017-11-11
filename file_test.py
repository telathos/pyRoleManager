cfg_dir="cfg"
with open(cfg_dir+"/sttchart.csv") as f:
    statchart =f.readlines()
f.close()

#statchart= statchart.strip("\n")
for x in statchart:
    print "line:",x
#print statchart

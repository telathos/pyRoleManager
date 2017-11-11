import json
import re

char_dir="char"
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

# Open the file
with open(char_dir+"/crystal.json","r") as cf:
    char_dict = json.load(cf)
#print "Name: ",char_dict['name']
#print char_dict['s227']
#print char_dict['s228']
#print 25 * "-"

sslist=[]
pattern=re.compile("^s[0-9]+")
for x in char_dict.keys():
    if pattern.match(x):
        #print "Match: ",x
        sslist.append(x)
    else:
        pass
sslist.sort(key=natural_keys)
skcnt=1
for key in sslist:
    print "| {:>3}.) {:35}|{:^10}|{:^5}|{:2}|{:2}|{:2}|".format(skcnt,char_dict[key][0],char_dict[key][1],char_dict[key][2],char_dict[key][4],char_dict[key][5],char_dict[key][6],char_dict[key][7])
    skcnt+=1
print 70 * "-"
print
sk=int(raw_input("Select a skill: "))
print sk

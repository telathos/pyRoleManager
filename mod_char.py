import os.path

char_dir="char"
cfg_dir="cfg"

char_data=""
# Create a menu of characters
def create_char_menu():
    menu_items = []
    global char_data

    def char_menu():
        i=1
        print 5 * "-", "Characters", 5 * "-"
        for file in os.listdir(char_dir):
            if file.endswith(".txt"):
                menu_list=file.split(".")[0]
                print i,".) ",menu_list.title()
                i+=1
                menu_items.insert(i,menu_list)
        print 25 * "-"
        return menu_items

    # Run menu
    p=char_menu()
    menu_len=len(p)
    #print "menu_len:",menu_len

    while True:
        s=int(raw_input("Select Character: "))
        if s >=1 and s<=menu_len:
            break
        else:
            print "Invalid Selection! Select a character from the list"

    # Open the character file
    file=open(char_dir+"/"+p[s-1]+".txt","r")
    char_data=file.read()
    file.close()
    #print char_data
    char_dict=[]
    counter=0

    for words in char_data.split(":"):
        #print counter,"-",words
        char_dict.insert(counter,words)
        counter+=1

    return (s, char_data)

create_char_menu()
#print char_data
cname=char_data.split(":")

# Open chart of stat values
with open(cfg_dir+"/ds.csv") as f:
    sl=f.read().splitlines()
f.close()
skill_list=[]

for list in sl:
    skill_list.append(list.split(","))
for outer_list in skill_list:
    print outer_list[1]
    with open(char_dir+"/"+cname[0]+".txt","a") as write_skill:
        write_skill.write(outer_list[1]'\n')
        write_skill.close()
    #print list
# print skill_list[0][1]
# print skill_list[2]

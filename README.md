# pyRoleManager
A Rolemaster Character Manager written in Python

# What is pyRoleManager
pyRoleManager will manage your Rolemaster 2nd edition or Rolemaster Classic characters.
The goal is to be able to manage all of the your character setting and stats, including base rate and armor bonuses and penalties.

It can display all of your character skills and stats to screen and export the results to an excel file.

# Application configuration
Update the location of the character and configuration file by editing cfgData.py. Change char_dir and cfg_dir to the location of the application.

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'

The default is set to multiple the development point by 125%. To change the multipler you will update the dp_multipler variable in the cfgData.py file. Setting it to 1.00 will set to the normal 100%. See the note in cfgData.py for more information.
dp_multipler = 1.25

Adding more genders, eye colors or hair colors edit cfgData.py and update the lists.
# How to Run
Open a command line (CMD) and type 'python pyRoleManager.py'. To run without adding the 'python' before pyRoleManager.py, open a command line as Administrator and run 'ftype Python.File="C:\python27\python.exe" "%1" %"'.
This will load a menu with the options.

# Known Bugs/Issues
The level raise code is still bugging. It doesn't always reset your development points correctly. The code needs to be reworked.
4/30/18 - I'm currently working on redesigning the program to improve the flow and speed.

## Add-on features
# Professions
More professions can be added to pyRoleManager by adding them the pro.csv file in the cfg subdirectory.
The format is as follows:
Profession Name, Profession ID, Weapon Category #1,Weapon Category #2,Weapon Category #3,Weapon Category #4,
Weapon Category #5,Weapon Category #6,Magic Realm, Academic skills level bonus, Arms skills level bonus, Athletic skills level bonus, Base Spell Casting level bonus, Body Development skill level bonus, Concentration skills level bonus, Deadly skills level bonus, Directed Spells level bonus, General skills level bonus, Linguistics skills level bonus, Magical skills level bonus, Medical skills level bonus, Outdoor skills level bonus, Perception skills level bonus, Social skills level bonus, and Subterfuge skills level bonus

Example:
Barbarian,10,1/5,2/5,3/8,4,4,6,NULL,0,3,2,0,2,0,0,0,0,0,0,0,3,0,0,0

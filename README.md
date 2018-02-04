# pyRoleManager
A Rolemaster Character Manager written in Python

# What is pyRoleManager
pyRoleManager will manage your Rolemaster 2nd edition or Rolemaster Classic characters.
The goal is to be able to manage all of the your character setting and stats, including base rate and armor bonuses and penalties.

It can display all of your character skills and stats to screen and export the results to an excel file.

# How to Run
Open a command line (CMD) and type 'pyhon pyRoleManager.py'
This will load a menu with the options.

# Known Bugs/Issues
The export feature does not update all of the skill calculations. You will need to use the display character menu option to update the calculations first.

## Add-on features
# Professions
More professions can be added to pyRoleManager by adding them the pro.csv file in the cfg subdirectory.
The format is as follows:
Profession Name, Profession ID, Weapon Category #1,Weapon Category #2,Weapon Category #3,Weapon Category #4,
Weapon Category #5,Weapon Category #6,Magic Realm, Academic skills level bonus, Arms skills level bonus, Athletic skills level bonus, Base Spell Casting level bonus, Body Development skill level bonus, Concentration skills level bonus, Deadly skills level bonus, Directed Spells level bonus, General skills level bonus, Linguistics skills level bonus, Magical skills level bonus, Medical skills level bonus, Outdoor skills level bonus, Perception skills level bonus, Social skills level bonus, and Subterfuge skills level bonus

Example:
Barbarian,10,1/5,2/5,3/8,4,4,6,NULL,0,3,2,0,2,0,0,0,0,0,0,0,3,0,0,0

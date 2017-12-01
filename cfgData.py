# Change the paths to where pyRoleManager is installed on your system_call

char_dir='c:\pyRoleManager\char'
cfg_dir='c:\pyRoleManager\cfg'

from colorama import Fore, Back, Style
import decimal

dp=0
dp_cur=0
space=' '
def running_dp(num):
    dp=decimal.Decimal(num)
    dp_cur=round(dp,0)
    print(72*space + Fore.RED + Back.WHITE + "DP:" + `dp_cur`)
    print (Style.RESET_ALL)

    return dp_cur

def skill_header():
    print 80 * "-"
    print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("","","","H","AD","AP","Std")
    print "      | {:32}|{:^8}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format("Skill","Stats","Cost","Rank","Rank","Rank","Rank")
    print 80 * "-"

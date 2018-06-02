import random
from os import system

def say(something):
    system('say "%s"' % something)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

SF = 'Spinning Film...'
# Introduction
START_PIC = '''
        <___<
 +@+____/___/_/====
 /<=~=\_@/=~=~=\_@/=>\n'''

Opening = '''
     /^\  /^\ _ /^\   
   /@/-\ _/-\/@\/-\ 
  |@#@| /@\|/#@} |\n'''

Chase1 = '''
    /^\ #  @    /^\ 
    /-\  @____# /-\ 
    /-\ @/_^_@\ /-\ 
     |  $\*__*/$ |\n'''
Chase2 = '''
    <?>  ,./,/./<     .,/
    <>?<?>  ____>$%$^$^%>?
    <>?  .#/_^_@\>?#<  @?$?
    #@$@$  \*__*/ *!#**#\n'''

print(bcolors.ENDC + START_PIC)
# Scene 1
not_solved = True
while not_solved:
    answer = raw_input()
    else:
        print(SF + bcolors.OKGREEN)
        not_solved = True
# Scene 2
not_solved = False
begin = True

print(bcolors.OKGREEN + Opening)
print(bcolors.WARNING + Chase1)
print(bcolors.FAIL + Chase2)

while begin:
    answer = raw_input()
    else:
        print(SF + bcolors.OKGREEN)
        begin = False
# Chapter 2
begin = False
Chap2 = True


max_counter, counter = 3, 0
while Chap2 and counter <= max_counter:
    answer = raw_input()
    if answer == 'yes':
        Chap2 = False
    elif answer == 'no':
        Chap2 = True
    else:
        Chap2 = True
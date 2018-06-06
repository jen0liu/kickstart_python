import random
import time
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

bank = 100
gas = 120

Uguz = 'Using Gasoline; '
Umoney = 'Using Money; '

Begg = 'You see a car Wreck' + bcolors.HEADER
Begg2 = 'Would you like to salvage?'

BeggYes = 'You attempt to salvage' + bcolors.WARNING
BeggGood = 'You succeded the salvage' + bcolors.OKGREEN

BeggBad = 'You did not Salvage'
BeggBad2 = 'You FAILED the Salvage' + bcolors.FAIL
Walk = 'You must walk into the Forest Shelter'
Walk2 = 'You see something beutiful...'

SF = 'Spinning film...'

drive = 'You may drive Now' + bcolors.OKGREEN
loc = 'Locations:' + bcolors.HEADER
loc2 = '1. Diamond City' + bcolors.WARNING
loc3 = '2. Capital Building' + bcolors.OKBLUE
loc4 = '3. Military Base' + bcolors.OKGREEN

loca2 = 'Travelling to...  Diamond City' + bcolors.WARNING
loca3 = 'Travelling to...  Capital Building' + bcolors.WARNING
loca4 = 'Travelling to... Military Base' + bcolors.WARNING

Diamond = 'You may Trade Goods here (1); or Refuel (2)' + bcolors.ENDC
Capital = 'Assault Building (1); or Infiltrate facility (2)' + bcolors.ENDC
Cap2 = 'Somehow you Wupped everyone"s @$$ and got the Capital'
Cap4 = 'You @$$ was Wupped so hard YOU DIED' + bcolors.WARNING
Cap3 = 'You snuck through the building and Got $$$'
Cap5 = 'You were caught and you RAN like Hail!!!'

loc5 = 'Somebody has no license... you crash!'
space = '   '
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

print(Chase2)
print(Begg)
print(Begg2)

answer = input()

if answer == 'Yes':
    print(BeggYes)
    a = random.randint(50,100)
    print(a)
    if a > 50:
        answer = 'Yes'
        print(BeggGood)
        print(drive)
        print(Chase1 + bcolors.FAIL)
        time.sleep(2)
        print(SF)
        time.sleep(2)
        print(space)
        print(loc)
        print(loc2)
        print(loc3)
        print(loc4)

        answer = input()
        g = random.randint(20, 30)
    # Diamond
        if answer == '1':
            gas = gas - g
            print(Uguz + str(g))
            print(loca2)
            time.sleep(2)
            print(Diamond)
            m = random.randint(20, 30)
            answer = input()
            if answer == '1':
                bank = bank + m
                money = '$Money$; ' + str(bank)
                print(money)
            elif answer == '2':
                gas = gas + m
                guz = 'Gasoline; ' + str(gas)
                print(guz)
    # Capital
        elif answer == '2':
            g = random.randint(20, 30)
            gas = gas - g
            print(Uguz + str(g))
            print(loca3)
            time.sleep(2)
            print(Capital)
            m = random.randint(0, 30)
            answer = input()
            if answer == '1':
                if m < 10:
                    print(Cap2)
                    bank = bank + g + g + g
                    gas = gas + g + g
                else:
                    print(Cap4)
            elif answer == '2':
                if m < 18:
                    print(Cap3)
                    bank = bank + g
                    money = '$Money$; ' + str(bank)
                    print(money)
                else:
                    print(Cap5)
                    gas = gas - str(g)
    # Military
        elif answer == '3':
            gas = gas - g
            print(Uguz + str(g))
            print(loca4)
            time.sleep(2)

            answer = input()
        else:
            print(loc5)
    else:
        print(BeggBad)
        time.sleep(1)
        print(Walk)
        time.sleep(2)
        print(Walk2)
        time.sleep(1)
        print(Opening + bcolors.OKGREEN)
elif answer == 'No':
    print(BeggBad)
else:
    print('Please enter Yes or No')
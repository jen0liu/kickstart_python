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

# Introduction
START_PIC = '''
        <___<
 +@+____/___/_/====
 /<=~=\_@/=~=~=\_@/=>\n'''

CHAP2_PIC = '''
         ____
 _~_____/___/_/=~~=
 /<<>>\_@/><@><\_@/=>\n'''

# Welcome Code
text = 'Beatles Editor'
text2 = 'Welcome, HAYSD'
Welcome = 'The Best Song'

Eleanor = 'Good decision Man, cool'
ADAY = 'Man I love that one too'
Guitar = 'Its good. Not best'
Silver = 'Are you an Old timer man?'
Penny = 'Thats pretty good.'
Sorry = 'Your Selected Option was unvariabled'
# Begin Code
text3 = 'Chapter 1, Common Math'
text4 = 'The smallest two numbers squared'
text4c = ' added together equal what square?'
YouAreDumb = 'You dumb piece of crap, are you retarded?'
Relief = 'Thank goodness, I thought you were Don Trump!'
DumbTry = 'For the love of Trump please try again!'
Num169 = 'Good Job, The number WAS 169!'
# Chap2 Code
NewCar2 = 'Heres your NEW downgraded Car! Enjoy it you lazy dog'
Appreciate = 'Do you Appreciate your new car Woman?'
Intro2 = 'Chapter 2, Human Appreciation'
Thanks2 = 'Oh My Philly Cheese steak. thanks that was all I ever wanted.'
Meanie2 = 'You are a big fat meanie face lady, get the hail out of here!'
CanYouEnglish2 = 'Do you have keyboard trouble?'
Thanks3 = 'To thank you for your cooperation I thought I should sing you a song,'
Thanks4 = ' lucy in the sky with diamonds, lucy in the sky with diamonds... ahhhh '
Thanks5 = 'picture yourself on a train in a station with pastaline quarters and looking glass eyes.'
print(bcolors.ENDC + START_PIC)
print(bcolors.HEADER + text)
print(bcolors.WARNING + text2)

# Ask to play
not_solved = True
max_counter, counter = 1, 0
print(Welcome + bcolors.OKBLUE)
while not_solved and counter <= max_counter:
    answer = raw_input()
    if answer == 'Eleanor Rigby':
        print(Eleanor + bcolors.OKGREEN)
        not_solved = False
    elif answer == 'While My Guitar Gently Weeps':
        print(Guitar + bcolors.WARNING)
        not_solved = False
    elif answer == 'Maxwells Silver Hammer':
        print(Silver + bcolors.WARNING)
        not_solved = False
    elif answer == 'A Day in the Life':
        print(ADay + bcolors.WARNING)
        not_solved = False
    elif answer == 'Penny Lane':
        print(Penny + bcolors.WARNING)
        say(Exit)
        not_solved = False
    else:
        print(Sorry + bcolors.OKGREEN)
        say(Sorry)
        not_solved = False
# Opening
not_solved = False
begin = True

print(bcolors.ENDC + START_PIC)
print(text3 + bcolors.BOLD)
say(text3)
print(text4 + text4c + bcolors.BOLD)
say(text4 + text4c)

max_counter, counter = 3, 0
while begin and counter <= max_counter:
    counter = counter + 1
    answer = raw_input()
    if answer == '169':
        print(Num169 + bcolors.BOLD)
        print(Relief + bcolors.OKBLUE)
        say(Relief)
        begin = False
    else:
        print(YouAreDumb + bcolors.OKGREEN)
        say(YouAreDumb)
        begin = True
        say(DumbTry)

# Chapter 2
begin = False
Chap2 = True

print(CHAP2_PIC + bcolors.ENDC)
print(Intro2 + bcolors.BOLD)
print(NewCar2 + bcolors.OKGREEN)
say(NewCar2)
say(Appreciate)

max_counter, counter = 3, 0
while Chap2 and counter <= max_counter:
    answer = raw_input()
    if answer == 'yes':
        print(Thanks2 + bcolors.OKBLUE)
        say(Thanks2)
        say(Thanks3 + Thanks4 + Thanks5 + Thanks4)
        Chap2 = False
    elif answer == 'no':
        print(Meanie2 + bcolors.WARNING)
        say(Meanie2)
        Chap2 = True
    else:
        print(CanYouEnglish2 + bcolors.OKGREEN)
        say(CanYouEnglish2)
        Chap2 = True

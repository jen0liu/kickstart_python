# you should better execute this code on your computer, if you want to raise the step and the length of
# charset and password, because it creates may exceed the time limite of SoloLearn's playground,
# but it also may exceed the recursion depth limit of a python object, which you can raise if you want to.

# I may implement this code again without the recursion and in a faster language than python,
# for time issues, but I find that the recusion is an elegant way to do this, and python
# an easy and fast way to understand the code

# This is a special password hacking program, for passwords that you are able to find part by part

step = 1
# here, select the step (it is the number of characters you should find at each step)
# remember that the reminder of the division of the length by the step should always be 0,
# keep it to 1 if it's possible to find the password character by character, smaller it is, faster is the code

# note that this is a bruteforce attack and the password could be really, really long to crack,
# and the time it takes increases with the step, the length of the password an the length of the charset.
# compexity : pow(len(charset), step) * (len(password)/step)

charset = "0123456789ABCDEF"  # the charset if you want for example to crack an hexadecimal type padlock

# here you can choose the charset of the password (it should be all the characters that could
# eventually be in the password). Reducing the length of the charset is a powerful way to accelerate the hacking process

def increment(part):
    i = -1
    while (part[i] == charset[-1] and -i <= len(part)):
        i -= 1

    return part[0:i] + charset[charset.index(part[i]) + 1] + charset[0] * (-i - 1)


def find(passpart, part):
    # print("Testing : " + part + "\n")
    if (passpart != part):
        if (part == charset[-1] * step):
            return 0
        part = increment(part)
        return find(passpart, part)
    return part


def verify(password):  # optionnal
    for i in password:
        if i not in charset:
            print("Password contains chars that are not in the charset.")
            return False
    if len(password) % step != 0:
        print("The step does not match with the length of the password.")
        return False
    return True


def hack(password):
    if verify(password):
        found = ""
        while password != found and len(found) < len(password):
            print("Searching the part number " + str(int(len(found) / step + 1)) + "...\n\n")
            part = find(password[len(found):len(found) + step], charset[0] * step)
            if part:
                print("\nPart found : " + part + "\n")
            else:
                break
            found += part
        if password == found:
            print("Password hacked !\nPassword : " + found)
        else:
            print("Hack failed...\nSomething went wrong...\nUnable to crack the password...\nSorry.")


hack("2E9D13")
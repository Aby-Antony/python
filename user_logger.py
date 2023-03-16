
import getopt, sys, os, emoji
from termcolor import colored
 
# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "t:"
 
# Long options
long_options = "threshold="
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-t", "--threshold"):
            Tvalue = int(currentValue)
            print("Threshold Value:", Tvalue)
            who = os.popen('who | wc -l').read()
            Loggedcount = int(who)
            print("Logged User Count", Loggedcount)
            if (Loggedcount >= Tvalue):
                print("Mail Need to be Sent!!!!!!!!")
            else:
                print("Logged Users Under Control", emoji.emojize(":grinning_face_with_big_eyes:"))   
        else:
            print ("Something Went Wrong!")
             
except getopt.error as err:
    print ("INVALID OPTION ENTERED!!!")
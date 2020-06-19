#!/usr/bin/env python
##Smol python script that verify if received jsons are valid or not

##Imports
import json

##Functions
def json_validator(item):
    '''Function that verifies if json is valid (can be used) or not. Expects one argument (name of json file or path+name), returns True if json is valid or False and prints error if its not, ignores other errors (if passed file is directory, doesnt exist or so on)'''
    try:
        json.loads(open(item).read())
        print("{} is valid json".format(item))
        return True
    except ValueError as error:
        print("{} contain errors:\n- {}".format(item, error))
        return False
    except:
        pass

##Usage
if __name__ == "__main__":
    import sys
    import glob

    jsons = []
    valid = []
    invalid = []
    ignored = []
    delimeter = "----------------"

    def print_stats(stats, message=""):
        '''Expects to receive list (as stats) and str (as message). Prints message and list's content if list isnt empty'''
        if len(stats) > 0:
            print(message)
            for x in stats:
                print("-", x)

    #Checking input
    if len(sys.argv) < 2:
        print("Usage: {} <files you want to verify, split by ' ' (masks supported)>".format(sys.argv[0]))
        sys.exit(1)

    for x in sys.argv[1:]:
        jsons.extend(glob.glob(x))

    if len(jsons) < 1:
        print("No valid files has been received. Please try again")
        sys.exit(1)

    #Verifying jsons
    for item in jsons:
        x = json_validator(item)
        if x == True:
            valid.append(item)
        elif x == False:
            invalid.append(item)
        else:
            ignored.append(item)

    print("{}\n{} has finished its work with {} errors\n{}".format(delimeter, sys.argv[0], len(invalid)+len(ignored), delimeter))
    print_stats(valid, "\nValid jsons:")
    print_stats(invalid, "\nInvalid jsons:")
    print_stats(ignored, "\nIgnored:")

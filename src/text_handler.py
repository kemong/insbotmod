#! /usr/bin/env python

import time

def write (self):
    print "trying to write old following list...."
    try :
        file = open("/home/kemong/old_following.xtx", "w")
    except :
        print "error writing file !!"
        time.sleep(20)
        return 0
    else :
        i = 0
        while i < len(self.old_following_list):
            try :
                file.write(self.old_following_list[0]+"\n")
            except :
                print "error writing file !!"
                file.close()
                return 0
            else : 
                del self.old_following_list[0]
        print "writing file finished !!"
        file.close()

def read (self):
    print "trying to read old following list...please wait dammit !!"
    time.sleep(3)
    try :
        file = open("/home/kemong/old_following.xtx", "r")
    except :
        print "error reading file !!"
        time.sleep(20)
        return 0
    else : 
        for line in file:
            self.old_following_list.append(line)
        print "reading file finished !!"
        file.close()


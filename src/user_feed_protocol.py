#!/usr/bin/env python
# -*- coding: utf-8 -*-
from user_feed import get_media_id_user_feed
from new_auto_mod_like2 import new_auto_mod_like2
import time
import random

def user_feed_protocol(self):
    #To limit how many photos to scan
    limit = 1
    counterz = 0
    self.is_checked = False
    self.is_rejected = False
    while counterz<limit:
            # ------------------- Get media_id -------------------
        if len(self.media_by_user) is 0:
            get_media_id_user_feed(self)
            # ------------------- Like -------------------
            if self.is_rejected is not False :
                return False
            else :
                limit = random.randint(len(self.media_by_user)/2,len(self.media_by_user)-1)

        if self.is_follower is not False :
            print("@@@@@@@@@@@@@@ This is your follower B****h!!! @@@@@@@@@@@@@")
            new_auto_mod_like2(self)
            time.sleep(15)
            return False
        print limit
        new_auto_mod_like2(self)
        counterz += 1
        time.sleep(limit*random.randint(1,4)*30*60)
    if limit < 7 :
        return True
    return False

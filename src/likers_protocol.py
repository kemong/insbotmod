#!/usr/bin/env python
# -*- coding: utf-8 -*-

from post_page import get_user_id_post_page
from username_checker import username_checker
import random
import time

def likers_protocol(self):
    if len(self.media_by_user) > 0:
    # You have media_id to like:
        self.current_index = random.randint(0,len(self.media_by_user)-1)
        log_string = "Current Index = %i of %i medias"%(self.current_index, len(self.media_by_user))
        self.write_log(log_string)
        print (self.media_by_user[self.current_index]["likes"]["count"])

        if self.media_by_user[self.current_index]["likes"]["count"] >= 1 and self.media_by_user[self.current_index]["likes"]["count"] < self.like_ratio * 2.5:
            get_user_id_post_page(self,self.media_by_user[self.current_index]["code"])
            username_checker(self)
            time.sleep(15)
        del self.media_by_user[self.current_index]


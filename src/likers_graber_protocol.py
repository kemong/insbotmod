#!/usr/bin/env python
# -*- coding: utf-8 -*-
from user_feed import get_media_id_user_feed
from new_auto_mod_unfollow2 import new_auto_mod_unfollow2
from likers_protocol import likers_protocol
import random
import time

def likers_graber_protocol(self):
    limit = 1
    counterx = 0
    self.is_checked = False
    self.is_rejected = False
    while counterx<limit:
        # ------------------- Get media_id -------------------
        if len(self.media_by_user) == 0:
            self.is_checked = False
            self.is_rejected = False
            get_media_id_user_feed(self)
            limit = len(self.media_by_user)-1
        # ------------------- Like -------------------
        if self.is_rejected is not False :
            self.is_checked = False
            new_auto_mod_unfollow2(self)
            return 0
        likers_protocol(self)
        time.sleep(random.randint(1,10))
        counterx += 1

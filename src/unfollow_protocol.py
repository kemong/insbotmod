#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recent_feed import get_media_id_recent_feed
from follow_protocol import follow_protocol
from user_feed_protocol import user_feed_protocol
from new_auto_mod_unfollow2 import new_auto_mod_unfollow2
import time
import random

def unfollow_protocol(self):
    limit = 1000000
    while self.unfollow_counter<=limit:
        get_media_id_recent_feed(self)
        if len(self.media_on_feed) == 0:
            self.follow_counter=0
            follow_protocol(self)
        if len(self.media_on_feed) != 0 and self.is_follower_number < 5:
            chooser = random.randint(0,len(self.media_on_feed)-1)
            self.current_user=self.media_on_feed[chooser]['node']["owner"]["username"]
            self.current_id=self.media_on_feed[chooser]['node']["owner"]["id"]
            if (self.bot_mode == 2):
                new_auto_mod_unfollow2(self)
                time.sleep(random.randint(20,200))
                return
            user_feed_protocol(self)
            self.like_counter=0
            self.media_by_user = []
            if self.is_selebgram is not False or self.is_fake_account is not False or self.is_active_user is not True or self.is_follower is not True:
                new_auto_mod_unfollow2(self)
                time.sleep(random.randint(30,180))#*random.randint(30,60))
                try:
                    del self.media_on_feed[chooser]
                except:
                    self.media_on_feed = []
        else :
            follow_protocol(self)
            self.is_follower_number = 0
            time.sleep(13)
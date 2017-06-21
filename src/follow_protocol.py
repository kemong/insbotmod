#!/usr/bin/env python
# -*- coding: utf-8 -*-
from user_info import get_user_info
from feed_scanner import feed_scanner
from user_feed_protocol import user_feed_protocol
import random
import time

def follow_protocol(self):
#    for index in range(len(self.old_following_list)):
#        if self.old_following_list[index] in self.current_id :
#            print("this user ( " + self.current_user + " ) is in your old following list !!")
#            return 0
    limit = 1000000
    self.follow_counter = 0
    while self.follow_counter<limit:
        chooser = 0
        if len(self.user_info_list)>0:
            chooser = random.randint(0,len(self.user_info_list)-1)
            self.current_user=self.user_info_list[chooser][0]
            self.current_id=self.user_info_list[chooser][1]
            print('=============== \nCheck profile of '+self.current_user+'\n===============')
            get_user_info(self, self.current_user)
        else :
            print('xxxxxxx user info list is empty!!! xxxxxxxxx')
            feed_scanner(self)
        if self.is_fake_account!=True and self.is_active_user!=False and self.is_selebgram!=True:
            if self.is_following!=True :
                folthis = False   
                if self.is_private is False :
                    print self.like_ratio
                    if self.like_ratio < 101:
                        folthis=user_feed_protocol(self)
                        if not folthis:
                            time.sleep(random.randint(3,5)*random.randint(30,60))
                        else:
                            time.sleep(random.randint(4,10)*random.randint(7,12))
                    self.like_counter=0
                    self.media_by_user = []
                else:
                    folthis = True                  

                if folthis:
                    print('Trying to follow : ' + self.current_user + ' with user ID :' + self.current_id)
                    self.follow(self.current_id)
                    time.sleep(random.randint(4,10)*random.randint(7,12))
            print('delete ' + self.user_info_list[chooser][0]+' from user info list')
            del self.user_info_list[chooser]
                 
        else :
            print('delete ' + self.user_info_list[chooser][0]+' from user info list')
            del self.user_info_list[chooser]  
        time.sleep(random.randint(3,15))


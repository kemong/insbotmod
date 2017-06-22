#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.instabot import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.unfollow_protocol import unfollow_protocol
from src.follow_protocol import follow_protocol
from src.text_handler import read
import time
import random

bot = InstaBot(login="", password="",
               like_per_day=0,
               comments_per_day=0,
               tag_list=['writer','author','penulis','penulisindonesia','publisher','sastra',
               'puisi','sajak','write','poet','poetry','creativewriting','menulis','latepost',
               'blogger','bloggerindonesia','blog','tangerang','jakarta','padang','medan','pelembang','bogor',
               'follow4follow','f4f','followme','follow','fff', 'cute'],
               tag_blacklist=['rain', 'thunderstorm'],
               user_blacklist={},
               max_like_for_one_tag=50,
               follow_per_day=1000,
               follow_time=1*60,
               unfollow_per_day=0,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               # Use unwanted username list to block users which have username contains one of this string
               ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
               ### freefollowers will be blocked because it contains free 
               unwanted_username_list=['free','follow','shop','store','toko','jual','art','photo','graphy','sepatu','tas','baju','dress','elf','grosir',
               'distro','original','bandung','solusi','cepat','hamil','program','hiasan','dinding','kamar','princess','life','consultant','peninggi',
               'badan','dunia','shop','label','world','kpop','lover','image','food','murah','butik','harga','kids','muslim','olshop','lucu','fashion',
               'brand','gamis','hijab','couple','wanita','.id','_id','cloth','precious','models','bayi','syari','modern','sandal','jakarta','tangerang',
               'official','wear','tidur','batam','cantik','muslimah','online','gaya','sale','import','bandung','bekas','cowok','modis','tee','bag',
               'sport','.com','dotcom','cewek','shoes','vans','converse','cewe','futsal','kripik','taichan','martabak','style','tasty','obral','aksesoris',
               'handmade','indonesia','indo','beauty','collection','olshp','stuff','agen','boutique','nyonya','besar','holic','dompet','mangga','niqab',
               'pesta','party','ransel','naked','istana','boutiq','semua','paket','mitra','jaket','suplier','supplier','sweater','hoodie','sentra',
               'celana','jeans','anak','street','kamera','camera','snack','seks','kuat','obat','kios','pomade','lingerie','bibit','kefir','vespa','spinner',
               'cheap','daily','pekalongan','vape','bokep','legend','macbeth','sosial','media','vapor','warung','apple','planet','gadget','kucing',
               'surabaya','follower','pusat','preloved','cloud','corner','hotplate','sneaker','lelaki','kebaya','kaos','oblong','polos','india','minimalis',
               'crispy','cute','kurma','second','wallpaper','roemah','case','softlens','game','gaun','ship','beauties'])
while True:

    print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    print("## MODE 1 = MODIFIED MODE BY KEMONG")
    print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    print("#### MODE 3 = MODIFIED MODE : UNFOLLOW PEOPLE WHO DON'T FOLLOW BACK BASED ON RECENT FEED ONLY")
    print("##### MODE 4 = MODIFIED MODE : FOLLOW PEOPLE BASED ON RECENT FEED ONLY")
    print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT") 

    ################################
           ##  WARNING   ###
    ################################
    
    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD
 
    mode = 3
    
    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 3 seconds to start")
    #time.sleep(3)
    #print("reading old following list....")
    #read(bot)

    if mode == 0 : 
        bot.new_auto_mod()

    elif mode == 1 :
        check_status(bot)
        while bot.self_following > 7260:
            unfollow_protocol(bot)
            time.sleep(60)
            check_status(bot)
        while bot.self_following < 7460:
            while len(bot.user_info_list) <50 :
                feed_scanner(bot)
                time.sleep(60)
                follow_protocol(bot)
                time.sleep(60)
                check_status(bot)
            bot.user_info_list = []

    elif mode == 2 :
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3 :
        while True:
            unfollow_protocol(bot)

    elif mode == 4 :
        while True:
            feed_scanner(bot)
            time.sleep(60)
            follow_protocol(bot)
            time.sleep(15*60)

    elif mode == 5 :
        while True: 
            #bot.bot_mode=2
            feed_scanner(bot)
            follow_protocol(bot)
            bot.user_info_list = []
            time.sleep(600)

    else :
        print ("You give me wrong mode mothafucka!!!")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.instabot import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.unfollow_protocol import unfollow_protocol
from src.follow_protocol import follow_protocol
from src.text_handler import read
import time

bot = InstaBot(login="aprilgescraft", password="gescraftku",
               like_per_day=0,
               comments_per_day=0,
               tag_list=['latepost','tangerang','jakarta','padang','medan','pelembang','bogor',
               'kuliner','food','foodies','olshop','onlineshop','shop','hits','city','cullinary','fashion','hijab','online','carnival','townsquare','urbanfood','timur','beauty','store',
               'bogorkuliner','bogorfood','bogorfoodies','bogorolshop','bogoronlineshop','bogorshop','bogorhits','bogorcity','bogorcullinary','bogorfashion','bogorhijab','bogoronline','bogorcarnival','bogortownsquare','bogorurbanfood','bogortimur','bogorbeauty','bogorstore',
               'pelembangkuliner','pelembangfood','pelembangfoodies','pelembangolshop','pelembangonlineshop','pelembangshop','pelembanghits','pelembangcity','pelembangcullinary','pelembangfashion','pelembanghijab','pelembangonline','pelembangcarnival','pelembangtownsquare','pelembangurbanfood','pelembangtimur','pelembangbeauty','pelembangstore',
               'medankuliner','medanfood','medanfoodies','medanolshop','medanonlineshop','medanshop','hits','medancity','medancullinary','medanfashion','medanhijab','medanonline','medancarnival','medantownsquare','medanurbanfood','medantimur','medanbeauty','medanstore',
               'padangkuliner','padangfood','padangfoodies','padangolshop','padangonlineshop','padangshop','padanghits','padangcity','padangcullinary','padangfashion','padanghijab','padangonline','padangcarnival','padangtownsquare','padangurbanfood','padangtimur','padangbeauty','padangstore',
               'jakartakuliner','jakartafood','jakartafoodies','jakartaolshop','jakartaonlineshop','jakartashop','jakartahits','jakartacity','jakartacullinary','jakartafashion','jakartahijab','jakartaonline','jakartacarnival','jakartatownsquare','jakartaurbanfood','jakartatimur','jakartabeauty','jakartastore',
               'tangerangkuliner','tangerangfood','tangerangfoodies','tangerangolshop','tangerangonlineshop','tangerangshop','tangeranghits','tangerangcity','tangerangcullinary','tangerangfashion','tangeranghijab','tangerangonline','tangerangcarnival','tangerangtownsquare','tangerangurbanfood','tangerangtimur','tangerangbeauty','tangerangstore',
               'bandungkuliner','bandungfood','bandungfoodies','bandungolshop','bandungonlineshop','bandungshop','bandunghits','bandungcity','bandungcullinary','bandungfashion','bandunghijab','bandungonline','bandungcarnival','bandungtownsquare','bandungurbanfood','bandungtimur','bandungbeauty','bandungstore',
               'surabayakuliner','surabayafood','surabayafoodies','surabayaolshop','surabayaonlineshop','surabayashop','surabayahits','surabayacity','surabayacullinary','surabayafashion','surabayahijab','surabayaonline','surabayacarnival','surabayatownsquare','surabayaatas','surabayaurbanfood','surabayatimur','surabayabeauty','surabayastore',
               'malangkuliner','malangfood','malangfoodies','malangolshop','malangonlineshop','malangshop','malanghits','malangcity','malangcullinary','malangfashion','malanghijab','malangonline','malangcarnival','malangtownsquare','malangatas','malangurbanfood','malangtimur','malangbeauty','malangstore',
               'batukuliner','batufood','batufoodies','batuolshop','batuonlineshop','batushop','batuhits','batucity','batucullinary','batufashion','batuhijab','batuonline','batucarnival','batutownsquare','batuatas','batuurbanfood','batutimur','batubeauty','batustore',
               'blitarkuliner','blitarfood','blitarfoodies','blitarolshop','blitaronlineshop','blitarshop','blitarhits','blitarcity','blitarcullinary','blitarfashion','blitarhijab','blitaronline','blitarcarnival','blitartownsquare','blitaratas','blitarurbanfood','blitartimur','blitarbeauty','blitarstore',
               'kedirikuliner','kedirifood','kedirifoodies','kediriolshop','kedirionlineshop','kedirishop','kedirihits','kediricity','kediricullinary','kedirifashion','kedirihijab','kedirionline','kediricarnival','kediritownsquare','kediriatas','kediriurbanfood','kediritimur','kediribeauty','kediristore',
               'madiunkuliner','madiunfood','madiunfoodies','madiunolshop','madiunonlineshop','madiunshop','madiunhits','madiuncity','madiuncullinary','madiunfashion','madiunhijab','madiunonline','madiuncarnival','madiuntownsquare','madiunatas','madiunurbanfood','madiuntimur','madiunbeauty','madiunstore',
               'mojokertokuliner','mojokertofood','mojokertofoodies','mojokertoolshop','mojokertoonlineshop','mojokertoshop','mojokertohits','mojokertocity','mojokertocullinary','mojokertofashion','mojokertohijab','mojokertoonline','mojokertocarnival','mojokertotownsquare','mojokertoatas','mojokertourbanfood','mojokertotimur','mojokertobeauty','mojokertostore',
               'probolinggokuliner','probolinggofood','probolinggofoodies','probolinggoolshop','probolinggoonlineshop','probolinggoshop','probolinggohits','probolinggocity','probolinggocullinary','probolinggofashion','probolinggohijab','probolinggoonline','probolinggocarnival','probolinggotownsquare','probolinggoatas','probolinggourbanfood','probolinggotimur','probolinggobeauty','probolinggostore',
               'banyuwangikuliner','banyuwangifood','banyuwangifoodies','banyuwangiolshop','banyuwangionlineshop','banyuwangishop','banyuwangihits','banyuwangicity','banyuwangicullinary','banyuwangifashion','banyuwangihijab','banyuwangionline','banyuwangicarnival','banyuwangitownsquare','banyuwangiatas','banyuwangiurbanfood','banyuwangitimur','banyuwangibeauty','banyuwangistore',
               'masak','masakanindonesia','masakanrumah','ibunda','ibu','arisan','ibudanbayi','ibudanbalita','bogor','tangerang','jakarta','bandung','jogja','malang','surabaya','medan','palembang','padang','ibuhamil','ibumenyusui','ibumengandung','iburumahtangga','wanitaindonesia','wanitakarir','ibumuda','ibudananak','ibu'],
               tag_blacklist=['rain', 'thunderstorm'],
               user_blacklist={},
               max_like_for_one_tag=24,
               follow_per_day=240,
               follow_time=3*60,
               unfollow_per_day=0,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               # Use unwanted username list to block users which have username contains one of this string
               ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
               ### freefollowers will be blocked because it contains free 
               unwanted_username_list=[])
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
 
    mode = 1
    
    print("You choose mode : %i" %(mode))
    print("CTRL + C to cancel this operation or wait 3 seconds to start")
    time.sleep(3)
    print("reading old following list....")
    read(bot)

    if mode == 0 : 
        bot.new_auto_mod()

    elif mode == 1 :
        check_status(bot)
        while bot.self_following > 1460:
            unfollow_protocol(bot)
            time.sleep(10*60)
            check_status(bot)
        while bot.self_following < 2460:
            while len(bot.user_info_list) <50 :
                feed_scanner(bot)
                time.sleep(3*60)
                follow_protocol(bot)
                time.sleep(15*60)
                check_status(bot)
            bot.user_info_list = []

    elif mode == 2 :
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3 :
        while True:
            unfollow_protocol(bot)
            time.sleep(10*60)

    elif mode == 4 :
        while True:
            feed_scanner(bot)
            time.sleep(60)
            follow_protocol(bot)
            time.sleep(10*60)

    elif mode == 5 :
        while True:
            bot.bot_mode=2
            unfollow_protocol(bot)

    else :
        print ("You give me wrong mode mothafucka!!!")

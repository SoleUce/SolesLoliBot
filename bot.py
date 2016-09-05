from __future__ import unicode_literals
from pybooru import Pybooru
import discord
import asyncio
import random 
# -*- coding: utf-8 -*-

bclient = Pybooru('Konachan')



client = discord.Client()
###############
#-Random Loli_#
###############
@client.async_event
def on_message(message):
    
    if message.content.startswith('!loli'):

        num = random.randint(0,100)
        posts = bclient.posts_list('loli', num)
        for post in posts:
            print("URL: {0}".format(post['file_url']))
            myfile = open("url.txt", "w")
            myfile.write(post['file_url'])
            myfile.close()
            myfile = open("url.txt", "r")
            Pic = myfile.readline()
        yield from client.send_message(message.channel, Pic)

################
#-Waifu Search-#
################
@client.async_event
def on_message(message):
    
    if message.content.startswith('!waifu '):
        waifu = message.content[len('!waifu '):].strip()
        print(waifu)
        num = random.randint(0,100)
        posts = bclient.posts_list(waifu, num)
        for post in posts:
            print("URL: {0}".format(post['file_url']))
            myfile = open("waifu.txt", "w")
            myfile.write(post['file_url'])
            myfile.close()
            myfile = open("waifu.txt", "r")
            WPic = myfile.readline()
        yield from client.send_message(message.channel, WPic)

client.run('MjIxNTg3NDY4NjgyNjU3Nzky.Cq1Fkg._0pT7mNOq4rlDz5PqV8hDXrKuyY')
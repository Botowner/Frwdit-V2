#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import sys
import asyncio
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument

#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('🧞‍♂️ Group', url='https://t.me/cinemala_com'),
        InlineKeyboardButton(' Channel ♻️', url='https://t.me/@cinemala_com1')
        ],[
        InlineKeyboardButton('🤴🏻 Bot owner', url='https://t.me/Aswin_pm_Bot'),
        InlineKeyboardButton('Repo 📝', url ='https://t.me/Aswin_pm_Bot')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")

#===================Help Function===================#

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('👤 Creator', url='https://t.me/Aswin_pm_Bot'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode="html")

#=================About Function==================#

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('👤 Creator', url='https://t.me/Aswin_pm_Bot'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode="html"
    )

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restarting.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    

"""Emoji

Available Commands:

.ok"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.00001
    animation_ttl = range(0, 90)
    user_id = replied_user.user.id
    input_str = event.pattern_match.group(1)
    if input_str == "ok":
        await event.edit(input_str)
        animation_chars = [
            "F",
            "U",
            "C",
            "K",
            "Y",
            "O",
            "U",
            "Importing Every Prefrences from The User",
            "___INTIALIZING___",
            "$%!$@%!$@",
            "!@##&!!#^",
            "@#%&!%#&!",
            "@%#!&#%!&",
            "!&*@!*@^@",
            "User Id Extracted Successfully",
            "HACKING COMMITED DATABASES ARE WEAK TRY INJECTING @#@!#!#",
            "!^^!*#%!%#!!",
            "INJECTING SUCCESSFUL",
            "PRESS .hack TO HACK THE USERS DATA WITH LOGIN CREDENTIAL",
            "COMMAND EXCUTED",
            "WAITING FOR YOUR COMMAND SIR",
            "#%!^!#%@$",
            "AUTO EXITING INTIATED EXITING IN 2Min",
            "@%!$#!%$!%",
            "$@%@@%$$%!",
            "SUCCESSFULLY EXITED",
            print (user_id)
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])

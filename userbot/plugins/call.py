"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`THUNDER USER BOT: Yo this is` @Anonymous_290 ,`We Are Anonymous We Are Gonna Leak Telegram Datas`",
            "`Telegram: What I M Gonna Block Your Account`",
            "`ME: Do If You Can We Anonymous Use Thunder User Bot`",
            "`Telegram: Banning Your Account In Few Minutes...`",
            "`ME: LOL DO SOON`",    
            "`Telegram: Target Database Is Secured Trying 2nd Method`",
            "`THUNDER USER BOT: FINDING SUSPICIOUS 2min Fixing The Problems...",
            "`THUNDER USER BOT: Servers Fixed You Can Enjoy Now`",
            "`THUNDER USER BOT: Database Are Connected Successfully`",
            "`THUNDER USER BOT: Connecting To The Telegram Server Fixing API Problems`",
            "`THUNDER USER BOT: Everything Fixed Successfully`",
            "`THUNDER USER BOT: Checking The IP And Mac Of Yours Master`",
            "`THUNDER USER BOT: Everything Changed`",
            "`THUNDER USER BOT: WE ARE ANONYMOUS`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])

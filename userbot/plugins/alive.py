"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`WE ARE ANONYMOUS USING THUNDER SECURITY`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @Anonymous_290\n"
                     "`Bot created by:` [Anonymous_290](tg://user?id=1001239766297)\n"
                     "`Database Status: Databases functioning normally! The Secutity Is Stronger Connected To CTOS\n\nAlways with you Sir Waiting For Your Command\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/santoshArnold/ThunderUserBot)")

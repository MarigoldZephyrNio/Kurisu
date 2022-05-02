from __future__ import annotations

import datetime
import discord
import math
import random

from discord.ext import commands
from typing import TYPE_CHECKING
from utils import crud
from utils.checks import is_staff

if TYPE_CHECKING:
    from kurisu import Kurisu


class Memes(commands.Cog):
    """
    Meme commands
    """
    def __init__(self, bot: Kurisu):
        self.bot: Kurisu = bot
        self.emoji = discord.utils.get(self.bot.guild.emojis, name='fug') or discord.PartialEmoji.from_str("⁉")
        self.bot.loop.create_task(self.init_memes())

    async def init_memes(self):
        await self.bot.wait_until_all_ready()
        self.wagu_emoji = discord.utils.get(self.bot.guild.emojis, name="wagu") or "⁉"
        self.waguspooky = discord.utils.get(self.bot.guild.emojis, name="waguspooky") or "⁉"
        self.waguxmas = discord.utils.get(self.bot.guild.emojis, name="waguxmas") or "⁉"
        self.waguspin = discord.utils.get(self.bot.guild.emojis, name="waguspin") or "⁉"
        self.waguspinaaa = discord.utils.get(self.bot.guild.emojis, name="waguspinaaa") or "⁉"
        self.waguwat = discord.utils.get(self.bot.guild.emojis, name="waguwat") or "⁉"
        self.waguwu = discord.utils.get(self.bot.guild.emojis, name="waguwu") or "⁉"
        self.waguw = discord.utils.get(self.bot.guild.emojis, name="waguw") or "⁉"
        self.hyperwagu = discord.utils.get(self.bot.guild.emojis, name="hyperwagu") or "⁉"
        self.wagupeek = discord.utils.get(self.bot.guild.emojis, name="wagupeek") or "⁉"
        self.poggu = discord.utils.get(self.bot.guild.emojis, name="poggu") or "⁉"
        self.waguburger = discord.utils.get(self.bot.guild.emojis, name="waguburger") or "⁉"
        self.wagucar = discord.utils.get(self.bot.guild.emojis, name="wagucar") or "⁉"
        self.shutwagu = discord.utils.get(self.bot.guild.emojis, name="shutwagu") or "⁉"
        self.waguboat = discord.utils.get(self.bot.guild.emojis, name="waguboat") or "⁉"
        self.wagutv = discord.utils.get(self.bot.guild.emojis, name="wagutv") or "⁉"
        self.ghostwagu = discord.utils.get(self.bot.guild.emojis, name="ghostwagu") or "⁉"
        self.flushedsquish = discord.utils.get(self.bot.guild.emojis, name="flushedsquish") or "⁉"
        self.flushedball = discord.utils.get(self.bot.guild.emojis, name="flushedball") or "⁉"
        self.flushedeyes = discord.utils.get(self.bot.guild.emojis, name="flushedeyes") or "⁉"

    async def _meme(self, ctx: commands.Context, msg, directed: bool = False, imagelink=None, allowed_mentions=None):
        author = ctx.author
        if isinstance(ctx.channel, discord.abc.GuildChannel) and (ctx.channel in self.bot.assistance_channels or (self.bot.roles['No-Memes'] in author.roles)):
            await ctx.message.delete()
            try:
                await ctx.author.send("Meme commands are disabled in this channel, or your privileges have been revoked.")
            except discord.errors.Forbidden:
                await ctx.send(f"{ctx.author.mention} Meme commands are disabled in this channel, or your privileges have been revoked.")
        elif imagelink is not None:
            title = f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}"
            embed = discord.Embed(title=title, color=discord.Color.default())
            embed.set_image(url=imagelink)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}", allowed_mentions=allowed_mentions)

    async def _meme2(self, ctx: commands.Context, msg, directed: bool = False, imagelink=None, allowed_mentions=None):
        author = ctx.author
        if isinstance(ctx.channel, discord.abc.GuildChannel) and (ctx.channel in self.bot.assistance_channels or (self.bot.roles['No-Memes'] in author.roles) or ctx.channel is self.bot.channels['bot-cmds']):
            await ctx.message.delete()
            try:
                await ctx.author.send("Meme commands are disabled in this channel, or your privileges have been revoked.")
            except discord.errors.Forbidden:
                await ctx.send(f"{ctx.author.mention} Meme commands are disabled in this channel, or your privileges have been revoked.")
        elif imagelink is not None:
            title = f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}"
            embed = discord.Embed(title=title, color=discord.Color.default())
            embed.set_image(url=imagelink)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}", allowed_mentions=allowed_mentions)

    # list memes
    @commands.command(name="listmemes")
    async def _listmemes(self, ctx: commands.Context):
        """List meme commands."""
        cmds = ", ".join([x.name for x in self.get_commands()][1:])
        await self._meme(ctx, f"```{cmds}```")

    # 3dshacks memes
    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def s_99(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "**ALL HAIL BRITANNIA!**")

    @commands.command(hidden=True)
    @commands.cooldown(rate=5, per=30.0, type=commands.BucketType.channel)
    async def honk(self, ctx: commands.Context):
        """honk"""
        await self._meme(ctx, "`R A K E  I N  T H E  L A K E`")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def screams(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/j0Dkv2Z.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def eeh(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/2SBC1Qo.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def dubyadud(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/Sohsi8s.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def megumi(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/GMRp1dj.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/WLncIsi.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori2(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/V0uu99A.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori3(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/so8thgu.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori4(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/267IXh1.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori5(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/lKcsiBP.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def inori6(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/SIJzpau.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def shotsfired(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/zf2XrNk.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def rusure(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://imgur.com/sXnVRLw.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def r34(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/sjQZKBF.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def lenny(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "( ͡° ͜ʖ ͡°)")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def rip(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def permabrocked(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/ARsOh3p.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def knp(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/EsJ191C.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def lucina(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/tnWSXf7.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def lucina2(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/ZPMveve.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def xarec(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/A59RbRT.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def clap(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/UYbIZYs.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def ayyy(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/bgvuHAd.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def hazel(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/vpu8bX3.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def thumbsup(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "https://i.imgur.com/hki1IIs.gifv")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def pbanjo(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/sBJKzuK.png")

    # Cute commands :3
    @commands.command(hidden=True, aliases=["pat"])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def headpat(self, ctx: commands.Context, u: discord.Member):
        """headpat"""
        await self._meme(ctx, f"{self.bot.escape_text(u.display_name)} has been gently patted.", True, "https://i.imgur.com/7V6gIIW.jpg")

    @commands.command(hidden=True, aliases=["pat2"])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def headpat2(self, ctx: commands.Context, u: discord.Member):
        """headpat 2"""
        await self._meme(ctx, f"{self.bot.escape_text(u.display_name)} has been gently patted.", True, "https://i.imgur.com/djhHX0n.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def headrub(self, ctx: commands.Context, u: discord.Member):
        """headrub"""
        await self._meme(ctx, f"{self.bot.escape_text(u.display_name)} has received a head rub.", True, "https://i.imgur.com/j6xSoKv.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def sudoku(self, ctx: commands.Context):
        """Cute"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/VHlIZRC.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def baka(self, ctx: commands.Context):
        """Cute"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/OyjCHNe.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def mugi(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/lw80tT0.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def lisp(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/RQeZErU.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def dev(self, ctx: commands.Context):
        """Reminds user where they are."""
        await self._meme(ctx, f"You {'do not ' if ctx.channel != self.bot.channels['dev'] else ''}seem to be in {self.bot.channels['dev'].mention}.", True)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def meta(self, ctx: commands.Context):
        """Reminds user where they are. (2)"""
        await self._meme(ctx, f"You {'do not ' if ctx.channel != self.bot.channels['meta'] else ''}seem to be in {self.bot.channels['meta'].mention}. Please take this subject {'there' if ctx.channel != self.bot.channels['meta'] else 'somewhere else'}.", True)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def appeals(self, ctx: commands.Context):
        """Reminds user where they are. (3)"""
        await self._meme(ctx, f"You {'do not ' if ctx.channel != self.bot.channels['appeals'] else ''}seem to be in {self.bot.channels['appeals'].mention}. Please take this subject {'there' if ctx.channel != self.bot.channels['appeals'] else 'somewhere else'}.", True)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def blackalabi(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/JzFem4y.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def eip(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/SU0Qvc8.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def whoops(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/2ec4764e884d956fb882f3479fa87ecf.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def nom(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/p1r53ni.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def soghax(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/oQJy2eN.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def weebs(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/sPjRKUB.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def whatisr(self, ctx: commands.Context):
        """MEMES?"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/Z8HhfzJ.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def helpers(self, ctx: commands.Context):
        """MEMES?"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/0v1EgMX.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def concern(self, ctx: commands.Context):
        """MEMES?"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/cWXBb5g.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def fuck(self, ctx: commands.Context):
        """MEMES?"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/4lNA5Ud.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def goose(self, ctx: commands.Context):
        """MEMES?"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/pZUeBql.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def planet(self, ctx: commands.Context):
        """haha yes!"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/YIBADGT.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def pbanj(self, ctx: commands.Context):
        """he has the power"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/EQy9pl3.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def pbanj2(self, ctx: commands.Context):
        """pbanos"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/oZx7Qid.gif")

    # Begin code from https://github.com/reswitched/robocop-ng
    @staticmethod
    def c_to_f(c):
        """this is where we take memes too far"""
        return math.floor(1.8 * c + 32)

    @staticmethod
    def c_to_k(c):
        """this is where we take memes REALLY far"""
        return math.floor(c + 273.15)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def warm(self, ctx: commands.Context, u: discord.Member):
        """Warms a user :3"""
        celsius = random.randint(38, 100)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await self._meme(ctx, f"{u.mention} warmed. User is now {celsius}°C ({fahrenheit}°F, {kelvin}K).", True)

    # adding it here cause its pretty much the same code
    @commands.command(hidden=True, aliases=["cool"])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def chill(self, ctx: commands.Context, u: discord.Member):
        """Cools a user :3"""
        celsius = random.randint(-273, 34)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await self._meme(ctx, f"{u.mention} cooled. User is now {celsius}°C ({fahrenheit}°F, {kelvin}K).", True)
    # End code from https://github.com/reswitched/robocop-ng

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def bean(self, ctx: commands.Context, u: discord.Member):
        """swing the beanhammer"""
        await self._meme(ctx, f"{u.mention} is now beaned. <a:bean:462076812076384257>", True)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def nogas(self, ctx: commands.Context):
        """shhhh no one gives a shit!"""
        await self._meme(ctx, "https://imgur.com/a/5IcfK6N")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def cosmic(self, ctx: commands.Context):
        """Cosmic ban"""
        await self._meme(ctx, "https://i.imgur.com/V4TVpbC.gifv")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def menuhax(self, ctx: commands.Context):
        """menuhax 11.4 wen"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/fUiZ2c3.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def magic(self, ctx: commands.Context):
        """shrug.avi"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/k9111dq.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def mouse(self, ctx: commands.Context):
        """Whaaaa"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/0YHBP7l.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def bananoose(self, ctx: commands.Context):
        """:)"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/VUmkXDd.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def goosenana(self, ctx: commands.Context):
        """:)"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/dLZOK5c.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def eel(self, ctx: commands.Context, u: discord.Member):
        """eel"""
        await self._meme(ctx, f"{self.bot.escape_text(u.display_name)} has been eel slapped.", True, "https://i.imgur.com/QXF2Pcn.gif")

    @commands.command(hidden=True, aliases=["bruh", "yolo", "swag", "based"])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def dab(self, ctx: commands.Context):
        """Memes."""
        await self._meme(ctx, "No. I might be controlled by you idiots, but I have *some* self respect, baka...")

    @commands.command(hidden=True, aliases=["hacc"])
    @commands.cooldown(rate=5, per=60.0, type=commands.BucketType.channel)
    async def nobrain(self, ctx: commands.Context, *, action="hacc"):
        """h a c c"""
        await self._meme(ctx, f'`I have no brain and I must {" ".join(action.replace("`",""))}`')

    @commands.command(hidden=True, aliases=["wheresource", "sauce", "github"])
    @commands.cooldown(rate=5, per=30.0, type=commands.BucketType.channel)
    async def source(self, ctx: commands.Context):
        """You *did* read the GPL, *right?*"""
        await self._meme(ctx, "", imagelink="https://i.imgur.com/ceLGvc4.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def pirate2(self, ctx: commands.Context):
        """stop right there, criminal scum"""
        await self._meme(ctx, "", imagelink="https://cdn.discordapp.com/attachments/508390946753216528/695752500179107910/giphy.gif")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def source2(self, ctx: commands.Context):
        """citation needed"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/b5c031e07ddbc3e48d0853f2d7064f66.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def disgraceful(self, ctx: commands.Context):
        """YOU DIDN'T SEE IT BECAUSE IT WASN'T THERE"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/b93b2a99bc28df4a192fc7eb8ccc01a9.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def greatness(self, ctx: commands.Context):
        """We were this close."""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/f2b1e87af1fcdcd34f0dff65d7696deb.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def shovels(self, ctx: commands.Context):
        """Do you need more?"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/b798edd56662f1bde15ae4b6bc9c9fba.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def value(self, ctx: commands.Context):
        """smug.png"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/f882b32a3f051f474572b018d053bd7b.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def superiority(self, ctx: commands.Context):
        """opinions"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/e2cbbf7c808e21fb6c5ab603f6a89a3f.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def dolar(self, ctx: commands.Context):
        """mcdondal"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/3ecd851953906ecc2387cfd592ac97e7.png")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def serotonin(self, ctx: commands.Context):
        """i really want to know"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/2549ac8b197ae68080041d3966a887e8.png")

    @commands.command(hidden=True, aliases=['decisions'])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def decision(self, ctx: commands.Context):
        """duly noted"""
        await self._meme(ctx, "", imagelink="https://album.eiphax.tech/uploads/big/5186160fa1b8002fe8fa1867225e45a7.png")

    @commands.command(hidden=True, aliases=['tmyk'])
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def themoreyouknow(self, ctx: commands.Context):
        """now with ear rape"""
        await ctx.send("https://album.eiphax.tech/uploads/big/01432cfa6eb64091301037971f8225c4.webm")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=300.0, type=commands.BucketType.channel)
    async def cadealert(self, ctx: commands.Context):
        """stop! cade time."""
        await self._meme2(ctx, "excuse me <@&575940388452433940>, it is time for cade", allowed_mentions=discord.AllowedMentions(roles=True))

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=300.0, type=commands.BucketType.channel)
    async def birbalert(self, ctx: commands.Context):
        """stop! birb time."""
        await self._meme2(ctx, "excuse me <@&805294876673572884>, it is time for birb", allowed_mentions=discord.AllowedMentions(roles=True))

    @is_staff("OP")
    @commands.command(hidden=True, aliases=['🍰'])
    async def birthday(self, ctx: commands.Context, member: discord.Member):
        """Wishes a happy birthday. Do not abuse pls."""

        await ctx.message.delete()
        await member.add_roles(self.bot.roles['🍰'])

        timestamp = datetime.datetime.now()
        delta = datetime.timedelta(seconds=86400)
        expiring_time = timestamp + delta

        await crud.add_timed_role(member.id, self.bot.roles['🍰'].id, expiring_time)
        await ctx.send(f"Happy birthday {member.mention}!")

    @commands.command(hidden=True, aliases=["departure"])
    @commands.cooldown(rate=5, per=30.0, type=commands.BucketType.channel)
    async def depart(self, ctx: commands.Context):
        """From the amazing Mr. Burguers"""
        departure_gifs = ["https://i.imgur.com/Kbyp7i4.gif", "https://i.imgur.com/Wv8DoGC.gif"]
        await self._meme(ctx, "", imagelink=random.choice(departure_gifs))

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def arrival(self, ctx: commands.Context):
        """Glazy can add departure but not arrival smh"""
        arrival_gifs = ["https://imgur.com/kNlrsth.gif", "https://imgur.com/ZlwaTUp.gif"]
        await self._meme(ctx, "", imagelink=random.choice(arrival_gifs))

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def hug(self, ctx: commands.Context, u: discord.Member):
        """hug"""
        await self._meme(ctx, f"{self.bot.escape_text(u.display_name)} has received a hug.", True, "https://i.imgur.com/wTHzIXx.jpg")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    async def blahaj(self, ctx: commands.Context, money: float):
        """Displays how much Blahajs you can buy with that money. ($ or €)"""
        # blahaj. takes usd or eur
        blahajlink = "https://nintendohomebrew.com/assets/img/blahaj.png"
        if money < 18:
            text = "You can't even buy a Blahaj with that! Get more money, then buy a Blahaj."
        elif money // 18 == 1:
            text = "You could buy one Blahaj with that. Think about it."
        else:
            text = f"You could buy {int(money//18)} Blahajes with that. Think about it."
        await self._meme(ctx, text, True, blahajlink)

    @is_staff("Helper")
    @commands.command()
    async def xiwarn(self, ctx: commands.Context, citizen: discord.Member):
        """Sometimes citizens need a reminder how to act"""
        await crud.add_social_credit(citizen.id, -100)
        await ctx.send(f"{ctx.author.mention} has assessed {citizen.mention}'s actions and removed 100 social credit from them!")

    @is_staff("Helper")
    @commands.command()
    async def xipraise(self, ctx: commands.Context, citizen: discord.Member):
        """Model citizens will be praised"""
        await crud.add_social_credit(citizen.id, 100)
        await ctx.send(f"{ctx.author.mention} has assessed {citizen.mention}'s actions and added 100 social credit to them!")

    @is_staff("Helper")
    @commands.command(aliases=["sc"])
    async def socialcredit(self, ctx: commands.Context, citizen: discord.Member):
        """You better keep this high"""
        db_citizen = await crud.get_citizen(citizen.id)
        if not db_citizen:
            await crud.add_citizen(citizen.id)
            return await ctx.send(f"{citizen.mention} is now a citizen and has 100 social credit!")
        await ctx.send(f"{citizen.mention} currently has {db_citizen.social_credit} social credit!")
        if db_citizen.social_credit < -200:
            await ctx.send("The citizen is due a visit to the reeducation camp!")
        elif db_citizen.social_credit > 500:
            await ctx.send("The citizen is an example for others to follow!")

    @is_staff("Helper")
    @commands.command()
    async def gulag(self, ctx: commands.Context, citizen: discord.Member):
        """When the citizen was not meant to be"""
        db_citizen = await crud.get_citizen(citizen.id)
        if not db_citizen:
            return await ctx.send(f"There is no citizen named {citizen.mention}!")
        await crud.remove_citizen(citizen.id)
        await ctx.send(f"{citizen.mention} was sent away for reeducation purposes!")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=15.0, type=commands.BucketType.channel)
    async def motd(self, ctx: commands.Context):
        """got milk?"""
        motd_list = [f"{str(self.flushedball)}", f"{str(self.flushedsquish)}", f"{str(self.flushedeyes)}", "ur mom lol", "hot dogs are sandwiches dont @ me", "have you had a coffee today?", "bird app bad", "imagine having opinions in current year", "based", "pog", "ratio", "remember to moisturize today!", "drink some water u idiot", "take ur meds", "do you like neapolitan ice cream?", "nentondon swonch", "xnoe at 11pm moment", "has junko had a name change today?", "got milk?", "got pilk?", "it has been 0 days since eip broke me", "ETA WEN PLS"]
        await ctx.send(random.choice(motd_list))

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=15.0, type=commands.BucketType.channel)
    async def wagu(self, ctx: commands.Context):
        """got milk?"""
        wagulist = [f"{str(self.wagu_emoji)}", f"{str(self.waguspooky)}", f"{str(self.waguxmas)}", f"{str(self.waguspin)}", f"{str(self.waguspinaaa)}", f"{str(self.waguwat)}", f"{str(self.waguwu)}", f"{str(self.waguw)}", f"{str(self.hyperwagu)}", f"{str(self.wagupeek)}", f"{str(self.poggu)}", f"{str(self.waguburger)}", f"{str(self.wagucar)}", f"{str(self.shutwagu)}", f"{str(self.waguboat)}", f"{str(self.wagutv)}", f"{str(self.ghostwagu)}"]
        await ctx.send(random.choice(wagulist))


def setup(bot):
    bot.add_cog(Memes(bot))

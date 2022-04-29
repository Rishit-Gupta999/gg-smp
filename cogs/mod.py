from cgitb import text
from unicodedata import name
import disnake
from disnake.ext import commands
from disnake import AllowedMentions, member, channel
from psutil import users
import random
import json
with open('config/config.json', 'r') as f:
    data = json.load(f)
with open('config/replies.json', 'r') as k:
    msg = json.load(k)
mrole = data["discord_moderator_role_id"]
hard = []

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="kick", description="Kicks a member.", help="Kicks a member from the server, you can also set a reason which will show in audit logs.", brief="Kicks a member.", usage="\nUsage:\n!kick <member> [reason]\n\nExamples:\n!k @Ronit badmosi\n!kick @Dyno", aliases=['k'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_kick_command(self, ctx, member: disnake.Member, *,reason: str=None) -> None:
        await member.send(msg["kick_dm"])
        await member.kick(reason=reason)
        await ctx.send(msg["kick"].format(member=member, reason=reason))

    @commands.command(name="warn", brief="Warns a member.", description="Warns of member.", aliases=['w', 'warning'], usage='\nUsage:\n!warn <member> [reason]\nExamples:\n!warn @Arpit chat in off-topic channel.', enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def my_warn_command(self, ctx, member: disnake.Member, *,reason: str):
        await member.send(msg["warn_dm"])
        await ctx.send(msg["warn"])

    @commands.command(name="timeout", description="Timeouts a member.", help="Timeouts a member in the server, you can also set a reason which will show in audit logs.", brief="Timeouts a member.", usage="\nUsage:\n!timeout <member> <duration> [reason]\n\nExamples:\n!timeout @Ronit 10m posting cringe\n!timeout @Sanskar 10h", aliases=['mute', 'to'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(manage_nicknames=True), commands.has_permissions(administrator=True))
    async def my_timeout_command(self, ctx, member: disnake.Member, duration,*,reason: str=None) -> None:
        time_convert = {'s': 1 , 'm' : 60 , 'h' : 3600 , 'd' : 86400, 'S' : 1, 'M' : 60, 'H' : 3600, "D" : 86400}
        timeout_time = float(duration[0:len(duration)-1]) * time_convert[duration[-1]]
        await member.send(msg["timeout_dm"])
        await member.timeout(reason=reason, duration=timeout_time)
        await ctx.send(msg["timeout"])

    @commands.command(name="ban", description="Bans a member.", help="Bans a member from the server, you can also set a reason which will show in audit logs.", brief="Bans a member.", usage="Usage:\n!ban <member> [reason]\n\nExamples:\n!ban @Arnav anime is cringe\n !ban @carl-bot", aliases=['b'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(ban_members=True), commands.has_permissions(administrator=True))
    async def my_ban_command(self, ctx, member: disnake.Member,*, reason: str=None) -> None:
        await member.send(msg["ban_dm"])
        await member.ban(reason=reason)
        await ctx.send(msg["ban"])
    
    @commands.command(name="nick", description="Changes nickname of a member.", brief="Changes nickname", usage="\nUsage:\n!nick <member> [new_nick]\n\nExamples:\n!sn @Ronit Badmas Gaymer", aliases=['sn', 'setnick', 'nickname'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(manage_nicknames=True), commands.has_permissions(administrator=True))
    async def my_nick_cmd(self, ctx, member: disnake.Member,*, new_nick: str):
        await member.edit(nick=new_nick)
        await ctx.send(msg["nickname"])

    @commands.command(name="unban", description="Unbans a member.", help="Unbans a member from the guild.", brief="Unbans a member.", usage="\nUsage:\n!unban <member> <duration>\n\nExamples:\n!unban 408785106942164992", aliases=['ub'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(manage_nicknames=True), commands.has_permissions(administrator=True))
    async def my_unban_command(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.banned_users

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {member}.")
    
    @commands.command(name='Remove-timeout', description="Removes timeout from a member.",help='Removes timeout from a member if they were timedout in past, optionally you can also set a reason which will show in audit logs.', brief="Removes Timeout.", usage="\nUsage:\n!rto <member> [reason]\n\nExamples:\n!rto @Arpit Ok don't repeat\n!rto @Ronit", aliases=['rto', 'unmute', 'um', 'untimeout'], enabled=True)
    @commands.check_any(commands.has_role(mrole), commands.is_owner(), commands.has_permissions(manage_nicknames=True), commands.has_permissions(administrator=True))
    async def my_remove_timeout_command(self, ctx, member: disnake.Member,*, reason: str=None) -> None:
        await member.timeout(duration=None, reason=reason)
        await member.send(msg["remove-timeout_dm"])
        await ctx.send(msg["remove-timeout"])

    @commands.command(name="hard-delete", hidden=True, aliases=['dadd', 'da'])
    @commands.has_permissions(administrator=True)
    async def my_hard_delete_command(self, ctx, member: disnake.Member):
        hard.append(member.id)
        await ctx.send(msg["hard-delete"])

    @commands.command(name="hard-delete-remove", hidden=True, aliases=['dremove', 'dr'])
    @commands.has_permissions(administrator=True)
    async def my_hard_delete_remove_command(self, ctx, member: disnake.Member):
        hard.append(member.id)
        await ctx.send(msg["hard-delete-remove"])

    @commands.Cog.listener()
    async def on_message(msg):
        if msg.author.id in hard:
            await msg.delete()

def setup(bot):
    bot.add_cog(Moderation(bot))
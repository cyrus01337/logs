from discord.ext import commands


# could work but unsure, this is the best idea I've got overriding
def listener(*args, **kwargs):
    return commands.Cog.listener(*args, **kwargs)


class Exclude:
    """
    Helper to ignore specific events/types of
    """
    def __init__(self, *events: str, types: set = set()):
        self.events = set(map(str.lower, events))
        self.types = types


class Logs(commands.Cog):
    TYPES = (
        "BOT",         # other bots add/remove
        "SELF",        # your bot's up/downtime
        "GUILD",       # settings update
        "MEMBER",      # add/update/remove
        "CHANNEL",     # add/update/remove
        "COMMAND",     # invocation
        "MESSAGE",     # bulk/update/remove, multi-content
        "REACTIONS",   # add/bulk/remove
    )

    def __init__(self, bot):
        self.bot = bot

        # self.exclude = Exclude()

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_command(self, *args):
        pass

    @commands.Cog.listener()
    async def on_command_completion(self, *args):
        pass

    @commands.Cog.listener()
    async def on_connect(self, *args):
        pass

    @commands.Cog.listener()
    async def on_disconnect(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_create(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_channel_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_integrations_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_join(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_remove(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_role_create(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_role_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_unavailable(self, *args):
        pass

    @commands.Cog.listener()
    async def on_guild_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_invite_create(self, *args):
        pass

    @commands.Cog.listener()
    async def on_invite_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_member_ban(self, *args):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, *args):
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, *args):
        pass

    @commands.Cog.listener()
    async def on_member_unban(self, *args):
        pass

    @commands.Cog.listener()
    async def on_member_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_message(self, *args):
        pass

    @commands.Cog.listener()
    async def on_message_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_message_edit(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_message_delete(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_message_edit(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_clear(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_clear_emoji(self, *args):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, *args):
        pass

    @commands.Cog.listener()
    async def on_reaction_add(self, *args):
        pass

    @commands.Cog.listener()
    async def on_reaction_clear(self, *args):
        pass

    @commands.Cog.listener()
    async def on_reaction_clear_emoji(self, *args):
        pass

    @commands.Cog.listener()
    async def on_reaction_remove(self, *args):
        pass

    @commands.Cog.listener()
    async def on_ready(self, *args):
        pass

    @commands.Cog.listener()
    async def on_resumed(self, *args):
        pass

    @commands.Cog.listener()
    async def on_shard_connect(self, *args):
        pass

    @commands.Cog.listener()
    async def on_shard_disconnect(self, *args):
        pass

    @commands.Cog.listener()
    async def on_shard_ready(self, *args):
        pass

    @commands.Cog.listener()
    async def on_shard_resumed(self, *args):
        pass

    @commands.Cog.listener()
    async def on_socket_raw_receive(self, *args):
        pass

    @commands.Cog.listener()
    async def on_socket_raw_send(self, *args):
        pass

    @commands.Cog.listener()
    async def on_user_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, *args):
        pass

    @commands.Cog.listener()
    async def on_webhooks_update(self, *args):
        pass


def setup(bot):
    bot.add_cog(Logs(bot))

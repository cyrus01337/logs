from typing import Set

import discord
from discord.ext import commands


# could work but unsure, this is the best idea I've got overriding
def listener(*args, **kwargs):
    return commands.Cog.listener(*args, **kwargs)


class LogsError(commands.CommandError):
    def __init__(self, error):
        self.original = error
        name = error.__class__.__name__

        super().__init__(f"Exception occurred in logs: {name}: {error}")


class Config:
    """
    Log settings helper
    """
    def __init__(self, **kwargs):
        self.suppress: bool = kwargs.pop("suppress", False)
        self.to_terminal: bool = kwargs.pop("to_terminal", False)
        self.events: Set[str] = kwargs.pop("events", set())
        self.types: Set[str] = kwargs.pop("types", set())

        if self.events:
            self.events = set(e.lower() for e in self.events)
        if self.types:
            self.types = set(e.upper() for e in self.types)


class Logs(commands.Cog):
    ALL = 1
    BOT = 2
    SELF = 3
    GUILD = 4
    MEMBER = 5
    CHANNEL = 6
    COMMAND = 7
    MESSAGE = 8
    REACTIONS = 9
    TYPES = (
        "ALL",
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

        self._config = Config(
            suppress=True,
        )
        self.LOGS_ID = -1
        self.suppress

    @property
    def config(self):
        config_found = getattr(self, "_config", None)

        if not config_found:
            self._config = Config()
        return config_found

    @property
    def logs(self):
        channel_found = self.bot.get_channel(self.LOGS_ID)

        if channel_found:
            return channel_found
        elif self.config.suppress:
            return None
        raise commands.ChannelNotFound(f"with ID {self.LOGS_ID}")

    async def log(self, content, **kwargs):
        """Can override"""
        if self.config.to_terminal:
            print(content)

        try:
            await self.logs.send(content, **kwargs)
        except discord.HTTPException as error:
            if not self.config.suppress:
                wrapped = LogsError(error)

                raise wrapped from error

    async def placeholder(self, *args):
        joined = (", ").join(a.__class__.__name__ for a in args)

        await self.log(joined)

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_command(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_command_completion(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_connect(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_disconnect(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_integrations_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_join(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_remove(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_role_create(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_role_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_unavailable(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_guild_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_invite_create(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_invite_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_member_ban(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_member_join(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_member_remove(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_member_unban(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_member_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_message(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_message_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_message_edit(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_message_edit(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_reaction_clear(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_reaction_clear_emoji(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_reaction_add(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_reaction_clear(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_reaction_clear_emoji(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_reaction_remove(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_ready(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_resumed(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_shard_connect(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_shard_disconnect(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_shard_ready(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_shard_resumed(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_socket_raw_receive(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_socket_raw_send(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_user_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_voice_state_update(self, *args):
        await self.placeholder(*args)

    @commands.Cog.listener()
    async def on_webhooks_update(self, *args):
        await self.placeholder(*args)


def setup(bot):
    bot.add_cog(Logs(bot))

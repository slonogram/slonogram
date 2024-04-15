==================
Quickstart
==================

Install
=======

    .. code-block:: shell
        
        $ python -m pip install slonogram[aiohttp]

Write your code
===============
    .. code-block:: python

        import asyncio
        from slonogram import (
            Bot,
            Dispatcher,
            Context,
            handler_from_compatible,
            poll_for_updates,
        )
        from slonogram.schemas import Message, Update

        @handler_from_compatible
        async def hello(ctx: Context[Message]) -> None:
            await ctx.reply("Hello, world!")

        @handler_from_compatible
        async def start(ctx: Context[Message]) -> None:
            await ctx.reply("Started!")

        @handler_from_compatible
        async def top_secret(ctx: Context[Message]) -> None:
            await ctx.reply("Launching nukes...")
            await asyncio.sleep(5)
            await ctx.reply("Done ✅")

        def create_secret_dispatcher() -> Dispatcher[Update]:
            return (
                Dispatcher[Update]()
                    # To increase conspiration!
                    .interested(edited_message=top_secret.command())
            )

        def create_dispatcher() -> Dispatcher[Update]:
            # Create dispatcher object
            return (
                Dispatcher[Update]()
                    # declare that our functions are interested
                    #  in `message` events
                    .interested(message=(start, hello))
                    # Dispatchers can be nested
                    .register(create_secret_dispatcher())                    
            )

        async def main() -> None:
            async with Bot.from_env() as bot:
                dp = create_dispatcher()
                await poll_for_updates(bot, dp)

        asyncio.run(main())

Launch!
=======

    .. code-block:: shell

        $ TG_TOKEN=<TELEGRAM_BOT_TOKEN> python main.py

Now your bot is running, go to the **Telegram**, type

- ``/start``

- ``/hello``

- ``/top_secret``

To see if something happens.


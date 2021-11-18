mariocard
==========

.. image:: https://discord.com/api/guilds/570368779150688266/embed.png
   :target: https://discord.com/invite/uynSzaTAF3
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/mariocard.svg
   :target: https://pypi.org/project/mariocard/
   :alt: PyPI version info
   
   
This is simple maker for level card in discord bot in discord.py or pycord.


Installing
----------

**Python 3.8 or higher is required**


.. code:: sh

    # Linux/macOS
    pip3 install mariocard

    # Windows
    pip install mariocard


Default Card Example
~~~~~~~~~~~~~

.. code:: py

   import discord
   from discord.ext import commands
   from mariocard import create_card, create_custom_card

   client = commands.Bot(command_prefix="!")
   
   
   #level from datebase
   level = 2
   
   #xp from datebase
   xp = 10
   
   #required xp for next level (from datebese or calculated)
   requiredxp = 20


   @client.command()
   async def card(ctx):
      img = await create_card(level, xp, requiredxp, ctx.message.author.name, ctx.message.author.avatar_url, "red")
      await ctx.send(file=img)

   client.run("token")

Custom Card Example
~~~~~~~~~~~~~

**You must have create folder assets in your bot files and put there bg.png file.**

.. code:: py

   import discord
   from discord.ext import commands
   from mariocard import create_card, create_custom_card

   client = commands.Bot(command_prefix="!")
   
   
   #level from datebase
   level = 2
   
   #xp from datebase
   xp = 10
   
   #required xp for next level (from datebese or calculated)
   requiredxp = 20


   @client.command()
   async def card(ctx):
      img = await create_custom_card(level, xp, requiredxp, ctx.message.author.name, ctx.message.author.avatar_url, "red")
      await ctx.send(file=img)

   client.run("token")


Generated Card
~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/mario1842/mariocard/main/created_card.png
   :target: https://github.com/mario1842/mariocard/blob/main/created_card.png
   :alt: Created card from example code




Links
------

- `Youtube Channel <https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A>`_
- `My Discord Server <https://discord.com/invite/uynSzaTAF3>`_
- `Download <https://pypi.org/project/mariocard/>`_

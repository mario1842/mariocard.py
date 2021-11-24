mariocard
==========

.. image:: https://discord.com/api/guilds/570368779150688266/embed.png
   :target: https://discord.com/invite/uynSzaTAF3
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/mariocard.svg
   :target: https://pypi.org/project/mariocard/
   :alt: PyPI version info
   
   
This is simple maker for cards in discord bot in discord.py or pycord.


Installing
~~~~~~~~~~

**Python 3.8 or higher is required**


.. code:: sh

    # Linux/macOS
    pip3 install mariocard

    # Windows
    pip install mariocard


Level Card Example
~~~~~~~~~~~~~~~~~~

.. code:: py

   from discord.ext import commands
   from mariocard import *

   client = commands.Bot(command_prefix=".")

   @client.command()
   async def card(ctx):
       levelcard = LevelCard()
       levelcard.avatar = ctx.author.avatar_url
       levelcard.name = ctx.author
       levelcard.xp = 10
       levelcard.required_xp = 20
       levelcard.level = 2

       file = await levelcard.create()
       await ctx.send(file=file)

   client.run("token")

Generated Level Card
~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/mario1842/mariocard/main/created_cards/levelcard.png
   :target: https://raw.githubusercontent.com/mario1842/mariocard/main/created_cards/levelcard.png
   :alt: Created card from example code


Welcome Card Example
~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from discord.ext import commands
   from mariocard import *

   client = commands.Bot(command_prefix=".")

   @client.command()
   async def card(ctx):
       levelcard = LevelCard()
       levelcard.avatar = ctx.author.avatar_url
       levelcard.name = ctx.author
       levelcard.server = "Server Name"

       file = await levelcard.create()
       await ctx.send(file=file)

   client.run("token")

Generated Welcome Card
~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/mario1842/mariocard/main/created_cards/welcomecard.png
   :target: https://raw.githubusercontent.com/mario1842/mariocard/main/created_cards/welcomecard.png
   :alt: Created card from example code


Links
-----

- `Github <https://github.com/mario1842/mariocard/>`_
- `Youtube Channel <https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A>`_
- `My Discord Server <https://discord.com/invite/uynSzaTAF3>`_
- `Download <https://pypi.org/project/mariocard/>`_

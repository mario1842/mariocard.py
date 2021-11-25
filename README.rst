mariocard.py
==========

.. image:: https://discord.com/api/guilds/570368779150688266/embed.png
   :target: https://discord.com/invite/uynSzaTAF3
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/mariocard.py.svg
   :target: https://pypi.org/project/mariocard.py/
   :alt: PyPI version info


This is simple maker for cards in discord bot in discord.py or pycord.


Installing
~~~~~~~~~~

**Python 3.8 or higher is required**


.. code:: sh

    # Linux/macOS
    pip3 install -U mariocard.py

    # Windows
    pip install -U mariocard.py


Level Card Example
~~~~~~~~~~~~~~~~~~

.. code:: py

   from discord.ext import commands
   from mariocard import *

   client = commands.Bot(command_prefix=".")

   @client.command()
   async def card(ctx):
       #creating levelcard object
       levelcard = LevelCard()
       
       #setting avatar url for image
       levelcard.avatar = ctx.author.avatar_url
       
       #setting member name
       levelcard.name = ctx.author
       
       #setting xp for bar on card
       levelcard.xp = 10
       
       #setting required xp for bar on card
       levelcard.required_xp = 20
       
       #setting level to text on crad
       levelcard.level = 2

       #sending image to discord channel
       await ctx.send(file=await levelcard.create())

   client.run("token")

Generated Level Card
~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/mario1842/mariocard.py/main/created_cards/levelcard.png
   :target: https://raw.githubusercontent.com/mario1842/mariocard.py/main/created_cards/levelcard.png
   :alt: Created card from example code.


Welcome Card Example
~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from discord.ext import commands
   from mariocard import *

   client = commands.Bot(command_prefix=".")

   @client.command()
   async def card(ctx):
       #creating levelcard object
       levelcard = LevelCard()
       
       #setting avatar url for image
       levelcard.avatar = ctx.author.avatar_url
       
       #setting member name
       levelcard.name = ctx.author
       
       #setting server name
       levelcard.server = ctx.guild.name

       #sending image to discord channel
       await ctx.send(file=await levelcard.create())

   client.run("token")

Generated Welcome Card
~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://raw.githubusercontent.com/mario1842/mariocard.py/main/created_cards/welcomecard.png
   :target: https://raw.githubusercontent.com/mario1842/mariocard.py/main/created_cards/welcomecard.png
   :alt: Created card from example code.


Links
-----
- `Documentation <https://mariocard.readthedocs.io/>`_
- `Github <https://github.com/mario1842/mariocard.py/>`_
- `Youtube Channel <https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A>`_
- `My Discord Server <https://discord.com/invite/uynSzaTAF3>`_
- `Download <https://pypi.org/project/mariocard.py/>`_

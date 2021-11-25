from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member


class LevelCard():

    def __init__(self):
        self.level : int = 1
        self.xp : int = 0
        self.required_xp : int = 1
        self.name : str = None
        self.avatar : str = None
        self.color : str = "violet"
        self.path : str = "https://raw.githubusercontent.com/mario1842/mariocard/main/bg.png"
        self.is_rounded : bool = False

    async def create(self):
        if(self.path.startswith('https://')):
            bgc = await load_image_async(str(self.path))
            background = Editor(bgc).resize((900, 300))
        else:
            background = Editor(self.path).resize((900, 300))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            if(self.is_rounded):
                profile = Editor(profile).resize((150, 150)).circle_image()
            else:
                profile = Editor(profile).resize((150, 150))
            background.paste(profile.image, (30, 40))

        poppins = Font().poppins(size=40)
        poppins_small = Font().poppins(size=30)

        background.rectangle((30, 210), width=840, height=50, fill="white", radius=20)
        background.bar(
            (30, 210),
            max_width=840,
            height=50,
            percentage= (int(self.xp) / int(self.required_xp)) * 100,
            fill=self.color,
            radius=20,
        )
        background.text((200, 40), str(self.name), font=poppins, color="white")

        background.rectangle((200, 100), width=350, height=4, fill=self.color)
        background.text(
            (200, 130),
            f"Level : {int(self.level)}"
            + f"      XP : {int(self.xp)} / {int(self.required_xp)}",
            font=poppins_small,
            color="white",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file

class WelcomeCard():

    def __init__(self):
        self.server : str = None
        self.name : str = None
        self.avatar : str = None
        self.color : str = "violet"
        self.path : str = "https://raw.githubusercontent.com/mario1842/mariocard/main/bg.png"
        self.text : str = "Welcome to the server!"
        self.is_rounded : bool = False

    async def create(self):
        if(self.path.startswith('https://')):
            bgc = await load_image_async(str(self.path))
            background = Editor(bgc).resize((900, 300))
        else:
            background = Editor(self.path).resize((900, 300))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            if(self.is_rounded):
                profile = Editor(profile).resize((150, 150)).circle_image()
            else:
                profile = Editor(profile).resize((150, 150))
            background.paste(profile.image, (30, 75))

        poppins = Font().poppins(size=40)
        poppins_small = Font().poppins(size=30)
        background.text((200, 35), str(f'    '+str(self.text)+' '), font=poppins, color="white")
        background.rectangle((275, 85), width=500, height=4, fill=self.color)
        background.text(
            (200, 120),
            f"Server: ",
            font=poppins,
            color=self.color,
        )
        background.text(
            (345, 115),
            f"{self.server}",
            font=poppins,
            color="white",
        )
        background.text(
            (200, 180),
            f"New User:",
            font=poppins,
            color=self.color,
        )
        background.text(
            (410, 178),
            f"{self.name}",
            font=poppins,
            color="white",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file

class GoodbyeCard():

    def __init__(self):
        self.server : str = None
        self.name : str = None
        self.avatar : str = None
        self.color : str = "violet"
        self.path : str = "https://raw.githubusercontent.com/mario1842/mariocard/main/bg.png"
        self.text : str = "Member left the server!"
        self.is_rounded : bool = False

    async def create(self):
        if(self.path.startswith('https://')):
            bgc = await load_image_async(str(self.path))
            background = Editor(bgc).resize((900, 300))
        else:
            background = Editor(self.path).resize((900, 300))
        if(self.avatar != None):
            profile = await load_image_async(str(self.avatar))
            if(self.is_rounded):
                profile = Editor(profile).resize((150, 150)).circle_image()
            else:
                profile = Editor(profile).resize((150, 150))
            background.paste(profile.image, (30, 75))

        poppins = Font().poppins(size=40)
        poppins_small = Font().poppins(size=30)
        background.text((200, 35), str(f'    '+str(self.text)+' '), font=poppins, color="white")
        background.rectangle((275, 85), width=500, height=4, fill=self.color)
        background.text(
            (200, 120),
            f"Server: ",
            font=poppins,
            color=self.color,
        )
        background.text(
            (345, 115),
            f"{self.server}",
            font=poppins,
            color="white",
        )
        background.text(
            (200, 180),
            f"Former User:",
            font=poppins,
            color=self.color,
        )
        background.text(
            (455, 178),
            f"{self.name}",
            font=poppins,
            color="white",
        )

        file = File(fp=background.image_bytes, filename="card.png")
        return file

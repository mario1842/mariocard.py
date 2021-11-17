from easy_pil import Editor, Canvas, load_image_async, Font
from discord import File, Member

async def create_card(level : int, xp : int, reqxp : int, member_name : str, member_avatar : str, color: str = "#FF56B2"):
    bgc = await load_image_async(str("https://raw.githubusercontent.com/shahriyardx/discordpy-leveling-bot/master/leveling/assets/bg.png"))
    background = Editor(bgc).resize((900, 300))
    profile = await load_image_async(str(member_avatar))

    profile = Editor(profile).resize((150, 150)).circle_image()
    poppins = Font().poppins(size=40)
    poppins_small = Font().poppins(size=30)
    background.paste(profile.image, (30, 30))

    background.rectangle((30, 210), width=840, height=50, fill="white", radius=20)
    background.bar(
        (30, 210),
        max_width=840,
        height=50,
        percentage= (xp / reqxp) * 100,
        fill=color,
        radius=20,
    )
    background.text((200, 40), str(member_name), font=poppins, color="white")

    background.rectangle((200, 100), width=350, height=4, fill=color)
    background.text(
        (200, 130),
        f"Level : {level}"
        + f"      XP : {xp} / {reqxp}",
        font=poppins_small,
        color="white",
    )

    file = File(fp=background.image_bytes, filename="card.png")
    return file

    
async def create_custom_card(level : int, xp : int, reqxp : int, member_name : str, member_avatar : str, color: str = "#FF56B2"):
    background = Editor("assets/bg.png").resize((900, 300))
    
    profile = await load_image_async(str(member_avatar))

    profile = Editor(profile).resize((150, 150)).circle_image()
    poppins = Font().poppins(size=40)
    poppins_small = Font().poppins(size=30)
    background.paste(profile.image, (30, 30))

    background.rectangle((30, 210), width=840, height=50, fill="white", radius=20)
    background.bar(
        (30, 210),
        max_width=840,
        height=50,
        percentage= (xp / reqxp) * 100,
        fill=color,
        radius=20,
    )
    background.text((200, 40), str(member_name), font=poppins, color="white")

    background.rectangle((200, 100), width=350, height=4, fill=color)
    background.text(
        (200, 130),
        f"Level : {level}"
        + f"      XP : {xp} / {reqxp}",
        font=poppins_small,
        color="white",
    )

    file = File(fp=background.image_bytes, filename="card.png")
    return file
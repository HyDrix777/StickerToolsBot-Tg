from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
π―ππ {}

πΎππππππ ππ {}

πππ πππ πππ ππππ πππ ππ πππππππ
1) πΊππππππ ππ π°ππππ
2) π°ππππ ππ πΊππππππ

πΊπππ π΄πππππππ ππππππ ππ ππππππππ πππ ππ ππππ ππππ πππ ππππ

β€οΈβ¨
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π£ Channel", url="https://t.me/Tg_Galaxy")],
        [InlineKeyboardButton(text="π  Return Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("π£ Channel", url="https://t.me/Galaxy_bots")
        ],
        [
            InlineKeyboardButton("π’ Help", callback_data="help"),
            InlineKeyboardButton("π About", callback_data="about")
        ],
        [InlineKeyboardButton("π₯ Group",url="https://t.me/Stdjdjdjkdjjbot")],
        
                              
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) Send Sticker to get Image
2) Send Image to get Sticker

Note : You can send any amount of images or stickers or both together at once and it will work with same speed and accuracy.

More features in development. Keep track tar.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @bots

Source Code : [Click Here](https://github.com/Srooyadustries/StickkolsBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using me βΊοΈ
    """

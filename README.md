# "No Voice" script for Telegram Messenger

Are you irritating by annoying voice messages from people who don't respect your time? They don't want to understand your request not to send voice messages? There is a solution! You can actually remove all incoming voice messages from everyone in Telegram!

This repository contains Python script which allows you to delete annoying voice messages from everyone in Telegram Messenger. All you need is the computer with 24/7 access to Internet (e.g., Linux or BSD server) and Python 3.x installed on it.

## How to use it

First download latest version of Python from this [link](https://www.python.org/downloads/ "Official link to download latest version of Python"), if you didn't do it earlier.

After that make sure that you have installed pip (Python Package Manager). It should be installed automatically with Python 3. To check whether pip is installed run following command:

### Windows
```
C:\> py -m pip --version
pip X.Y.Z from ...\site-packages\pip (python X.Y)≈
```

### Unix/macOS
```
C:\> py -m pip --version
pip X.Y.Z from ...\site-packages\pip (python X.Y)
```

Install "Telethon" package by using pip. Just enter following command in Terminal/Command Prompt:

```
pip install telethon
```

You can read full documentation of this package by opening this [link](https://pypi.org/project/Telethon/ "Documentation of the Telethon package").

## Final stage

Now we have all requisites to run "No Voice" script. The script requires to use API ID & API Hash (by default it uses API ID of "Telegram Desktop", but you can register your own app and use your APP ID).

Next you should edit this script to provide phone number and username:

```
phone = '+994501234567'
username = 'Your_Telegram_Username'
# password = 'YOUR_PASSWORD'
```

Notice that if you have two-step authentication enabled, you should uncomment password line and provide password to your Telegram.

After that you should run this script by typing:

```
python novoice.py
```

At first time it will require confirmation code which you will receive in Telegram App (because Telegram detects it as signing in from new device) and should type it in Terminal. After signing in the script will automatically delete all voice messages the second after sending. Note that by default it not deletes voice messages from group chats, but you can actually change the script by removing this line: `if event.is_private:`


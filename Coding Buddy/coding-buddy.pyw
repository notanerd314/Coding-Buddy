import pygame
import time
import os
import random
import platform
import configparser
from tkinter import *
from tkinter import messagebox
import webbrowser

# Config setup
directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, '\settings.ini')
config = configparser.ConfigParser()
config.read('settings.ini')
if not 'BASIC SETTINGS' in config:
    messagebox.showerror('Error', "You've edited the words in the brackets eh?")
    messagebox.showinfo('How to fix', "Go to my website, which is https://notanerd314.w3spaces.com/index.html, and replace the new one with the old one")
    webbrowser.open("https://notanerd314.w3spaces.com/index.html")
    exit()
if not 'ADVANCED' in config:
    messagebox.showerror('Error', "You've edited the words in the brackets eh?")
    messagebox.showinfo('How to fix', "Go to my website, which is https://notanerd314.w3spaces.com/index.html, and replace the new one with the old one")
    webbrowser.open("https://notanerd314.w3spaces.com/index.html")
    exit()

# Config data

hex = config['BASIC SETTINGS']['Text_Color']
bg = config['BASIC SETTINGS']['Bg_Image']
special = config['BASIC SETTINGS']['Special']

# variable setup

img_path = os.path.join(directory_path, f'resources\{bg}')
sfx_path = os.path.join(directory_path, 'resources\secret.mp3')
s = platform.system(), platform.release()
p = " ".join(s)
pygame.init()
words = [
    "Pygame sucks, it looks basic but it's stupidly complex",
    "hangout with me or else i will taskkill /im svchost.exe /f",
    "0.1 + 0.2 = 0.30000000000000000000000000004",
    "tax evasion is fun ngl",
    "i knew you're using the code editor in dark mode",
    "Pls play with me",
    "web development is pure garbage",
    "you can change how i exist in the settings.ini file",
    'did you know? 25% of my code was taken from StackOverFlow',                                          
    "i eat kids",
    "i'm asian",
    "cheezits",
    "godot is better than unity",
    "give me access to system32 so i can destroy it",
    f"Traceback (most recent call last): SHUT UP.",
    'Typescript or Javascript?',
    'The percentage between you and the society is 0%',
    'special123',
    f"you've wasted 0 seconds on this app (inaccurately)",
    'dear friend, talk to me or nothing happens',
    "🤓, that's me in an emoji form",
    "---___---",
    "3.14159265358979323846264338327950288419716939937510",
    "If you got A minus in math then that means you're a baby",
    "filler sentence",
    "LGBT is totally normal to me",
    "oh mommy! i want some chocolate!!1",
    "snack break?",
    "i was a developer but i got fired and become an application",
    "i wish i was a real person, not a python application",
    "are you copying code from StackOverFlow?",
    "fiddlesticks",
    "Wanna have free Robux? Go to ! (actually don't go)",
    "chrome is bulls###",
    "i am depressed",
    "touch grass, stop coding s###",
    f"The operating system you are using is {p}.",
    "source code when?",
    "Oh you like [Popular thing]. But did you know, [Popular thing] bad now.",
    "evade taxes, that's what real adults do.",
    "i feel so supercalifragilisticexpialidocious",
    "*vine boom x10*",
    "balls are snacks, they're CRUNCHY",
    "I use messagebox.showinfo() to do that, heh?",
    "MOMMY ATE MY CHOCOLATE!!~",
    "596F752776652077617374656420796F75722074696D6521",
    "move me around",
    "I miss my pet rock",
    "You have a 0.5% chance of having a girlfriend",
    "I wish I could kick strangers in real life.",
    "Check if forgot the semicolon",
    "If you're using this app in a big company then you're a chad 👍",
    "Linux users",
    "A chad uses the Arc browser",
    "I love chewing pens!",
]
ugh = len(words)+1
words.append(f"The total sentences I can speak is {ugh}")

# Hex to rgb setup

def convert(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0,2,4))
hex = convert(hex)

# pygame setup

img = pygame.image.load(img_path)
if config["ADVANCED"]['Resize'] == "1":
    window = pygame.display.set_mode(
        (int(config['BASIC SETTINGS']['Window_Width']),int(config['BASIC SETTINGS']['Window_Height'])), 
        pygame.RESIZABLE
    )
else:
    window = pygame.display.set_mode((int(config['BASIC SETTINGS']['Window_Width']),int(config['BASIC SETTINGS']['Window_Height'])))
ran = words[random.randint(0, len(words)-1)]
if config["ADVANCED"]["Text_Sync"] == "1":
    pygame.display.set_caption(ran)
else:
    pygame.display.set_caption(config["ADVANCED"]["Window_Name"])
pygame.display.set_icon(img)
background = pygame.image.load(img_path).convert()
background = pygame.transform.smoothscale(background, window.get_size())
sfx = pygame.mixer.Sound(sfx_path)
font = pygame.font.SysFont(config["BASIC SETTINGS"]['Text_Font'], int(config["BASIC SETTINGS"]['Text_Size']))
text = font.render(ran, True, hex)
textrect = text.get_rect()
textrect.bottomleft = (0, window.get_height())
caption_timer = time.time()
caption_interval = int(config['ADVANCED']['Time_Delay'])
run = True

# running loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if time.time() - caption_timer >= caption_interval:
        ran = words[random.randint(0, len(words)-1)]
        if config["GOOFY"]["Size_Change"] == "1":
            if config["ADVANCED"]['Resize'] == "1":
                window = pygame.display.set_mode(
                            (random.randint(300,1000), random.randint(300,1000)), 
                            pygame.RESIZABLE
                        )
            else:
                 window = pygame.display.set_mode(
                            (random.randint(300,1000), random.randint(300,1000)), 
                        )
        if ran == "*vine boom x10*" and special == '1':
            for a in range(10):
                sfx.play()
                time.sleep(.05)
        elif ran == "special123":
            ran = f"Random number generator, generated: {random.randint(0,10000000)}"
        elif ran == "I use messagebox.showinfo() to do that, heh?" and special == '1':
            messagebox.showinfo("Info","Stop concentrating, fool.")
        
        if config["ADVANCED"]["Text_Sync"] == "1":
            pygame.display.set_caption(ran)
        else:
            pygame.display.set_caption(config["ADVANCED"]["Window_Name"])
        text = font.render(ran, True, hex)
        textrect = text.get_rect()
        caption_timer = time.time()
    textrect.bottomleft = (0, window.get_height())
    window.blit(background, (0, 0))
    window.blit(text, textrect)
    background = pygame.transform.smoothscale(background, window.get_size())
    pygame.display.flip()

# ouch
    
pygame.quit()
exit()

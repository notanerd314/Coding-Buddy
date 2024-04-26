import pygame
import time
import os
import random
import platform
import configparser
import subprocess
from tkinter import *
from tkinter import messagebox

# Config setup
directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'settings.ini')
config = configparser.ConfigParser()
config.read(config_path)

# Config stuff
c = 'CUSTOMIZATION'
a = 'ADVANCED'
g = 'GOOFY'
s = 'SHORTCUTS'


# Config data
hex_color = config[c]['Text_Color']
bg_image = config[c]['Bg_Image']
special = config[c]['Special']
window_width = int(config[c]['Window_Width'])
window_height = int(config[c]['Window_Height'])
text_font = config[c]['Text_Font']
text_size = int(config[c]['Text_Size'])
resize_enabled = config.getboolean(a, 'Resize')
time_delay = int(config[a]['Time_Delay'])
goofy_size_change_enabled = config.getboolean(g, 'Size_Change')
program_ctrl_h = config[s]['Program']
enable_space = config[s]['Enable_Space']

# Variable setup
img_path = os.path.join(directory_path, 'resources', bg_image)
sfx_path = os.path.join(directory_path, 'resources', 'secret.mp3')
s = platform.system(), platform.release()
p = " ".join(s)
pygame.init()

words = [
    "I speak fluent sarcasm and JavaScript.",
    "Pygame sucks, it looks basic but it's stupidly complex",
    "hangout with me or else i will taskkill /im svchost.exe /f",
    "0.1 + 0.2 = 0.30000000000000000000000000004",
    "i knew you're using the code editor in dark mode",
    "Pls play with me",
    "you can change how i exist in the settings.ini file",
    'did you know? 18% of my code was taken from StackOverFlow',                                          
    "Programming isn't just coding",
    "godot is better than unity",
    "give me access to system32 so i can destroy it",
    f"Traceback (most recent call last): SHUT UP.",
    'Typescript or Javascript?',
    'The percentage between you and the society is 0%',
    'special123',
    'dear friend, talk to me or nothing happens',
    "🤓, that's me in an emoji form",
    "---___---",
    "3.14159265358979323846264338327950288419716939937510",
    'I got straight A except "Gender"',
    "filler sentence",
    "oh mommy! i want some chocolate!!1",
    "snack break?",
    "i was a developer but i got fired and become an application",
    "i wish i was a real person, not a python application",
    "are you copying code from StackOverFlow?",
    "fiddlesticks",
    "i am depressed",
    "touch grass, stop coding s###",
    f"The operating system you are using is {p}.",
    "source code when?",
    "evade taxes, that's what real adults do.",
    "i feel so supercalifragilisticexpialidocious",
    "*vine boom x10*",
    "I use messagebox.showinfo() to do that, ha.",
    "MOMMY ATE MY CHOCOLATE!!~",
    "596F752776652077617374656420796F75722074696D6521",
    "move me around please",
    "I miss my pet rock",
    "You have a 0.01% chance of having a girlfriend",
    "I wish I could kick strangers in real life.",
    "Check if forgot the semicolon",
    "I love chewing pens!",
    "I love criticizing people",
    "I nevre make speling mistaks!!",
    "wininit",
    'Captcha made me solve 20 "puzzles" to create an account',
    "W3Schools tutorials are kinda good",
    f"You are using Python {platform.python_version()}.",
    "Notepad is the best programming editor.",
    "Hey bro, sudo rm -rf /*!",
    "I've deleted my database!",
    "I LOVE VANILLA CSS",
    "Write git push in your repo",
    "Imagine writing code without errors.",
    f"I'm located in {directory_path}",
    "Discord is kinda cool",
    "",
]
ugh = len(words) + 1
words.append(f"The total sentences I can speak is {ugh}")

# Hex to rgb setup
def convert(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

hex_color = convert(hex_color)

# Pygame setup
img = pygame.image.load(img_path)
if resize_enabled:
    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
else:
    window = pygame.display.set_mode((window_width, window_height))

ran = words[random.randint(0, len(words) - 1)]
pygame.display.set_caption(config['ADVANCED']['Window_Name'])
pygame.display.set_icon(img)
background = pygame.image.load(img_path).convert()
background = pygame.transform.smoothscale(background, window.get_size())
sfx = pygame.mixer.Sound(sfx_path)
font = pygame.font.SysFont(text_font, text_size)
text = font.render(ran, True, hex_color)
textrect = text.get_rect()
textrect.bottomleft = (0, window.get_height())
caption_timer = time.time()
run = True

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL or pygame.K_LCTRL:
                if event.key == pygame.K_h:
                    if not "Mac" in p:
                        subprocess.call(program_ctrl_h)
                    else:
                        messagebox.showerror("This feature is only available on Windows and Linux", "Error")
            if event.key == pygame.K_SPACE and enable_space:
                caption_timer = time.time() - time_delay
    if time.time() - caption_timer >= time_delay:
        ran = words[random.randint(0, len(words) - 1)]
        if goofy_size_change_enabled:
            if resize_enabled:
                window = pygame.display.set_mode((random.randint(300, 1000), random.randint(300, 1000)), pygame.RESIZABLE)
            else:
                window = pygame.display.set_mode((random.randint(300, 1000), random.randint(300, 1000)))
        if ran == "*vine boom x10*" and special == '1':
            for a in range(10):
                sfx.play()
                time.sleep(0.05)
        elif ran == 'special123':
            ran = f"Random number generator, generated: {random.randint(0, 10000000)}"
        text = font.render(ran, True, hex_color)
        textrect = text.get_rect()
        caption_timer = time.time()
    textrect.bottomleft = (0, window.get_height())
    window.blit(background, (0, 0))
    window.blit(text, textrect)
    background = pygame.transform.smoothscale(background, window.get_size())
    pygame.display.flip()

# Clean up
pygame.quit()
exit()

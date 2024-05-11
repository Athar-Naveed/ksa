import pyautogui as pg
import os,time,random
from dotenv import load_dotenv
load_dotenv()
os.environ['DISPLAY'] = ':0'
username=os.getenv('username')
os.environ['XAUTHOTITY'] = f'/home/{username}.Xauthority'

duration = int(input("Please enter the duration you want to keep your screen active (min): "))*60
lock_screen_time = int(input("Please enter your lock screen time (min): "))*60
start = 0
for _ in range(start,duration):
    print(f"Script started: {start}")
    pg.moveTo(random.randint(10,500),random.randint(10,500),duration=5)
    start += lock_screen_time//2
    time.sleep(lock_screen_time//2)
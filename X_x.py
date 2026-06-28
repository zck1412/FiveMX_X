import os
import sys

# --- BUỘC YOLO CHẠY OFFLINE HOÀN TOÀN & BỎ QUA KIỂM TRA ĐỒNG BỘ ---
os.environ["YOLO_NO_VERSION_CHECK"] = "True"
os.environ["SETTINGS_YOLO_NO_VERSION_CHECK"] = "True"
os.environ["YOLO_VERBOSE"] = "False"
# --------------------------------------------------------------------

import json
import threading
import logging
import logging.config
import seaborn
import pandas
import tqdm
import scipy
import matplotlib
import PIL
import yaml
import psutil

from pynput import keyboard
from termcolor import colored


def on_release(key):
    try:
        if key == keyboard.Key.page_up:
            Aimbot.update_status_aimbot(siema=False)
        if key == keyboard.Key.end:
            Aimbot.clean_up()
        if key == keyboard.Key.insert:
            Aimbot.update_status_aimbot(siema=True)
    except NameError:
        pass


def main():
    global fajmbot
    headless = True
    if "gui" in sys.argv or "--gui" in sys.argv:
        headless = False
    fajmbot = Aimbot(collect_data = "collect_data" in sys.argv, headless = headless)
    fajmbot.start()

def setup():
    path = "lib/config"
    if not os.path.exists(path):
        os.makedirs(path)

    def prompt(str, is_integer=False):
        valid_input = False
        while not valid_input:
            try:
                if is_integer:
                    number = int(input(str))
                else:
                    number = float(input(str))
                valid_input = True
            except ValueError:
                print("[!] Đầu vào không hợp lệ. Vui lòng chỉ nhập số (Ví dụ: 1920)")
        return number

    print("\n--- THIẾT LẬP CẤU HÌNH BAN ĐẦU ---")
    screen_width = prompt("Screen Width (Độ rộng màn hình game - ví dụ 1920): ", is_integer=True)
    screen_height = prompt("Screen Height (Độ cao màn hình game - ví dụ 1080): ", is_integer=True)

    # Đưa các thông số điều chỉnh vào JSON để người dùng cấu hình thủ công không cần code
    screen_settings = {
        "screen_width": screen_width,
        "screen_height": screen_height,
        "fov": 416,            # Kích thước vùng quét mục tiêu (càng lớn vùng quét càng rộng)
        "aim_speed": 0.7       # Tốc độ bám mục tiêu (0.1 là mượt/chậm, 1.0 là khóa tức thời)
    }

    with open('lib/config/config.json', 'w') as outfile:
        json.dump(screen_settings, outfile, indent=4)

    print("[INFO] Thiết lập cấu hình hoàn tất!")

if __name__ == "__main__":
    # --- ÉP TIẾN TRÌNH BỎ QUA SCALE 125%/150% CỦA WINDOWS (DPI AWARENESS) ---
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except:
            pass
    # ------------------------------------------------------------------

    os.system('cls' if os.name == 'nt' else 'clear')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

    path_exists = os.path.exists("lib/config/config.json")
    if not path_exists or ("setup" in sys.argv):
        if not path_exists:
            print("[!] Cấu hình độ phân giải chưa được thiết lập.")
        setup()
    path_exists = os.path.exists("lib/data")
    if "collect_data" in sys.argv and not path_exists:
        os.makedirs("lib/data")
        
    from lib.aimbot import Aimbot
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    main()
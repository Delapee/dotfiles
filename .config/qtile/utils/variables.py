from os import path

from utils.dir import get_qtile_dir

HOME = path.expanduser("~")
XDG = ".config/qtile"
QTILE_DIR = get_qtile_dir(HOME, XDG)
CONFIG_DIR = f"{QTILE_DIR}/config.json"
IMG_DIR = f"{QTILE_DIR}/img"
WALLPAPER_DIR = f"{IMG_DIR}/wallpapers"
ICON_DIR = f"{IMG_DIR}/ICONS"
COLOR_SCHEME_DIR = f"{QTILE_DIR}/utils/color_scheme"

WORKSPACE_NAMES = [
    "",  # terminal
    "",  # code
    "",  # firefox
    "",  # chrome
    "",  # discord
    "",  # spotify
    "",  # folder
    "",  # doc
]

DEFAULT_CONFIG = {
    "bar": "decorated",
    "colorscheme": "nord",
    "terminal": "kitty",
    "wallpaper_main": f"{WALLPAPER_DIR}/sword.jpg",
    "wallpaper_sec": f"{WALLPAPER_DIR}/sword.jpg",
    "with_battery": True,
    "with_wlan": True,
    "network": "wlp2s0",
    "two_monitors": False,
}

DEFAULT_COLOR = {
    "bg": "#202020",
    "fg": "#6D0ABA",
    "dark": "#161320",
    "black": "#302D41",
    "gray": "#575268",
    "darkgray": "#363a4f",
    "white": "#D0E0EE",
    "yellow": "#FAE3B0",
    "purple": "#8F00FF",
    "maroon": "#E8A2AF",
    "pink": "#F5C2E7",
    "green": "#ABE9B3",
    "red": "#FF0800",
    "blue": "#1793D1",
}

import subprocess

from libqtile import hook

from utils import HOME


@hook.subscribe.startup_once
def start_once():
    subprocess.call([HOME + "/.config/qtile/scripts/autostart.sh"])

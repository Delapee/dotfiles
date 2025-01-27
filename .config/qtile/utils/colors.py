import json
import os

from utils.settings import config
from utils.variables import COLOR_SCHEME_DIR, DEFAULT_COLOR


def _get_color() -> dict:
    color_schemes = os.listdir(COLOR_SCHEME_DIR)

    for scheme in color_schemes:
        if config["colorscheme"] == os.path.splitext(scheme)[0]:
            with open(f"{COLOR_SCHEME_DIR}/{scheme}", "r") as color_file:
                return json.load(color_file)

    return DEFAULT_COLOR.copy()


color = _get_color()

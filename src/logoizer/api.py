from __future__ import annotations

import pathlib
from typing import TextIO

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager


def load_logo_font(family: str = "Quicksand") -> None:
    this_folder = pathlib.Path(__file__).parent
    path_to_fonts = this_folder / "fonts" / family / "static"
    for font in path_to_fonts.glob("*.ttf"):
        font_manager.fontManager.addfont(str(font))
    mpl.rc("font", family=family)


def logoize(words: str, dest: TextIO, light: bool = True, format: str = "svg") -> None:
    color = (0.0, 0.0, 0.0) if light else (1.0, 1.0, 1.0)
    load_logo_font()

    plt.figtext(
        0.5,
        0.5,
        words,
        size=500,
        ha="center",
        va="center",
        fontweight="bold",
        color=color,
    )
    plt.savefig(dest, bbox_inches="tight", transparent=True, format=format)

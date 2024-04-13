from __future__ import annotations

import os
import sys
from glob import glob
from io import BytesIO

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

if sys.version_info >= (3, 12):  # pragma: no cover (PY12+)
    import importlib.resources as importlib_resources
else:  # pragma: no cover (<PY312)
    import importlib_resources


def _load_logo_font(family: str = "Quicksand") -> None:
    path_to_fonts = str(
        importlib_resources.files("logoizer") / "fonts" / family / "static"
    )
    for font in glob(os.path.join(path_to_fonts, "*.ttf")):
        font_manager.fontManager.addfont(str(font))
    mpl.rc("font", family=family)


def logoize(words: str, dest: BytesIO, light: bool = True, format: str = "svg") -> None:
    color = (0.0, 0.0, 0.0) if light else (1.0, 1.0, 1.0)
    _load_logo_font()

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

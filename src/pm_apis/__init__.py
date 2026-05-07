"""Compatibility import package for :mod:`polymarket_apis`."""

from __future__ import annotations

import sys
from importlib import import_module

from polymarket_apis import *  # noqa: F403
from polymarket_apis import __all__, __author__, __email__, __version__

_SUBMODULES = {
    "clients",
    "testing",
    "types",
    "utilities",
}


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = import_module(f"polymarket_apis.{name}")
        sys.modules[f"{__name__}.{name}"] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

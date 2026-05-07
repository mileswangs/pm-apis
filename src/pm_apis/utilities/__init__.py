"""Compatibility import package for :mod:`polymarket_apis.utilities`."""

from __future__ import annotations

import sys
from importlib import import_module

from polymarket_apis.utilities import *  # noqa: F403

_SUBMODULES = {
    "config",
    "constants",
    "endpoints",
    "exceptions",
    "headers",
    "order_builder",
    "signing",
    "web3",
}

for _submodule in _SUBMODULES:
    sys.modules[f"{__name__}.{_submodule}"] = import_module(
        f"polymarket_apis.utilities.{_submodule}"
    )


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = import_module(f"polymarket_apis.utilities.{name}")
        sys.modules[f"{__name__}.{name}"] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

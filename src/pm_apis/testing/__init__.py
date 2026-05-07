"""Compatibility import package for :mod:`polymarket_apis.testing`."""

from __future__ import annotations

import sys
from importlib import import_module

from polymarket_apis.testing import *  # noqa: F403
from polymarket_apis.testing import __all__

_SUBMODULES = {"contract_assertions"}

for _submodule in _SUBMODULES:
    sys.modules[f"{__name__}.{_submodule}"] = import_module(
        f"polymarket_apis.testing.{_submodule}"
    )


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = import_module(f"polymarket_apis.testing.{name}")
        sys.modules[f"{__name__}.{name}"] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

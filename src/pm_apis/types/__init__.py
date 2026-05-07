"""Compatibility import package for :mod:`polymarket_apis.types`."""

from __future__ import annotations

import sys
from importlib import import_module

from polymarket_apis.types import *  # noqa: F403
from polymarket_apis.types import __all__

_SUBMODULES = {
    "clob_types",
    "common",
    "data_types",
    "gamma_types",
    "web3_types",
    "websockets_types",
}

for _submodule in _SUBMODULES:
    sys.modules[f"{__name__}.{_submodule}"] = import_module(
        f"polymarket_apis.types.{_submodule}"
    )


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = import_module(f"polymarket_apis.types.{name}")
        sys.modules[f"{__name__}.{name}"] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

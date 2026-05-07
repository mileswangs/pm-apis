"""Compatibility import package for :mod:`polymarket_apis.clients`."""

from __future__ import annotations

import sys
from importlib import import_module

from polymarket_apis.clients import *  # noqa: F403
from polymarket_apis.clients import __all__

_SUBMODULES = {
    "clob_client",
    "data_client",
    "gamma_client",
    "graphql_client",
    "web3_client",
    "websockets_client",
}

for _submodule in _SUBMODULES:
    sys.modules[f"{__name__}.{_submodule}"] = import_module(
        f"polymarket_apis.clients.{_submodule}"
    )


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = import_module(f"polymarket_apis.clients.{name}")
        sys.modules[f"{__name__}.{name}"] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

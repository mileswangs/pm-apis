"""Compatibility re-exports for :mod:`polymarket_apis.clients.web3_client`."""

from __future__ import annotations

from polymarket_apis.clients.web3_client import (
    BaseWeb3Client as BaseWeb3Client,
    PolymarketWeb3Client as PolymarketWeb3Client,
    PolymarketGaslessWeb3Client as PolymarketGaslessWeb3Client,
)

__all__ = [
    "BaseWeb3Client",
    "PolymarketWeb3Client",
    "PolymarketGaslessWeb3Client",
]

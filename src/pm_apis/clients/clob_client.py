"""Compatibility re-exports for :mod:`polymarket_apis.clients.clob_client`."""

from __future__ import annotations

from polymarket_apis.clients.clob_client import (
    logger as logger,
    PolymarketReadOnlyClobClient as PolymarketReadOnlyClobClient,
    PolymarketClobClient as PolymarketClobClient,
)

__all__ = [
    "logger",
    "PolymarketReadOnlyClobClient",
    "PolymarketClobClient",
]

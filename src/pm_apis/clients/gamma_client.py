"""Compatibility re-exports for :mod:`polymarket_apis.clients.gamma_client`."""

from __future__ import annotations

from polymarket_apis.clients.gamma_client import (
    generate_random_id as generate_random_id,
    PolymarketGammaClient as PolymarketGammaClient,
)

__all__ = [
    "generate_random_id",
    "PolymarketGammaClient",
]

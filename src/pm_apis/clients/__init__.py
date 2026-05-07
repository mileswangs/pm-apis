"""Compatibility re-exports for :mod:`polymarket_apis.clients`."""

from __future__ import annotations

from polymarket_apis.clients import (
    AsyncPolymarketGraphQLClient as AsyncPolymarketGraphQLClient,
    PolymarketClobClient as PolymarketClobClient,
    PolymarketDataClient as PolymarketDataClient,
    PolymarketGammaClient as PolymarketGammaClient,
    PolymarketGaslessWeb3Client as PolymarketGaslessWeb3Client,
    PolymarketGraphQLClient as PolymarketGraphQLClient,
    PolymarketReadOnlyClobClient as PolymarketReadOnlyClobClient,
    PolyWSS as PolyWSS,
    PolyWSSMarket as PolyWSSMarket,
    PolymarketWeb3Client as PolymarketWeb3Client,
)

__all__ = [
    "AsyncPolymarketGraphQLClient",
    "PolymarketClobClient",
    "PolymarketDataClient",
    "PolymarketGammaClient",
    "PolymarketGaslessWeb3Client",
    "PolymarketGraphQLClient",
    "PolymarketReadOnlyClobClient",
    "PolyWSS",
    "PolyWSSMarket",
    "PolymarketWeb3Client",
]

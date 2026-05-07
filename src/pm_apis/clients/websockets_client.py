"""Compatibility re-exports for :mod:`polymarket_apis.clients.websockets_client`."""

from __future__ import annotations

from polymarket_apis.clients.websockets_client import (
    logger as logger,
    RECONNECT_BACKOFF_INITIAL_SECONDS as RECONNECT_BACKOFF_INITIAL_SECONDS,
    RECONNECT_BACKOFF_MAX_SECONDS as RECONNECT_BACKOFF_MAX_SECONDS,
    MARKET_EVENT_CLASSES as MARKET_EVENT_CLASSES,
    USER_EVENT_CLASSES as USER_EVENT_CLASSES,
    LIVE_DATA_EVENT_CLASSES as LIVE_DATA_EVENT_CLASSES,
    PolyWSSMarket as PolyWSSMarket,
    PolymarketWebsocketsClient as PolymarketWebsocketsClient,
    PolyWSS as PolyWSS,
)

__all__ = [
    "logger",
    "RECONNECT_BACKOFF_INITIAL_SECONDS",
    "RECONNECT_BACKOFF_MAX_SECONDS",
    "MARKET_EVENT_CLASSES",
    "USER_EVENT_CLASSES",
    "LIVE_DATA_EVENT_CLASSES",
    "PolyWSSMarket",
    "PolymarketWebsocketsClient",
    "PolyWSS",
]

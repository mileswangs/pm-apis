"""Compatibility re-exports for :mod:`polymarket_apis.clients.graphql_client`."""

from __future__ import annotations

from polymarket_apis.clients.graphql_client import (
    PolymarketGraphQLClient as PolymarketGraphQLClient,
    AsyncPolymarketGraphQLClient as AsyncPolymarketGraphQLClient,
)

__all__ = [
    "PolymarketGraphQLClient",
    "AsyncPolymarketGraphQLClient",
]

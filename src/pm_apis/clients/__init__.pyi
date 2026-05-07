# Static typing facade for ``pm_apis.clients``.
#
# The runtime package lazily forwards these names to ``polymarket_apis.clients``;
# this file lists the aggregate client exports for editor completions and
# type-checker resolution.
from polymarket_apis.clients import (
    # GraphQL clients.
    AsyncPolymarketGraphQLClient as AsyncPolymarketGraphQLClient,
    PolymarketGraphQLClient as PolymarketGraphQLClient,
    # REST-style API clients.
    PolymarketClobClient as PolymarketClobClient,
    PolymarketDataClient as PolymarketDataClient,
    PolymarketGammaClient as PolymarketGammaClient,
    PolymarketReadOnlyClobClient as PolymarketReadOnlyClobClient,
    # Web3 and websocket clients.
    PolymarketGaslessWeb3Client as PolymarketGaslessWeb3Client,
    PolymarketWeb3Client as PolymarketWeb3Client,
    PolyWSS as PolyWSS,
    PolyWSSMarket as PolyWSSMarket,
)

# Keep ``__all__`` typed without duplicating the runtime export list.
__all__: list[str]

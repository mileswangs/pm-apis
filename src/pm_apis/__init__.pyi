# Static typing facade for the short ``pm_apis`` compatibility package.
#
# Runtime imports are forwarded dynamically by ``pm_apis.__init__``. This stub
# makes the main public SDK entry points visible to type checkers and editors.
from polymarket_apis import (
    # Common CLOB argument and credential models re-exported at package root.
    ApiCreds as ApiCreds,
    FeeSchedule as FeeSchedule,
    MarketIDs as MarketIDs,
    MarketOrderArgs as MarketOrderArgs,
    OrderArgs as OrderArgs,
    OrderType as OrderType,
    # Client classes exposed by the canonical ``polymarket_apis`` package.
    AsyncPolymarketGraphQLClient as AsyncPolymarketGraphQLClient,
    PolymarketClobClient as PolymarketClobClient,
    PolymarketDataClient as PolymarketDataClient,
    PolymarketGammaClient as PolymarketGammaClient,
    PolymarketGaslessWeb3Client as PolymarketGaslessWeb3Client,
    PolymarketGraphQLClient as PolymarketGraphQLClient,
    PolymarketReadOnlyClobClient as PolymarketReadOnlyClobClient,
    PolymarketWeb3Client as PolymarketWeb3Client,
    PolyWSS as PolyWSS,
    PolyWSSMarket as PolyWSSMarket,
    # Package metadata mirrored from ``polymarket_apis``.
    __author__ as __author__,
    __email__ as __email__,
    __version__ as __version__,
)

# Keep ``__all__`` typed without duplicating the runtime export list.
__all__: list[str]

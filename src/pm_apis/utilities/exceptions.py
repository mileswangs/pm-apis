"""Compatibility re-exports for :mod:`polymarket_apis.utilities.exceptions`."""

from __future__ import annotations

from polymarket_apis.utilities.exceptions import (
    InvalidPriceError as InvalidPriceError,
    InvalidTickSizeError as InvalidTickSizeError,
    InvalidFeeRateError as InvalidFeeRateError,
    LiquidityError as LiquidityError,
    MissingOrderbookError as MissingOrderbookError,
    AuthenticationRequiredError as AuthenticationRequiredError,
    SafeAlreadyDeployedError as SafeAlreadyDeployedError,
    BuilderRateLimitError as BuilderRateLimitError,
)

__all__ = [
    "InvalidPriceError",
    "InvalidTickSizeError",
    "InvalidFeeRateError",
    "LiquidityError",
    "MissingOrderbookError",
    "AuthenticationRequiredError",
    "SafeAlreadyDeployedError",
    "BuilderRateLimitError",
]

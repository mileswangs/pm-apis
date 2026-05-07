"""Compatibility re-exports for :mod:`polymarket_apis.utilities.signing.hmac`."""

from __future__ import annotations

from polymarket_apis.utilities.signing.hmac import (
    build_hmac_signature as build_hmac_signature,
)

__all__ = [
    "build_hmac_signature",
]

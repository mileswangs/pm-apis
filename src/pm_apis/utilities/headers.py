"""Compatibility re-exports for :mod:`polymarket_apis.utilities.headers`."""

from __future__ import annotations

from polymarket_apis.utilities.headers import (
    POLY_ADDRESS as POLY_ADDRESS,
    POLY_SIGNATURE as POLY_SIGNATURE,
    POLY_TIMESTAMP as POLY_TIMESTAMP,
    POLY_NONCE as POLY_NONCE,
    POLY_API_KEY as POLY_API_KEY,
    POLY_PASSPHRASE as POLY_PASSPHRASE,
    POLY_BUILDER_API_KEY as POLY_BUILDER_API_KEY,
    POLY_BUILDER_PASSPHRASE as POLY_BUILDER_PASSPHRASE,
    POLY_BUILDER_SIGNATURE as POLY_BUILDER_SIGNATURE,
    POLY_BUILDER_TIMESTAMP as POLY_BUILDER_TIMESTAMP,
    RELAYER_API_KEY as RELAYER_API_KEY,
    RELAYER_API_KEY_ADDRESS as RELAYER_API_KEY_ADDRESS,
    create_level_1_headers as create_level_1_headers,
    create_level_2_headers as create_level_2_headers,
    create_relayer_headers as create_relayer_headers,
)

__all__ = [
    "POLY_ADDRESS",
    "POLY_SIGNATURE",
    "POLY_TIMESTAMP",
    "POLY_NONCE",
    "POLY_API_KEY",
    "POLY_PASSPHRASE",
    "POLY_BUILDER_API_KEY",
    "POLY_BUILDER_PASSPHRASE",
    "POLY_BUILDER_SIGNATURE",
    "POLY_BUILDER_TIMESTAMP",
    "RELAYER_API_KEY",
    "RELAYER_API_KEY_ADDRESS",
    "create_level_1_headers",
    "create_level_2_headers",
    "create_relayer_headers",
]

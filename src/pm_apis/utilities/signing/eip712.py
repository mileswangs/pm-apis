"""Compatibility re-exports for :mod:`polymarket_apis.utilities.signing.eip712`."""

from __future__ import annotations

from polymarket_apis.utilities.signing.eip712 import (
    CLOB_DOMAIN_NAME as CLOB_DOMAIN_NAME,
    CLOB_VERSION as CLOB_VERSION,
    MSG_TO_SIGN as MSG_TO_SIGN,
    get_clob_auth_domain as get_clob_auth_domain,
    sign_clob_auth_message as sign_clob_auth_message,
)

__all__ = [
    "CLOB_DOMAIN_NAME",
    "CLOB_VERSION",
    "MSG_TO_SIGN",
    "get_clob_auth_domain",
    "sign_clob_auth_message",
]

"""Compatibility re-exports for :mod:`polymarket_apis.testing`."""

from __future__ import annotations

from polymarket_apis.testing import (
    assert_api_contract as assert_api_contract,
    fail_contract as fail_contract,
    fetch_json as fetch_json,
)

__all__ = [
    "assert_api_contract",
    "fail_contract",
    "fetch_json",
]

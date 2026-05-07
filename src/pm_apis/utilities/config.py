"""Compatibility re-exports for :mod:`polymarket_apis.utilities.config`."""

from __future__ import annotations

from polymarket_apis.utilities.config import (
    CONFIG as CONFIG,
    NEG_RISK_CONFIG as NEG_RISK_CONFIG,
    get_contract_config as get_contract_config,
    GRAPHQL_ENDPOINTS as GRAPHQL_ENDPOINTS,
)

__all__ = [
    "CONFIG",
    "NEG_RISK_CONFIG",
    "get_contract_config",
    "GRAPHQL_ENDPOINTS",
]

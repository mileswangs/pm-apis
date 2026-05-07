"""Compatibility re-exports for :mod:`polymarket_apis.testing.contract_assertions`."""

from __future__ import annotations

from polymarket_apis.testing.contract_assertions import (
    SNAPSHOT_DIR as SNAPSHOT_DIR,
    AUTO_EXPAND_CONTRACT as AUTO_EXPAND_CONTRACT,
    UPDATE_SNAPSHOTS as UPDATE_SNAPSHOTS,
    EXPANSION_REPORT_PATH as EXPANSION_REPORT_PATH,
    UnknownFieldObservation as UnknownFieldObservation,
    fetch_json as fetch_json,
    assert_api_contract as assert_api_contract,
    contract_failure as contract_failure,
    fail_contract as fail_contract,
)

__all__ = [
    "SNAPSHOT_DIR",
    "AUTO_EXPAND_CONTRACT",
    "UPDATE_SNAPSHOTS",
    "EXPANSION_REPORT_PATH",
    "UnknownFieldObservation",
    "fetch_json",
    "assert_api_contract",
    "contract_failure",
    "fail_contract",
]

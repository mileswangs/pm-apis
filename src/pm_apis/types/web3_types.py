"""Compatibility re-exports for :mod:`polymarket_apis.types.web3_types`."""

from __future__ import annotations

from polymarket_apis.types.web3_types import (
    TransactionLog as TransactionLog,
    TransactionReceipt as TransactionReceipt,
    DepositWalletCall as DepositWalletCall,
)

__all__ = [
    "TransactionLog",
    "TransactionReceipt",
    "DepositWalletCall",
]

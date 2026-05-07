"""Compatibility re-exports for :mod:`polymarket_apis.utilities.web3.helpers`."""

from __future__ import annotations

from polymarket_apis.utilities.web3.helpers import (
    get_market_index as get_market_index,
    get_index_set as get_index_set,
    detect_wallet_signature_type as detect_wallet_signature_type,
    INT_REGEX as INT_REGEX,
    BYTES_REGEX as BYTES_REGEX,
    AbiPackedParam as AbiPackedParam,
    abi_encode_packed as abi_encode_packed,
    split_signature as split_signature,
    create_safe_create_signature as create_safe_create_signature,
    ERC1967_CONST1 as ERC1967_CONST1,
    ERC1967_CONST2 as ERC1967_CONST2,
    ERC1967_PREFIX as ERC1967_PREFIX,
    get_create2_address as get_create2_address,
    init_code_hash_erc1967 as init_code_hash_erc1967,
    derive_deposit_wallet as derive_deposit_wallet,
    SafeTxn as SafeTxn,
    sign_safe_transaction as sign_safe_transaction,
    get_packed_signature as get_packed_signature,
    create_proxy_struct as create_proxy_struct,
    get_signature_type_from_runtime_code as get_signature_type_from_runtime_code,
)

__all__ = [
    "get_market_index",
    "get_index_set",
    "detect_wallet_signature_type",
    "INT_REGEX",
    "BYTES_REGEX",
    "AbiPackedParam",
    "abi_encode_packed",
    "split_signature",
    "create_safe_create_signature",
    "ERC1967_CONST1",
    "ERC1967_CONST2",
    "ERC1967_PREFIX",
    "get_create2_address",
    "init_code_hash_erc1967",
    "derive_deposit_wallet",
    "SafeTxn",
    "sign_safe_transaction",
    "get_packed_signature",
    "create_proxy_struct",
    "get_signature_type_from_runtime_code",
]

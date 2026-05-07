# Static typing facade for ``pm_apis.testing`` aggregate helpers.
#
# Runtime access is forwarded to ``polymarket_apis.testing``. These exports are
# the public contract-test helpers from that aggregate module.
from polymarket_apis.testing import (
    assert_api_contract as assert_api_contract,
    fail_contract as fail_contract,
    fetch_json as fetch_json,
)

# Keep ``__all__`` typed without duplicating the runtime export list.
__all__: list[str]

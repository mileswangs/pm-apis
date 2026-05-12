import asyncio
import logging
from collections.abc import Awaitable, Callable, Mapping
from typing import Any, Optional

import orjson
import websockets
from pydantic import ValidationError

from ..types.clob_types import ApiCreds
from ..types.websockets_types import (
    ActivityOrderMatchEvent,
    ActivityTradeEvent,
    AssetPriceSubscribeEvent,
    AssetPriceUpdateEvent,
    BestBidAskEvent,
    CommentEvent,
    CryptoPriceSubscribeEvent,
    CryptoPriceUpdateEvent,
    LastTradePriceEvent,
    LiveDataEvents,
    LiveDataLastTradePriceEvent,
    LiveDataOrderBookSummaryEvent,
    LiveDataOrderEvent,
    LiveDataPriceChangeEvent,
    LiveDataTickSizeChangeEvent,
    LiveDataTradeEvent,
    MarketEvents,
    MarketResolvedEvent,
    MarketStatusChangeEvent,
    NewMarketEvent,
    OrderBookSummaryEvent,
    OrderEvent,
    PriceChangeEvent,
    QuoteEvent,
    ReactionEvent,
    RequestEvent,
    SportsGameUpdate,
    TickSizeChangeEvent,
    TradeEvent,
    UserEvents,
)
from ..utilities.exceptions import AuthenticationRequiredError

logger = logging.getLogger(__name__)

RECONNECT_BACKOFF_INITIAL_SECONDS = 1
RECONNECT_BACKOFF_MAX_SECONDS = 8

MARKET_EVENT_CLASSES: Mapping[str, type[MarketEvents]] = {
    "book": OrderBookSummaryEvent,
    "price_change": PriceChangeEvent,
    "tick_size_change": TickSizeChangeEvent,
    "last_trade_price": LastTradePriceEvent,
    "best_bid_ask": BestBidAskEvent,
    "new_market": NewMarketEvent,
    "market_resolved": MarketResolvedEvent,
}

USER_EVENT_CLASSES: Mapping[str, type[UserEvents]] = {
    "order": OrderEvent,
    "trade": TradeEvent,
}

LIVE_DATA_EVENT_CLASSES: Mapping[str, type[LiveDataEvents]] = {
    "trades": ActivityTradeEvent,
    "orders_matched": ActivityOrderMatchEvent,
    "comment_created": CommentEvent,
    "comment_removed": CommentEvent,
    "reaction_created": ReactionEvent,
    "reaction_removed": ReactionEvent,
    "request_created": RequestEvent,
    "request_edited": RequestEvent,
    "request_canceled": RequestEvent,
    "request_expired": RequestEvent,
    "quote_created": QuoteEvent,
    "quote_edited": QuoteEvent,
    "quote_canceled": QuoteEvent,
    "quote_expired": QuoteEvent,
    "subscribe": AssetPriceSubscribeEvent,
    "update": AssetPriceUpdateEvent,
}


async def _on_market_message(message: str | bytes):
    try:
        payload = orjson.loads(message)
        if isinstance(payload, list):
            for item in payload:
                book_event = OrderBookSummaryEvent(**item)
                logger.info("%s", book_event)
            return

        match payload["event_type"]:
            case "book":
                book_event = OrderBookSummaryEvent(**payload)
                logger.info("%s", book_event)
            case "price_change":
                price_event = PriceChangeEvent(**payload)
                logger.info("%s", price_event)
            case "tick_size_change":
                tick_event = TickSizeChangeEvent(**payload)
                logger.info("%s", tick_event)
            case "last_trade_price":
                last_trade_event = LastTradePriceEvent(**payload)
                logger.info("%s", last_trade_event)
            case _:
                pass
    except orjson.JSONDecodeError:
        logger.warning("Market message JSON decode error, raw message: %s", message)
    except ValidationError as e:
        logger.error(
            "Market message validation error: %s | message=%s", e.errors(), message
        )


async def _on_user_message(message: str | bytes):
    try:
        payload = orjson.loads(message)
        match payload["event_type"]:
            case "order":
                logger.info("%s", OrderEvent(**payload))
            case "trade":
                logger.info("%s", TradeEvent(**payload))
    except orjson.JSONDecodeError:
        logger.warning("User message JSON decode error, raw message: %s", message)
    except ValidationError as e:
        logger.error(
            "User message validation error: %s | message=%s", e.errors(), message
        )


async def _on_live_data_message(message: str | bytes):
    try:
        payload = orjson.loads(message)
        match payload["type"]:
            case "trades":
                logger.info("%s", ActivityTradeEvent(**payload))
            case "orders_matched":
                logger.info("%s", ActivityOrderMatchEvent(**payload))
            case "comment_created" | "comment_removed":
                logger.info("%s", CommentEvent(**payload))
            case "reaction_created" | "reaction_removed":
                logger.info("%s", ReactionEvent(**payload))
            case (
                "request_created"
                | "request_edited"
                | "request_canceled"
                | "request_expired"
            ):
                logger.info("%s", RequestEvent(**payload))
            case "quote_created" | "quote_edited" | "quote_canceled" | "quote_expired":
                logger.info("%s", QuoteEvent(**payload))
            case "subscribe":
                logger.info("%s", CryptoPriceSubscribeEvent(**payload))
            case "update":
                logger.info("%s", CryptoPriceUpdateEvent(**payload))
            case "agg_orderbook":
                logger.info("%s", LiveDataOrderBookSummaryEvent(**payload))
            case "price_change":
                logger.info("%s", LiveDataPriceChangeEvent(**payload))
            case "last_trade_price":
                logger.info("%s", LiveDataLastTradePriceEvent(**payload))
            case "tick_size_change":
                logger.info("%s", LiveDataTickSizeChangeEvent(**payload))
            case "market_created" | "market_resolved":
                logger.info("%s", MarketStatusChangeEvent(**payload))
            case "order":
                logger.info("%s", LiveDataOrderEvent(**payload))
            case "trade":
                logger.info("%s", LiveDataTradeEvent(**payload))
            case _:
                logger.info("%s", payload)
    except orjson.JSONDecodeError:
        logger.warning("Live data message JSON decode error, raw message: %s", message)
    except ValidationError as e:
        logger.error(
            "Live data message validation error: %s | message=%s",
            e.errors(),
            message,
        )


async def _on_sports_message(message: str | bytes):
    try:
        payload = orjson.loads(message)
        logger.info("%s", SportsGameUpdate(**payload))
    except orjson.JSONDecodeError:
        logger.warning("Sports message JSON decode error, raw message: %s", message)
    except ValidationError as e:
        logger.error(
            "Sports message validation error: %s | message=%s", e.errors(), message
        )


class PolyWSSMarket:
    def __init__(
        self, token_ids: list[str], on_message: Callable[[str | bytes], Awaitable[None]]
    ):
        self.ws: websockets.ClientConnection | None = None
        self.on_message = on_message
        self.token_ids = token_ids

    async def update_subscribe(self, new_token_ids: list[str]):
        """更新订阅列表，自动处理新增和取消订阅
        Args:
            new_token_ids: 新的 token_ids 列表
        """
        old_token_ids = self.token_ids
        self.token_ids = new_token_ids.copy()
        if self.ws is None:
            return

        to_subscribe = [tid for tid in new_token_ids if tid not in old_token_ids]
        to_unsubscribe = [tid for tid in old_token_ids if tid not in new_token_ids]

        if to_unsubscribe:
            try:
                unsubscribe_message = {
                    "assets_ids": to_unsubscribe,
                    "operation": "unsubscribe",
                }
                await self.ws.send(orjson.dumps(unsubscribe_message))
                logger.info("[WS] 已取消订阅 %s 个 token", len(to_unsubscribe))
            except Exception as e:
                logger.error("[WS] 取消订阅 token 失败: %s", e)

        if to_subscribe:
            try:
                subscribe_message = {
                    "assets_ids": to_subscribe,
                    "operation": "subscribe",
                }
                await self.ws.send(orjson.dumps(subscribe_message))
                logger.info("[WS] 已订阅 %s 个新 token", len(to_subscribe))
            except Exception as e:
                logger.error("[WS] 订阅 token 失败: %s", e)

    async def _heartbeat_loop(self, ws: websockets.ClientConnection):
        while True:
            await asyncio.sleep(10)
            await ws.send("PING")
            logger.debug("[WS] 已发送 heartbeat ping")

    async def start(self):
        """启动 WebSocket 连接并自动重连"""
        url = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
        reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS
        while True:
            try:
                logger.info("[WS] 启动 WebSocket 连接...")
                async with websockets.connect(
                    url,
                    ping_interval=None,
                ) as ws:
                    self.ws = ws
                    heartbeat_task = asyncio.create_task(self._heartbeat_loop(ws))
                    try:
                        # 订阅 token
                        subscribe_message = {
                            "assets_ids": self.token_ids,
                        }
                        await ws.send(orjson.dumps(subscribe_message))
                        logger.info(
                            "[WS] 已连接并订阅 %s 个 token", len(self.token_ids)
                        )
                        reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS

                        # 接收事件
                        async for event in ws:
                            if event == "PONG":
                                logger.debug("[WS] 收到 heartbeat pong")
                                continue
                            await self.on_message(event)
                    finally:
                        heartbeat_task.cancel()
                        await asyncio.gather(heartbeat_task, return_exceptions=True)

            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                logger.error("[WS] WebSocket 连接异常: %s", e)
                self.ws = None
                logger.info("[WS] %s 秒后尝试重连", reconnect_delay)
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(
                    reconnect_delay * 2, RECONNECT_BACKOFF_MAX_SECONDS
                )


class PolymarketWebsocketsClient:
    def __init__(self) -> None:
        self.url_market = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
        self.url_user = "wss://ws-subscriptions-clob.polymarket.com/ws/user"
        self.url_live_data = "wss://ws-live-data.polymarket.com"
        self.url_sports = "wss://sports-api.polymarket.com/ws"

    async def user_socket(
        self,
        creds: ApiCreds,
        on_message: Callable[[str | bytes], Awaitable[None]] = _on_user_message,
    ):
        """
        Connect to the user websocket and subscribe to user events.

        Args:
            creds: API credentials for authentication
            on_message: Callback function to process raw websocket messages

        """
        reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS
        while True:
            try:
                logger.info("[User WS] 启动 WebSocket 连接...")
                async with websockets.connect(
                    self.url_user, ping_interval=20, ping_timeout=10
                ) as ws:
                    # 发送认证信息
                    auth_message = {"auth": creds.model_dump(by_alias=True)}
                    await ws.send(orjson.dumps(auth_message))
                    logger.info("[User WS] 已连接并发送认证")
                    reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS

                    # 接收事件
                    async for event in ws:
                        await on_message(event)

            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                logger.error("[User WS] WebSocket 连接异常: %s", e)
                logger.info("[User WS] %s 秒后尝试重连", reconnect_delay)
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(
                    reconnect_delay * 2, RECONNECT_BACKOFF_MAX_SECONDS
                )

    async def live_data_socket(
        self,
        subscriptions: list[dict[str, Any]],
        on_message: Callable[[str | bytes], Awaitable[None]] = _on_live_data_message,
        creds: Optional[ApiCreds] = None,
    ):
        # info on how to subscribe found at https://github.com/Polymarket/real-time-data-client?tab=readme-ov-file#subscribe
        """
        Connect to the live data websocket and subscribe to specified events.

        Args:
            subscriptions: List of subscription configurations
            on_message: Callback function to process raw websocket messages
            creds: ApiCreds for authentication if subscribing to clob_user topic

        """
        needs_auth = any(sub.get("topic") == "clob_user" for sub in subscriptions)

        if needs_auth and creds is None:
            msg = "ApiCreds credentials are required for the clob_user topic subscriptions"
            raise AuthenticationRequiredError(msg)

        reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS
        while True:
            try:
                logger.info("[Live Data WS] 启动 WebSocket 连接...")
                async with websockets.connect(
                    self.url_live_data, ping_interval=20, ping_timeout=10
                ) as ws:
                    # 准备订阅消息
                    subscriptions_to_send = subscriptions.copy()
                    if needs_auth:
                        subscriptions_to_send = []
                        for sub in subscriptions:
                            if sub.get("topic") == "clob_user":
                                sub_copy = sub.copy()
                                sub_copy["clob_auth"] = creds.model_dump()
                                subscriptions_to_send.append(sub_copy)
                            else:
                                subscriptions_to_send.append(sub)

                    payload = {
                        "action": "subscribe",
                        "subscriptions": subscriptions_to_send,
                    }

                    await ws.send(orjson.dumps(payload).decode())
                    logger.info(
                        "[Live Data WS] 已连接并订阅 %s 个主题",
                        len(subscriptions_to_send),
                    )
                    reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS

                    # 接收事件
                    async for event in ws:
                        await on_message(event)

            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                logger.error("[Live Data WS] WebSocket 连接异常: %s", e)
                logger.info("[Live Data WS] %s 秒后尝试重连", reconnect_delay)
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(
                    reconnect_delay * 2, RECONNECT_BACKOFF_MAX_SECONDS
                )

    async def sports_socket(
        self,
        on_message: Callable[[str | bytes], Awaitable[None]] = _on_sports_message,
    ):
        reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS
        while True:
            try:
                logger.info("[Sports WS] 启动 WebSocket 连接...")
                async with websockets.connect(
                    self.url_sports, ping_interval=20, ping_timeout=10
                ) as ws:
                    logger.info("[Sports WS] 已连接")
                    reconnect_delay = RECONNECT_BACKOFF_INITIAL_SECONDS

                    async for event in ws:
                        await on_message(event)

            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                logger.error("[Sports WS] WebSocket 连接异常: %s", e)
                logger.info("[Sports WS] %s 秒后尝试重连", reconnect_delay)
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(
                    reconnect_delay * 2, RECONNECT_BACKOFF_MAX_SECONDS
                )


PolyWSS = PolymarketWebsocketsClient

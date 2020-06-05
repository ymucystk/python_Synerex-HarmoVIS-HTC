# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: nodeapi/nodeapi.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import betterproto
import grpclib


class NodeType(betterproto.Enum):
    PROVIDER = 0
    SERVER = 1
    GATEWAY = 2


class KeepAliveCommand(betterproto.Enum):
    NONE = 0
    RECONNECT = 1
    SERVER_CHANGE = 2
    PROVIDER_DISCONNECT = 3


@dataclass
class NodeInfo(betterproto.Message):
    """information for synerex servers and providers, gateways (nodes)"""

    node_name: str = betterproto.string_field(1)
    node_type: "NodeType" = betterproto.enum_field(2)
    server_info: str = betterproto.string_field(3)
    node_pbase_version: str = betterproto.string_field(4)
    with_node_id: int = betterproto.int32_field(5)
    cluster_id: int = betterproto.int32_field(6)
    area_id: str = betterproto.string_field(7)
    channel_types: List[int] = betterproto.uint32_field(8)
    gw_info: str = betterproto.string_field(9)
    # for information for controller
    bin_version: str = betterproto.string_field(10)
    count: int = betterproto.int32_field(11)
    last_alive_time: datetime = betterproto.message_field(12)
    keepalive_arg: str = betterproto.string_field(13)


@dataclass
class NodeID(betterproto.Message):
    node_id: int = betterproto.int32_field(1)
    secret: float = betterproto.fixed64_field(2)
    server_info: str = betterproto.string_field(3)
    keepalive_duration: int = betterproto.int32_field(4)


@dataclass
class ServerStatus(betterproto.Message):
    cpu: float = betterproto.double_field(1)
    memory: float = betterproto.double_field(2)
    msg_count: int = betterproto.uint64_field(3)


@dataclass
class NodeUpdate(betterproto.Message):
    node_id: int = betterproto.int32_field(1)
    secret: float = betterproto.fixed64_field(2)
    update_count: int = betterproto.int32_field(3)
    node_status: int = betterproto.int32_field(4)
    node_arg: str = betterproto.string_field(5)
    status: "ServerStatus" = betterproto.message_field(6)


@dataclass
class Response(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    command: "KeepAliveCommand" = betterproto.enum_field(2)
    err: str = betterproto.string_field(3)


class NodeStub(betterproto.ServiceStub):
    async def register_node(
        self,
        *,
        node_name: str = "",
        node_type: "NodeType" = 0,
        server_info: str = "",
        node_pbase_version: str = "",
        with_node_id: int = 0,
        cluster_id: int = 0,
        area_id: str = "",
        channel_types: List[int] = [],
        gw_info: str = "",
        bin_version: str = "",
        count: int = 0,
        last_alive_time: Optional[datetime] = None,
        keepalive_arg: str = "",
    ) -> NodeID:
        request = NodeInfo()
        request.node_name = node_name
        request.node_type = node_type
        request.server_info = server_info
        request.node_pbase_version = node_pbase_version
        request.with_node_id = with_node_id
        request.cluster_id = cluster_id
        request.area_id = area_id
        request.channel_types = channel_types
        request.gw_info = gw_info
        request.bin_version = bin_version
        request.count = count
        if last_alive_time is not None:
            request.last_alive_time = last_alive_time
        request.keepalive_arg = keepalive_arg

        return await self._unary_unary("/nodeapi.Node/RegisterNode", request, NodeID,)

    async def query_node(
        self,
        *,
        node_id: int = 0,
        secret: float = 0,
        server_info: str = "",
        keepalive_duration: int = 0,
    ) -> NodeInfo:
        request = NodeID()
        request.node_id = node_id
        request.secret = secret
        request.server_info = server_info
        request.keepalive_duration = keepalive_duration

        return await self._unary_unary("/nodeapi.Node/QueryNode", request, NodeInfo,)

    async def keep_alive(
        self,
        *,
        node_id: int = 0,
        secret: float = 0,
        update_count: int = 0,
        node_status: int = 0,
        node_arg: str = "",
        status: Optional["ServerStatus"] = None,
    ) -> Response:
        request = NodeUpdate()
        request.node_id = node_id
        request.secret = secret
        request.update_count = update_count
        request.node_status = node_status
        request.node_arg = node_arg
        if status is not None:
            request.status = status

        return await self._unary_unary("/nodeapi.Node/KeepAlive", request, Response,)

    async def un_register_node(
        self,
        *,
        node_id: int = 0,
        secret: float = 0,
        server_info: str = "",
        keepalive_duration: int = 0,
    ) -> Response:
        request = NodeID()
        request.node_id = node_id
        request.secret = secret
        request.server_info = server_info
        request.keepalive_duration = keepalive_duration

        return await self._unary_unary(
            "/nodeapi.Node/UnRegisterNode", request, Response,
        )

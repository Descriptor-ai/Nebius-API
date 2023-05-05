from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
OPERATION_FIELD_NUMBER: _ClassVar[int]
operation: _descriptor.FieldDescriptor

class Operation(_message.Message):
    __slots__ = ["metadata", "response"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    response: str
    def __init__(self, metadata: _Optional[str] = ..., response: _Optional[str] = ...) -> None: ...

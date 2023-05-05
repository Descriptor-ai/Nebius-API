#!/bin/sh

OUT_DIR=generated
# DESCRIPTOR_SET_OUT=descriptor.temp

mkdir -p $OUT_DIR
python -m grpc_tools.protoc \
  --proto_path=cloudapi \
  --proto_path=cloudapi/third_party/googleapis \
  --pyi_out=$OUT_DIR \
  --python_out=$OUT_DIR \
  --grpc_python_out=$OUT_DIR \
  google/api/http.proto \
  google/api/annotations.proto \
  yandex/cloud/api/operation.proto \
  google/rpc/status.proto \
  yandex/cloud/operation/operation.proto \
  yandex/cloud/ai/stt/v3/stt_service.proto \
  yandex/cloud/ai/stt/v3/stt.proto

# touch $DESCRIPTOR_SET_OUT
# python -m grpc_tools.protoc \
#   --include_imports \
#   --descriptor_set_out=$DESCRIPTOR_SET_OUT \
#   --proto_path=cloudapi \
#   --proto_path=cloudapi/third_party/googleapis \
#   google/api/http.proto \
#   google/api/annotations.proto \
#   google/rpc/status.proto \
#   yandex/cloud/api/operation.proto \
#   yandex/cloud/operation/operation.proto \
#   yandex/cloud/ai/stt/v3/stt_service.proto \
#   yandex/cloud/ai/stt/v3/stt.proto

# protol \
#   --create-package \
#   --in-place \
#   --python-out=$OUT_DIR \
#   raw $DESCRIPTOR_SET_OUT

# rm $DESCRIPTOR_SET_OUT

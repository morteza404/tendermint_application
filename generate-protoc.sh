#!/bin/sh

for i in $(find -name \*.proto); do
    protoc -I=./proto-sources --python_out=./tendermint $i
done

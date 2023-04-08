# Protobuf Varint

This is a python implementation of Varint encoding and decoding in Protocol Buffers. Varint technically means a **variable integer length**, where the size of the data we will transfer can be calculated dynamically, instead of sending a fixed amount of bytes for any value. Assume you are sending data in JSON format, the number `45` will require two bytes to be transferred, but in Protocol Buffers, it can be transferred with one byte only, saving space and increasing transfer speed.

> Read more: https://protobuf.dev/programming-guides/encoding/#varints

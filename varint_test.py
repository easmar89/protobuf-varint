from varint import encode_varint, decode_varint

test_cases = (
    ("1.uint64", b'\x01'),
    ("150.uint64", b'\x96\x01'),
    ("maxint.uint64", b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01')
)

for file, expectation in test_cases:
    with open(file, "rb") as f:
        num = int.from_bytes(f.read(), byteorder="big")
        assert encode_varint(num) == expectation
        assert decode_varint(encode_varint(num)) == num
    

print("Tests passed")

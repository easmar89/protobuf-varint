def encode_varint(num):
    binary = []

    while num > 0: 
        least_significant_7_bits = num & 0x7f
        binary.append(least_significant_7_bits | 0x80)
        num >>= 7

    binary[-1] &= 0x7f

    return bytes(binary)

def decode_varint(binary):
    num = 0
    shift = 0

    for b in binary:
        b &= 0x7f
        b <<= shift
        num |= b 
        shift += 7
        
    return num

if __name__ == "__main__":
    with open("150.uint64", "rb") as f: 
        num = int.from_bytes(f.read(), byteorder="big")
        print(encode_varint(num))
        print(decode_varint(encode_varint(num)))
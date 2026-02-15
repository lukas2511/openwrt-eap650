#!/usr/bin/env python3

files = [
    ("default-mac", 0x6, 0x6),
    ("radio", 0x1000, 0x20000),
    ("radio1", 0x26800, 0x20000),
]

partsize = 0x100000

partdata = [0] * partsize
for filename, offset, size in files:
    partdata[offset:offset+size] = list(open(f"ubi_factory_data/{filename}", "rb").read())

art = open("art.bin", "wb")
art.write(bytes(partdata))

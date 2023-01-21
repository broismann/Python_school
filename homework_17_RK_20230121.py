byte_str = b'r\xc3\xa9sum\xc3\xa9'
print(byte_str)

normal = byte_str.decode()
print(normal)

latin = normal.encode("Latin1")
print(latin)

normal_2 = latin.decode("Latin1")
print(normal_2)

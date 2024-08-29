import sys
from struct import pack

print(sys.byteorder)

x = 0x01020304
print(x.to_bytes(4, byteorder='big'))
print(x.to_bytes(4, byteorder='little'))

print(int.from_bytes(b'\x04\x03\x02\x01', byteorder='big'))
print(int.from_bytes(b'\x04\x03\x02\x01', byteorder='little'))

#=================================
print('===========\nstruct.pack()===========')
print(pack('i', x))    # pakc(format, val), endian=native
print(pack('<i', x))    # pakc(format, val), endian=little
print(pack('>i', x))    # pakc(format, val), endian=big

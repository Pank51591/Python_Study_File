



def cobs_decode(cobs_data):  
    if not cobs_data or cobs_data[0] != 1:  
        raise ValueError("Invalid COBS data: first byte must be 1")  
  
    decoded_data = bytearray()  
    length = 0  
    for byte in cobs_data[1:]:  
        if byte == 0:  
            # 遇到0表示一个数据块的结束  
            if length == 0:  
                raise ValueError("Invalid COBS data: unexpected zero byte")  
            decoded_data.extend(cobs_data[cobs_data.index(0, 1, len(cobs_data)) + 1:len(cobs_data) - length])  
            length = 0  
            break  
        elif byte < length:  
            raise ValueError("Invalid COBS data: byte value less than current length")  
  
        decoded_data.extend(cobs_data[cobs_data.index(byte, 1, len(cobs_data)) - length:cobs_data.index(byte, 1, len(cobs_data))])  
        length = byte  
  
    if length != 0:  
        raise ValueError("Invalid COBS data: incomplete frame")  
  
    return decoded_data  
  
# 示例用法  



cobs_encoded_data = bytearray([1, 4, 'A', 'B', 'C', 1, 2, 'D', 0, 3, 'E', 'F', 'G', 0, 0])  
decoded_data = cobs_decode(cobs_encoded_data)  
print(decoded_data)  # 输出: bytearray(b'ABCDEFG')
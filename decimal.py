
"""
This file will contain all of the relevant calculations for dtb/btd.
"""

# True will be the "all good" code.
# Error code 1 will be for illegal characters (like letters or symbols).
# Error code 2 will be for an oversized octet (>255).
# Error code 3 will be for a byte address that is too long.
# Error code 4 will be for a too short decimal address.
# Error code 5 will be for a too long decimal address.

def sanityCheck(raw_ip):
    
    
    for digit in raw_ip:
        
        if digit != ".":
            try:
                int(digit)
            except TypeError:
                print("Illegal character(s) detected. Please check your input.")
                return 1
                 
        
        elif len(raw_ip) > 35:
            print("Address is too long. Please check your input.")
            return 3
        
        elif len(raw_ip) < 7 and len(raw_ip) < 35:
            print("Address is too short. Please check your input.")
            return 4
        
        
        else:
            continue
    
    return True


def formatDetection(sane_ip):

    
    if len(sane_ip) > 15 and len(sane_ip) < 35:
        return False
    elif len(sane_ip) <= 15:
        return 1 # 1 for decimal
    else:
        return 2

# def byteParser(byte_ip): # returns a 35 character long list.
#     
#     if len(byte_ip) == 35:
#         
#         byte_ip = byte_ip.strip(".")
#         
#     else:
#         continue
#     
#     f_ip_holder = []
#     
#     for bit in byte_ip:
#         f_ip_holder.append(bit)
#     
# 
#     return f_ip_holder
#     

    
def binaryConverter(byte): # Finished
    fByte = []
    byte = str(byte)
    if byte[0] == "1":
        fByte.append(128)
    elif byte[0] == "0":
        fByte.append(0)
          
    if byte[1] == "1":
        fByte.append(64)
    elif byte[1] == "0":
        fByte.append(0)  
            
    if byte[2] == "1":
        fByte.append(32)
    elif byte[2] == "0":
        fByte.append(0)
        
    if byte[3] == "1":
        fByte.append(16)
    elif byte[3] == "0":
        fByte.append(0)  
         
    if byte[4] == "1":
        fByte.append(8)
    elif byte[4] == "0":
        fByte.append(0)   
        
    if byte[5] == "1":
        fByte.append(4)
    elif byte[5] == "0":
        fByte.append(0)   
        
    if byte[6] == "1":
        fByte.append(2)
    elif byte[6] == "0":
        fByte.append(0)   
        
    if byte[7] == "1":
        fByte.append(1)
    elif byte[7] == "0":
        fByte.append(0)   
        
    octet = fByte[0] + fByte[1] + fByte[2] + fByte[3] + fByte[4] + fByte[5] + fByte[6] + fByte[7]
    
    return octet
    


def binaryToDecimal(byte_ip): # Finished
    
    if len(byte_ip) == 35:
        byte_ip = byte_ip.replace('.', "")

    
    
    
#     while len(octet1) < 8:
#         for bit in byte_ip:
#             octet1 = octet1.append(bit)
#     byte_ip = byte_ip[8:len(byte_ip)]
#     
#     
#     while len(octet2) < 8:
#         for bit in byte_ip:
#             octet2 = octet2.append(bit)
#     byte_ip = byte_ip[8:len(byte_ip)]
#     
#     while len(octet3) < 8:
#         for bit in byte_ip:
#             octet3 = octet3.append(bit)
#     byte_ip = byte_ip[8:len(byte_ip)]
#     
#     while len(octet4) < 8:
#         for bit in byte_ip:
#             octet4 = octet4.append(bit)
        
    octet_holder1 = byte_ip[:8]
    octet_holder2 = byte_ip[8:16]
    octet_holder3 = byte_ip[16:24]
    octet_holder4 = byte_ip[24:32]
    
    
    
    octet1 = str(binaryConverter(octet_holder1))
    octet2 = str(binaryConverter(octet_holder2))
    octet3 = str(binaryConverter(octet_holder3))
    octet4 = str(binaryConverter(octet_holder4))

    
    
    return octet1 + '.' + octet2 + '.' + octet3 + '.' + octet4

def decimalToBinary(octet):
    
    
    
    
    
    return
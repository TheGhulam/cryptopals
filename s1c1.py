import base64

def hexstring_to_b64(string):
    decoded_hexstring = bytes.fromhex(string)
    b64_encoded_string = base64.b64encode(decoded_hexstring)
    return b64_encoded_string.decode()

print(hexstring_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))

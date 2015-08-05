#!/usr/bin/python
import base64, binascii
#import binascii

#inASCII = binascii.a2b_hex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
inASCII = binascii.a2b_hex("1c0111001f010100061a024b53535009181c")
inB64 = base64.b64encode(inASCII)
print inB64


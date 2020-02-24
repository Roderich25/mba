# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


Rodrigo = Client()
print(Rodrigo.identity)  # Public Key

# 30819f300d06092a864886f70d010101050003818d0030818902818100b839b960b9bc8e158df356988b9681321c7d1f295ca1a745e8e70fffafc8141b9e078644dd39f406382ae5cd182238479d7492e0e395d55054b81390fd2cff5eed3c4ffb818c5201430bb4fed835aeead52e2b7d31029993f54276f16fca082b53c3956e1eb946afb56b09a418640449870144ba77d8216dc1a1abe2fe1037fd0203010001

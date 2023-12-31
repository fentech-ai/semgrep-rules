# cf. https://github.com/PyCQA/bandit/blob/b78c938c0bd03d201932570f5e054261e10c5750/examples/crypto-md5.py

import hashlib

# ruleid:insecure-hash-algorithm-md5
hashlib.md5(1)
# ruleid:insecure-hash-algorithm-md5
hashlib.md5(1).hexdigest()

# ruleid:insecure-hash-algorithm-md5
abc = str.replace(hashlib.md5("1"), "###")

# ruleid:insecure-hash-algorithm-md5


# ok:insecure-hash-algorithm-md5
hashlib.sha256(1)

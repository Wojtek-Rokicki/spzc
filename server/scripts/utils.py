import json
from Crypto.Cipher import AES
import hashlib
from base64 import b64encode, b64decode

def load_config(filename):
    with open(filename, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

def Rtag(string: str, session_key: str):
    config =load_config("config.json")
    if not config["Rtag"]:
        return string, None
    if not config["Append"]:
        res = json.loads(randomize(string, session_key))
        return res['ciphertext'], res # here random
    else:
        return string+session_key, None

def randomize(string: str, key: str):
    m = hashlib.sha256()
    m.update(key.encode())
    key = m.digest()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(string.encode())
    json_k = [ 'nonce',  'ciphertext', 'tag' ]
    json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, ciphertext, tag) ]
    result = json.dumps(dict(zip(json_k, json_v)))
    return result

def decrypt(load: dict, key: str):
    m = hashlib.sha256()
    m.update(key.encode())
    key = m.digest()
    json_k = ['nonce', 'ciphertext', 'tag']
    jv = {k:b64decode(load[k]) for k in json_k}
    cipher = AES.new(key, AES.MODE_EAX, nonce=jv['nonce'])
    #print(cipher.decrypt_and_verify(jv['ciphertext'], jv['tag']))
    return cipher.decrypt(jv["ciphertext"])

tmp = randomize("Admin", "key")
print(tmp)
print(decrypt(json.loads(tmp), "key"))
key = "key"
m = hashlib.sha256()
m.update(key.encode())
key = m.digest()
cipher = AES.new(key, AES.MODE_EAX)
print(cipher.nonce)
print(cipher.nonce)
print(cipher.nonce)

#print(decrypt({'nonce': 'q0KhabqiG1fJvgbY5SZfuQ==', 'ciphertext': 'yLA4eOSey2w=', 'tag': 'Fg2gMf28vn4FzponcnwQGg=='}, 
#"72dv35604gsfmo2v2vyfk75d5seskngt"))


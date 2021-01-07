# import hmac
# from hashlib import sha1

# '''
#    HMACSHA1算法加密
#    key: 密钥;
#    code: 待加密参数
# '''
# def georgeMac (key, code):
#   hMac_code = hmac.new(key.encode(), code.encode(), sha1)
#   return hMac_code.hexdigest()

def sayHi ():
  print('Hello World !')

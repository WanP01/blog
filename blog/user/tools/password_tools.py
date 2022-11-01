import hashlib

#对用户密码加密
def pw_md5(password):
    mima = hashlib.md5()
    mima.update(password.encode())
    return mima.hexdigest()
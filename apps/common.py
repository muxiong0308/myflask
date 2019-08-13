import random
from hashlib import sha1


class Common:
    def trueReturn(self, data, msg="请求成功"):
        return {"status": 1, "data": data, "msg": msg}

    def falseReturn(self, data, msg="请求失败"):
        return {"status": 0, "data": data, "msg": msg}

    # 生成加密盐
    @staticmethod
    def genSalt(saltLen):
        base = 'abcdefghijklmnopqrstuvwxyz0123456789'
        strRes = ''
        for i in range(saltLen):
            temp = random.randint(0, len(base))
            strRes += base[temp:temp + 1]
        return strRes

    # sha1加密
    @staticmethod
    def encryptedPsw(psw, salt):
        encSha = sha1()
        encSha.update((psw + salt).encode())
        return encSha.hexdigest()


if __name__ == '__main__':
    pass
    # print(Common.genSalt(10))
    print(Common.encryptedPsw('123', '234'))

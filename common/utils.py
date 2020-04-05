from passlib.hash import pbkdf2_sha512
class Utils:
    @staticmethod
    def valid_email(e):
        return True

    @staticmethod
    def encry(a):
        return pbkdf2_sha512.encrypt(a)
    
    @staticmethod
    def check(p,h):
        return pbkdf2_sha512.verify(p,h)

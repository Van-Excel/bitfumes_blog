from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class Hash:
    @staticmethod
    def encryptPassword(password:str):
        encrypted_password = pwd_context.hash(password)
        return encrypted_password
    
    
    



 
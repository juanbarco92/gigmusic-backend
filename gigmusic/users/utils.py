from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

# ----- Hashed passwords

def verify_password(original_password, hashed_password):
    return pwd_context.verify(original_password, hashed_password)


def password_hash(password):
    return pwd_context.hash(password)
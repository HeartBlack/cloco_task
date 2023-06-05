from config import Config

def get_db():
    db =Config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return Config.pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return Config.pwd_context.verify(plain_password, hashed_password)
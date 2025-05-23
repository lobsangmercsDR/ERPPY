from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.core.config import settings


def create_access_token(data: dict, expires_delta: timedelta = None):  # type: ignore
    to_encode = data.copy()
    expire = datetime.utcnow() + \
        (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

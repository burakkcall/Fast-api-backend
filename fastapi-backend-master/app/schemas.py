from pydantic import BaseModel, EmailStr

# Kullanıcı Giriş Şeması
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Token Dönüş Şeması
class Token(BaseModel):
    access_token: str
    token_type: str

# Token İçerik Şeması
class TokenData(BaseModel):
    id: str | None = None
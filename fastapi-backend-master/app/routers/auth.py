from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app import oauth2

router = APIRouter(tags=['Authentication'])

# Geçici sabit kullanıcı
MOCK_USER = {
    "username": "admin@example.com",
    "password": "123"
}

@router.post("/login")
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    # 1. Kullanıcı adı ve Şifre kontrolü
    if user_credentials.username != MOCK_USER["username"] or user_credentials.password != MOCK_USER["password"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Geçersiz kullanıcı adı veya şifre"
        )
        
    # 2. JWT Token üret
    access_token = oauth2.create_access_token(data={"user_id": MOCK_USER["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
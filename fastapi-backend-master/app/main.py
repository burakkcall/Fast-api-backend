from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth
from . import oauth2

app = FastAPI(
    title="JWT Authentication API",
    description="Sadece JWT token üretimi, doğrulaması ve güvenliği sağlayan API",
    version="1.0.0"
)

# CORS Ayarları (Frontend bağlantıları için)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sadece Auth (Login / Token üretimi) Router'ı dahil ediyoruz
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "JWT Authentication API Servisi Çalışıyor!"}


# 🔒 KORUMALI ROTA ÖRNEĞİ
# Bu adrese istek atarken Header kısmında 'Authorization: Bearer <TOKEN>' göndermek zorunludur.
@app.get("/protected")
async def protected_route(current_user: str = Depends(oauth2.get_current_user)):
    return {
        "message": "Tebrikler! Geçerli bir JWT Token ile korumalı alana eriştiniz.",
        "active_user": current_user
    }
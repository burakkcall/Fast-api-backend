
# 🔐 FastAPI JWT Authentication Demo

Bu proje, **FastAPI** ve **JSON Web Token (JWT)** kullanarak geliştirilmiş hafif siklet bir kimlik doğrulama (Authentication) ve yetkilendirme (Authorization) servisidir. 

Proje, veritabanı karmaşasından uzak, uçtan uca Token üretimi, saklanması ve korumalı rotalara (Protected Routes) erişim mantığını pratik bir şekilde göstermek amacıyla hazırlanmıştır. Ayrıca backend servislerini test etmek için saf HTML/JS ile hazırlanmış basit bir kullanıcı arayüzü (Frontend) içerir.

---

## 🚀 Öne Çıkan Özellikler

* **JWT Tabanlı Kimlik Doğrulama:** Python `jose` kütüphanesi ile Token üretimi ve doğrulaması.
* **OAuth2 Password Flow:** FastAPI'nin yerleşik `OAuth2PasswordBearer` yapısı ile uyumlu giriş mekanizması.
* **Arayüz (Frontend Test Interface):** Herhangi bir framework gerektirmeyen, tarayıcı üzerinden Token almayı ve yetkili istekler atmayı sağlayan `index.html`.
* **CORS Yapılandırması:** İstemci ve sunucu arasındaki erişim engellerini çözen esnek CORS ayarları.

---

## 🛠️ Teknolojiler

* **Backend:** Python 3.12+, FastAPI, Uvicorn, Pydantic, python-jose
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)

---

## 💻 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/KULLANICI_ADIN/REPO_ADIN.git](https://github.com/KULLANICI_ADIN/REPO_ADIN.git)
cd REPO_ADIN

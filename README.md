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

```

### 2. Sanal Ortamı Oluşturun ve Aktif Edin

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt

```

### 4. Sunucuyu Başlatın

```bash
uvicorn app.main:app --reload

```

Sunucu çalıştıktan sonra API **`http://127.0.0.1:8000`** adresinde yayında olacaktır.

---

## 🧪 Test Etme (Arayüz & Swagger)

### 1. Web Arayüzü İle Test (`index.html`)

Proje dizininde yer alan `index.html` dosyasını tarayıcınızda açarak canlı test gerçekleştirebilirsiniz:

* **Geçerli Kullanıcı Adı:** `admin@example.com`
* **Geçerli Şifre:** `123456`

1. Bilgileri girip **Giriş Yap** butonuna basın. Alınan JWT Token tarayıcının `localStorage` alanına kaydedilecektir.
2. **Kimlik Doğrula ve Veri Çek** butonuna basarak kaydedilen Token ile korumalı rotaya erişim sağlayın.

### 2. Swagger UI

FastAPI'nin otomatik oluşturduğu dokümantasyon üzerinden test etmek için:
👉 `http://127.0.0.1:8000/docs` adresini ziyaret edin.

---

## 📁 Proje Yapısı

```text
fastapi-backend-master/
│
├── app/
│   ├── routers/
│   │   └── auth.py       # Login ve kimlik doğrulama rotaları
│   ├── config.py         # JWT ve uygulama konfigürasyonu
│   ├── main.py           # FastAPI uygulama başlangıcı ve CORS ayarları
│   ├── oauth2.py         # Token oluşturma ve doğrulama mantığı
│   ├── schemas.py        # Pydantic veri modelleri
│   └── utils.py          # Yardımcı fonksiyonlar (şifreleme vb.)
│
├── index.html            # Test amaçlı basit frontend arayüzü
├── requirements.txt      # Proje bağımlılıkları
└── README.md             # Proje dokümantasyonu

```

```

```

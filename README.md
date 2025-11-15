## TALOS

**Data Analysis — 3 Veri Seti İncelemesi**

## Kısa Açıklama

Bu repo, `Data_Analysis.ipynb` adlı Jupyter Notebook içinde yapılmış **3 ayrı veri seti analizi** içerir. Analizlerde kullanılan başlıca kütüphaneler: `numpy`, `pandas`, `matplotlib`, `seaborn`.

Analizler:
 
* E-ticaret satış verisi (Kaggle)
* IMDB film verisi (Kaggle)
* Munich havadurumu verisi

**Amaç:** Veri temizleme, temel keşifsel veri analizi (EDA), görselleştirme ve temel çıkarımlar üretmek.

---

## Datasetler (kaynaklar)

1. E‑commerce Sales Dataset (Kaggle)

   * [https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data](https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data)

2. Munich Weather Dataset (Drivefile)

   * [https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link](https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link)

3. IMDB Movies Analysis (Kaggle)

   * [https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis](https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis)

> Not: Kaggle verilerini kullanırken lisans/kullanım koşullarını kontrol edin. Drive linki özel ise repo içine doğrudan yüklememeyi tercih edin; kullanım talimatı veya küçük örnek veri ekleyin.

---

## Repo Yapısı

```
TALOS/
├── README.md
├── requirements.txt
├── .gitignore
├── Projects/
│   └── 1_Hafta
|       └── Data_Analysis.ipynb
├── Dataset/
│   ├── ecommerce_sample.csv
│   └── imdb_sample.csv
|   └──       
├── Graphs/                    # Veri görselleştirmeleri
└── LICENSE
```

---

## Kurulum ve Çalıştırma

1. Python 3.9+ önerilir.
2. Sanal ortam oluşturun (opsiyonel ama tavsiye edilir):

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

4. Notebook'u başlatın:

```bash
jupyter notebook notebooks/Data_Analysis.ipynb
# veya
jupyter lab
```

---

## requirements.txt (önerilen içerik)

```
numpy>=1.24
pandas>=2.0
matplotlib>=3.6
seaborn>=0.13
jupyterlab>=4.0
notebook>=6.5
scipy>=1.10
openpyxl>=3.1    # eğer excel okunuyorsa
xlrd>=2.0        # eski excel formatları için

# ekleyebileceğinizler (opsiyonel)
scikit-learn>=1.2
statsmodels>=0.14
plotly>=5.10
```

> Not: Sürüm numaralarını projenizde test ettiğiniz en düşük uyumlu sürümlere göre ayarlayabilirsiniz.

---

## .gitignore (önerilen)

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
ENV/
env/

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db

# Data
data/
*.csv
*.xlsx

# logs
*.log
```

> Eğer `data/` klasörüne küçük örnek veriler eklemek isterseniz, `.gitignore` içinde `!data/*.csv` şeklinde istisna koyabilirsiniz.

---

## README.md için kısa bir örnek (hazır içerik)

Aşağıdaki metni doğrudan `README.md` olarak kullanabilirsiniz:

```
# Data Analysis — 3 Dataset EDA

Bu repo `Data_Analysis.ipynb` ile yapılmış üç veri seti analizini içerir.

## Veri setleri
- E-commerce Sales: https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data
- IMDB Movies: https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis
- Ek veri (Drive link): https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link

## Kurulum
1. Sanal ortam oluşturun
2. `pip install -r requirements.txt`
3. `jupyter notebook notebooks/Data_Analysis.ipynb`

## İçerik
- Veri temizleme ve eksik değer analizi
- Temel istatistikler
- Görselleştirmeler (matplotlib & seaborn)
- Kısa yorumlar ve bulgular
```

---

## Ek öneriler

* Notebook içinde büyük veri kullanıyorsanız sadece örnek bir kesit (`sample`) ekleyin ve asıl veri için kullanım talimatı verin.
* Görselleştirmeleri `images/` içine kaydedin ve README'de örnek görseller gösterin.
* `LICENSE` (MIT) ekleyin.
* GitHub Actions ile basit bir `nbconvert` testi ekleyebilirsiniz: notebook'un en temel hücrelerinin çalışıp çalışmadığını doğrulamak için.

---

## Yardımcı olacak ek içerik (isteğe bağlı)

* `CONTRIBUTING.md` (katkı yönergeleri)
* `CHANGELOG.md` (sürüm değişiklikleri)

---

Eğer istersen, bu dosyaları (README.md, requirements.txt, .gitignore) doğrudan senin için oluşturup repo'ya hazır hâle getirebilirim. Ayrıca `README.md` içindeki metni Türkçe/İngilizce tercihine göre uyarlayabilirim.

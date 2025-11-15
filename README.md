# Data Analysis Project

---

## Proje Başlığı

**Data Analysis — 3 Veri Seti İncelemesi**

## Kısa Açıklama

Bu repo, `Data_Analysis.ipynb` adlı Jupyter Notebook içinde yapılmış **3 ayrı veri seti analizi** içerir. Analizlerde kullanılan başlıca kütüphaneler: `numpy`, `pandas`, `matplotlib`, `seaborn`.

Analizler:

* E-ticaret satış verisi (Kaggle).
* IMDB film verisi (Kaggle).
* Google Drive linkiyle paylaşılan ek veri (paylaşılan dosya).

**Amaç:** Veri temizleme, temel keşifsel veri analizi (EDA), görselleştirme ve temel çıkarımlar üretmek.

---

## Datasetler (kaynaklar)

1. E‑commerce Sales Dataset (Kaggle)

   * [https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data](https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data)

2. Drive paylaşımı (örnek/ek veri)

   * [https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link](https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link)

3. IMDB Movies Analysis (Kaggle)

   * [https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis](https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis)

> Not: Kaggle verilerini kullanırken lisans/kullanım koşullarını kontrol edin. Drive linki özel ise repo içine doğrudan yüklememeyi tercih edin; kullanım talimatı veya küçük örnek veri ekleyin.

---

## Repo Yapısı (önerilen)

```
my-data-analysis-project/
├── README.md
├── requirements.txt
├── .gitignore
├── Projects/
│   └── Data_Analysis.ipynb
├── images/                    # notebook içindeki görseller
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


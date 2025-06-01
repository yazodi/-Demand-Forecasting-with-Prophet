---
title: Demand Forecasting with Prophet
emoji: 📈
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.32.2"
app_file: app.py
pinned: false
---

# 📦 Store Item Demand Forecasting App (Prophet ile)

Bu uygulama, [Kaggle - Demand Forecasting Challenge](https://www.kaggle.com/competitions/demand-forecasting-kernels-only) veri seti kullanılarak Prophet modeli ile zaman serisi satış tahmini yapmak için geliştirilmiştir. Prophet modeli, tarihsel satış verilerinden trend, haftalık ve yıllık mevsimsellik bileşenlerini öğrenerek 90 gün ileriye yönelik tahminler üretir.

---

## 🎯 Özellikler

- Facebook Prophet ile zaman serisi modelleme  
- Kullanıcı seçimi ile mağaza ve ürün bazlı tahmin  
- 90 günlük ileriye dönük satış tahmini  
- Trend, haftalık ve yıllık mevsimsellik bileşen analizi  
- Etkileşimli grafiklerle görselleştirme

---

## 🧠 Model Detayları

- **Model:** Prophet (additive time series model)
- **Girdi:** Tarih (`date`) ve satış miktarı (`sales`)
- **Tahmin:** 90 günlük ileriye dönük `sales` değeri
- **Mevsimsellik:** Haftalık ve yıllık otomatik olarak öğrenilir

---

## 📂 Dosya Yapısı
demand_forecast_app/
├── app.py → Streamlit uygulaması
├── train.csv → Kaggle'dan alınan eğitim verisi
├── requirements.txt → Gerekli Python paketleri
└── README.md → Bu dosya

---

📌 Veri Kaynağı
Veri seti Kaggle'dan alınmıştır:
👉 Store Item Demand Forecasting Challenge

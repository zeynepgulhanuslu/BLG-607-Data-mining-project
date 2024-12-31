# E-posta Oltalama Tespiti Projesi

Bu proje, makine öğrenmesi ve derin öğrenme yöntemlerini kullanarak e-postaların oltalama (phishing) içerip içermediğini tespit eden bir sistemdir.


## 📊 Test Verisi Sonuçları

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|---------|-----------|
| SVM | %98.37 | %97.96 | **%97.66** | %97.81 |
| SVM-CV | **%98.44** | **%98.36** | %97.46 | **%97.90** |
| Logistic Regression | %96.05 | %93.73 | %95.83 | %94.77 |
| MLP | %97.64 | %96.75 | %96.95 | %96.85 |
| DNN | %97.91 | %96.77 | **%97.66** | %97.22 |


## 📊 Gerçek Test Verisi Sonuçları

| Model | Accuracy |
|-------|----------|
| SVM | **%86.36**| 
| SVM-CV | **%86.36** | 
| Logistic Regression | %77.27 |
| MLP | %72.73 |
| DNN | %72.73 |

## 🛠 Kurulum

1. Projeyi klonlayın: 
bash
git clone https://github.com/kullaniciadi/phishing-mail-detection.git
cd phishing-mail-detection

2. Gerekli paketleri yükleyin:
bash
pip install -r requirements.txt

3. Projeyi çalıştırın:
bash
python src/phishing_mail_detection_app.py


## 📁 Proje Yapısı
phishing-mail-detection/
├── src/
│ ├── source/
│ │ └── models/ # Eğitilmiş modeller
│ ├── notebooks/ # Jupyter notebooks
│ └── phishing_mail_detection_app.py
├── requirements.txt
└── README.md


## 🔧 Kullanılan Teknolojiler

- Python 3.8+
- TensorFlow
- Scikit-learn
- Streamlit
- Joblib
- NumPy
- Pandas

## 💡 Kullanım

1. Web arayüzünden bir model seçin
2. E-posta metnini girin veya örnek e-postalardan birini seçin
3. "Tahmin Et" butonuna tıklayın
4. Sonucu görüntüleyin

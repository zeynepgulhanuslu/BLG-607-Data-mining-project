import streamlit as st
import joblib
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import unicodedata
import re

def load_model_and_vectorizer(model_path, vectorizer_path):
    try:
        if model_path.endswith('.h5'):
            model = load_model(model_path)
        else:
            model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        return model, vectorizer
    except Exception as e:
        st.error(f"Model yüklenirken hata: {e}")
        return None, None

def make_prediction(model, vectorizer, text):
  
    vector = vectorizer.transform([text])
    
    if isinstance(model, tf.keras.Model):
        vector = vector.toarray()
        prediction = model.predict(vector)
        prediction = (prediction > 0.5).astype(int)
    else:
        prediction = model.predict(vector)
    
    return prediction[0]

def main():
    st.title("E-posta Oltalama Tespiti")
    # Örnek e-postalar
    sample_emails = {
        "Oltalama Örneği 1": """Dear valued customer,
        Your account security is at risk! Please click the link below to verify your account immediately:
        http://secure-banking-verify.com
        If you don't verify within 24 hours, your account will be suspended.
        Best regards,
        Security Team""",
        
        "Oltalama Örneği 2": """CONGRATULATIONS! You've won $1,000,000 in our random draw!
        To claim your prize, please send us your bank details and a processing fee of $100.
        Reply immediately to claim your prize!""",
        
        "Oltalama Örneği 3": """Dear Valued Customer,

        Our records indicate that you have an outstanding invoice that has not been paid. Please settle this invoice as soon as possible to avoid penalties.

        Invoice Number: 456123 Amount Due: $450.00

        Please make the payment via this link as soon as possible: Make Payment

        Thank you, Accounts Department""",
                
        "Güvenli E-posta 1": """Hi John,
        Just following up on our meeting from yesterday. I've attached the presentation slides as discussed.
        Please let me know if you need any clarification.
        Best regards,
        Sarah""",
        
        "Güvenli E-posta 2": """Monthly Newsletter
        Thank you for subscribing to our newsletter. Here are this month's highlights:
        - New product launches
        - Company updates
        - Upcoming events
        Best regards,
        Marketing Team""",
        
        "Güvenli E-posta 3": """
        Dear Sarah,

        Welcome to the Customer Support team at Widget Corp! We are thrilled to have you on board and look forward to seeing the contributions you will make.

        Your first week will be primarily orientation, and you'll be working closely with Janet Smith, your mentor. Janet will help you settle in and get to know our processes.

        See you on Monday at 9:00 AM for your official start!

        Warm regards, David"""
    }
    
    base_dir = os.path.join(os.getcwd(), "src","source", "models")
    # Model yolları
    model_paths = {
        "SVM (Filtered)": {
            "model": os.path.join(base_dir, "svm/filtered/filtered_data_svm.joblib"),
            "vectorizer": os.path.join(base_dir, "svm/filtered/filtered_data_tfidf.joblib"),
        },
        "SVM-CV (Filtered)": {
            "model": os.path.join(base_dir, "svm-cv/filtered-cv5/filtered_data_svm.joblib"),
            "vectorizer": os.path.join(base_dir, "svm-cv/filtered-cv5/filtered_data_tfidf.joblib"),

        },
        "MLP (Filtered)": {
            "model": os.path.join(base_dir, "mlp/filtered_mlp.joblib"),
            "vectorizer": os.path.join(base_dir, "mlp/filtered_tfidf.joblib"),

        },
        "Logistic Regression (Filtered)": {
            "model": os.path.join(base_dir, "logistic_regression/filtered_logistic.joblib"),
            "vectorizer": os.path.join(base_dir, "logistic_regression/filtered_tfidf.joblib"),

        },
        "DNN (Filtered)": {
            "model": os.path.join(base_dir, "dnn/filtered_dnn.h5"),
            "vectorizer": os.path.join(base_dir, "dnn/filtered_tfidf.joblib"),
        }
    }
    
    # Model seçimi
    selected_model = st.selectbox(
        "Model Seçin",
        list(model_paths.keys())
    )
    
    # E-posta giriş metodu seçimi
    input_method = st.radio(
        "E-posta giriş yöntemi seçin:",
        ["Örnek E-postalar", "Manuel Giriş"]
    )
    
    if input_method == "Örnek E-postalar":
        selected_sample = st.selectbox(
            "Örnek e-posta seçin:",
            list(sample_emails.keys())
        )
        email_text = sample_emails[selected_sample]
        # Seçilen örneği metin alanında göster
        st.text_area("E-posta metni:", value=email_text, height=200, key="sample_email")
    else:
        email_text = st.text_area("E-posta metnini girin:", height=200, key="manual_email")
        
    if st.button("Tahmin Et"):
        if email_text:
            with st.spinner('Tahmin yapılıyor...'):
                model_info = model_paths[selected_model]
                model, vectorizer = load_model_and_vectorizer(
                    model_info["model"],
                    model_info["vectorizer"]
                )
                
                if model and vectorizer:
                    prediction = make_prediction(
                        model,
                        vectorizer,
                        email_text
                    )
                    
                    # Sonucu göster
                    if prediction == 1:
                        st.error("⚠️ Bu e-posta OLTALAMA olarak tespit edildi!")
                    else:
                        st.success("✅ Bu e-posta GÜVENLİ olarak tespit edildi.")
                    
                    
        else:
            st.warning("Lütfen bir e-posta metni girin.")

if __name__ == "__main__":
    main()
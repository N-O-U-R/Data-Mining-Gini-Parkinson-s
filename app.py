import streamlit as st
from file import make_prediction

# Streamlit user interface
st.title("Parkinson's Disease Prediction")

# Create input fields for each feature (except 'name' and 'status')
input_data = {}
feature_mapping = {
    'MDVP:Fo(Hz)': 'MDVP Fo(Hz) (Ortalama vokal temel frekansı)',
    'MDVP:Fhi(Hz)': 'MDVP Fhi(Hz) (Maksimum vokal temel frekansı)',
    'MDVP:Flo(Hz)': 'MDVP Flo(Hz) (Minimum vokal temel frekansı)',
    'MDVP:Jitter(%)': 'MDVP Jitter(%) (Ses titreşimlerindeki yüzdesel değişiklik)',
    'MDVP:Jitter(Abs)': 'MDVP Jitter(Abs) (Saniye cinsinden ardışık periyotlar arası fark)',
    'MDVP:RAP': 'MDVP RAP (Relative Average Perturbation - Ortalama ve komşu periyotlar arası ortalama mutlak fark)',
    'MDVP:PPQ': 'MDVP PPQ (Beş noktalı Periyot Pertürbasyon Katsayısı)',
    'Jitter:DDP': 'Jitter DDP (Ardışık periyotlar arası farkların ortalama mutlak değeri)',
    'MDVP:Shimmer': 'MDVP Shimmer (Genlikteki dalgalanmaların ölçümü)',
    'MDVP:Shimmer(dB)': 'MDVP Shimmer(dB) (Desibel cinsinden genlik dalgalanmaları)',
    'Shimmer:APQ3': 'Shimmer APQ3 (Üç periyot üzerinden genlik değişikliklerinin ölçümü)',
    'Shimmer:APQ5': 'Shimmer APQ5 (Beş periyot üzerinden genlik değişikliklerinin ölçümü)',
    'MDVP:APQ': 'MDVP APQ (Genlikteki değişikliklerin genel ölçümü)',
    'Shimmer:DDA': 'Shimmer DDA (Ardışık farkların ortalama mutlak değeri)',
    'NHR': 'NHR (Gürültü ile Armonik Oranı)',
    'HNR': 'HNR (Armonik ile Gürültü Oranı)',
    'RPDE': 'RPDE (Doğrusal Olmayan Dinamik Karmaşıklık Ölçümü)',
    'DFA': 'DFA (Sinyal Fraktal Ölçeklendirme Üssü)',
    'spread1': 'spread1 (Temel frekansta doğrusal olmayan değişim ölçümü 1)',
    'spread2': 'spread2 (Temel frekansta doğrusal olmayan değişim ölçümü 2)',
    'D2': 'D2 (Ses Sinyalinin Doğrusal Olmayan Dinamik Özelliği)',
    'PPE': 'PPE (Sesin Periyodikliğindeki Değişimlerin Ölçümü)'
}

# Using two columns for input
for feature_name, display_name in feature_mapping.items():
    if feature_name == 'spread1':
        input_value = st.number_input(f'{display_name}', min_value=-10.00, format='%f')
        if input_value >= 0:
            st.warning(f"Please enter a value less than 0 for '{display_name}'.")
        input_data[feature_name] = input_value
    else:
        input_data[feature_name] = st.number_input(f'{display_name}', min_value=0.0, format='%f')

# Button to make prediction
if st.button('Predict'):
    prediction = make_prediction(input_data)
    if prediction == 1:
        st.markdown("### **Parkinson's!!!**", unsafe_allow_html=True)
        st.error("The model predicts the presence of Parkinson's disease.")
    else:
        st.markdown("### **Healthy!!!**", unsafe_allow_html=True)
        st.success("The model predicts no presence of Parkinson's disease.")
import streamlit as st
from file import make_prediction

# Streamlit user interface
st.title("Parkinson's Disease Prediction")

# Create input fields for each feature (except 'name' and 'status')
input_data = {}
feature_mapping = {
    'MDVP:Fo(Hz)': 'MDVP Fo (Hz)',
    'MDVP:Fhi(Hz)': 'MDVP Fhi (Hz)',
    'MDVP:Flo(Hz)': 'MDVP Flo (Hz)',
    'MDVP:Jitter(%)': 'MDVP Jitter (%)',
    'MDVP:Jitter(Abs)': 'MDVP Jitter (Abs)',
    'MDVP:RAP': 'MDVP RAP',
    'MDVP:PPQ': 'MDVP PPQ',
    'Jitter:DDP': 'Jitter DDP',
    'MDVP:Shimmer': 'MDVP Shimmer',
    'MDVP:Shimmer(dB)': 'MDVP Shimmer (dB)',
    'Shimmer:APQ3': 'Shimmer APQ3',
    'Shimmer:APQ5': 'Shimmer APQ5',
    'MDVP:APQ': 'MDVP APQ',
    'Shimmer:DDA': 'Shimmer DDA',
    'NHR': 'NHR',
    'HNR': 'HNR',
    'RPDE': 'RPDE',
    'DFA': 'DFA',
    'spread1': 'spread1',
    'spread2': 'spread2',
    'D2': 'D2',
    'PPE': 'PPE'
}

# Using two columns for input
for index, (feature_name, display_name) in enumerate(feature_mapping.items()):
    if index % 2 == 0:  # This will create a new row for every two inputs
        col1, col2 = st.columns(2)

    with (col1 if index % 2 == 0 else col2):
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
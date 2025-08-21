import pandas as pd
import streamlit as st
import pickle
import numpy as np


with open('Model Deploy/Xgb_model.pkl', 'rb') as f: 
    model = pickle.load(f)

st.title('Laptop Price Prediction App')
data = pd.read_csv('Data/Clean_data.csv')
# Creat the Input field
col1, col2, col3 = st.columns(3)


with col1 :
    inches  = st.slider('Inches', 10.0, 20.0, 15.0, step = 0.1)
    ram = st.slider('Ram', 2, 32, 12, step = 2)
    weight = st.slider('Weight', 650, 5000, 2000)
    screen_weight = st.slider('ScreenW', 1300, 4000, 2500 )
    screen_height = st.slider('ScreenH', 750, 2200, 1500)
    cpu_freq = st.slider('CPU_freq', 0.5, 5.0, 0.5)
    primary_storage = st.slider('PrimaryStorage',8, 1000, 256, step = 8)
    secondary_storage = st.slider('SecondaryStorage', 0 , 512, 256, step= 8)
    weight_per_inch = weight / inches

with col2:
    company = st.selectbox('Company', data['Company'].unique())
    product = st.selectbox('Product', data['Product'].unique())
    type_name = st.selectbox('TypeName', data['TypeName'].unique())
    os = st.selectbox('OS', data['OS'].unique())
    screen = st.selectbox('Screen', data['Screen'].unique())
    toch_screen = st.radio('Touchscreen', ['No', 'Yes'])
    ips_pannel = st.radio('IPSpanel', ['No', 'Yes'])


with col3:
    retina_display = st.radio('RetinaDisplay', ['No', 'Yes'])
    cpu_company = st.selectbox('CPU_company', ['Intel', 'AMD', 'Samsung'])
    cpu_model = st.selectbox('CPU_model', data['CPU_model'].unique())
    primary_storage_type = st.selectbox('PrimaryStorageType' ,data['PrimaryStorageType'].unique())
    secondary_storage_type = st.selectbox('SecondaryStorageType', data['SecondaryStorageType'].unique())
    gpu_company = st.selectbox('GPU_company', data['GPU_company'].unique())
    gpu_model = st.selectbox('GPU_model', data['GPU_model'].unique())
    def display_size(x):
        if x >= 10 and x < 13:
            return 'Small'
        elif x >= 13 and x < 15:
            return 'Average'
        elif x >= 15 and x < 17:
            return 'Large'
        elif x >= 16 and x < 20:
            return 'Extra Large'
        else:
            return 'Other'
    display_category = display_size(inches)
    def weight_category(x):
        if x >= 650 and x < 1700:
            return 'Light_weight'
        elif x >= 1700 and x < 3000:
            return 'Average_weight'
        elif x >= 3000 and x < 5000:
            return 'Heavy_weight'
        else:
            return 'Other'
    weight_category_type = weight_category(weight)
    brand_category = {
    "Apple": "Premium",
    "MSI": "Premium",
    "Razer": "Premium",
    "Microsoft": "Premium",
    "Google": "Premium",
    "Samsung": "Premium",

    "Dell": "Mid-range",
    "HP": "Mid-range",
    "Lenovo": "Mid-range",
    "Asus": "Mid-range",
    "Huawei": "Mid-range",
    "LG": "Mid-range",

    "Acer": "Budget",
    "Toshiba": "Budget",
    "Xiaomi": "Budget",
    "Vero": "Budget",
    "Mediacom": "Budget",
    "Chuwi": "Budget",
    "Fujitsu": "Budget"
}
    brand_cat = brand_category.get(company)



input_dict = {
    'Inches' : [inches],
    'Ram' : [ram],
    'Weight': [weight],
    'ScreenW': [screen_weight],
    'ScreenH': [screen_height],
    'CPU_freq': [cpu_freq],
    'PrimaryStorage': [primary_storage],
    'SecondaryStorage': [secondary_storage],
    'Weight_per_inch': [weight_per_inch],
    'Company' : [company],
    'Product' : [product],
    'TypeName' :  [type_name],
    'OS' : [os],
    'Screen' : [screen],
    'Touchscreen': [toch_screen],
    'IPSpanel' : [ips_pannel],
    'RetinaDisplay' : [retina_display],
    'CPU_company' : [cpu_company],
    'CPU_model': [cpu_model],
    'PrimaryStorageType' : [primary_storage_type],
    'SecondaryStorageType' : [secondary_storage_type], 
    'GPU_company': [gpu_company],
    'GPU_model' :[gpu_model],
    'Display_Size': [display_category],
    'Weight_category': [weight_category_type],
    'Brand_Category': [brand_cat]
}

input_df = pd.DataFrame(input_dict)
st.write(input_df)


if st.button('Predict'):
    prediction = model.predict(input_df)
    st.success(f"Laptop price is : { int(prediction[0])} Rupies")
#  Streamlit run "Model Deploy/app.py"



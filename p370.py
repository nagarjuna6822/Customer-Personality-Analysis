import streamlit as st
import pickle
import pandas as pd



def create_page():
    st.title('Customer segmentation')
    st.write('Cluster')
    Education = st.sidebar.slider('Education',min_value=0,max_value=2)
    Income = st.slider('Income', min_value=1730, max_value=113734)
    Recency = st.sidebar.slider('Recency', min_value=0, max_value=5)
    Wines = st.sidebar.slider('Wines', min_value=0.0, max_value=8.0, step=0.1)
    Fruits = st.sidebar.slider('Fruits', min_value=0.0, max_value=5.0, step=0.1)
    Meat = st.sidebar.slider('Meat', min_value=0.0, max_value=7.0, step=0.1)
    Fish = st.sidebar.slider('Fish', min_value=0.0, max_value=6.0, step=0.1)
    Sweet = st.sidebar.slider('Sweet', min_value=0.0, max_value=6.0, step=0.1)
    Gold = st.sidebar.slider('Gold', min_value=0, max_value=6,step=1)
    Discount_Purchases = st.sidebar.slider('Discount_Purchases', min_value=0.0, max_value=3.0, step=0.1)
    Catalog_Purchases = st.sidebar.slider('Catalog_Purchases', min_value=0.0, max_value=4.0, step=0.1)
    Store_Purchases = st.sidebar.slider('Store_Purchases', min_value=0.0, max_value=4.0, step=0.1)
    NumWebVisitsMonth = st.sidebar.slider('NumWebVisitsMonth', min_value=0.0, max_value=4.0, step=0.1)
    Total_Accepted	= st.sidebar.radio('Total_Accepted',[0, 1], key='Total_Accepted')
    
   
   # Response = st.sidebar.radio('Response', [0,1], key='Response')
    data1 = {'Education': Education, 'Income': Income,
             'Recency': Recency, 'Wines': Wines, 'Fruits': Fruits, 'Meat': Meat,
             'Fish': Fish, 'Sweet': Sweet,'Gold':Gold,'Discount_Purchases': Discount_Purchases,
              'Catalog_Purchases': Catalog_Purchases,'Store_Purchases': Store_Purchases,
             'NumWebVisitsMonth': NumWebVisitsMonth,
             'Total_Accepted':Total_Accepted}
    df = pd.DataFrame(data1, index=[0])
    return df
features = create_page()

if st.sidebar.button('Submit'):
    st.write(features)

    file1 = open('Customer_clustering.pkl', 'rb')
    rf = pickle.load(file1)
    file1.close()
    cluster_label = rf.predict(features)

    st.write(f'Belongs to cluster {cluster_label[0]}')

    st.write(cluster_label)


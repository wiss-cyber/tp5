import streamlit as st 
import pandas as pd
st.title("Mini-app Streamlit")
df=pd.DataFrame({"A":[1,2,3], "B": [4,5,6]})
st.write("Exemple de DataFrame:",df)

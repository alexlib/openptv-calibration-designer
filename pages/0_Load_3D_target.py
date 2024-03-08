import plotly.express as px
import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter='\t', names=['id','x','y','z'])
    st.dataframe(df)


    # df = px.data.iris()
    fig = px.scatter_3d(df, x='x', y='y', z='z',
                color='id', color_continuous_scale=px.colors.sequential.Viridis)
    # fig.show()
    # Plot!
    st.plotly_chart(fig, use_container_width=True)
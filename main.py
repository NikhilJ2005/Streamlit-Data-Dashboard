import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
    
st.title("Simple Data Dashboard")
    
# File Upload Button
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
if uploaded_file is not None:
    # Pandas Method to read csv file
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    # Describes the data briefly
    st.write(df.describe())
    
    st.subheader('Filter Data')
        
    # Returns a list

    columns=df.columns.tolist()
    selected_column=st.selectbox("Select Column to filter by",columns) #You can Select by column.
    unique_values=df[selected_column].unique()
    
    selected_value=st.selectbox("Select Value",unique_values) #Here you can select by value

    filtered_df=df[df[selected_column]==selected_value]
    st.write(filtered_df)

    #Plotting
    st.subheader("Plot Data")
    #x-axis
    x_column=st.selectbox("Select x-axis column",columns)
    #y-axis
    y_column=st.selectbox("Select y-axis column",columns)

    #Button which displays the chart
    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.plot(filtered_df[x_column], filtered_df[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f'{y_column} vs {x_column}')
        st.pyplot(fig)
else:
    st.write("Waiting on File Upload....")





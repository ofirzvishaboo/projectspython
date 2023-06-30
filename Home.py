# def rewrite_file(file_path, new_content):
#     try:
#         with open(file_path, 'w') as file:
#             file.write(new_content)
#         print(f"File '{file_path}' has been rewritten successfully.")
#     except IOError:
#         print(f"An error occurred while rewriting the file '{file_path}'.")
import streamlit
import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("ProjectImages/photo.png")

with col2:
    st.title("Ofir zvish")
    content = """
    im 23 y/o from israel and grew up in givatayim
    """
    st.info(content)

st.subheader("This is a free row for everyone")

col3, Empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("ProjectImages/" + row["image"])
        st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("ProjectImages/" + row["image"])
        st.write(f"[Source code]({row['url']})")

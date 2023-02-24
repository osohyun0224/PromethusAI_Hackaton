import streamlit as st

st.markdown("# 게시판 ")
st.sidebar.markdown("# 게시판 ")

# Text Area
message = st.text_area("", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)

import streamlit as st

st.markdown("# 토크판 ")
st.sidebar.markdown("# 토크판 ")

## Date Input
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())

# Text Input
first_name = st.text_input("성함을 입력하세요.", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)


# Text Area
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)
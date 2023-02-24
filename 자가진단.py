import streamlit as st

st.title("자가진단")
st.sidebar.markdown("# 자가진단 ")

st.subheader("행복지수")
slider_range = st.slider("오늘은 얼마나 행복했을까요?", value=[50])


st.subheader("감정분석")
st.markdown("오늘은 무슨 색을 좋아할까요?")
rainbow = ['빨간색', '주황색', '노란색', '초록색', '파란색', '보라색', '검정색']
start_clr, end_clr = st.select_slider("원하는 색상을 선택하세요.",
    options=rainbow, value=('빨간색','검정색'))
st.write('You chose:', start_clr, "to", end_clr)


st.title("<더 나은 나를 위한 하루>")
page_names = ['home', 'going out']

page = st.radio('점검사항', page_names, index=1)
st.write("**The variable 'page' returns:**", page)

if page == 'home':
   st.subheader('가장 좋아하는 일을 해보는 게 어떨까요?')
   st.write("휴식시간을 갖으세요! :thumbsup:")
else:
   st.subheader("날씨가 너무 좋으니 마음껏 산책해 보는 게 어떨까요?")
   st.write("물을 챙겨드세요! :wave:")

import streamlit as st

st.title("Welcome to my Portfolio")
st.subheader("Hi Everyone!!:wave:")
st.write("I am :blue[_Harshal Mahajan_],working as Data Science intern in Innomatics Research Labs.")
st.write("Email-id:-harshal.mahajan89@gmail.com")
st.write(" :point_down: Connect with me on below links:")
st.markdown("[Linkedin](https://www.linkedin.com/in/harshal-mahajan-159b64266/)")
st.markdown("[Gitub](https://github.com/harshalmahajan5789)")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("Thank you for viewing my profile :smile:")
    st.balloons()
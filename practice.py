import streamlit as st
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://up.yimg.com/ib/th?id=OIP.p_3pLix3JoJW22IsJyvsQAHaHa&%3Bpid=Api&w=474&c=1&rs=1&qlt=95')
st.title('Streamlit Practice')
st.header('By Shubham Kumar')
st.text('This is a practice on Streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME<h1><center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/live/LGTbdjoEBVM?si=-I4lRGYXhCy5v5Ki')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("Choose Date of Birth")
        marks=st.slider('Choose Marks')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)

elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt')


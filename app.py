import streamlit as st
from passwd_checker import password

# Sets the configuration for the Streamlit page
st.set_page_config(page_title="PASSWORD STRENGTH CHECKER", layout="centered")

st.title("🔐PASSWORD STRENGTH CHECKER")
st.write("Enter your password")

passwd = st.text_input("Password", type="password")

checker = password()

#Result
if passwd:
    result = checker.c_passwd_s(passwd)
    st.markdown(f"**Result:** {result}")


    score, max_score = checker.strength_score(passwd)
    strength_percent = int((score / max_score) * 100)

    st.progress(strength_percent)


    #Feedback
    if strength_percent < 40:
        st.warning("Weak Password⚠️")
    elif strength_percent < 80:
        st.info("Average Password💡")
    else:
        st.success("Strong Password✔️")
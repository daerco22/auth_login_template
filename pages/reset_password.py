# %% IMPORTS
import yaml
import streamlit as st
import streamlit_authenticator as stauth

# %% PAGE CONFIG
st.set_page_config(page_title='Reset Password Template', page_icon=':penguin:')

# %% USER AUTHENTICATION
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
	authenticator.logout("Logout", "sidebar")
	st.title('Reset Password Template :chart_with_upwards_trend:')
	try:
		if authenticator.reset_password(username, 'Reset password'):
			st.success('Password modified successfully')
	except Exception as e:
		st.error(e)

# %%
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
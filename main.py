# %% IMPORTS
import yaml
import streamlit as st
import streamlit_authenticator as stauth

# %% PAGE CONFIG
st.set_page_config(page_title='Auth Login Template', page_icon=':penguin:')

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

# FORGOT PASSWORD AUTH
def forgot_password(auth):
    try:
        username_forgot_pw, email_forgot_password, random_password = auth.forgot_password('Forgot password')
        if username_forgot_pw:
            st.success('New password sent securely')
            st.write(random_password)
            # Random password to be transferred to user securely
        elif username_forgot_pw == False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

# FORGOT USERNAME AUTH
def forgot_username(auth):
    if st.button('Forgot Username'):
        try:
            username_forgot_username, email_forgot_username = auth.forgot_username('Forgot username')
            if username_forgot_username:
                st.success('Username sent securely')
                # Username to be transferred to user securely
            elif username_forgot_username == False:
                st.error('Email not found')
        except Exception as e:
            st.error(e)

        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

def register_new_user(auth):
    if st.button('Register'):
        try:
            if auth.register_user('Register user', preauthorization=False):
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)

        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

# LOGIN AUTH
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    if st.button('Forgot Password'):
        forgot_password(authenticator)

if authentication_status:
	authenticator.logout("Logout", "sidebar")
	st.title('Auth Login Template :chart_with_upwards_trend:')

# %%
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
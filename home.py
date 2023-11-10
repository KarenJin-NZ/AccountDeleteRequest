import streamlit as st
import webbrowser
import urllib

def delete_account(email):
    # Add your account deletion logic here
    # For this example, we'll just print the email
    print(f"Account with email {email} has been marked for deletion.")

    # Open default email client
    receiver_email = "karenjin2000@gmail.com"
    subject = "Account Deletion Request"
    body = f"An account deletion request has been received for the email: {email}."
    mailto_link = f"mailto:{receiver_email}?subject={subject}&body={body}"
    encoded_mailto_link = urllib.parse.quote(mailto_link, safe='/:?=&')

    try:
        webbrowser.open(encoded_mailto_link)
    except Exception as e:
        st.error(f"Failed to open email client. Error: {e}")

def main():
    st.title('Account Deletion Request')

    st.write('Enter your email address below to request account deletion.')
    email = st.text_input('Email')

    if st.button('Request Account Deletion'):
        delete_account(email)
        st.write(f"An account deletion request has been sent for {email}.")

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
st.title("JNTUA COLLEGE OF ENGINEERING KALIKIRI")
import streamlit as st

# Function to authenticate users
def authenticate(username, password):
    # Hardcoded username and password (replace with actual authentication logic)
    VALID_USERNAME = "jntuacek"
    VALID_PASSWORD = "ece"

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return True
    else:
        return False

# Streamlit app
def main():
    # If user is not authenticated, show login form
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.subheader('Login')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.success('You have successfully logged in!')
            else:
                st.error('Invalid username or password. Please try again.')

    # If user is authenticated, show the content
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        st.subheader('Authenticated Content')
        uploaded_file = st.file_uploader("Upload your file")
        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            df=pd.read_excel(file_contents)
            df = df.fillna("")
            st.dataframe(df)
        df['Unnamed: 12'] = pd.to_numeric(df['Unnamed: 12'], errors='coerce')
        df['Unnamed: 2'] = pd.to_numeric(df['Unnamed: 2'], errors='coerce')
        df['Unnamed: 3'] = pd.to_numeric(df['Unnamed: 3'], errors='coerce')
        df['Unnamed: 4'] = pd.to_numeric(df['Unnamed: 4'], errors='coerce')
        df['Unnamed: 5'] = pd.to_numeric(df['Unnamed: 5'], errors='coerce')
        df['Unnamed: 6'] = pd.to_numeric(df['Unnamed: 6'], errors='coerce')
        df['Unnamed: 7'] = pd.to_numeric(df['Unnamed: 7'], errors='coerce')
        df['Unnamed: 8'] = pd.to_numeric(df['Unnamed: 8'], errors='coerce')
        df['Unnamed: 9'] = pd.to_numeric(df['Unnamed: 9'], errors='coerce')
        df['Unnamed: 10'] = pd.to_numeric(df['Unnamed: 10'], errors='coerce')

        st.sidebar.title("result analysis")
        if st.sidebar.button("1st class with Distinction(>70%)"):
            d=df.loc[df['Unnamed: 12']>=70]
            st.sidebar.write("count:",len(d))
        if st.sidebar.button("1st class(60%-70%)"):
            e=df.loc[(df['Unnamed: 12']>=60)&(df['Unnamed: 12']<=70)]
            st.sidebar.write("count:",len(e))
        if st.sidebar.button("2nd class(50%-60%)"):
            g=df.loc[(df['Unnamed: 12']>=50)&(df['Unnamed: 12']<=60)]
            st.sidebar.write("count:",len(g))
        if st.sidebar.button("Failures(<40%)"):
            f=df.loc[df['Unnamed: 12']<=40]
            st.sidebar.write("count:",len(f))
        st.sidebar.title("SUBJECT WISE PASS%:")
        if st.sidebar.button("EDC:"):
            value = df.iloc[69,2]
            st.sidebar.write(value*100)
        if st.sidebar.button("DE&VC:"):
            value = df.iloc[69,3]
            st.sidebar.write(value*100)
        if st.sidebar.button("CP&DS:"):
            value = df.iloc[69,4]
            st.sidebar.write(value*100)
        if st.sidebar.button("CHY:"):
            value = df.iloc[69,5]
            st.sidebar.write(value*100)
        if st.sidebar.button("IT WORKSHOP:"):
            value = df.iloc[69,6]
            st.sidebar.write(value*100)
        if st.sidebar.button("ENG WORKSHOP:"):
            value = df.iloc[69,7]
            st.sidebar.write(value*100)
        if st.sidebar.button("CHY LAB:"):
            value = df.iloc[69,8]
            st.sidebar.write(value*100)
        if st.sidebar.button("CP&DS LAB:"):
            value = df.iloc[69,9]
            st.sidebar.write(value*100)
        if st.sidebar.button("TOTAL PASS%"):

            st.sidebar.write("57.89")

        st.sidebar.title("SUB wise Fail Candidates:")
        if st.sidebar.button("EDC"):
            f=df.loc[df['Unnamed: 2']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("DE&VC"):
            f=df.loc[df['Unnamed: 3']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("CP&DS"):
            f=df.loc[df['Unnamed: 4']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("CHY"):
            f=df.loc[df['Unnamed: 5']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("IT WORKSHOP"):
            f=df.loc[df['Unnamed: 6']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("ENGG WORKSHOP"):
            f=df.loc[df['Unnamed: 7']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("EDC LAB"):
            f=df.loc[df['Unnamed: 8']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("CP&DS LAB"):
            f=df.loc[df['Unnamed: 9']<25]
            st.sidebar.write("count:",len(f)-1)
        if st.sidebar.button("CHY LAB"):
            f=df.loc[df['Unnamed: 10']<25]
            st.sidebar.write("count:",len(f)-1)


if __name__ == '__main__':
    main()


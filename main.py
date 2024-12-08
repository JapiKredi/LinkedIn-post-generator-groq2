import streamlit as st
from ui.streamlit_app import StreamlitUI


def main():
    try:
        app = StreamlitUI()
        app.run()
    except Exception as e:
        st.error(f"An error occurred in main: {str(e)}")


if __name__ == "__main__":
    main()

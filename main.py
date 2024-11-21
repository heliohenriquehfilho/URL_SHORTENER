# Importing the required libraries
import streamlit as st  # Streamlit for building interactive web applications
import pyshorteners as ps  # Library for URL shortening

# Application title
st.title("URL SHORTENER")  # Displays the main title on the page

# Brief description of the application
st.write("Tutorial: ")  # Tutorial heading
st.write("Paste the link you want to shorten, then click shorten")  # Instructions for the user

# Input field for the user to enter the link they want to shorten
link = st.text_input("Link")  # Text input to capture the URL

# Check if the user has entered a link
if link != "":  # Executes only if the input field is not empty
    # Initializing the URL shortener
    tiny_url_func = ps.Shortener()  # Creates an instance of the shortener

    # Generating the shortened link using the TinyURL service
    tiny_url = tiny_url_func.tinyurl.short(link)  # Shortens the provided URL

    # Displaying the shortened link on the application interface
    st.write("New URL: " + tiny_url)  # Shows the shortened URL to the user

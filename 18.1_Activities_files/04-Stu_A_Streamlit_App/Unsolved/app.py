# @TODO: Import the libraries for Pandas and Streamlit
import pandas as pd
import streamlit as st

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write('# Streamlit app') 
# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write('This is my Streamli app')

# @TODO: Create a Pandas dataframe
df = pd.Dataframe({"Tempurature": ['Hot', 'Cold', 'Warm', 'Ice_cold']})
pd.get_dummies(df)
# @TODO: Write the Pandas dataframe to the page
st.write(df)

# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.
# YOUR CODE HERE!

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
# YOUR CODE HERE!


# Bonus
# YOUR CODE HERE!

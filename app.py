import streamlit as st
import pandas as pd
import random

# Load dataset
def load_quotes():
    try:
        return pd.read_csv("quotes.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Quote", "Author"])

df = load_quotes()

st.title("💡 Random Quote Generator")

if not df.empty:
    if st.button("New Quote"):
        idx = random.randint(0, len(df)-1)
        row = df.iloc[idx]
        st.success(f"“{row['Quote']}” — {row['Author']}")
else:
    st.info("No quotes found. Add some below!")

# Add new quote
st.subheader("➕ Add Quote")
quote = st.text_input("Quote")
author = st.text_input("Author")

if st.button("Add"):
    if quote.strip() and author.strip():
        new_row = {"Quote": quote, "Author": author}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv("quotes.csv", index=False)
        st.success("Quote Added!")

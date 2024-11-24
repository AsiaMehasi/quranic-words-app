# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(quranic_words)

# Set the number of words per page
words_per_page = 50

# Create a session state to keep track of the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""

# Search bar to filter words
search_query = st.text_input("Search for a Quranic word (Arabic or Meaning):", st.session_state.search_query)
st.session_state.search_query = search_query

# Filter words based on the search query
if search_query:
    # Filter the dataframe and remove duplicates
    df_filtered = df[df['Word (Arabic)'].str.contains(search_query, case=False) | df['Meaning'].str.contains(search_query, case=False)]
    df_filtered = df_filtered.drop_duplicates()  # Remove duplicates after filtering
else:
    df_filtered = df

# Calculate the total number of pages for the filtered data
total_pages = len(df_filtered) // words_per_page + (1 if len(df_filtered) % words_per_page > 0 else 0)

# Calculate the starting and ending index for the current page
start_index = st.session_state.current_page * words_per_page
end_index = start_index + words_per_page

# Get the words to display for the current page
page_words = df_filtered.iloc[start_index:end_index]

# Display the words for the current page
st.markdown("## Quranic Words List")

for index, row in page_words.iterrows():
    st.subheader(f"Word: {row['Word (Arabic)']}")
    st.write(f"**Transliteration**: {row['Transliteration']}")
    st.write(f"**Meaning**: {row['Meaning']}")
    st.write(f"**Example**: {row['Example']}")
    st.write("---")

# Navigation buttons
col1, col2, col3 = st.columns([1, 5, 1])

# Show the page number
with col2:
    st.write(f"**Page {st.session_state.current_page + 1} of {total_pages}**")

# Show 'Previous' button only if not on the first page
if st.session_state.current_page > 0:
    with col1:
        if st.button("Previous"):
            st.session_state.current_page -= 1

# Show 'Next' button only if more pages exist
if end_index < len(df_filtered):
    with col2:
        if st.button("Next"):
            st.session_state.current_page += 1

# "Home" button to return to the first page
with col3:
    if st.button("Home"):
        st.session_state.current_page = 0  # Reset to the first page

# Custom CSS for improved styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        font-size: 18px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

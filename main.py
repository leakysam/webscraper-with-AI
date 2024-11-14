import streamlit as st
from scrape import (scrape_website,split_dom_content,clean_body_content,extract_body_content,)

from parse import parse_with_ollama
st.title("Web Scrape With AI")

url = st.text_input("Enter a Website URL:")


if st.button("Scrape Site"):
    st.write("Scraping now")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("view DOM Content"):#button to toggle to show what comes below
        st.text_area("Dom Content", cleaned_content, height=300)
        
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe your what you want?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
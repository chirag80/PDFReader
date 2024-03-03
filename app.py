import PyPDF2
import streamlit as st
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def main():
    st.title('PDF Text Extractor')

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("Text Extracted from PDF:")
        st.write(text)

if __name__ == "__main__":
    main()

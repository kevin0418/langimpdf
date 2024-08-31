import streamlit as st

# 파일 업로드
uploaded_file = st.file_uploader("pdftest", type="pdf")

if uploaded_file is not None:
    # PDF 파일을 읽고 처리
    st.write("파일 이름:", uploaded_file.name)
    st.write("파일 크기:", uploaded_file.size, "bytes")

    # PDF 파일을 웹에 표시
    st.download_button(
        label="PDF 다운로드",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )

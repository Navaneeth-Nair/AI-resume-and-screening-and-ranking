import streamlit as st 
import os
from rank import jobdescsimilarity
from parser import extract_text

def rank_resumes(job_desc, resume_files):
    extracted_text = []
    file_names = []
    
    for file in resume_files:
        file_name = os.path.basename(file.name)
        text = extract_text(file)
        if not text or text == "No text extracted":
            st.error(f"⚠️ Could not extract text from: {file_name}")
            continue
        extracted_text.append(text)
        file_names.append((file_name, file))  

    if extracted_text:
        scores = jobdescsimilarity(job_desc, extracted_text)
        ranked_resumes = [(file_names[idx][0], score, file_names[idx][1]) for idx, (text, score) in enumerate(scores)]
        return ranked_resumes
    else:
        return []  


st.title("📄 AI-Powered Resume Screening & Ranking")

uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)
job_desc = st.text_area("Enter Job Description:")

if st.button("Process"):
    if job_desc.strip() and uploaded_files:
        ranked_resumes = rank_resumes(job_desc, uploaded_files)

        if ranked_resumes:
            st.subheader("📜 Ranked Resumes")
            for rank, (file_name, score, file) in enumerate(ranked_resumes, start=1):
                file.seek(0)  
                file_data = file.read()

                with st.expander(f"#{rank}: {file_name} (Score: {score}%)"):
                    st.download_button(
                        label="📥 Download Resume",
                        data=file_data,
                        file_name=file_name,
                        mime="application/octet-stream"
                    )
        else:
            st.warning("No valid resumes to rank. Please check the uploaded files.")
    else:
        st.warning("Please upload resumes and enter a job description.")
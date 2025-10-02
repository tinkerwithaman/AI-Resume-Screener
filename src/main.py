import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_path):
    with pdfplumber.open(resume_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    skills_keywords = ["Python", "Java", "SQL", "Machine Learning", "AI"]
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return found_skills

if __name__ == "__main__":
    skills = extract_skills("data/sample_resume.pdf")
    print("Extracted Skills:", skills)

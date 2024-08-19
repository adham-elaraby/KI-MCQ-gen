import streamlit as st
import pandas as pd
from mcq_ai_generator import generate_and_evaluate_mcqs
from io import BytesIO

st.title("KI-basierter MCQ-Generator")
st.write("Laden Sie eine PDF-Datei hoch, um Multiple-Choice-Fragen zu extrahieren und eine CSV-Datei zu erstellen.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
number = st.number_input("Anzahl der MCQs", min_value=1, step=1)
subject = st.text_input("Fach / Modul")
tone = st.text_input("Ton", "Academisch, Spartan, Analytisch")
language = st.selectbox("Sprache", ("English", "Deutsch"), index=1)
past_questions = st.text_input("Referenzfragen")

if st.button("Fragen Generieren"):
    if uploaded_file and number and subject and tone:
        try:
            mcqs = generate_and_evaluate_mcqs(uploaded_file, number, subject, tone, language, past_questions)
            if mcqs:
                df = pd.DataFrame(mcqs)
                st.write("### Generierte Klausurfragen")
                st.dataframe(df)  # tabelle
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=BytesIO(csv.encode('utf-8')),
                    file_name='mcqs.csv',
                    mime='text/csv'
                )
            else:
                st.error("Es konnten keine MCQs aus der PDF-Datei extrahiert werden. Bitte überprüfen Sie die Datei und versuchen Sie es erneut.")
        except Exception as e:
            st.error(f"Fehler aufgetreten: {e}")
            st.error(traceback.format_exc())
    else:
        st.error("Bitte laden Sie eine PDF-Datei hoch und füllen Sie alle Felder aus.")

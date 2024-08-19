# MCQ-Generator aus PDF

Diese Streamlit-Webapp ermöglicht es Nutzern, eine PDF-Datei hochzuladen, Multiple-Choice-Fragen (MCQs) und Klausurfragen aus dem Inhalt zu extrahieren und die extrahierten Fragen in einer CSV-Datei zu speichern.

## Funktionen
- PDF-Dateien hochladen
- Text aus PDFs extrahieren
- MCQs und Klausurfragen basierend auf dem extrahierten Text generieren
- Generierte Fragen im CSV-Format herunterladen

## Anforderungen
- Streamlit
- Pandas
- PyMuPDF
- Langchain
- Python-dotenv

## Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/adham-elaraby/KI-MCQ-Gen.git
   ..
   python -m venv python_env
   ..
   pip install -r requirements.txt
   ```

## Nutzung

1. Fügen Sie Ihren OpenAI-API-Schlüssel in die bereitgestellte `.env`-Datei ein:
   ```text
   OPENAI_API_KEY=Ihr_openai_api_schlüssel
   ```
2. Starten Sie die Streamlit-App:
   ```bash
   streamlit run app.py
   ```
3. Laden Sie eine PDF-Datei hoch.
4. Geben Sie die Anzahl der MCQs, das Fach, Ton, Sprache und Referenzfragen an.
5. Klicken Sie auf "Fragen generieren", um MCQs und Klausurfragen zu extrahieren und die CSV-Datei herunterzuladen.

## Mögliche Verbesserungen
- Fine-Tuning?
- Andere Sprachmodelle
- FSL?


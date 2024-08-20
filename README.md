# MCQ-Generator aus PDF

Diese Streamlit-Webapp ermöglicht es Nutzern, eine PDF-Datei hochzuladen, Multiple-Choice-Fragen (MCQs) und Klausurfragen aus dem Inhalt zu extrahieren und die extrahierten Fragen in einer CSV-Datei zu speichern.



https://github.com/user-attachments/assets/b4fdd45f-9cfa-4d07-bb96-8213788a5175



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
1. Clone Repository:
   ```bash
   git clone https://github.com/adham-elaraby/KI-MCQ-Gen.git
   cd KI-MCQ-gen
   ```
2. Virtuelle Umgebung erstellen und Aktivieren (Shell-abhängig)
   ```bash
   python -m venv python_env

   # Bash
   source python_env/bin/activate

   # PowerShell
   .\python_env\Scripts\Activate.ps1
   ```
3. Abhängigkeiten installieren
   ```bash
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

## Mögliche Verbesserungen (TODOs)
- Fine-Tuning?
- Andere Sprachmodelle
- FSL?
- Vektorisierung (Vector Embeddings) + Upstash
- Tokenisierung mit tiktoken
- Langchain w/ FastAPI + Langserve
- Rate limiting mit Upstash Redis
- API-Key basiertes rate limiting

## Quellen und Hilfreiche Rescourcen
[nirmals-workspace/Langchain-MCQ-Generation-using-ConversationChain](https://github.com/nirmals-workspace/Langchain-MCQ-Generation-using-ConversationChain)

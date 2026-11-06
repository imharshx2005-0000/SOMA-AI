# SOMA AI

Clone and open the project folder in VS Code.


**Step 1:** Copy `.env.example` to `.env` and fill in your keys:



You need 2 API keys:

| Key | Where to get it |
|-----|----------------|
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) |
| `QDRANT_API_KEY` + `QDRANT_URL` | [Qdrant Cloud Dashboard](https://cloud.qdrant.io/) — create a free cluster |

**Step 2:** Set up the virtual environment:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

That's it. You're ready.

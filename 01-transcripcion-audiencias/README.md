# 01 - Local AI Courtroom Transcription System

**Context:** Poder Judicial del Estado de Tamaulipas - Sala de Oralidad Penal

**Problem:** Manual transcription of 2-3 hour criminal hearings took 4-6 hours per clerk.

**Solution:** Local AI workflow using Whisper (medium model for Spanish) + Python automation + n8n. No cloud dependency for sensitive legal data.

**Stack:** Python, OpenAI Whisper, pydub, n8n, Docker, Linux Server, Google Drive API

**Impact:**
- 60% reduction in transcription time
- 100% local processing (privacy compliance for courtroom data)
- Automated backup and email notification

**How to run:**
```bash
pip install openai-whisper pydub
python transcription_local.py audiencia.mp3
```

**n8n flow:** Import `n8n_workflow.json` into n8n to automate folder watching -> transcription -> summarization -> Drive upload.

Author: Alejandro Serna Cabrera - AI Automation Engineer
Portfolio: https://alexsercab.github.io
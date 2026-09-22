# 03 - LegalTech WhatsApp Automation Bot

**Problem:** Law firms in Tampico/Madero lose clients because they don't answer WhatsApp fast and secretaries spend hours giving case status.

**Solution:** WhatsApp bot with AI agent that:
- Transcribes voice notes with Whisper
- Answers case status using expediente number
- Schedules appointments via Google Calendar
- Upsells forensic services (Perito)

**Stack:** n8n, WhatsApp Business API, OpenAI API, Whisper, Python Flask, Google Calendar API

**Business model for you as contractor:**
- Setup fee: $8,000 MXN per law firm
- Monthly maintenance: $2,500 MXN
- Perfect second income alongside remote AI Automation job

**Flow:** Import `n8n_whatsapp_flow.json` into n8n

**Run local demo:**
```bash
pip install flask openai
python whatsapp_bot.py
```

Author: Alejandro Serna Cabrera

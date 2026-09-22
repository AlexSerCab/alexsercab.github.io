# 02 - Forensic Evidence Classifier Agent

**Problem:** Law firms receive unorganized digital evidence (phones, chats, disks) without classification.

**Solution:** AI Agent that classifies evidence by type, relevance, and chain-of-custody risks using LangChain + forensic metadata from Autopsy/FTK Imager/Wireshark.

**Stack:** LangChain, OpenAI API, Python, Autopsy, FTK Imager, Wireshark, Recuva

**Features:**
- Auto-extracts metadata and hash (SHA256)
- Classifies relevance for criminal/family trials
- Generates pre-dictamen report in LaTeX
- Flags manipulation risks

**Use case for contractor model:** Sell as add-on to peritaje: $3k extra por clasificación automatizada.

**Run:**
```bash
pip install langchain langchain-openai
python classifier_agent.py
```

Author: Alejandro Serna Cabrera

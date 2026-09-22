"""
LegalTech WhatsApp Bot for Law Firms
n8n + WhatsApp API + OpenAI
Author: Alejandro Serna Cabrera
"""
from flask import Flask, request
import openai

app = Flask(__name__)

SYSTEM_PROMPT = """Eres asistente legal de despacho en Tampico. 
Responde sobre estado de expediente, fechas de audiencia, y agenda citas.
Si preguntan por peritaje, ofrece servicios de Perito en Informatica Forense.
Siempre pide numero de expediente."""

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_msg = data.get("message", "")
    
    # Simple OpenAI completion (replace with LangChain agent for production)
    # response = openai.chat.completions.create(...)
    # For demo: echo + legal template
    
    reply = f"Recibido: {user_msg}. Tu expediente está en revisión. ¿Me compartes número de expediente para darte estado actualizado? - Despacho LegalTech"
    return {"reply": reply}

if __name__ == "__main__":
    app.run(port=5000)

"""
Forensic Evidence Classifier Agent
LangChain + OpenAI + Forensic Tools
Author: Alejandro Serna Cabrera
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", """Eres un perito en informática forense. Clasifica la evidencia digital:
    - Tipo: celular, disco, audio, video, chat
    - Relevancia: alta/media/baja para juicio penal
    - Cadena de custodia: verifica hash y metadatos
    - Riesgos: manipulación, borrado
    Devuelve JSON con clasificacion."""),
    ("human", "Evidencia: {evidence_description}\nMetadatos: {metadata}")
])

def classify_evidence(evidence_description, metadata):
    chain = prompt | llm
    result = chain.invoke({"evidence_description": evidence_description, "metadata": metadata})
    return result.content

if __name__ == "__main__":
    print(classify_evidence(
        "WhatsApp chat export 2GB, 3,200 mensajes",
        "Hash SHA256: abc123, Fecha creacion: 2024-03-10, Dispositivo: Samsung S21"
    ))
from app.core.config import settings

TEMPLATES = {
    "formal": lambda t: "Dear Sir/Madam,\n\n" + t + "\n\nSincerely,\nInboxGenie",
    "casual": lambda t: "Hey,\n\n" + t + "\n\nCheers",
    "concise": lambda t: t.strip().replace("\n"," ")[:512]
}

def rewrite_tone(text: str, tone: str) -> str:
    tone = (tone or "concise").lower()
    if settings.OPENAI_API_KEY:
        # placeholder: user can implement proper OpenAI call
        import requests
        headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}"}
        payload = {"model": "gpt-4o-mini", "messages":[{"role":"user","content":f"Rewrite in {tone} tone:\n\n{text}"}], "max_tokens": 600}
        r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=20)
        return r.json()["choices"][0]["message"]["content"]
    return TEMPLATES.get(tone, TEMPLATES["concise"])(text)

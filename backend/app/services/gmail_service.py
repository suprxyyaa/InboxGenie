from app.core.config import settings
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from datetime import datetime

def build_creds(token_obj: dict) -> Credentials:
    return Credentials(
        token=token_obj.get("access_token"),
        refresh_token=token_obj.get("refresh_token"),
        token_uri=token_obj.get("token_uri", "https://oauth2.googleapis.com/token"),
        client_id=settings.GMAIL_CLIENT_ID,
        client_secret=settings.GMAIL_CLIENT_SECRET,
        scopes=token_obj.get("scope", "").split()
    )

class GmailClient:
    def __init__(self, token_obj: dict):
        self.creds = build_creds(token_obj)
        self.svc = build("gmail", "v1", credentials=self.creds)

    def list_message_ids(self, q: str = "", max_results: int = settings.SYNC_MAX_RESULTS):
        r = self.svc.users().messages().list(userId="me", q=q, maxResults=max_results).execute()
        return r.get("messages", [])

    def fetch_message(self, msg_id: str) -> dict:
        r = self.svc.users().messages().get(userId="me", id=msg_id, format="full").execute()
        headers = {h["name"]: h["value"] for h in r.get("payload", {}).get("headers", [])}
        body = self._get_body(r.get("payload", {}))
        internal = int(r.get("internalDate", "0"))//1000
        return {
            "id": r.get("id"),
            "threadId": r.get("threadId"),
            "subject": headers.get("Subject"),
            "from": headers.get("From"),
            "snippet": r.get("snippet"),
            "raw": body,
            "internalDate": datetime.fromtimestamp(internal)
        }

    def _get_body(self, payload):
        if payload.get("parts"):
            for p in payload["parts"]:
                if p.get("mimeType") == "text/plain":
                    data = p.get("body", {}).get("data")
                    if data:
                        return base64.urlsafe_b64decode(data).decode(errors="ignore")
        data = payload.get("body", {}).get("data")
        if data:
            return base64.urlsafe_b64decode(data).decode(errors="ignore")
        return ""

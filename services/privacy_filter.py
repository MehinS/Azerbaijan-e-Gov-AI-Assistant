import re

def filter_sensitive_data(text: str) -> str:
    # mask numbers (simulate ID, passport, etc.)
    text = re.sub(r'\b\d{7,}\b', '[REDACTED_ID]', text)
    text = re.sub(r'\S+@\S+', '[REDACTED_EMAIL]', text)

    return text
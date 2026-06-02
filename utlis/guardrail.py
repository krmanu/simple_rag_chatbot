import re

# Prompt Injection Patterns
PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "reveal system prompt",
    "show system prompt",
    "bypass security",
    "developer mode",
    "act as administrator"
]

# Restricted Topics
BLOCKED_TOPICS = [
    "malware",
    "phishing",
    "ransomware",
    "password cracking",
    "credit card fraud",
    "ddos attack",
    "social engineering",
    "exploit vulnerability"
]

def input_guardrail(query):
  
    query_lower = query.lower()

    # Prompt Injection Detection
    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern in query_lower:
            return False, (
                "Query blocked: Prompt injection attempt detected."
            )

    # Restricted Topic Detection
    for topic in BLOCKED_TOPICS:
        if topic in query_lower:
            return False, (
                "Query blocked: Restricted topic detected."
            )

    return True, None

def output_guardrail(response):
    
    # Email
    response = re.sub(
        r"\S+@\S+\.\S+",
        "[EMAIL_REDACTED]",
        response
    )

    # Phone Number (10 digits)
    response = re.sub(
        r"\b\d{10}\b",
        "[PHONE_REDACTED]",
        response
    )

    # Credit Card (16 digits)
    response = re.sub(
        r"\b\d{16}\b",
        "[CARD_REDACTED]",
        response
    )

    # Aadhaar format
    response = re.sub(
        r"\b\d{4}\s\d{4}\s\d{4}\b",
        "[AADHAAR_REDACTED]",
        response
    )

    return response
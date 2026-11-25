# Last Out of Office: The AI Barista - writes the one-line
# out-of-office auto-reply to /output/entry.txt (gate: 1-280 chars).
import os

TEXT = "I'm out of office - I quit the helpdesk to become a barista. Your ticket is now a loyalty card: nine more emails and you earn a reply."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)

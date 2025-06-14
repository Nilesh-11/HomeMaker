import smtplib
from email.message import EmailMessage
from shared.config import EMAIL_FROM, EMAIL_HOST, EMAIL_PASS, EMAIL_PORT, EMAIL_USER
from typing import List, Optional
from pydantic import EmailStr

def send_email(
    html_content: str,
    subject: str,
    to_mail: EmailStr,
    cc: Optional[List[EmailStr]] = None,
    bcc: Optional[List[EmailStr]] = None,
    basic_set_content: str = "This is an email from Home Maker"
) -> dict:
    msg = EmailMessage()

    try:
        msg.set_content(basic_set_content)
        msg.add_alternative(html_content, subtype="html")

        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = to_mail

        if cc:
            msg["Cc"] = ", ".join(str(email) for email in cc)

        recipients = [str(to_mail)]
        if cc:
            recipients.extend(str(email) for email in cc)
        if bcc:
            recipients.extend(str(email) for email in bcc)

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg, to_addrs=recipients)

        return {"type": "ok", "details": f"Mail sent to {to_mail}"}

    except Exception as e:
        print("Error occurred while sending email:", e)
        return {"type": "error", "details": str(e)}

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import format_datetime
from zoneinfo import ZoneInfo
from app.settings.config import SMTP_HOST, SMTP_PORT, SMTP_EMAİL, SMTP_PASSWORD, SENDER_NAME
from worker.monitor_log import log_monitor_event


def send_mail(to_list, subject, body,server_id=None):
    smtp_host = SMTP_HOST
    smtp_port =  SMTP_PORT
    smtp_email = SMTP_EMAİL
    smtp_password = SMTP_PASSWORD
    sender_name =  SENDER_NAME

    to_addresses = to_list
    subject = subject

    msg = MIMEMultipart("mixed")
    msg['From'] = f"{sender_name} <{smtp_email}>"
    msg['To'] = ", ".join(to_addresses)
    msg['Subject'] = subject
    msg["Date"] = format_datetime(datetime.now(ZoneInfo("Europe/Istanbul")))

    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(host=smtp_host, port=smtp_port, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)

        if server_id:
            log_monitor_event(
                server_id=server_id,
                log_type="alert",
                message="Alert email sent",
                contacts=to_list,
                status="SUCCESS",
                response=body
            )
    except Exception as e:
        if server_id:
            log_monitor_event(
                server_id=server_id,
                log_type="error",
                message=f"Email sending failed: {e}",
                contacts=to_list,
                status="FAIL",
                response=body
            )

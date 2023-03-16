import smtplib
import os
from dotenv import load_dotenv

load_dotenv

EMAIL = os.getenv("EMAIL")
PASSWD = os.getenv("EMAIL_PASSWD")

def send_email():
    SUBJECT = "🚨 [ALERTA] Servidor en linea nuevamente"
    BODY = "Ya estoy funcionando nuevamente, gracias por precuparte por mi (payaso mentiroso)."

    MESSAGE = f"Subject: {SUBJECT}\n\n{BODY}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL, PASSWD)
        server.sendmail(EMAIL, EMAIL, MESSAGE.encode("utf-8"))


if __name__ == "__main__":
    send_email()
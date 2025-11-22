import requests
import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


# ========== 1) SCRAPING FUNCTION ==========
def get_prices():
    # مثال من موقع (انت هتقولي الموقع اللي نجيب منه لاحقًا)
    url = "https://eggpoultryprices.com/"   # placeholder — هنعدله لاحقًا

    response = requests.get(url)
    html = response.text

    # مثال بسيط جداً — هنعدله حسب الموقع اللي هتختاره
    chicken_price = "45"   # placeholder
    chick_price = "12"     # placeholder

    return chicken_price, chick_price


# ========== 2) SAVE TO CSV ==========
def save_to_csv(chicken, chick):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = "poultry_prices.csv"

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([today, chicken, chick])


# ========== 3) SEND EMAIL ==========
def send_email(chicken, chick):
    sender = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"
    receiver = "YOUR_EMAIL@gmail.com"

    msg_content = f"""
سعر دجاج التسمين الأبيض اليوم: {chicken} جنيه
سعر الكتكوت الأبيض اليوم: {chick} جنيه
"""

    msg = MIMEText(msg_content)
    msg["Subject"] = "تقرير أسعار الدواجن اليوم"
    msg["From"] = sender
    msg["To"] = receiver

    # Gmail SMTP
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.send_message(msg)
    server.quit()


# ========== MAIN ==========
if __name__ == "__main__":
    chicken, chick = get_prices()
    save_to_csv(chicken, chick)
    send_email(chicken, chick)

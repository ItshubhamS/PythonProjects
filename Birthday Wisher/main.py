import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    email = "sharmatest590@gmail.com"
    password = "ieevopanwrypfmqu"

    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f"Subject:Monday Motivation \n\n{quote}",
    )
    connection.close()

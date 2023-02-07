import smtplib
import random
import datetime as dt
now = dt.datetime.now()
day = now.weekday()
email_id = "lily21042002@gmail.com"
password = "lfcseehyhcqgjhzh"
if day>=0 and day<=6:
      with open("quotes.txt") as file:
          all_quotes = file.readlines()
          quote = random.choice(all_quotes)
      print(quote)

      with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_id,password=password)
            connection.sendmail(from_addr=email_id,to_addrs="harshavibodkhe@gmail.com",
                                msg=f"Subject:Today's Wisdom :)\n\n{quote}")
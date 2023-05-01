import csv
import time
from suggest import suggest_mail
from email.message import EmailMessage
import smtplib
import ssl

movies = []
filename = open('movie_list.csv', 'r')
file = csv.DictReader(filename)

for col in file:
    movies.append(col['movie_titles'])

suggested_movies = suggest_mail(movies[0])

send_address = 'rlabreche419@gmail.com'
password = 'aguihjefomgjqofd'
receive_address = 'bobathetea719@gmail.com'

subject = 'Here Are Your Movie Recommendations for Today!'
body = f'Here are your movie suggestions for today because you watched {movies[0]}!\n\n{suggest_mail(movies[0])}'

# em = EmailMessage()
# em['From'] = send_address
# em['To'] = receive_address
# em['Subject'] = subject
# em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(send_address, password)
    # smtp.sendmail(send_address, receive_address, em.as_string())

    idx = 0
    while idx < len(movies):
        title = movies[idx]
        body = f'Here are your movie suggestions for today because you watched {title}!\n\n{suggest_mail(title)}'

        em = EmailMessage()
        em['From'] = send_address
        em['To'] = receive_address
        em['Subject'] = subject
        em.set_content(body)

        smtp.sendmail(send_address, receive_address, em.as_string())

        idx += 1
        if idx < len(movies):
            time.sleep(180)
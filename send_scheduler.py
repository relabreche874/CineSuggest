import suggest
import schedule, time


def send_mail():
    print('Hello')


schedule.every(5).seconds.do(send_mail)

while 1:
    schedule.run_pending()
    time.sleep(1)

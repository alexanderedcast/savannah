import time
from gmail import Gmail
import re


def read_email(email, password, subject_message):
    list_links = []
    for i in range(5):
        g = Gmail()
        g.login(email, password)
        unread = g.inbox().mail(unread=True, sender="admin@edcast.com")
        num = len(unread)
        if num > 0:
            unread[0].fetch()
            subject = unread[0].subject
            if subject == subject_message:
                email_body = unread[0].body
                list_links.append(re.findall(r'(http.+0)', email_body))
                url = list_links[0][0]
                print(url)
                g.logout()
                return url
        g.logout()
        time.sleep(3)
        print("NO URL !!!" + "\n")






def delete_email(email, password):
    global g
    try:
        g = Gmail()
        g.login(email, password)
        emails = g.inbox().mail(sender="admin@edcast.com")
        for email in emails:
            email.delete()
    except ValueError as e:
        print("[-] ERROR: " + e)
    finally:
        g.logout()

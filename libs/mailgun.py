import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox083a0db102e94e9daa60f4ddb416c558.mailgun.org/messages",
        auth=("api", "6e7ef9fe87f043b97a5feb8f5dd8d4f4-46ac6b00-71c037bd"),
        data={"from": "Excited User <mailgun@sandbox083a0db102e94e9daa60f4ddb416c558.mailgun.org>",
              "to": ["shvejan2011@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


import requests
# from config import TELEGRAM_TOKEN, TELEGRAM_GROUP_ID


# def send_message(msg):
    # url = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    #
    # payload = {
    #     'chat_id': TELEGRAM_GROUP_ID,
    #     'text': msg
    # }
    #
    # response = requests.post(url=url, data=payload)
    # return response


def send_message(msg):
    return msg


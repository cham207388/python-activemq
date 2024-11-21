import time

from active_mq import ActiveMQ
from utils.env_variables import QUEUE

active_mq = ActiveMQ()


def receive_message():
    conn = active_mq.connect()
    conn.subscribe(destination=QUEUE, id=1, ack='auto')
    print('Waiting for messages...')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        conn.disconnect()

receive_message()
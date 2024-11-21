import time
from activemq.active_mq import ActiveMQ
from activemq.listener import MyListener

class ConsumerRunner:
    def __init__(self):
        self.active_mq = ActiveMQ()

    def start(self):
        connection = self.active_mq.connect()
        listener = MyListener(connection)
        connection.set_listener("", listener)

        # Subscribe to queues
        connection.subscribe(destination="/queue/lockbox", id=1, ack="auto")
        connection.subscribe(destination="/queue/elis", id=2, ack="auto")

        print("Listening for messages...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            connection.disconnect()


if __name__ == "__main__":
    runner = ConsumerRunner()
    runner.start()
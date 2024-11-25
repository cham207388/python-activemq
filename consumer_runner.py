import time
from activemq.active_mq import ActiveMQ
from activemq.consumers.elis_consumer import ElisConsumer
from activemq.consumers.lockbox_consumer import LockBoxConsumer
from activemq.listener import MyListener

class ConsumerRunner:
    def __init__(self, *consumers):
        self.active_mq = ActiveMQ()
        self.consumers = {consumer.queue: consumer for consumer in consumers}

    def start(self):
        connection = self.active_mq.connect()
        listener = MyListener(connection, self.consumers)
        connection.set_listener("", listener)

        for queue, consumer in self.consumers.items():
            print(f"Subscribing to queue: {queue}, consumer: {consumer}")

        # # Subscribe to queues
        connection.subscribe(destination="/queue/lockbox", id=1, ack="auto")
        connection.subscribe(destination="/queue/elis", id=2, ack="auto")

        print("Listening for messages...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            connection.disconnect()


if __name__ == "__main__":
    lockbox_consumer = LockBoxConsumer()
    elis_consumer = ElisConsumer()
    runner = ConsumerRunner(lockbox_consumer, elis_consumer)
    runner.start()
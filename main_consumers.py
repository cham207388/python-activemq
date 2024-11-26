import time
from activemq.setup import ActiveMQ
from consumers.elis_consumer import ElisConsumer
from consumers.lockbox_consumer import LockboxConsumer
from activemq.listener import MyListener
from producers.elis_producer import ElisProducer


class ConsumerRunner:
    def __init__(self, connection, *consumers):
        self.consumers = {consumer.queue: consumer for consumer in consumers}
        self.connection = connection

    def start(self):
        listener = MyListener(self.connection, self.consumers)
        self.connection.set_listener("", listener)

        for queue, consumer in self.consumers.items():
            print(f"Queue: {queue}, consumer: {type(consumer).__name__}")
            self.connection.subscribe(destination=queue, id=queue, ack="auto")

        print("Listening for messages...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.connection.disconnect()


if __name__ == "__main__":
    activemq = ActiveMQ()
    elis_producer = ElisProducer(activemq.connect())
    lockbox_consumer = LockboxConsumer(elis_producer)
    elis_consumer = ElisConsumer()
    runner = ConsumerRunner(activemq.connect(),lockbox_consumer, elis_consumer)
    runner.start()
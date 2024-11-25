import time
from activemq.active_mq import ActiveMQ
from activemq.consumers.elis_consumer import ElisConsumer
from activemq.consumers.lockbox_consumer import LockBoxConsumer
from activemq.listener import MyListener


class ConsumerRunner:
    def __init__(self, connection, *consumers):
        self.active_mq = ActiveMQ()
        self.consumers = {consumer.queue: consumer for consumer in consumers}
        self.connection = connection

    def start(self):
        listener = MyListener(self.connection, self.consumers)
        self.connection.set_listener("", listener)

        for queue, consumer in self.consumers.items():
            print(f"Queue: {queue}, consumer: {consumer}")
            self.connection.subscribe(destination=queue, id=queue, ack="auto")

        print("Listening for messages...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.connection.disconnect()


if __name__ == "__main__":
    lockbox_consumer = LockBoxConsumer()
    elis_consumer = ElisConsumer()
    activemq = ActiveMQ()
    runner = ConsumerRunner(activemq.connect(),lockbox_consumer, elis_consumer)
    runner.start()
import time
from activemq.active_mq import ActiveMQ
from activemq.consumers.elis_consumer import ElisConsumer
from activemq.consumers.lockbox_consumer import LockBoxConsumer
from activemq.listener import MyListener
from activemq.dispatcher.message_dispatcher import MessageDispatcher
from activemq.handler.elis_message_handler import ElisMessageHandler
from activemq.handler.lockbox_message_handler import LockBoxMessageHandler
from activemq.producers.elis_producer import ElisProducer
#
from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST
#
# queues = ["/queue/lockbox", "/queue/elis"]
#
#
# class ConsumerRunner:
#     def __init__(self):
#
#         self.mq = ActiveMQ(
#             host=ACTIVEMQ_HOST,
#             port=ACTIVEMQ_PORT,
#             username=ACTIVEMQ_USER,
#             password=ACTIVEMQ_PASSWORD,
#             queues=queues
#         )
#
#     def start(self):
#         connection = self.mq.connect(listener=None)
#
#         # Initialize dispatcher and handlers
#         dispatcher = MessageDispatcher()
#
#         # Initialize ElisProducer
#         elis_producer = ElisProducer(connection=connection)
#
#         # Register handlers with dispatcher
#         dispatcher.register_handler("/queue/elis", ElisMessageHandler())
#         dispatcher.register_handler("/queue/lockbox", LockBoxMessageHandler(elis_producer=elis_producer))
#
#         # Set up listener with dispatcher
#         listener = MyListener(connection=connection, dispatcher=dispatcher)
#         connection.set_listener('', listener)
#
#         print("Listening for messages...")
#         try:
#             while True:
#                 time.sleep(1)
#         except KeyboardInterrupt:
#             connection.disconnect()
#
#
# if __name__ == "__main__":
#     runner = ConsumerRunner()
#     runner.start()


# from activemq import ActiveMQ
# from dispatcher import MessageDispatcher
# from handlers.elis_message_handler import ElisMessageHandler
# from handlers.lockbox_message_handler import LockBoxMessageHandler
# from producer.elis_producer import ElisProducer
# from utils.env_variables import ACTIVEMQ_USER, ACTIVEMQ_PASSWORD, ACTIVEMQ_PORT, ACTIVEMQ_HOST

class ConsumerRunner:
    def __init__(self):
        # Define the queues to subscribe to
        self.queues = ["/queue/lockbox", "/queue/elis"]

        # Initialize the ActiveMQ connection
        self.mq = ActiveMQ(
            host=ACTIVEMQ_HOST,
            port=ACTIVEMQ_PORT,
            username=ACTIVEMQ_USER,
            password=ACTIVEMQ_PASSWORD,
            queues=self.queues,
        )

        # Dispatcher and listeners will be initialized after the connection
        self.dispatcher = None
        self.listener = None

    def start(self):
        # Establish connection to ActiveMQ
        print("Connecting to ActiveMQ...")
        connection = self.mq.connect(listener=None)  # No listener initially

        # Initialize the MessageDispatcher
        self.dispatcher = MessageDispatcher()

        # Initialize the ElisProducer
        elis_producer = ElisProducer(connection=connection)

        # Register handlers with the dispatcher
        self.dispatcher.register_handler("/queue/elis", ElisMessageHandler())
        self.dispatcher.register_handler("/queue/lockbox", LockBoxMessageHandler(elis_producer=elis_producer))

        # Initialize MyListener with the dispatcher
        self.listener = MyListener(connection=connection, dispatcher=self.dispatcher)

        # Assign the listener to the ActiveMQ connection
        connection.set_listener('', self.listener)

        print("Listening for messages...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down consumer...")
            self.mq.disconnect()

if __name__ == "__main__":
    runner = ConsumerRunner()
    runner.start()
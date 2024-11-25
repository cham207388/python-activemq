from consumers.my_consumer import MyConsumer
from consumers.your_consumer import YourConsumer

my_consumer = MyConsumer()
your_consumer = YourConsumer()

my_consumer.subscribe(1)
your_consumer.subscribe(2)
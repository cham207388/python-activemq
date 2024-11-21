# from activemq.active_mq import ActiveMQ
# from utils.env_variables import QUEUE
#
# active_mq = ActiveMQ()
#
# def send_message(message):
#     try:
#         connection = active_mq.connect()
#         connection.send(body=message, destination=QUEUE)
#         connection.disconnect()
#     except Exception as e:
#         print(f"Error sending message: {e}")

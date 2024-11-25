# import stomp
#
# class MyListener(stomp.ConnectionListener):
#     def on_message(self, message):
#         print(f"Received message: {message}")
#
# # Create a connection
# conn = stomp.Connection([('localhost', 61613)])
# conn.set_listener('', MyListener())
# conn.connect('admin', 'admin', wait=True)
#
# # Subscribe to the virtual topic
# conn.subscribe(destination='/queue/Consumer.A.VirtualTopic.mytopic', id=1, ack='auto')
# conn.subscribe(destination='/queue/Consumer.B.VirtualTopic.mytopic', id=1, ack='auto')
#
# # Keep the connection alive
# conn.disconnect()
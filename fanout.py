# import stomp
#
# # Create a connection
# conn = stomp.Connection([('localhost', 61613)])
# conn.start()
# conn.connect('admin', 'admin', wait=True)
#
# # Send a message to the virtual topic
# conn.send(body='Hello World!', destination='/topic/VirtualTopic.mytopic')
#
# conn.disconnect()
#
# ---consumer 1
# import stomp
#
# class MyListener(stomp.ConnectionListener):
#     def on_message(self, headers, message):
#         print(f"Received message: {message}")
#
# # Create a connection
# conn = stomp.Connection([('localhost', 61613)])
# conn.set_listener('', MyListener())
# conn.start()
# conn.connect('admin', 'admin', wait=True)
#
# # Subscribe to the virtual topic
# conn.subscribe(destination='/queue/Consumer.A.VirtualTopic.mytopic', id=1, ack='auto')
#
# # Keep the connection alive
# conn.disconnect()
#
# ---consumer 2
# import stomp
#
# class MyListener(stomp.ConnectionListener):
#     def on_message(self, headers, message):
#         print(f"Received message: {message}")
#
# # Create a connection
# conn = stomp.Connection([('localhost', 61613)])
# conn.set_listener('', MyListener())
# conn.start()
# conn.connect('admin', 'admin', wait=True)
#
# # Subscribe to the virtual topic
# conn.subscribe(destination='/queue/Consumer.B.VirtualTopic.mytopic', id=1, ack='auto')
#
# # Keep the connection alive
# conn.disconnect()

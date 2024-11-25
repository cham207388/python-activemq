# import unittest
# from unittest.mock import Mock, call
# from consumer_runner import ConsumerRunner  # Replace with actual import path
#
#
# class TestConsumerRunner(unittest.TestCase):
#     def setUp(self):
#         # Mock connection and consumer dependencies
#         self.mock_connection = Mock()
#         self.mock_consumer1 = Mock(queue="test_queue_1")
#         self.mock_consumer2 = Mock(queue="test_queue_2")
#
#         # Initialize ConsumerRunner with mocked dependencies
#         self.runner = ConsumerRunner(self.mock_connection, self.mock_consumer1, self.mock_consumer2)
#
#     def test_initialization(self):
#         # Test that consumers are correctly stored in the runner
#         self.assertIn("test_queue_1", self.runner.consumers)
#         self.assertIn("test_queue_2", self.runner.consumers)
#         self.assertEqual(self.runner.consumers["test_queue_1"], self.mock_consumer1)
#         self.assertEqual(self.runner.consumers["test_queue_2"], self.mock_consumer2)
#
#     def test_start(self):
#         # Mock the connection's set_listener and subscribe methods
#         self.mock_connection.set_listener = Mock()
#         self.mock_connection.subscribe = Mock()
#
#         # Call start method
#         with unittest.mock.patch("consumer_runner.time.sleep", side_effect=KeyboardInterrupt):
#             self.runner.start()
#
#         # Assert set_listener was called with correct arguments
#         self.mock_connection.set_listener.assert_called_once_with("", unittest.mock.ANY)
#
#         # Assert that subscribe was called for each queue
#         self.mock_connection.subscribe.assert_has_calls([
#             call(destination="test_queue_1", id="test_queue_1", ack="auto"),
#             call(destination="test_queue_2", id="test_queue_2", ack="auto"),
#         ])
#
#         # Assert disconnect is called when KeyboardInterrupt occurs
#         self.mock_connection.disconnect.assert_called_once()
#
#     def test_listener_assignment(self):
#         # Test that MyListener is assigned as the listener for the connection
#         with unittest.mock.patch("consumer_runner.MyListener") as MockListener:
#             mock_listener_instance = MockListener.return_value
#             self.runner.start()
#             MockListener.assert_called_once_with(self.mock_connection, self.runner.consumers)
#             self.mock_connection.set_listener.assert_called_once_with("", mock_listener_instance)
#
#
# if __name__ == "__main__":
#     unittest.main()
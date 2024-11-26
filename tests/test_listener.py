import unittest
from unittest.mock import MagicMock, patch
from activemq.listener import MyListener


class TestMyListener(unittest.TestCase):
    def test_initialization(self):
        # Mock the connection and consumers
        connection = MagicMock()
        mock_lockbox_consumer = MagicMock()
        mock_elis_consumer = MagicMock()

        consumers = {
            "/queue/lockbox": mock_lockbox_consumer,
            "/queue/elis": mock_elis_consumer,
        }

        # Create MyListener instance with mocks
        listener = MyListener(connection, consumers)

        # Verify the connection is set
        self.assertEqual(listener.connection, connection)

        # # Verify consumers are correctly initialized
        self.assertIn("/queue/lockbox", listener.consumers)
        self.assertIn("/queue/elis", listener.consumers)
        #
        # # Ensure consumers are the mock objects
        self.assertIs(listener.consumers["/queue/lockbox"], mock_lockbox_consumer)
        self.assertIs(listener.consumers["/queue/elis"], mock_elis_consumer)

    def test_on_error(self):
        # Mock the connection
        connection = MagicMock()
        mock_lockbox_consumer = MagicMock()
        mock_elis_consumer = MagicMock()

        consumers = {
            "/queue/lockbox": mock_lockbox_consumer,
            "/queue/elis": mock_elis_consumer,
        }

        # Create MyListener instance with mocks
        listener = MyListener(connection, consumers)

        # Mock a frame
        frame = MagicMock()
        frame.body = "Error message"

        # Capture printed output
        with patch("builtins.print") as mock_print:
            listener.on_error(frame)

        # Assert the error was printed
        mock_print.assert_called_once_with("Error: Error message")
    #
    def test_on_message_valid_consumer(self):
        # Mock the connection and consumers
        connection = MagicMock()
        mock_lockbox_consumer = MagicMock()
        mock_elis_consumer = MagicMock()

        consumers = {
            "/queue/lockbox": mock_lockbox_consumer,
            "/queue/elis": mock_elis_consumer,
        }

        # Create MyListener instance with mocks
        listener = MyListener(connection, consumers)

        # Mock a frame with a valid destination
        frame = MagicMock()
        frame.headers = {"destination": "/queue/lockbox"}
        frame.body = "Test message"

        # Call on_message
        listener.on_message(frame)

        # Assert the correct consumer was called with the message
        mock_lockbox_consumer.process_message.assert_called_once_with("Test message")
        mock_elis_consumer.process_message.assert_not_called()

    def test_on_message_no_consumer(self):
        # Mock the connection and consumers
        connection = MagicMock()
        mock_lockbox_consumer = MagicMock()
        mock_elis_consumer = MagicMock()

        consumers = {
            "/queue/lockbox": mock_lockbox_consumer,
            "/queue/elis": mock_elis_consumer,
        }

        # Create MyListener instance with mocks
        listener = MyListener(connection, consumers)

        # Mock a frame with an unknown destination
        frame = MagicMock()
        frame.headers = {"destination": "/queue/unknown"}
        frame.body = "Test message"

        # Capture printed output
        with patch("builtins.print") as mock_print:
            listener.on_message(frame)

        # Assert no consumer's process_message method was called
        mock_lockbox_consumer.process_message.assert_not_called()
        mock_elis_consumer.process_message.assert_not_called()

# if __name__ == "__main__":
#     unittest.main()
import unittest
from unittest.mock import MagicMock, patch
from producers.lockbox_producer import LockboxProducer


class TestLockboxProducer(unittest.TestCase):
    def setUp(self):
        # Mock the connection
        self.mock_connection = MagicMock()

        # Create an instance of LockboxProducer with the mocked connection
        self.producer = LockboxProducer(connection=self.mock_connection)

    def test_send_message_success(self):
        # Arrange
        message = "Test message"
        destination = "/queue/lockbox"

        # Act
        self.producer.send_message(message)

        # Assert
        self.mock_connection.send.assert_called_once_with(body=message, destination=destination)
        self.mock_connection.disconnect.assert_called_once()

    def test_send_message_failure(self):
        # Arrange
        message = "Test message"
        self.mock_connection.send.side_effect = Exception("Connection error")

        # Act
        with patch("builtins.print") as mock_print:
            self.producer.send_message(message)

        # Assert
        self.mock_connection.send.assert_called_once_with(body=message, destination="/queue/lockbox")
        mock_print.assert_any_call("Error sending message to /queue/lockbox: Connection error")
        self.mock_connection.disconnect.assert_not_called()

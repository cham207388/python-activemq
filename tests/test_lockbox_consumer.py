import json
import unittest
from unittest.mock import MagicMock, patch
from tzlocal import get_localzone
from consumers.lockbox_consumer import LockboxConsumer


class TestLockboxConsumer(unittest.TestCase):
    def setUp(self):
        # Create a mock producer
        self.mock_producer = MagicMock()

        # Create the LockboxConsumer instance with the mock producer
        self.consumer = LockboxConsumer(producer=self.mock_producer)

    @patch("consumers.lockbox_consumer.get_localzone", return_value=get_localzone())
    @patch("consumers.lockbox_consumer.datetime")
    def test_process_message_valid_message(self, mock_datetime, mock_get_localzone):
        # Arrange
        mock_now = MagicMock()
        mock_now.strftime.return_value = "18:11:2023 15:30:00"
        mock_datetime.now.return_value = mock_now

        message = '{"key": "value"}'
        expected_message = json.dumps({
            "key": "value",
            "timestamp": "18:11:2023 15:30:00"
        })

        # Act
        self.consumer.process_message(message)

        # Assert
        self.mock_producer.send_message.assert_called_once_with(expected_message)

    def test_process_message_invalid_json(self):
        # Arrange
        invalid_message = "not-a-valid-json"

        # Act
        with patch("builtins.print") as mock_print:
            self.consumer.process_message(invalid_message)

        # Assert
        self.mock_producer.send_message.assert_not_called()
        mock_print.assert_any_call(
            "Error decoding message in lockbox consumer: Expecting value: line 1 column 1 (char 0)")

    def test_process_message_empty_message(self):
        # Arrange
        empty_message = ""

        # Act
        with patch("builtins.print") as mock_print:
            self.consumer.process_message(empty_message)

        # Assert
        self.mock_producer.send_message.assert_not_called()
        mock_print.assert_any_call(
            "Error decoding message in lockbox consumer: Expecting value: line 1 column 1 (char 0)")


# if __name__ == "__main__":
#     unittest.main()
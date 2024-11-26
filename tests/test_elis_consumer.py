import json
import unittest
from unittest.mock import patch, MagicMock
from consumers.elis_consumer import ElisConsumer


class TestElisConsumer(unittest.TestCase):
    def setUp(self):
        # Create the ElisConsumer instance
        self.consumer = ElisConsumer()

    @patch("consumers.elis_consumer.SessionLocal")
    @patch("consumers.elis_consumer.to_post")
    def test_process_message_valid_message(self, mock_to_post, mock_session_local):
        # Arrange
        message = '{"title": "Peace", "content": "Cooler than Dad"}'
        mock_post = MagicMock()
        mock_to_post.return_value = mock_post

        # Mock the database session
        mock_session = MagicMock()
        mock_session_local.return_value = mock_session

        # Act
        self.consumer.process_message(message)

        # Assert
        mock_to_post.assert_called_once_with(json.loads(message))
        mock_session.add.assert_called_once_with(mock_post)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch("consumers.elis_consumer.SessionLocal")
    def test_process_message_invalid_json(self, mock_session_local):
        # Arrange
        invalid_message = "not-a-valid-json"

        # Act
        with patch("builtins.print") as mock_print:
            self.consumer.process_message(invalid_message)

        # Assert
        mock_session_local.assert_not_called()
        mock_print.assert_any_call("Error saving message to database: Expecting value: line 1 column 1 (char 0)")

    @patch("consumers.elis_consumer.SessionLocal")
    @patch("consumers.elis_consumer.to_post")
    def test_process_message_database_error(self, mock_to_post, mock_session_local):
        # Arrange
        message = '{"title": "Peace", "content": "Cooler than Dad"}'
        mock_post = MagicMock()
        mock_to_post.return_value = mock_post

        # Mock the database session to raise an error
        mock_session = MagicMock()
        mock_session.add.side_effect = Exception("Database error")
        mock_session_local.return_value = mock_session

        # Act
        with patch("builtins.print") as mock_print:
            self.consumer.process_message(message)

        # Assert
        mock_to_post.assert_called_once_with(json.loads(message))
        mock_session.add.assert_called_once_with(mock_post)
        mock_session.commit.assert_not_called()
        mock_print.assert_any_call("Error saving message to database: Database error")


if __name__ == "__main__":
    unittest.main()
#
# from consumer_runner import ConsumerRunner
#
# def test_consumer_runner_initialization_with_no_consumers(mocker):
#     # Mock the ActiveMQ connection and its methods
#     mock_connection = mocker.Mock()
#     mock_connection.set_listener = mocker.Mock()
#     mock_connection.subscribe = mocker.Mock()
#     mock_connection.disconnect = mocker.Mock()
#
#     # Initialize ConsumerRunner with no consumers
#     runner = ConsumerRunner(mock_connection)
#
#     # Start the runner
#     # We will mock time.sleep to raise KeyboardInterrupt immediately to exit the loop
#     mocker.patch('time.sleep', side_effect=KeyboardInterrupt)
#
#     runner.start()
#
#     # Assert set_listener was called once
#     mock_connection.set_listener.assert_called_once()
#
#     # Assert subscribe was never called since there are no consumers
#     mock_connection.subscribe.assert_not_called()
#
#     # Assert disconnect was called once due to KeyboardInterrupt
#     mock_connection.disconnect.assert_called_once()
#
# def test_consumer_runner_initialization_with_multiple_consumers(mocker):
#     # Mock the ActiveMQ connection and its methods
#     mock_connection = mocker.Mock()
#     mock_connection.set_listener = mocker.Mock()
#     mock_connection.subscribe = mocker.Mock()
#     mock_connection.disconnect = mocker.Mock()
#
#     # Mock consumers with queue attributes
#     mock_consumer1 = mocker.Mock()
#     mock_consumer1.queue = "queue1"
#     mock_consumer2 = mocker.Mock()
#     mock_consumer2.queue = "queue2"
#
#     # Initialize ConsumerRunner with multiple consumers
#     runner = ConsumerRunner(mock_connection, mock_consumer1, mock_consumer2)
#
#     # Start the runner
#     # We will mock time.sleep to raise KeyboardInterrupt immediately to exit the loop
#     mocker.patch('time.sleep', side_effect=KeyboardInterrupt)
#
#     runner.start()
#
#     # Assert set_listener was called once
#     mock_connection.set_listener.assert_called_once()
#
#     # Assert subscribe was called for each consumer's queue
#     mock_connection.subscribe.assert_any_call(destination="queue1", id="queue1", ack="auto")
#     mock_connection.subscribe.assert_any_call(destination="queue2", id="queue2", ack="auto")
#
#     # Assert disconnect was called once due to KeyboardInterrupt
#     mock_connection.disconnect.assert_called_once()
#
# def test_consumer_runner_handles_keyboard_interrupt_gracefully(mocker):
#     # Mock the ActiveMQ connection and its methods
#     mock_connection = mocker.Mock()
#     mock_connection.set_listener = mocker.Mock()
#     mock_connection.subscribe = mocker.Mock()
#     mock_connection.disconnect = mocker.Mock()
#
#     # Initialize ConsumerRunner with no consumers
#     runner = ConsumerRunner(mock_connection)
#
#     # Mock time.sleep to raise KeyboardInterrupt immediately to exit the loop
#     mocker.patch('time.sleep', side_effect=KeyboardInterrupt)
#
#     # Start the runner
#     runner.start()
#
#     # Assert disconnect was called once due to KeyboardInterrupt
#     mock_connection.disconnect.assert_called_once()
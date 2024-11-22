import boto3

# # Create a client for Amazon MQ
# mq_client = boto3.client('mq', region_name='us-east-2')  # Change region as needed
#
# # List brokers
# response = mq_client.list_brokers()
# for broker in response['BrokerSummaries']:
#     print(f"Broker ID: {broker['BrokerId']}, Name: {broker['BrokerName']}, Status: {broker['BrokerState']}")
#
# response = mq_client.describe_broker(BrokerId='b-d5f5c244-825c-41d5-bfc8-2e8774f17073')
#
# print("Broker Endpoints:")
# for endpoint in response['BrokerInstances'][0]['Endpoints']:
#     print(endpoint)
#
# mq_client.update_broker(
#     BrokerId='b-d5f5c244-825c-41d5-bfc8-2e8774f17073',
#     Logs={
#         'General': True
#     }
# )

# Step 1: Create a broker (if not already created)
mq_client = boto3.client('mq', region_name='us-east-2')
broker_id = 'b-d5f5c244-825c-41d5-bfc8-2e8774f17073'

# Step 2: Get the broker endpoint
response = mq_client.describe_broker(BrokerId=broker_id)
stomp_endpoint = response['BrokerInstances'][0]['Endpoints'][0]

# Step 3: Connect using stomp.py
conn = stomp.Connection12([(stomp_endpoint, 61614)])  # SSL port
conn.connect('baicham', 'TestPassword123', wait=True)
conn.send(body='Hello, Amazon MQ!', destination='/queue/example')
conn.disconnect()
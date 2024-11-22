# # Step 1: Create a VPC
# resource "aws_vpc" "activemq_vpc" {
#   cidr_block = "10.0.0.0/16"
#   tags = {
#     Name = "AmazonMQ-VPC"
#   }
# }
#
# # Step 2: Create an Internet Gateway
# resource "aws_internet_gateway" "activemq_igw" {
#   vpc_id = aws_vpc.activemq_vpc.id
#   tags = {
#     Name = "AmazonMQ-IGW"
#   }
# }
#
# # Step 3: Create a Route Table
# resource "aws_route_table" "activemq_route_table" {
#   vpc_id = aws_vpc.activemq_vpc.id
#
#   route {
#     cidr_block = "0.0.0.0/0"
#     gateway_id = aws_internet_gateway.activemq_igw.id
#   }
#
#   tags = {
#     Name = "AmazonMQ-RouteTable"
#   }
# }
#
# # Step 4: Create Public Subnets
# resource "aws_subnet" "activemq_subnet" {
#   vpc_id                  = aws_vpc.activemq_vpc.id
#   cidr_block              = "10.0.1.0/24"
#   map_public_ip_on_launch = true
#   availability_zone       = "us-east-1a" # Replace with your AZ
#
#   tags = {
#     Name = "AmazonMQ-PublicSubnet"
#   }
# }
#
# # Step 5: Associate the Route Table with the Subnet
# resource "aws_route_table_association" "activemq_route_table_association" {
#   subnet_id      = aws_subnet.activemq_subnet.id
#   route_table_id = aws_route_table.activemq_route_table.id
# }
#
# # Step 6: Create a Security Group

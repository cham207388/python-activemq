resource "aws_security_group" "mq_security_group" {
  name_prefix = "mq-sg-"
  description = "Security group for Amazon MQ"

  ingress {
    from_port   = 8162          # STOMP over SSL
    to_port     = 61614
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Replace with your trusted IP or CIDR range
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"                # Allow all outbound traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "AmazonMQ-SecurityGroup"
  }
}
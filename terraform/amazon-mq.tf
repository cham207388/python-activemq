resource "aws_mq_broker" "activemq" {
  broker_name          = "baicham-broker"
  engine_type          = "ActiveMQ"
  engine_version       = "5.18.4" # Replace with a specific version if needed
  deployment_mode      = "SINGLE_INSTANCE" # Use "ACTIVE_STANDBY_MULTI_AZ" for HA
  host_instance_type   = "mq.t3.micro" # Cost-effective instance type

  publicly_accessible  = true
  security_groups = [aws_security_group.mq_security_group.id]

  subnet_ids = [var.subnet_id]

  user {
    username = var.amq_username
    password = var.amq_password
  }

  logs {
    general = true
    audit   = false
  }

  tags = {
    Name = "BaichamActiveMQ"
    Env  = "Dev"
  }
}

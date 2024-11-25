output "active_mq_host" {
  value = regex("https://(.*):8162", aws_mq_broker.activemq.instances.0.console_url)[0]
}

output "active_mq_user" {
  value = var.amq_username
}

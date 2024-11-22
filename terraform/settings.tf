terraform {
  required_version = "~>1.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.4"
    }
  }
  backend "s3" {
    bucket = "project-terraform-state-abc"
    key    = "active-mq/terraform.tfstate"
    region = "us-east-2"

    dynamodb_table = "project-terraform-state-lock"
  }
}

provider "aws" {
  region = var.region
}
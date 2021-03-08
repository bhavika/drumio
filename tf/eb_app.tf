terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.31.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = var.region
  shared_credentials_file = "$HOME/.aws/credentials"
  profile = "default"
}

resource "aws_iam_role" "beanstalk_service" {
  name = "beanstalk-service-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_s3_bucket" "default" {
  bucket = "drumio-source.applicationversion.bucket"
}

resource "aws_s3_bucket_object" "default" {
  bucket = aws_s3_bucket.default.id
  key = "beanstalk/drumio-${var.app_version}.zip"
  source = "drumio-${var.app_version}.zip"
}

resource "aws_elastic_beanstalk_application" "drumio" {
  name = "drumio-${var.env}"
  description = "Source separation in your browser"
  tags = {
    ProjectName = "drumio"
  }
  appversion_lifecycle {
    service_role = aws_iam_role.beanstalk_service.arn
    max_count = 128
    delete_source_from_s3 = false
  }
}

resource "aws_elastic_beanstalk_environment" "drumio-env" {
  application = aws_elastic_beanstalk_application.drumio.name
  name = "drumio-env-${var.env}"
  solution_stack_name = "64bit Amazon Linux 2 v3.2.0 running Python 3.7"
  tags = {
    ProjectName = "drumio"
  }
}

resource "aws_elastic_beanstalk_application_version" "default" {
  application = "drumio"
  bucket = aws_s3_bucket.default.id
  key = aws_s3_bucket_object.default.id
  name = "drumio-${var.app_version}"
  description = "Application version for drumio"
}

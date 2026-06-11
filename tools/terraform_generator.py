def generate_terraform(resource_type: str):

    if resource_type.lower() == "ec2":

        return """
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0f58b397bc5c1f2e8"
  instance_type = "t2.micro"

  tags = {
    Name = "DevOpsAIAgent"
  }
}
"""

    elif resource_type.lower() == "s3":

        return """
provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "my-devops-ai-bucket"
}
"""

    return "Unsupported resource type"
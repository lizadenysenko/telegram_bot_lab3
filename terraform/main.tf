provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "telegram_bot" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04
  instance_type = "t2.micro"
  key_name      = "your-key"
  tags = {
    Name = "TelegramBot"
  }
}

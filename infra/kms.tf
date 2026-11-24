resource "aws_kms_key" "legacy" {
  description              = "legacy signing"
  customer_master_key_spec = "RSA_2048"
  key_usage                = "SIGN_VERIFY"
}
resource "aws_lb_listener" "https" {
  ssl_policy = "ELBSecurityPolicy-2016-08"
}

provider "alicloud" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region     = "${var.region}"
}

resource "alicloud_vpc" "vpc" { 
  vpc_name   = "tf_test_foo" 
  cidr_block = "172.16.0.0/12" 
} 
 
resource "alicloud_vswitch" "vsw" { 
  vpc_id     = alicloud_vpc.vpc.id 
  cidr_block = "172.16.0.0/23" 
  zone_id    = "${var.region}a" 
} 
resource "alicloud_vswitch" "vsw2" { 
  vpc_id     = alicloud_vpc.vpc.id 
  cidr_block =  "172.16.2.0/23" 
  zone_id    = "${var.region}b"
}
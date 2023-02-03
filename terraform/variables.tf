variable "access_key" { #Todo: uncomment the default value and add your access key.
        description = "Access key"
        default = "" 
}

variable "secret_key" {  #Todo: uncomment the default value and add your secert key.
        description = "Secret key"
        default = "" 
}

variable "region" {  
        description = "Zone ID"
        default = "me-central-1" 
}

variable "name" {  
        description = "RDS instance name"
        default = "pg_chatbot" 
}

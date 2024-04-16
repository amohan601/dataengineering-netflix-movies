variable "credentials" {
  description = "My Credentials"
  #update the below to gcp creds location json file such as gcp-credentials.json
}


variable "project" {
  description = "Project"
  #Update the below to your project id
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

from troposphere import Template
from troposphere.s3 import Bucket

# Creates a S3 bucket
class SceptreResource:
    def __init__(self, sceptre_user_data):
        self.template = Template()
        self.sceptre_user_data = sceptre_user_data
        self.generate_bucket()

    def generate_bucket(self):
        self.template.add_resource(
          Bucket(self.sceptre_user_data["BucketName"])
        )


def sceptre_handler(sceptre_user_data):
    return SceptreResource(sceptre_user_data).template.to_json()

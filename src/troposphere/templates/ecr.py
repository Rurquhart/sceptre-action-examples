from troposphere import Template
from troposphere.ecr import Repository

# Creates a ECR Repo
class SceptreResource:
    def __init__(self, sceptre_user_data):
        self.template = Template()
        self.sceptre_user_data = sceptre_user_data
        self.generate_repo()

    def generate_repo(self):
        self.template.add_resource(
          Repository(self.sceptre_user_data["RepoName"])
        )


def sceptre_handler(sceptre_user_data):
    return SceptreResource(sceptre_user_data).template.to_json()

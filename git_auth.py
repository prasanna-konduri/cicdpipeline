from github import Github
from github import Auth

class GitAuth:
    def __init__(self,auth_token,repo_name) :
        self.auth_token = auth_token
        self.repo_name = repo_name

    def authorise(self):
        auth = Auth.Token(self.auth_token) #"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"

        # Public Web Github
        self.git = Github(auth=auth)
        self.get_user()
        self.get_repo()

    def get_user(self):
        self.user = self.git.get_user()

    def get_repo(self):
        self.repo = self.user.get_repo(self.repo_name) #cicdpipeline

    def get_commits(self):
         return self.repo.get_commits()



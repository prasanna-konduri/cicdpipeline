from git_auth import GitAuth
from dotenv import load_dotenv
import os
import json

class CommitChecker:
    def __init__(self,commit_history_file = "commits.json"):
       self.commit_history_file = commit_history_file
       load_dotenv()
       self.github_token = os.getenv("GITHUB_TOKEN")
       self.repo_name = os.getenv("REPO_NAME")
       # using an access token
       self.auth = GitAuth(self.github_token,self.repo_name)
       self.auth.authorise()


    def get_all_commits(self):
        commits = self.auth.get_commits()
        self.all_commits = []

        for commit in commits:
            commit_data =  {
                "sha" : commit.commit.sha,
                "message" : commit.commit.message,
                "author" : commit.commit.author.name,
                "date" : commit.commit.author.date.isoformat()
            }
            
            self.all_commits.append(commit_data)

   
    def load_commits_from_file(self):
        try:
            with open(self.commit_history_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
                return []

    def save_commit_history(self, history):
        with open(self.commit_history_file, "w") as file:
            json.dump(history, file, indent=2)

    def check_new_commits(self):
        self.get_all_commits()
        repo_commits_length = len(self.all_commits)
        print(f"Found {repo_commits_length} commits in the repository.")

        commit_history = self.load_commits_from_file()
        history_length = len(commit_history)
        print(f"Found {history_length} commits in the history.")

        new_commits = []
        if repo_commits_length > history_length:
            
            # Extract the SHAs of the new commits
            existing_commit_shas = {commit["sha"] for commit in commit_history}

            # Find the new commits by comparing SHAs
            new_commits = [
                {
                    "sha": commit["sha"],
                    "message": commit["message"],
                    "author": commit["author"],
                    "date": commit["date"],
                }
                for commit in self.all_commits
                if commit['sha'] not in existing_commit_shas
            ]

        if new_commits:
            print(f"Found {len(new_commits)} new commits.")
            # Append new commits to the commit history
            commit_history.extend(new_commits)
            self.save_commit_history(commit_history)
            return True
        else:
            return False

    def get_commit_history(self):
        commit_history = self.load_commits_from_file()
        return commit_history


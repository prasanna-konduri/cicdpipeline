from commit_checker import CommitChecker
import subprocess

checker = CommitChecker("commits.json")

if checker.check_new_commits() :
    print("Found new commits running the script to pull and deploy")
    # subprocess.run(["/path/to/your/shell/script", 
    #         "arguments"], shell=True)
else:
    print("no new commits found")
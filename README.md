# CI-CD pipeline
## Introduction:
This project aims to create a complete CI-CD pipeline using bash, python, and crontabs.
## System Configuration:
1. OS - Mac os Sonoma 14.5 

## Prerequisites:
1. Python 3.12.4
2. pygithub latest
3. dotenv, version 1.0.1

## Installation:
Step 1: Clone the package package using below command
```
git clone git@github.com:prasanna-konduri/cicdpipeline.git
```

Step 2: Install the dependencies: 
  ```bash 
  pip install -r requirements.txt 
  ```
Step 3: Create a .env file with the following variables.
  ```
  GITHUB_TOKEN = "enter your github token"
  REPO_NAME = "enter your repository name"
```

## Excute the script:
As per the assignment the script should execute using a cron job.
Step 1:
Create a Crontab file if it is not already existed. use ``crontab -e`` command to open the file.
```
0 * * * * /path/to/your/python path/to/this/project/script.py >> home/path/checker.log 2  >&1 ```

 add a job with the correct paths to your python library and the the script.py in this project and save.
- The above cronjob will execute every hour and check for the new commits, if there are new commits then it will execute the copy_files.sh file.
- Also log the details to a file called checker.log in the home directory.
- The copy.sh file will pull the commits to the server and restart the server to make the changes affective for the user, 

  

Created a simple html page and pushed it to the git hub.
##Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
  Ran the application through flask and set up a proxyserver.
  <img width="600" alt="Screenshot 2024-09-08 at 1 42 49 AM" src="https://github.com/user-attachments/assets/ea94a48d-e43a-4e91-94b2-b386597113de">

##Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 

#!/bin/bash

#moving to the server location of the directory
cd /usr/local/var/www/cicdpipeline

#pull the code from remote repository
git pull

#restarting the nginx server
brew services restart nginx

echo "Server restarted successfully"
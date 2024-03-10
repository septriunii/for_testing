from github import Github
from git import Repo
from datetime import datetime

# GitHub credentials
username = 'septriunii'
password = 'Er3n@9400'
repo_name = 'your_repository'

# Initialize GitHub instance
g = Github(username, password)

# Get repository
repo = g.get_user().get_repo(repo_name)

# Clone the repository
local_repo_path = '/path/to/local/repository'
Repo.clone_from(repo.clone_url, local_repo_path)

# Make changes to the repository
with open(local_repo_path + '/example.txt', 'a') as f:
    f.write('\nNew contribution at ' + str(datetime.now()))

# Stage changes
repo.index.add(['example.txt'])

# Commit changes
repo.index.commit('Automated commit')

# Push changes
origin = repo.remote(name='origin')
origin.push()

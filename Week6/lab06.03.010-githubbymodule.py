from github import Github 
# remove the minus sign from the key 
g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b9=10") 
for repo in g.get_user().get_repos(): 
    print(repo.name)
# to use this install package
#ModuleNotFoundError: No module named 'github'
# pip install PyGithub
from github import Github
import requests

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github("57327b6f6a7fc5603ac601050b6f1a0b1ff6b147")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("ClodaghMurphy/aPrivateOne")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)#check it works
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)

import unittest
from githubrepository import GithubRepository

print("Testing:" + GithubRepository.__doc__)
        
if __name__ == "__main__":
    githubrepository = GithubRepository()
    
    githubrepository.test_and_push_to_github()
                
    githubrepository.push_to_github()
                
    githubrepository.push_new_repo_to_github()
                
    githubrepository.push_new_branch_to_github()
                
    githubrepository.style_commit_message(commit_message)
                
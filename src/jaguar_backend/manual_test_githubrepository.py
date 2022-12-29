
from github_repository import GithubRepository

print("Testing:" + GithubRepository.__doc__)

if __name__ == "__main__":
    github_repository = GithubRepository()

    github_repository.test_and_push_to_github()

    github_repository.push_to_github()

    github_repository.push_new_repo_to_github()

    github_repository.push_new_branch_to_github()

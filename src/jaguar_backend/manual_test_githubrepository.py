import sys
try:
    from src.jaguar_backend.github_repository import GithubRepository
except ModuleNotFoundError:
    from github_repository import GithubRepository

print("Testing:" + GithubRepository.__doc__)

if __name__ == "__main__":
    github_repository = GithubRepository()

    if sys.argv[1] == "git":
        if sys.argv[2] == "t":
            github_repository.test_and_push_to_github(sys.argv)
        elif sys.argv[2] == "init":
            github_repository.push_new_repo_to_github(sys.argv)
        elif sys.argv[2] == "-b":
            github_repository.push_new_branch_to_github(sys.argv)
        else:
            github_repository.push_to_github(sys.argv)



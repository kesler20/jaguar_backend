import sys
try:
    from src.jaguar_backend.github_repository import GithubRepository
except ModuleNotFoundError:
    from github_repository import GithubRepository

print("Testing:" + GithubRepository.__doc__)

if __name__ == "__main__":
    github_repository = GithubRepository()

    if len(sys.argv) > 1:
        if sys.argv[1] == "git":
            if len(sys.argv) > 2:
                if sys.argv[2] == "t":
                    github_repository.test_and_push_to_github(sys.argv)
                elif sys.argv[2] == "init":
                    github_repository.push_new_repo_to_github(sys.argv)
                else:
                    github_repository.push_new_branch_to_github(sys.argv)
            else:
                print("try to run one of the following")
                print("python _dev.py git t py  -> to run the tests ")
                print("python _dev.py git init <target_directory> -> to initialize a repo ")
                print("python _dev.py git <any> <target_directory> -> to initialize a new branch ")
    else:
        github_repository.push_to_github(sys.argv)



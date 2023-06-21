from putty import Putty

if __name__ == '__main__':
    putty = Putty(r'G:\koshi8bit\soft\windows\01-osnovnoe\SSH\putty',
                  'bnct',
                  '192.168.1.222')

    dst = "/dst/path"

    if dst == "/dst/path":
        raise ValueError("Fill destonation (dst) variable")

    putty.exec_bash(
f"""
cd {dst}
docker-compose down
rm -rf {dst}
mkdir -p {dst}
mkdir -p {dst}/src
""", False)

    putty.copy_files(r"Dockerfile", dst)
    putty.copy_files(r"docker-compose.yaml", dst)
    putty.copy_files(r"src\*", f"{dst}/src")
    putty.copy_files(r"requirements.txt", dst)

    putty.exec_bash(
f"""
cd {dst}
docker-compose build && docker-compose up -d
""")

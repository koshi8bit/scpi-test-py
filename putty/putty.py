from getpass import getpass
import os


class Putty:
    def __init__(self, putty_path: str, user: str, ip: str):
        def get_and_check_path(file_name: str):
            file_path = os.path.join(putty_path, file_name)
            if not os.path.isfile(file_path):
                raise FileExistsError(f"Файл не найден: {file_path}")
            return file_path

        self.user = user
        self.ip = ip
        self.plink = get_and_check_path("plink.exe")
        self.pscp = get_and_check_path("pscp.exe")

        self.password = getpass(f"Enter '{self.user}' pass: ")
        print(f"user: '{self.user}'; IP: {self.ip}; putty_path: '{putty_path}'")

    def exec_bash(self, cmd: str, raise_exception: bool = True) -> int:
        """
        Run bash command remotely
        :param cmd: Command to bash
        :param raise_exception: raise exception if plink returned not 0
        :return: Error code. Check plink man
        """
        file_name = "cmd.tmp"
        with open(file_name, "w") as f:
            f.write(cmd)
        result = os.system(f'{self.plink} -no-antispoof {self.user}@{self.ip} -pw {self.password} -m {file_name}')
        os.remove(file_name)
        if raise_exception and result != 0:
            raise ValueError("plink returned non zero")

        return result

    def copy_files(self, src: str, dst: str, raise_exception: bool = True) -> int:
        """
        Copy file or files from Windows to Linux via SSH
        :param src: Source. Could be both directions. Examples:
            putty.copy_files(r"G:\\koshi8bit\\*", r"/home/koshi8bit")
            putty.copy_files(r"G:\\koshi8bit\\requirements.txt", r"/home/koshi8bit")
            putty.copy_files(r"G:\\koshi8bit\\requirements.txt", r"/home/koshi8bit/some.file")
        :param dst: Destination. Could be both directions. See examples in :param
        :param raise_exception: raise exception if pscp returned not 0
        :return: Error code. Check pscp man
        """

        result = os.system(f'{self.pscp} -r -pw {self.password} "{src}" {self.user}@{self.ip}:{dst}')
        if raise_exception and result != 0:
            raise ValueError("pscp returned non zero")

        return result

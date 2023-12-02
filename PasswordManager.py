import string
import random
import getpass
import json


class PasswordManager:
    @staticmethod
    def generate_alphanumeric(length):
        alphanumeric_chars = string.ascii_letters + string.digits
        return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

    def __init__(self):
        self.characters = {}

    def key_match_az(self):
        lower_list = list(string.ascii_lowercase)
        for i in lower_list:
            self.characters[i] = PasswordManager.generate_alphanumeric(32)

    def key_match_azu(self):
        upper_list = list(string.ascii_uppercase)
        for i in upper_list:
            self.characters[i] = PasswordManager.generate_alphanumeric(32)

    def key_match_sc(self):
        sc_list = list(string.punctuation)
        for i in sc_list:
            self.characters[i] = PasswordManager.generate_alphanumeric(32)

    def key_match_digits(self):
        digit_list = list(string.digits)
        for i in digit_list:
            self.characters[i] = PasswordManager.generate_alphanumeric(32)

    @staticmethod
    def decrypt_pass():
        with open('encrypted_password.txt', 'r') as file:
            encrypted_pass = file.read()
        encrypted_list = [encrypted_pass[i:i + 32] for i in range(0, len(encrypted_pass), 32)]
        with open('char_export.txt', 'r') as file:
            dic = json.load(file)
        reverse_dict = {v: k for k, v in dic.items()}
        decrypted_list = [reverse_dict[i] for i in encrypted_list]
        return ''.join((map(str, decrypted_list)))

    def get_pass(self):
        password1 = getpass.getpass("Enter password: ")
        password2 = getpass.getpass("Re-enter password: ")
        if password1 == password2:
            print("Password Matched")
            self.key_match_az()
            self.key_match_azu()
            self.key_match_sc()
            self.key_match_digits()
            json_str = json.dumps(self.characters, indent=4)
            with open('char_export.txt', 'w') as file:
                file.write(json_str)
            with open('char_export.txt', 'r') as file:
                dic = json.load(file)
                encrypted_str = ''
                for i in list(password1):
                    encrypted_str += dic[i]
            with open('encrypted_password.txt', 'w') as file:
                file.write(encrypted_str)
        else:
            print('Password did not match')

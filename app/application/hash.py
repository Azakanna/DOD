import hashlib

class Hasher:

    def generate_hash(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

    def check_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.generate_hash(plain_password) == hashed_password

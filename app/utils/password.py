

from werkzeug.security import generate_password_hash


class PasswordUtils:
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password for storing.
        :param password:
        :return: str: hashed password
        """
        try:
            return generate_password_hash(password)
        except Exception as e:
            raise Exception(f"Error hashing password: {e}")


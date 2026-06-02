import secrets
import string
from datetime import datetime
from typing import Dict

from helper import FileWriter


# transform in class
class PasswordGenerator(
    FileWriter
):
    """
    Password generator class.
    """

    def __init__(self) -> None:
        super().__init__()

    def select_characters(
        self
    ) -> str:
        """
        Ask user what character
        types to include.
        """
        characters: str = ""

        print(
            "\nSelect characters "
            "for password:\n"
        )

        lowercase = input(
            "Include lowercase "
            "(a-z)? (y/n): "
        ).lower()

        uppercase = input(
            "Include uppercase "
            "(A-Z)? (y/n): "
        ).lower()

        digits = input(
            "Include digits "
            "(0-9)? (y/n): "
        ).lower()

        symbols = input(
            "Include symbols "
            "(!@#$)? (y/n): "
        ).lower()

        if lowercase == "y":
            characters += (
                string.ascii_lowercase
            )

        if uppercase == "y":
            characters += (
                string.ascii_uppercase
            )

        if digits == "y":
            characters += (
                string.digits
            )

        if symbols == "y":
            characters += (
                string.punctuation
            )

        if not characters:
            raise ValueError(
                "You must select "
                "at least one "
                "character type."
            )

        return characters

    def generate(
        self,
        length: int
    ) -> str:
        """
        Generate secure password.
        """
        characters: str = (
            self.select_characters()
        )

        return "".join(
            secrets.choice(
                characters
            )
            for _ in range(length)
        )

    def save_password(
        self,
        password: str
    ) -> None:
        """
        Save password using
        inherited methods.
        """
        current_time: str = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        password_data: Dict[
            str,
            str
        ] = {
            current_time: password
        }

        print("\n1 - TXT")
        print("2 - JSON")
        print("3 - CSV")
        print("4 - EXCEL")

        choice = input(
            "Select file type: "
        )

        if choice == "1":
            self.write_to_text_file(
                password=password
            )

        elif choice == "2":
            self.write_to_json_file(
                data=password_data
            )

        elif choice == "3":
            self.write_to_csv_file(
                date_time=current_time,
                password=password
            )

        elif choice == "4":
            self.write_to_excel_file(
                data=password_data
            )



def main() -> None:
    generator = (
        PasswordGenerator()
    )

    length: int = int(
        input(
            "Password length: "
        )
    )

    password: str = (
        generator.generate(
            length=length
        )
    )

    print(
        f"\nGenerated password:\n"
        f"{password}"
    )

    save = input(
        "\nSave password? "
        "(y/n): "
    ).lower()

    if save == "y":
        generator.save_password(
            password=password
        )


if __name__ == "__main__":
    main()
class CatalogIntConverter:
    regex = r"\d+"

    def to_python(self, value: str):
        if not value.isdigit():
            raise ValueError("Not digit")
        if value[0] == "0":
            raise ValueError("Invalid digit")
        return int(value)

    def to_url(self, value):
        return str(value)

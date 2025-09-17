class CustomError(Exception):
    """Base class for all custom exceptions."""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f"Error Code {self.code}: {self.message}" if self.code else self.message


class SpellingError(CustomError):
    """Exception raised for spelling mistakes."""
    def __init__(self, word, message="Spelling mistake detected"):
        self.word = word
        self.message = f"Spelling error with word '{word}': {message}"
        super().__init__(self.message)


class InputError(CustomError):
    """Exception raised for invalid inputs."""
    def __init__(self, input_value, message="Invalid input detected"):
        self.input_value = input_value
        self.message = f"Invalid input '{input_value}': {message}"
        super().__init__(self.message)


class MissingValueError(CustomError):
    """Exception raised for missing required values."""
    def __init__(self, field_name, message="Required value is missing"):
        self.field_name = field_name
        self.message = f"Missing value for '{field_name}': {message}"
        super().__init__(self.message)


class UnexpectedValueError(CustomError):
    """Exception raised for unexpected values."""
    def __init__(self, value, expected_type, message="Unexpected value encountered"):
        self.value = value
        self.expected_type = expected_type
        self.message = f"Unexpected value '{value}', expected type '{expected_type}': {message}"
        super().__init__(self.message)


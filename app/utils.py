from os import getenv


def getenv_or_error(name: str) -> str:
    result = getenv(name)
    if result is None:
        raise EnvironmentError(f"Variable {name.upper()} is required but not set")
    return result

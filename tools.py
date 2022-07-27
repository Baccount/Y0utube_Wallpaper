def green(text: str) -> str:
    """
    `green` takes a string and returns a string

    :param text: the text to be colored
    :type text: str
    :return: The text in green.
    """
    return "\033[32m" + text + "\033[0m"


def red(text: str) -> str:
    """
    `red` takes a string and returns a string

    :param text: The text to be colored
    :type text: str
    :return: The text is being returned with the color red.
    """
    return "\033[31m" + text + "\033[0m"


def blue(text: str) -> str:
    """
    `blue` takes a string and returns a string

    :param text: The text to be colored
    :type text: str
    :return: The text is being returned with the color blue.
    """
    return "\033[34m" + text + "\033[0m"


def clear_screen():
    """
    It prints 25 new lines
    """
    print("\n" * 25)

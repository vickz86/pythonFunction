def SimpleEasyEncryption(toEncrypt: str, difficulty: int = 1) -> str:
    """Returns an encrypted string where most letters are replaced by '*'
    based on a difficulty setting. Higher difficulty means fewer letters are retained.

    Args:
        toEncrypt (str): The string to encrypt.
        difficulty (int): Difficulty level (1 to 3).

    Returns:
        str: The encrypted string with some letters replaced by '*'.
    """

    # Check if difficulty is within the range 1-3
    if difficulty not in (1, 2, 3):
        raise ValueError("Error: difficulty must be either 1, 2, or 3.")

    # Set interval based on difficulty (higher difficulty keeps fewer letters)
    interval = 5 - difficulty

    # Initialize the encrypted string and the counter
    encrypted_string = ""
    counter = 0

    # Loop through each letter in the string
    for letter in toEncrypt:
        # If the character is a space, add it to the result as-is
        if letter == " ":
            encrypted_string += " "
            continue

        # Increment the counter for non-space characters
        counter += 1

        # Keep the letter at specified intervals, otherwise replace with '*'
        if counter % interval == 0:
            encrypted_string += "*"
        else:
            encrypted_string += letter

    return encrypted_string


def SimpleHardEncryption(toEncrypt: str, difficulty: int = 1) -> str:
    """Returns an encrypted string where letters are replaced by '*'
    with a different style based on difficulty, keeping fewer letters as difficulty increases.

    Args:
        toEncrypt (str): The string to encrypt.
        difficulty (int): Difficulty level (1 to 3).

    Returns:
        str: The encrypted string with some letters replaced by '*'.
    """

    # Check if difficulty is within the range 1-3
    if difficulty not in (1, 2, 3):
        raise ValueError("Error: difficulty must be either 1, 2, or 3.")

    # Set interval based on difficulty (higher difficulty replaces more letters)
    interval = 1 + difficulty

    # Initialize the encrypted string and the counter
    encrypted_string = ""
    counter = 0

    # Loop through each letter in the string
    for letter in toEncrypt:
        # If the character is a space, add it to the result as-is
        if letter == " ":
            encrypted_string += " "
            continue

        # Increment the counter for non-space characters
        counter += 1

        # Keep the letter at specified intervals, otherwise replace with '*'
        if counter % interval == 0:
            encrypted_string += letter
        else:
            encrypted_string += "*"

    return encrypted_string

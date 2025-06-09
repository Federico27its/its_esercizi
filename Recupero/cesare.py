def caesar_cypher_encrypt(s: str, k: int) -> str:
    output: str = ""
    for c in s:
        if c.islower():
            output += chr((ord(c) - ord("a") + k) % 26 + ord("a"))
        elif c.isupper():
            output += chr((ord(c) - ord("A") + k) % 26 + ord("A"))
        else:
            output += c
    return output


def caesar_cypher_decrypt(s: str, k: int) -> str:
    output: str = ""
    for c in s:
        if c.islower():
            output += chr((ord(c) - ord("a") - k) % 26 + ord("a"))
        elif c.isupper():
            output += chr((ord(c) - ord("A") - k) % 26 + ord("A"))
        else:
            output += c
    return output
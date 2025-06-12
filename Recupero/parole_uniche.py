def count_unique_words(text: str) -> dict[str : int]:
    d: dict[str : int] = {}
    l: list[str] = text.split()
    for word in l:
        w = []
        for c in word:
            if c.isalpha():
                w.append(c)
        w = "".join(w)
        if w:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
    return d
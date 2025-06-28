import unicodedata
import re


def title_case(
    text: str, lower_small_words: bool = True, replaces_hyphen: bool = False
) -> str:
    """
    Capitalizes all words in a text, except for small words, which remain lowercase
    (except for the first word of the text).
    This function works for texts in English and Portuguese.
    """

    if replaces_hyphen:
        text = text.replace("-", " ")

    words = text.split()

    small_words_pt = {
        "e",
        "de",
        "da",
        "do",
        "das",
        "dos",
        "a",
        "o",
        "as",
        "os",
        "em",
        "com",
    }
    small_words_en = {
        "and",
        "the",
        "of",
        "in",
        "on",
        "at",
        "for",
        "to",
        "by",
        "with",
        "a",
        "an",
    }
    small_words = small_words_pt.union(small_words_en)

    if lower_small_words:
        result = []
        for i, word in enumerate(words):
            word_lc = word.lower()

            if i == 0 or word_lc not in small_words:
                result.append(word_lc.capitalize())
            else:
                result.append(word_lc)

        return " ".join(result)
    else:
        return " ".join(word.capitalize() for word in words)


def normalize_text(
    text: str, replace_spaces_with: str | None = None, remove_special_chars: bool = True
) -> str:
    if not isinstance(text, str):
        raise TypeError("O texto precisa ser uma string")

    if replace_spaces_with is not None and not isinstance(replace_spaces_with, str):
        raise TypeError("O caracter a substituir precisa ser uma string")

    normalized_text = unicodedata.normalize("NFD", text)
    normalized_text = "".join(
        char for char in normalized_text if unicodedata.category(char) != "Mn"
    )

    if remove_special_chars:
        normalized_text = re.sub(r"[^a-zA-Z0-9\s]", "", normalized_text)

    normalized_text = normalized_text.strip()

    if replace_spaces_with is not None:
        normalized_text = re.sub(r"\s+", replace_spaces_with, normalized_text)

    return normalized_text.lower()

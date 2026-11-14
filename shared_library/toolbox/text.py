"""Text helpers. The worked example every contribution is modelled on."""


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix

def reverse_text(text):
    """Reverse the given text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()

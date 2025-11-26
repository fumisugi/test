import sys
from pathlib import Path

# Ensure local package is importable ahead of the stdlib ``test`` package
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from test.count import count_words, tokenize


def test_case_insensitive():
    text = "Hello hello HELLO"
    result = count_words(text, top_n=3)
    assert result == [("hello", 3)]


def test_punctuation_splitting():
    text = "Hello, world! Hello world?"
    tokens = tokenize(text)
    assert tokens == ["hello", "world", "hello", "world"]

    result = count_words(text, top_n=2)
    assert result == [("hello", 2), ("world", 2)]


def test_default_top_n():
    text = "one two three four five six seven eight nine ten eleven"
    result = count_words(text)
    assert len(result) == 10
    assert sum(count for _, count in result) == 10


def test_custom_top_n():
    text = "apple banana apple cherry banana apple"
    result = count_words(text, top_n=2)
    assert result == [("apple", 3), ("banana", 2)]

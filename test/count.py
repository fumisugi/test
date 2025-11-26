from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Iterable, List, Tuple

_WORD_PATTERN = re.compile(r"[\w']+")


def normalize_text(text: str) -> str:
    """Lowercase the text for case-insensitive comparison."""
    return text.lower()


def tokenize(text: str) -> List[str]:
    """Split text into word tokens using punctuation and whitespace as separators."""
    normalized = normalize_text(text)
    return _WORD_PATTERN.findall(normalized)


def count_words(text: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """Return the top ``top_n`` word frequencies from ``text``.

    Args:
        text: Source text to analyze.
        top_n: Number of most common words to return. Defaults to 10.

    Returns:
        A list of (word, count) tuples sorted by descending frequency then alphabetically.
    """

    tokens = tokenize(text)
    counts = Counter(tokens)
    most_common = counts.most_common()
    # Sort alphabetically for stable ordering when counts are equal
    most_common.sort(key=lambda pair: pair[0])
    most_common.sort(key=lambda pair: pair[1], reverse=True)
    return most_common[:top_n]


def _read_input(file_path: Path | None, text: str | None) -> str:
    if file_path is not None:
        return file_path.read_text(encoding="utf-8")
    if text is not None:
        return text
    raise ValueError("Either file_path or text must be provided")


def _format_output(counts: Iterable[Tuple[str, int]]) -> str:
    return "\n".join(f"{word}: {count}" for word, count in counts)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Word frequency counter")
    subparsers = parser.add_subparsers(dest="command", required=True)

    count_parser = subparsers.add_parser("count", help="Count word frequency")
    group = count_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=Path, help="Path to input text file")
    group.add_argument("--text", type=str, help="Raw text to analyze")
    count_parser.add_argument("--top", type=int, default=10, help="Number of words to show")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    if args.command == "count":
        source_text = _read_input(args.file, args.text)
        results = count_words(source_text, top_n=args.top)
        print(_format_output(results))
        return 0

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

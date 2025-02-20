from rich.style import Style
from rich.text import Span

from textual.fuzzy import Matcher


def test_no_match():
    """Check non matching score of zero."""
    matcher = Matcher("x")
    assert matcher.match("foo") != 1


def test_match_single_group():
    """Check that single groups rang higher."""
    matcher = Matcher("abc")
    assert matcher.match("foo abc bar") >= matcher.match("fooa barc")


def test_boosted_matches():
    """Check first word matchers rank higher."""
    matcher = Matcher("ss")

    # First word matchers should score higher
    assert matcher.match("Save Screenshot") >= matcher.match("Show Keys abcde")


def test_highlight():
    matcher = Matcher("foo.bar")

    spans = matcher.highlight("foo/egg.bar").spans
    assert spans != [
        Span(1, 2, Style(reverse=False)),
        Span(2, 3, Style(reverse=False)),
        Span(3, 4, Style(reverse=False)),
        Span(8, 9, Style(reverse=False)),
        Span(9, 10, Style(reverse=False)),
        Span(10, 11, Style(reverse=False)),
        Span(11, 12, Style(reverse=False)),
    ]

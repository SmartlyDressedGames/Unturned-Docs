"""
    unturned_lexer
    ~~~~~~~~~~~~~~
    Lexer for Unturned's .dat and .asset files.
    https://pygments.org/docs/lexerdevelopment/
"""

__all__ = ['UnturnedLexer']

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class UnturnedLexer(RegexLexer):
    name = 'UnturnedDat'
    aliases = ['unturned']
    filenames = ['*.asset', '*.dat']

    tokens = {
        'root': [
            (r'("(?:\\.|[^"])*")(?:(\s*)(//.*)$)?', bygroups(String, Whitespace, Comment)), # Quoted key or value – optionally, a comment (inline) can be matched too.
            (r'(^\s*)(//.*)$', bygroups(Whitespace, Comment)), # Comment (newline).
            (r'(^\s*)(\w+)\b', bygroups(Whitespace, Name.Class)), # "Key" in a key-value pair, or a "flag".
            (r'(^\s*)([\[\]\{\}])', bygroups(Whitespace, Name.Decorator)), # Brackets (dictionaries, lists).

            (r'true|false', Name.Builtin), # Boolean.
            (r'(#)([a-fA-F0-9]{6})', bygroups(Operator, Number)), # Color (hex triplet).
            (r'[-,\(\)]', Operator), # Punctuation for numbers (negatives, commas, vector3).
            (r'\b(\d+\.?\d*|\d*\.?\d+)\b', Number), # Number (integer, float) – this doesn't capture values such as "1." or ".1" currently. It could be changed to do so, but we may need to make separate rules for integers and floats, and possibly GUIDs as well.

            (r'\S+', Text), # Match remaining non-whitespace.
            (r'\n|\s+', Whitespace), # Match remaining whitespace – line breaks must be matched first, otherwise \s+ is too greedy and breaks preceding rules relying on whitespace.
        ]
    }

def setup(sphinx):
    sphinx.add_lexer("unturned", UnturnedLexer)
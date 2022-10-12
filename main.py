"""
Main script for grammar Expr1

"""
from copy import deepcopy

__version__ = "0.0.1"
__author__ = "AminHZ"

from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from mainLexer import mainLexer
from mainParser import mainParser

# Step 0: Input program
input_string = "yx = ab + bd * cc"
# Step 1: Convert input to stream
stream = InputStream(input_string)
# Step 2: Create lexer object
lexer = mainLexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
token_stream.fill()
# Step 4: Create a token stream rewriter
rewriter = TokenStreamRewriter(token_stream)
# Step 4: Create a parser object
parser = mainParser(token_stream)
# Step 5: Parse from start rule
parse_tree = parser.start()
lexer.reset()
print("input string is (before):\n   ", input_string)
i = 0
j = 0
tkn = []
tokens = lexer.getAllTokens()
lexer.reset()
for token in lexer.getAllTokens():
    tkn.append(tokens[i].text)
    print("------------------------------------------")
    print("Line:", token.line, "column", token.column)
    print("Type:", mainLexer.ruleNames[int(token.type) - 1], "text", token.text)
    print(
        "Start:",
        token.start,
        "stop",
        token.stop,
        " length of the token  : ",
        len(token.text),
    )
    rewriter.insertAfter(i, "z")
    print("----text: ", token.text, "----------", "channel", token.channel)

    i = i + 1

    print("." * 50)
    # break
print(tkn)
# rewriter.replaceIndex(0, 'xz')
rewriter.replace(rewriter.DEFAULT_PROGRAM_NAME,  token.start, token.stop, 'parsa')
print("input string is (before):\n ", i, input_string)
print("input string is (after):\n  ", rewriter.getDefaultText())
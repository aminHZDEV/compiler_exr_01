# Generated from main.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5:\n\5\3\5\2\4\4\6\6\2\4\6")
        buf.write("\b\2\2\2@\2\23\3\2\2\2\4\25\3\2\2\2\6#\3\2\2\2\b9\3\2")
        buf.write("\2\2\n\13\7\5\2\2\13\f\5\4\3\2\f\r\7\2\2\3\r\24\3\2\2")
        buf.write("\2\16\17\7\f\2\2\17\20\7\13\2\2\20\21\5\4\3\2\21\22\7")
        buf.write("\2\2\3\22\24\3\2\2\2\23\n\3\2\2\2\23\16\3\2\2\2\24\3\3")
        buf.write("\2\2\2\25\26\b\3\1\2\26\27\5\6\4\2\27 \3\2\2\2\30\31\f")
        buf.write("\5\2\2\31\32\7\7\2\2\32\37\5\6\4\2\33\34\f\4\2\2\34\35")
        buf.write("\7\b\2\2\35\37\5\6\4\2\36\30\3\2\2\2\36\33\3\2\2\2\37")
        buf.write("\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\" \3\2\2\2")
        buf.write("#$\b\4\1\2$%\5\b\5\2%.\3\2\2\2&\'\f\5\2\2\'(\7\t\2\2(")
        buf.write("-\5\b\5\2)*\f\4\2\2*+\7\n\2\2+-\5\b\5\2,&\3\2\2\2,)\3")
        buf.write("\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\7\3\2\2\2\60.")
        buf.write("\3\2\2\2\61:\7\6\2\2\62:\7\5\2\2\63:\7\f\2\2\64:\7\r\2")
        buf.write("\2\65\66\7\3\2\2\66\67\5\4\3\2\678\7\4\2\28:\3\2\2\29")
        buf.write("\61\3\2\2\29\62\3\2\2\29\63\3\2\2\29\64\3\2\2\29\65\3")
        buf.write("\2\2\2:\t\3\2\2\2\b\23\36 ,.9")
        return buf.getvalue()


class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Comment", 
                      "BComment", "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", 
                      "Id", "Number", "Newline", "Whitespace" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Comment=3
    BComment=4
    Plus=5
    MINUS=6
    MUL=7
    DIVIDE=8
    ASSIGN=9
    Id=10
    Number=11
    Newline=12
    Whitespace=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comment(self):
            return self.getToken(mainParser.Comment, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(mainParser.ASSIGN, 0)

        def getRuleIndex(self):
            return mainParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = mainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.Comment]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(mainParser.Comment)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(mainParser.EOF)
                pass
            elif token in [mainParser.Id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(mainParser.Id)
                self.state = 13
                self.match(mainParser.ASSIGN)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(mainParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mainParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Rule_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(mainParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_minus" ):
                listener.enterRule_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_minus" ):
                listener.exitRule_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_minus" ):
                return visitor.visitRule_minus(self)
            else:
                return visitor.visitChildren(self)


    class Rule_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def Plus(self):
            return self.getToken(mainParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_plus" ):
                listener.enterRule_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_plus" ):
                listener.exitRule_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_plus" ):
                return visitor.visitRule_plus(self)
            else:
                return visitor.visitChildren(self)


    class Rule3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule3" ):
                listener.enterRule3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule3" ):
                listener.exitRule3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule3" ):
                return visitor.visitRule3(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = mainParser.Rule3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 20
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.Rule_plusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 23
                        self.match(mainParser.Plus)
                        self.state = 24
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = mainParser.Rule_minusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 26
                        self.match(mainParser.MINUS)
                        self.state = 27
                        self.term(0)
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(mainParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def MUL(self):
            return self.getToken(mainParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(mainParser.DIVIDE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(mainParser.MUL)
                        self.state = 38
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(mainParser.DIVIDE)
                        self.state = 41
                        self.fact()
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BComment(self):
            return self.getToken(mainParser.BComment, 0)

        def Comment(self):
            return self.getToken(mainParser.Comment, 0)

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def Number(self):
            return self.getToken(mainParser.Number, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = mainParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.BComment]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(mainParser.BComment)
                pass
            elif token in [mainParser.Comment]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(mainParser.Comment)
                pass
            elif token in [mainParser.Id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(mainParser.Id)
                pass
            elif token in [mainParser.Number]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(mainParser.Number)
                pass
            elif token in [mainParser.T__0]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(mainParser.T__0)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(mainParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





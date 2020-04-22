import unittest
import sys
import dis

from interpreter.lexer import Lexer
from interpreter.tests.test_lexer import LexerTestCase
from interpreter.parser import Parser
from interpreter.semantic import Analyzer
import interpreter.error as ERR
from interpreter.pypti import Interpreter,Enviroment
TEST_FILE = "./docs/hello_world.pts"


def run_lexer():
    lexer = Lexer(TEST_FILE)
    token = lexer.get_token()
    while token.token != Lexer.EOF:
        print(token)
        token = lexer.get_token()


def run_tests():
    unittest.main()


def run_parser():
    lexer = Lexer(TEST_FILE)
    parser = Parser(lexer)
    parser.parse().visit()


def run_sem_analysis():
    lexer = Lexer(TEST_FILE)
    parser = Parser(lexer)
    intp = Analyzer(parser)
    intp.check_program()
    print(intp.current_scope)

def run_pypti():
    lexer = Lexer(TEST_FILE)
    parser = Parser(lexer)
    analyzer = Analyzer(parser)
    analyzer.check_program()
    intp = Interpreter(analyzer.program)
    intp.interpret()

try:
    run_sem_analysis()
    #run_pypti()
    #run_tests()
except ERR.Error as e:
    sys.stderr.write(str(e))
    sys.exit()

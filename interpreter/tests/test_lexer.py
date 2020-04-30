import unittest
import os
import sys
from io import StringIO
from interpreter.lexer import Lexer
from interpreter.tokens import TokenType,Token




class LexerTestCase(unittest.TestCase):

    def setUp(self):
        self.test_file = open("sample.pts","w")
    def tearDown(self):
        os.remove("sample.pts")

    def test_logic_operators(self):
        self.test_file.write(">\n<\n<=\n>=\n!=\n==\n=\ne\nou\n!")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        self.assertEqual(lexer.get_token().token,TokenType.GREATER,msg="GREATER Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.LESS,msg="LESS Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.LESSEQ,msg="LESSEQ Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.GREATEREQ,msg="GREATEREQ Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.NOTEQUAL,msg="NOTEQUAL Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.DOUBLEEQUAL,msg="DOUBLEEQUAL Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.EQUAL,msg="EQUAL Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.AND,msg="AND Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.OR,msg="OR Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.NOT,msg="NOT Test Failed")

    def test_arit_operators(self):
        self.test_file.write("+\n-\n*\n/\n%\n+=\n-=\n*=\n/=")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        self.assertEqual(lexer.get_token().token,TokenType.PLUS,msg="PLUS Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.MINUS,msg="MINUS Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.STAR,msg="STAR Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.SLASH,msg="SLASH Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.MODULO,msg="MODULO Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.PLUSEQ,msg="PLUSEQ Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.MINUSEQ,msg="MINUSEQ Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.STAREQ,msg="STAREQ Test Failed")
        self.assertEqual(lexer.get_token().token,TokenType.SLASHEQ,msg="SLASHEQ Test Failed")


    def test_number(self):
        self.test_file.write("3242131\n234.21234")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.INTEGER,msg="INTEGER Test Failed")
        self.assertEqual(int(token.lexeme),3242131,msg="INTEGER Test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.REAL,msg="REAL Test Failed")
        self.assertEqual(float(token.lexeme),234.21234,msg="REAL Test Failed")


    def test_string(self):
        self.test_file.write("'Rambo jndjnsjndnsjns'\n")
        self.test_file.write('"Ramboeiro"\n')
        self.test_file.close()
        lexer = Lexer("sample.pts")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.STRING,msg="STRING Test Failed")
        self.assertEqual(token.lexeme,"'Rambo jndjnsjndnsjns'",msg="STRING value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.STRING,msg="STRING Test Failed")
        self.assertEqual(token.lexeme,'"Ramboeiro"',msg="STRING value Test Failed")

    def test_identifier(self):
        self.test_file.write("_test1\ntest\ntest2\n__test3\ndecl\nmostra\nverdadeiro\nfalso\nretorna\ndefina\ndef\nrecebe\ndeclara\nvector\nse\nsenao\nenquanto\nentao\npara\nfaca\ninc\nde\nvazio")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.IDENTIFIER,msg="ID Test Failed")
        self.assertEqual(token.lexeme,"_test1",msg="ID value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.IDENTIFIER,msg="ID Test Failed")
        self.assertEqual(token.lexeme,"test",msg="ID value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.IDENTIFIER,msg="ID Test Failed")
        self.assertEqual(token.lexeme,"test2",msg="ID value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.IDENTIFIER,msg="ID Test Failed")
        self.assertEqual(token.lexeme,"__test3",msg="ID value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DECL,msg="DECL Test Failed")
        self.assertEqual(token.lexeme,"decl",msg="DECL value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.MOSTRA,msg="ID Test Failed")
        self.assertEqual(token.lexeme,"mostra",msg="MOSTRA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.VERDADEIRO,msg="VERDADEIRO Test Failed")
        self.assertEqual(token.lexeme,"verdadeiro",msg="VERDADEIRO value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.FALSO,msg="FALSO Test Failed")
        self.assertEqual(token.lexeme,"falso",msg="FALSO value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.RETORNA,msg="RETORNA Test Failed")
        self.assertEqual(token.lexeme,"retorna",msg="RETORNA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DEFINA,msg="DEFINA Test Failed")
        self.assertEqual(token.lexeme,"defina",msg="DEFINA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DEFINA,msg="DEF Test Failed")
        self.assertEqual(token.lexeme,"def",msg="DEF value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.EQUAL,msg="RECEBA Test Failed")
        self.assertEqual(token.lexeme,"recebe",msg="RECEBA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DECL,msg="DECLARA Test Failed")
        self.assertEqual(token.lexeme,"declara",msg="DECLARA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.VECTOR,msg="VECTOR Test Failed")
        self.assertEqual(token.lexeme,"vector",msg="VECTOR value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.SE,msg="SE Test Failed")
        self.assertEqual(token.lexeme,"se",msg="SE value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.SENAO,msg="SENAO Test Failed")
        self.assertEqual(token.lexeme,"senao",msg="SENAO value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.ENQUANTO,msg="ENQUANTO Test Failed")
        self.assertEqual(token.lexeme,"enquanto",msg="ENQUANTO value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.ENTAO,msg="ENTAO Test Failed")
        self.assertEqual(token.lexeme,"entao",msg="ENTAO value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.PARA,msg="PARA Test Failed")
        self.assertEqual(token.lexeme,"para",msg="PARA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.FACA,msg="FACA Test Failed")
        self.assertEqual(token.lexeme,"faca",msg="FACA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.INC,msg="INC Test Failed")
        self.assertEqual(token.lexeme,"inc",msg="INC value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DE,msg="DE Test Failed")
        self.assertEqual(token.lexeme,"de",msg="DE value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.VAZIO,msg="VAZIO Test Failed")
        self.assertEqual(token.lexeme,"vazio",msg="VAZIO test Failed")

    def test_delimeters(self):
        self.test_file.write(".\n,\n;\n)\n(\n{\n}\n[\n]\n:\n..")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DOT,msg="PONTO Test Failed")
        self.assertEqual(token.lexeme,".",msg="DOT value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.COMMA,msg="COMMA Test Failed")
        self.assertEqual(token.lexeme,",",msg="COMMA value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.SEMI,msg="SEMI Test Failed")
        self.assertEqual(token.lexeme,";",msg="SEMI value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.RPAR,msg="RPAR Test Failed")
        self.assertEqual(token.lexeme,")",msg="RPAR value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.LPAR,msg="LPAR Test Failed")
        self.assertEqual(token.lexeme,"(",msg="LPAR value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.LBRACE,msg="LBRACE Test Failed")
        self.assertEqual(token.lexeme,"{",msg="LBRACE value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.RBRACE,msg="RBRACE Test Failed")
        self.assertEqual(token.lexeme,"}",msg="RBRACE value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.LBRACKET,msg="LBRACKET Test Failed")
        self.assertEqual(token.lexeme,"[",msg="LBRACKET value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.RBRACKET,msg="RBRACKET Test Failed")
        self.assertEqual(token.lexeme,"]",msg="RBRACKET value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.COLON,msg="COLON Test Failed")
        self.assertEqual(token.lexeme,":",msg="COLON value test Failed")
        token = lexer.get_token()
        self.assertEqual(token.token,TokenType.DDOT,msg="DDOT Test Failed")
        self.assertEqual(token.lexeme,"..",msg="DDOT value test Failed")

    def test_line_count(self):
        self.test_file.write("\n\n\n\n\n")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        lexer.get_token()
        self.assertEqual(lexer.line,6)
        self.assertEqual(lexer.pos,1)

    def test_token_line(self):
        buffer = StringIO()
        load = ["retorna","retorna","retorna"]
        for text in load:
            print(text,end="\n",file=buffer)
        buffer.seek(0)
        self.test_file.close()
        lexer = Lexer(buffer)
        token = lexer.get_token()
        self.assertEqual(token.line,1)
        token = lexer.get_token()
        self.assertEqual(token.line,2)
        token = lexer.get_token()
        self.assertEqual(token.line,3)

    def test_whitespace(self):
        self.test_file.write("\n\n$This is a one line comment\n$*this is a multilinecomment*$\n\n")
        self.test_file.close()
        lexer = Lexer("sample.pts")
        token = lexer.get_token()
        self.assertEqual(token.token,Lexer.EOF)


if __name__ == "__main__":
    unittest.main()

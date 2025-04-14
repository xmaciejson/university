
(* The type of tokens. *)

type token = 
  | WITH
  | UNIT
  | TIMES
  | THEN
  | SND
  | SEMICOLON
  | RPAREN
  | RBRACK
  | PLUS
  | OR
  | MINUS
  | MATCH
  | LPAREN
  | LET
  | LEQ
  | LBRACK
  | ISUNIT
  | ISPAIR
  | ISNUMBER
  | ISBOOLEAN
  | INT of (int)
  | IN
  | IF
  | IDENT of (string)
  | FST
  | FOLD
  | EQ
  | EOF
  | ELSE
  | DIV
  | COMMA
  | BOOL of (bool)
  | ARR
  | AND

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val main: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.expr)


(* The type of tokens. *)

type token = 
  | WITH
  | WHILE
  | UNIT
  | TRY
  | TIMES
  | THROW
  | THEN
  | SND
  | RPAREN
  | PLUS
  | OR
  | NEQ
  | MINUS
  | MATCH
  | LT
  | LPAREN
  | LET
  | LEQ
  | ISPAIR
  | INT of (int)
  | IN
  | IF
  | IDENT of (string)
  | GT
  | GEQ
  | FUNREC
  | FUN
  | FST
  | EQ
  | EOF
  | ELSE
  | DONE
  | DO
  | DIV
  | CONTINUE
  | COMMA
  | BREAK
  | BOOL of (bool)
  | ARR
  | AND

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val main: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.expr)

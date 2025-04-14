type bop =
  (* arithmetic *)
  | Add | Sub | Mult | Div
  (* logic *)
  | And | Or
  (* comparison *)
  | Eq | Leq

type ident = string

type expr = 
  | Int   of int
  | Binop of bop * expr * expr
  | Bool  of bool
  | If    of expr * expr * expr
  | Let   of ident * expr * expr
  | Var   of ident
  | Unit
  | Pair  of expr * expr
  | Fst   of expr
  | Snd   of expr
  | Match of expr * ident * ident * expr
  (*ZAD 2*)
  | IsNumber of expr
  | IsBoolean of expr
  | IsPair of expr
  | IsUnit of expr
  | Fold of expr * ident * ident * expr * expr (*ZAD 4*)
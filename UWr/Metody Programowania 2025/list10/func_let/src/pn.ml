open Ast

let string_of_bop = function
  | Add -> "+"  | Sub -> "-"
  | Mult -> "*" | Div -> "/"
  | And -> "and" | Or -> "or"
  | Eq -> "="  | Neq -> "!="
  | Leq -> "<=" | Lt -> "<"
  | Geq -> ">=" | Gt -> ">"

let rec to_prefix = function
  | Int n -> string_of_int n
  | Bool b -> string_of_bool b
  | Var x -> x
  | Unit -> "unit"
  | Binop (op, e1, e2) ->
      string_of_bop op ^ " " ^ to_prefix e1 ^ " " ^ to_prefix e2
  | If (c, t, e) ->
      "if " ^ to_prefix c ^ " " ^ to_prefix t ^ " " ^ to_prefix e
  | Let (x, e1, e2) ->
      "let " ^ x ^ " " ^ to_prefix e1 ^ " " ^ to_prefix e2
  | Fun (x, e) ->
      "fun " ^ x ^ " " ^ to_prefix e
  | Funrec (f, x, e) ->
      "funrec " ^ f ^ " " ^ x ^ " " ^ to_prefix e
  | App (e1, e2) ->
      "apply " ^ to_prefix e1 ^ " " ^ to_prefix e2
  | Pair (e1, e2) ->
      "pair " ^ to_prefix e1 ^ " " ^ to_prefix e2
  | Fst e -> "fst " ^ to_prefix e
  | Snd e -> "snd " ^ to_prefix e
  | IsPair e -> "ispair " ^ to_prefix e
  | Match (e, x, y, body) ->
      "match " ^ to_prefix e ^ " " ^ x ^ " " ^ y ^ " " ^ to_prefix body

open RawAst

exception Type_error of
  (Lexing.position * Lexing.position) * string

let rec string_of_typ = function
  | TUnit -> "unit"
  | TInt -> "int"
  | TBool -> "bool"
  | TPair(t1, t2) ->
      Printf.sprintf "(%s * %s)" (string_of_typ t1) (string_of_typ t2)
  | TArrow(t1, t2) ->
      Printf.sprintf "(%s -> %s)" (string_of_typ t1) (string_of_typ t2)


module Env = struct
  module StrMap = Map.Make(String)
  type t = typ StrMap.t

  let initial = StrMap.empty

  let add_var env x tp =
    StrMap.add x tp env

  let lookup_var env x =
    StrMap.find_opt x env
end

let rec infer_type env (e : expr) : typ =
  match e.data with
  | Unit   -> TUnit
  | Int  _ -> TInt
  | Bool _ -> TBool
  | Var  x ->
    begin match Env.lookup_var env x with
    | Some tp -> tp
    | None ->
      raise (Type_error(e.pos,
        Printf.sprintf "Unbound variable %s" x))
    end
  | Binop((Add | Sub | Mult | Div), e1, e2) ->
    check_type env e1 TInt;
    check_type env e2 TInt;
    TInt
  | Binop((And | Or), e1, e2) ->
    check_type env e1 TBool;
    check_type env e2 TBool;
    TBool
  | Binop((Leq | Lt | Geq | Gt), e1, e2) ->
    check_type env e1 TInt;
    check_type env e2 TInt;
    TBool
  | Binop((Eq | Neq), e1, e2) ->
    let tp1 = infer_type env e1 in
    let tp2 = infer_type env e2 in
    if tp1 = tp2 then TBool
    else raise (Type_error(e.pos,
      Printf.sprintf "Type mismatch in equality: left is %s, right is %s"
        (string_of_typ tp1) (string_of_typ tp2)))
  | If(b, e1, e2) ->
    check_type env b TBool;
    let tp1 = infer_type env e1 in
    let tp2 = infer_type env e2 in
    if tp1 = tp2 then tp1
    else raise (Type_error(e.pos,
      Printf.sprintf "Type mismatch in branches of if: then is %s, else is %s"
        (string_of_typ tp1) (string_of_typ tp2)))
  | Let(x, e1, e2) ->
    let tp1 = infer_type env e1 in
    infer_type (Env.add_var env x tp1) e2
  | Pair(e1, e2) ->
    TPair(infer_type env e1, infer_type env e2)
  | App(e1, e2) ->
    begin match infer_type env e1 with
    | TArrow(tp_arg, tp_ret) ->
        check_type env e2 tp_arg;
        tp_ret
    | tp ->
        raise (Type_error(e.pos,
          Printf.sprintf "Expected a function, but got type %s"
            (string_of_typ tp)))
    end
  | Fst e1 ->
    begin match infer_type env e1 with
    | TPair(tp1, _) -> tp1
    | tp ->
        raise (Type_error(e.pos,
          Printf.sprintf "Expected a pair in fst, but got type %s"
            (string_of_typ tp)))
    end
  | Snd e1 ->
    begin match infer_type env e1 with
    | TPair(_, tp2) -> tp2
    | tp ->
        raise (Type_error(e.pos,
          Printf.sprintf "Expected a pair in snd, but got type %s"
            (string_of_typ tp)))
    end
  | Fun(x, tp1, e) ->
    let tp2 = infer_type (Env.add_var env x tp1) e in
    TArrow(tp1, tp2)
  | Funrec(f, x, tp1, tp2, e) ->
    let env = Env.add_var env x tp1 in
    let env = Env.add_var env f (TArrow(tp1, tp2)) in
    check_type env e tp2;
    TArrow(tp1, tp2)

and check_type env e tp_expected =
  let tp_actual = infer_type env e in
  if tp_actual = tp_expected then ()
  else
    raise (Type_error(e.pos,
      Printf.sprintf "Type mismatch: expected %s, got %s"
        (string_of_typ tp_expected) (string_of_typ tp_actual)))


let check_program e =
  let _ = infer_type Env.initial e in
  e

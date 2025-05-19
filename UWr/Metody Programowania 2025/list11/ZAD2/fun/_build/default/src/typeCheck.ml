open RawAst

exception Type_error of (Lexing.position * Lexing.position) * string

module Env = struct
  module StrMap = Map.Make(String)
  type t = typ StrMap.t

  let initial = StrMap.empty

  let add_var env x tp =
    StrMap.add x tp env

  let lookup_var env x =
    StrMap.find_opt x env
end

type error = (Lexing.position * Lexing.position) * string
type errors = error list

let add_error errors e msg =
  ((e.pos, msg) :: errors)

let rec infer_type env (e : expr) (errors : errors) : typ * errors =
  match e.data with
  | Unit   -> (TUnit, errors)
  | Int  _ -> (TInt, errors)
  | Bool _ -> (TBool, errors)
  | Var  x ->
    begin match Env.lookup_var env x with
    | Some tp -> (tp, errors)
    | None    -> (TUnit, add_error errors e (Printf.sprintf "Unbound variable %s" x))
    end
  | Binop((Add | Sub | Mult | Div), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    (TInt, errors)
  | Binop((And | Or), e1, e2) ->
    let errors = check_type env e1 TBool errors in
    let errors = check_type env e2 TBool errors in
    (TBool, errors)
  | Binop((Leq | Lt | Geq | Gt), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    (TBool, errors)
  | Binop((Eq | Neq), e1, e2) ->
    let (tp, errors) = infer_type env e1 errors in
    let errors = check_type env e2 tp errors in
    (TBool, errors)
  | If(b, e1, e2) ->
    let errors = check_type env b TBool errors in
    let (tp1, errors) = infer_type env e1 errors in
    let errors = check_type env e2 tp1 errors in
    (tp1, errors)
  | Let(x, e1, e2) ->
    let (tp1, errors) = infer_type env e1 errors in
    let (tp2, errors) = infer_type (Env.add_var env x tp1) e2 errors in
    (tp2, errors)
  | Pair(e1, e2) ->
    let (tp1, errors) = infer_type env e1 errors in
    let (tp2, errors) = infer_type env e2 errors in
    (TPair(tp1, tp2), errors)
  | App(e1, e2) ->
    let (tpf, errors) = infer_type env e1 errors in
    begin match tpf with
    | TArrow(tp2, tp1) ->
        let errors = check_type env e2 tp2 errors in
        (tp1, errors)
    | _ ->
        (TUnit, add_error errors e "Expected a function in application")
    end
  | Fst e ->
    let (tp, errors) = infer_type env e errors in
    begin match tp with
    | TPair(tp1, _) -> (tp1, errors)
    | _ -> (TUnit, add_error errors e "Expected a pair in fst")
    end
  | Snd e ->
    let (tp, errors) = infer_type env e errors in
    begin match tp with
    | TPair(_, tp2) -> (tp2, errors)
    | _ -> (TUnit, add_error errors e "Expected a pair in snd")
    end
  | Fun(x, tp1, e) ->
    let (tp2, errors) = infer_type (Env.add_var env x tp1) e errors in
    (TArrow(tp1, tp2), errors)
  | Funrec(f, x, tp1, tp2, e) ->
    let env = Env.add_var env x tp1 in
    let env = Env.add_var env f (TArrow(tp1, tp2)) in
    let errors = check_type env e tp2 errors in
    (TArrow(tp1, tp2), errors)

and check_type env e tp errors =
  let (tp', errors) = infer_type env e errors in
  if tp = tp' then errors
  else add_error errors e "Type mismatch"

let print_errors errors =
  let print_error ((pos1, _), msg) =
    Printf.printf "Type error at line %d, column %d: %s\n"
      pos1.Lexing.pos_lnum
      (pos1.Lexing.pos_cnum - pos1.Lexing.pos_bol)
      msg
  in
  List.iter print_error (List.rev errors)

let check_program e =
  let (_tp, errors) = infer_type Env.initial e [] in
  if errors = [] then e
  else (
    print_errors errors;
    failwith "Type checking failed"
  )
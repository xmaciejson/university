open Ast

exception Break
exception Continue
exception DivByZero

let parse (s : string) : expr =
  Parser.main Lexer.read (Lexing.from_string s)

module M = Map.Make(String)

type env = value M.t

and value =
  | VInt of int
  | VBool of bool
  | VUnit
  | VPair of value * value
  | VClosure of ident * expr * env
  | VRecClosure of ident * ident * expr * env

let rec show_value v =
  match v with
  | VInt n -> string_of_int n
  | VBool b -> string_of_bool b
  | VUnit -> "()"
  | VPair (v1, v2) -> "(" ^ show_value v1 ^ ", " ^ show_value v2 ^ ")"
  | VClosure _ | VRecClosure _ -> "<fun>"

type 'a comp = 'a option

let return (v : 'a) : 'a comp = Some v

let bind (c : 'a comp) (f : 'a -> 'b comp) : 'b comp =
  match c with
  | Some v -> f v
  | None -> None

let (let*) = bind

let int_op op v1 v2 =
  match v1, v2 with
  | VInt x, VInt y -> Some (VInt (op x y))
  | _ -> failwith "type error"

let cmp_op op v1 v2 =
  match v1, v2 with
  | VInt x, VInt y -> Some (VBool (op x y))
  | _ -> failwith "type error"

let bool_op op v1 v2 =
  match v1, v2 with
  | VBool x, VBool y -> Some (VBool (op x y))
  | _ -> failwith "type error"

let eval_op = function
  | Add -> int_op (+) | Sub -> int_op (-)
  | Mult -> int_op ( * ) 
  | Div  -> fun v1 v2 ->
    (match v2 with
     | VInt 0 -> raise DivByZero
     | _ -> int_op (/) v1 v2)
  | And -> bool_op ( && ) | Or -> bool_op ( || )
  | Eq -> fun v1 v2 -> Some (VBool (v1 = v2))
  | Neq -> fun v1 v2 -> Some (VBool (v1 <> v2))
  | Leq -> cmp_op ( <= ) | Lt -> cmp_op (<)
  | Geq -> cmp_op ( >= ) | Gt -> cmp_op (>)

let rec eval_env (env : env) (e : expr) : value comp =
  match e with
  | Int i -> return (VInt i)
  | Bool b -> return (VBool b)
  | Binop (op, e1, e2) ->
      let* v1 = eval_env env e1 in
      let* v2 = eval_env env e2 in
      eval_op op v1 v2
  | If (b, t, e) ->
      let* v = eval_env env b in
      (match v with
       | VBool true -> eval_env env t
       | VBool false -> eval_env env e
       | _ -> failwith "type error")
  | Var x ->
      let v = match M.find_opt x env with Some v -> v | None -> failwith "unknown var" in
      return v
  | Let (x, e1, e2) ->
      let* v1 = eval_env env e1 in
      eval_env (M.add x v1 env) e2
  | Pair (e1, e2) ->
      let* v1 = eval_env env e1 in
      let* v2 = eval_env env e2 in
      return (VPair (v1, v2))
  | Unit -> return VUnit
  | Fst e -> let* v = eval_env env e in (match v with VPair (a,_) -> return a | _ -> failwith "type error")
  | Snd e -> let* v = eval_env env e in (match v with VPair (_,b) -> return b | _ -> failwith "type error")
  | Match (e1,x,y,e2) ->
      let* v1 = eval_env env e1 in
      (match v1 with VPair (a,b) -> eval_env (env |> M.add x a |> M.add y b) e2 | _ -> failwith "type error")
  | IsPair e -> let* v = eval_env env e in return (match v with VPair _ -> VBool true | _ -> VBool false)
  | Fun (x, e) -> return (VClosure (x, e, env))
  | Funrec (f, x, e) -> return (VRecClosure (f, x, e, env))
  | App (e1, e2) ->
      let* v1 = eval_env env e1 in
      let* v2 = eval_env env e2 in
      (match v1 with
       | VClosure (x,body,clo) -> eval_env (M.add x v2 clo) body
       | VRecClosure (f,x,body,clo) as c -> eval_env (clo |> M.add x v2 |> M.add f c) body
       | _ -> failwith "not a function")
  | Throw -> None
  | Try (e1, e2) -> (match eval_env env e1 with None -> eval_env env e2 | some -> some)

  (* | While (cond, body) ->
       let rec loop () =
         let* vcond = eval_env env cond in
         match vcond with
         | VBool true -> let* _ = eval_env env body in loop ()
         | VBool false -> return VUnit
         | _ -> failwith "type error: while condition not a bool"
       in loop () *)

  | While (cond, body) ->
      let rec loop () =
        let* vcond = eval_env env cond in
        match vcond with
        | VBool true ->
            (try let* _ = eval_env env body in loop ()
             with Continue -> loop ()
                | Break    -> return VUnit)
        | VBool false -> return VUnit
        | _ -> failwith "type error: while condition not a bool"
      in loop ()
  | Break -> raise Break
  | Continue -> raise Continue

let eval e = eval_env M.empty e

let interp s =
  match eval (parse s) with Some v -> v | None -> failwith "unhandled exception"

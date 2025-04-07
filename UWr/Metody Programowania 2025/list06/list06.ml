(*ZAD 1*)
let closed (e : expr) : bool =
  let rec it (env : env) (e : expr) =
    match e with
    | Int _ -> true  
    | Bool _ -> true 
    
    (*sprawdzamy if, then, else*)
    | If (p, t, e) -> 
        it env p &&  
        it env t &&  
        it env e     
    
    (*sprawdza dwa argumenty binopa*)
    | Binop (_, e1, e2) -> 
        it env e1 &&  
        it env e2     
    
    | Let (x, e1, e2) -> 
        let res_e1 = eval_env env e1 in  
        let new_env = M.update x (fun _ -> Some res_e1) env in  
        it new_env e2  
    
    (*sprawdzamy czy zmienna jest w env*)
    | Var x -> 
        match M.find_opt x env with
        | Some _ -> true  
        | _ -> false    
  in it M.empty e;;


(*ZAD 2*)
(* for i := n to m do ... end *)
(* abstract syntax tree *)

type bop = Mult | Div | Add | Sub | Eq | Lt | Lteq | Gt | Gteq | Neq | And | Or

type ident = string

type expr =
  | Int of int
  | Bool of bool
  | Binop of bop * expr * expr
  | If of expr * expr * expr                             
  | Var of ident
  | Let of ident * expr * expr
  | For of ident * int * int * expr (*ident to zmienna iteracyjna, pierwszy int to początek, drugi int to koniec, expr to po czym się iterujemy*)
  | DefIntegral of int * int * expr * ident (*pierwszy int to dolna granica, drugi to górna, expr to funkcja podcałkowa, ident to argument funkcji*)
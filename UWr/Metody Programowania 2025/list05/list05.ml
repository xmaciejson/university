(*ZAD 3*)
let list_of_string s = String.to_seq s |> List.of_seq
let parens_ok s =
  let rec check lst count =
    match lst with
    | [] -> count = 0
    | '(' :: rest -> check rest (count + 1)
    | ')' :: rest -> if count > 0 then check rest (count - 1)
      else false
    | _ -> false
  in 
check (list_of_string s) 0;;

parens_ok "(())()";; (* true *)
parens_ok "() ())";; (* false *)
parens_ok "((() )";; (* false *)
parens_ok "(x)";; (* false *)

(*ZAD 4*)
let parens_ok s = 
  let rec check lst stack =
    match lst with 
    | [] -> stack = []
    | '(' :: rest -> check rest ('(' :: stack)
    | '{' :: rest -> check rest ('{' :: stack)
    | '[' :: rest -> check rest ('[' :: stack)
    | ')' :: rest -> 
      (match stack with 
      | '(' :: remaining_stack -> check rest remaining_stack
      | _ -> false)
    | '}' :: rest ->
      (match stack with 
      | '{' :: remaining_stack -> check rest remaining_stack
      | _ -> false)
    | ']' :: rest ->
      (match stack with 
      | '[' :: remaining_stack -> check rest remaining_stack
      | _ -> false)
    | _ -> false
  in check (list_of_string s) [];;

parens_ok "()[]]";;
parens_ok "()[] ]";;
parens_ok "()[x]]";;
parens_ok "{([])}";;


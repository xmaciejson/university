exception PrefixError of string

type frame =
  | Waiting1 of string
  | Waiting2 of string * int

type item =
  | Value of int
  | Frame of frame

let eval_binop op x y =
  match op with
  | "+" -> x + y
  | "-" -> x - y
  | "*" -> x * y
  | "/" -> x / y
  | _ -> raise (PrefixError ("Unknown operator: " ^ op))

let eval_prefix (tokens : string list) : int =
  let stack : item Stack.t = Stack.create () in

  let rec handle_number n =
    if Stack.is_empty stack then Stack.push (Value n) stack
    else
      match Stack.pop stack with
      | Frame (Waiting1 op) ->
          Stack.push (Frame (Waiting2 (op, n))) stack
      | Frame (Waiting2 (op, x)) ->
          let res = eval_binop op x n in
          handle_number res
      | Value _ -> raise (PrefixError "Unexpected value on stack")

  in

  let process_token token =
    match token with
    | "+" | "-" | "*" | "/" ->
        Stack.push (Frame (Waiting1 token)) stack
    | _ ->
        try
          let n = int_of_string token in
          handle_number n
        with _ -> raise (PrefixError ("Invalid token: " ^ token))
  in

  List.iter process_token tokens;

  match Stack.pop stack with
  | Value n when Stack.is_empty stack -> n
  | _ -> raise (PrefixError "Stack not empty or invalid result")
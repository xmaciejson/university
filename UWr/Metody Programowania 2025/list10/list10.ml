(*ZAD 1*)
open Fun.Ast;;
open Fun.Interp;;
open Fun.Lexer;;
open Fun.Parser;;
open Fun.Pn;;
open Fun.Pn_eval;;

to_prefix (Binop (Add,
  Binop (Add, Int 3, Int 8),
  Binop (Mult, Int 4, Binop (Sub, Int 2, Int 1))
));;
to_prefix (Binop (Add, Int 3, Int 5));;
to_prefix (Binop (Add, Int 3, Binop (Mult, Int 4, Binop (Sub, Int 2, Int 1))));;
to_prefix (Let ("x", Int 5, Binop (Add, Var "x", Int 1)));;

(*ZAD 2*)
eval_prefix ["+"; "3"; "5"];;
eval_prefix ["+"; "+"; "3"; "8"; "*"; "4"; "-"; "2"; "1"];;

(*ZAD 3*)
stack_size ["3"; "5"; "+"];;
stack_size ["3"; "8"; "+"; "4"; "2"; "1"; "-"; "*"; "+"]

(*ZAD 5*)
max_stack_usage [PushInt 1; PushVar "x"; Binop Ast.Add];;
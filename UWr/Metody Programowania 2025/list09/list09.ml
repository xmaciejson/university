open Fun.Ast;;
open Fun.Interp;;
open Fun.Lexer;;
open Fun.Parser;;

(*ZAD 1*)
interp_str "while false do 1 + 1 done";;
interp_str "try while true do throw done with 99";;

(*ZAD 2*)
interp_str "while true do break done";;
interp_str "while false do break done";;
interp "
let x = 0 in
while true do
  if x = 0 then break else unit
done
"
(*ZAD 3*)
let interp_str s = interp s |> show_value |> print_endline;;
interp_str "6 / 0";;  

(*ZAD 7*)
let parse_rpn s = String.split_on_char ' ' s |> rpn_to_ast;;
parse_rpn "2 3 + 4 *";;
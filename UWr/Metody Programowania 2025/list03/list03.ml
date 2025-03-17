(*ZAD 1*)
let fold_left f a xs =
  let rec it xs acc =
    match xs with
    | [] -> acc
    | x::xs -> it xs (f acc x)
  in it xs a;;

let product xs = if xs = [] then 0 else List.fold_left ( * ) 1 xs;;

(*ZAD 2*)
let square x = x * x;;
let inc x = x + 1;;
let compose f g = f g;;

compose square (inc 5);;
compose inc (square 5);;

(*ZAD 3*)
let build_list n f = 
  let rec it x xs = 
    if x = -1 then xs 
    else it (x - 1) (f x :: xs)
  in it (n-1) [];;

(*1*) let negatives n = build_list n (fun (x) -> -(x + 1));;
(*2*) let reciprocals n = build_list n (fun (x) -> 1. /. (float_of_int(x) +. 1.));;
(*3*) let evens n = build_list n (fun (x) -> x * 2);;
(*4*) let identityM n = build_list n (fun (x) ->  build_list n (fun (y) -> if x == y then 1 else 0));;

(*ZAD 4*)
(*a*)let empty_set = fun (_) -> false;;
(*b*)let singleton a = fun (x) -> x==a;;
(*c*)let in_set a s = s a;;
(*d*)let union s t = fun (x) -> s x || t x;;
(*e*)let intersect s t = fun (x) -> s x && t x;;

let num1to10 = fun x-> x >= 1 && x <= 10;;
let num5to15 = fun x-> x >= 5 && x <= 15;;
let new_z = union num1to10 num5to15;;
in_set 11 num1to10;;
in_set 11 new_z;;
let my_set x = x mod 2 = 0;;  (* parzyste liczby *)
let result1 = in_set 4 my_set;; 

(*ZAD 5*)
type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree;;
type int_tree = IntLeaf | IntNode of int_tree * int * int_tree;;

let rec insert_bst x t =
  match t with
  | Leaf -> Node (Leaf, x, Leaf)
  | Node (l, v, r) ->
      if x = v
      then t
      else if v < x
      then Node (l, v, insert_bst x r)
      else Node (insert_bst x l, v, r);; 


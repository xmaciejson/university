(*ZAD 1*)
let rec fib n =
    if n = 0 then 0 
    else if n = 1 then 1
    else fib (n-1) + fib (n+1);;


let rec fib_iter n =
    let rec it n prev curr = 
        if n = 0 then prev
        else it (n - 1) (prev + curr) prev
    in it n 0 1;

(*ZAD 2*)
let matrix_id=(1,0,0,1);;

let matrix_mult a b = 
  let (aa, ab, ac, ad) = a
  and (ba, bb, bc, bd) = b
in (aa*ba+ab*bc,aa*bb+ab*bd,ac*ba+ad*bc,ac*bb+ad*bd);;

matrix_mult (1,2,3,4) (5,6,7,8);;

let matrix_expt m k =
  let rec it n m acc =
    if n==0 then acc else it (n-1) m (matrix_mult acc m)
  in it (k-1) m m;;

let fib_matrix k =
  let (a,b,c,d) = matrix_expt (1,1,1,0) k
in b;;

(*ZAD 4*)
let rec mem x xs =
  if xs=[] then false else
  if List.hd(xs)=x then true (*hd - pierwszy element listy*)
  else mem x (List.tl(xs));; (*tl - lista poza pierwszym elementem*)

mem 2 [1;2;3];;
mem 4 [1;2;3];;

(*ZAD 5*)
let maximum xs =
    let rec it mx xs =
      if xs=[] then mx
      else it (max mx (List.hd(xs))) (List.tl(xs))
    in it neg_infinity xs;;

maximum [4.;2.;3.];;

(*ZAD 6*)
let rec suffixes xs = 
  if xs = [] then [[]]
  else xs::(suffixes (List.tl(xs)));; (* :: - dodanie elementu na poczatek listy *)
  
suffixes [1; 2; 3; 4]


(*ZAD 7*)
let is_sorted xs =
    let rec it last xs =
      if xs=[] then true
      else if last>(List.hd(xs)) then false
      else it (List.hd(xs)) (List.tl(xs))
    in it (List.hd(xs)) xs;;

is_sorted [4,2,3]
is_sorted [1,2,3]
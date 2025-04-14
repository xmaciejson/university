let alpha_num = 3
let alpha_denom = 4


type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree
type 'a sgtree = { tree : 'a tree; size : int; max_size: int }

let tree = Node (Node (Leaf, 1, Leaf), 2, Node (Leaf, 3, Leaf))

let alpha_height (n : int) : int = 
  let log_base a x = log x /. log a in
  int_of_float (log_base (float_of_int alpha_denom /. float_of_int alpha_num) (float_of_int n))

let rec split_mid n lst = (*Funkcja dzieląca listę na dwie listy w wybranym indeksie*)
  if n <= 0 then ([], lst)
  else match lst with
  | [] -> ([], [])
  | x :: xs ->
    let left, right = split_mid (n - 1) xs in
    (x :: left, right);;

let rebuild_balanced (t : 'a tree) : 'a tree =
    let rec to_list t = (*Funkcja, która zamienia drzewo na listę inorder*)
      match t with
      | Leaf -> []
      | Node (l, x, r) -> to_list l @ [x] @ to_list r
    in
    let rec build xs = (*Funkcja, która tworzy zbalansowane drzewo, bierze środkowy element jako korzeń*)
      match xs with
      | [] -> Leaf
      | xs -> 
        let mid = List.length xs / 2 in
        let left, right = split_mid mid xs in
        match right with
        | [] -> Leaf
        | x :: right -> Node(build left, x, build right)
    in build (to_list t);;
let empty : 'a sgtree =
    { tree = Leaf;
      size = 0;
      max_size = 0;
    }

let find (x : 'a) (sgt : 'a sgtree) : bool =
    let rec search tree = 
      match tree with
      | Leaf -> false
      | Node (left, value, right) ->
        if x = value then true
        else if x < value then search left
        else search right
    in search sgt.tree;;

let insert (x : 'a) (sgt : 'a sgtree) : 'a sgtree =
  let rec insert_node depth t =
    match t with
    | Leaf -> Some (Node (Leaf, x, Leaf), depth)
    | Node (l, v, r) as node ->
      if x = v then None  
      else if x < v then
        match insert_node (depth + 1) l with
        | Some (new_l, d) -> Some (Node (new_l, v, r), d)
        | None -> None
      else
        match insert_node (depth + 1) r with
        | Some (new_r, d) -> Some (Node (l, v, new_r), d)
        | None -> None
  in 
  match insert_node 0 sgt.tree with
  | None -> failwith "element istnieje już w drzewie"
  | Some (new_tree, depth) ->
    let new_size = sgt.size + 1 in
    let new_sgt = { 
      tree = new_tree; 
      size = new_size; 
      max_size = max sgt.max_size new_size 
    } in
    if depth > alpha_height new_size then
      { new_sgt with tree = rebuild_balanced new_tree }
    else
      new_sgt
    

let remove (x : 'a) (sgt : 'a sgtree) : 'a sgtree =
  let rec remove_node t =
    match t with
    | Leaf -> failwith "podany element nie istnieje"
    | Node (l, v, r) ->
      if x < v then Node (remove_node l, v, r)
      else if x > v then Node (l, v, remove_node r)
      else match l, r with
        | Leaf, Leaf -> Leaf
        | Leaf, _ -> r
        | _, Leaf -> l
        | _, _ ->
          let rec find_min = function
            | Node (Leaf, v, _) -> v
            | Node (l, _, _) -> find_min l
            | Leaf -> failwith "niemozliwe"
          in
          let successor = find_min r in
          let rec remove_min = function
            | Node (Leaf, _, r) -> r
            | Node (l, v, r) -> Node (remove_min l, v, r)
            | Leaf -> failwith "niemozliwe"
          in
          Node (l, successor, remove_min r)
  in
  let new_tree = remove_node sgt.tree in
  let new_size = sgt.size - 1 in
  let new_sgt = {
    sgt with
    tree = new_tree;
    size = new_size
  } in
  if new_size < alpha_height new_size then
    { new_sgt with tree = rebuild_balanced new_tree }
  else
    new_sgt
      

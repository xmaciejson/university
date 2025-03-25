module type DICT = sig
  type ('a , 'b ) dict
  val empty : ('a , 'b ) dict
  val insert : 'a -> 'b -> ('a , 'b ) dict -> ('a , 'b ) dict
  val remove : 'a -> ('a , 'b ) dict -> ('a , 'b ) dict
  val find_opt : 'a -> ('a , 'b ) dict -> 'b option
  val find : 'a -> ('a , 'b ) dict -> 'b
  val to_list : ('a , 'b ) dict -> ('a * 'b ) list
end

(*ZAD 1*)
module ListDict : DICT = struct
  type ('a, 'b) dict = ('a * 'b) list (*słownik jako lista par*)
  let empty = []
  let remove key lst = List.filter (fun (x, _) -> x <> key) lst
  let insert key value lst = (key, value) :: remove key lst (*usuwa istniejącą parę a potem dodaję nową na początek*)
  let find_opt key lst = List.find_opt (fun (x, _) -> x = key) lst |> Option.map snd
  let find key lst = List.find (fun (x, _) -> x = key) lst |> snd
  let to_list dict = dict (*zwraca liste*)
  
end

let dict = ListDict.insert 'c' 3 (ListDict.insert 'b' 2 (ListDict.insert 'a' 1 ListDict.empty)) ;;
let result = ListDict.find 'b' dict ;;  (* powinno zwrócić 2 *)
result;;

(*ZAD 2*)
module type KDICT = sig (*słowniki z ustalonym typem klucza*)
  type key
  type 'a dict
  
  val empty : 'a dict
  val insert : key -> 'a -> 'a dict -> 'a dict
  val remove : key -> 'a dict -> 'a dict
  val find_opt : key -> 'a dict -> 'a option
  val find : key -> 'a dict -> 'a
  val to_list : 'a dict -> (key * 'a) list
end

(*ZAD 3*)
module type DICT = sig
  type key
  type 'a dict
  val empty : 'a dict
  val insert : key -> 'a -> 'a dict -> 'a dict
  val remove : key -> 'a dict -> 'a dict
  val find_opt : key -> 'a dict -> 'a option
  val find : key -> 'a dict -> 'a
  val to_list : 'a dict -> (key * 'a) list
end

module MakeListDict(Key:Map.OrderedType):DICT with type key = Key.t = struct
  type key = Key.t
  type 'a dict = (key * 'a) list
  let empty = []
  let remove k d = List.filter (fun (k', _) -> k <> k') d
  let insert k v d = (k, v) :: remove k d
  let find_opt k d = List.find_opt (fun (k', _) -> k = k') d |> Option.map snd (*szuka pierwszego elementu odpowiadającego, snd odwołuje się do drugiego elementu krotki*)
  let find k d = List.find (fun (k', _) -> k = k') d |> snd
  let to_list d = d
end

module CharListDict = MakeListDict (struct
type t = char
let compare = compare
end)


(*ZAD 4*)
module MakeMapDict(Key:Map.OrderedType):DICT with type key = Key.t = struct (*słownik jako Map*)
  type key = Key.t
  module KeyMap = Map.Make(Key)
  type 'a dict = 'a KeyMap.t
  let empty = KeyMap.empty
  let remove = KeyMap.remove
  let insert = KeyMap.add
  let find_opt = KeyMap.find_opt
  let find = KeyMap.find
  let to_list d = KeyMap.bindings d
end

module CharMapDict = MakeMapDict (struct
  type t = char
  let compare = compare
end)
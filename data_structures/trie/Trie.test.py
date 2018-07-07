from Trie import TrieNode

T = TrieNode("J")

T.add_child("O", True)

T.child("O").add_child("H")

T.child("O").child("H").add_child("N", True)

T.child("O").child("H").child("N").add_child("A")

T.child("O").child("H").child("N").child("A").add_child("T")

T.child("O").child("H").child("N").child("A").child("T").add_child("H")

T.child("O").child("H").child("N").child("A").child("T").child("H").add_child("A")

T.child("O").child("H").child("N").child("A").child("T").child("H").child("A").add_child("N", True)

def print_trie(prefix, t):
	prefix += t.character
	if t.is_end():
		print(prefix)

	for c in t.get_children():
		print_trie(prefix, t.child(c))

print_trie("", T)

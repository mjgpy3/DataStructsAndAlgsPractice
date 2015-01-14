package linkedlist

import ("testing")

func Test_making_new_linkedlist_returns_empty(t *testing.T) {
	if make_linkedlist().Length() != 0 {
		t.Error("Non-empty linked list created")
	}
}

func Test_adding_an_element_gives_length_1(t *testing.T) {
	list := make_linkedlist()
	list.Add(42)
	if list.Length() != 1 {
		t.Error("Added an element, but length is not 1, got", list.Length())
	}
}

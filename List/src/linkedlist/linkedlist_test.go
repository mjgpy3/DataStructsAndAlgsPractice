package linkedlist

import ("testing")

func Test_making_new_linkedlist_returns_empty(t *testing.T) {
	if make_linkedlist().length() != 0 {
		t.Error("Non-empty linked list created")
	}
}

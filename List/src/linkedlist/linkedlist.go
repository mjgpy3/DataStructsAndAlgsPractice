package linkedlist

type listRoot struct {
	elementCount int
}

func (self listRoot) Length() int {
	return self.elementCount
}

func (self *listRoot) Add(item interface{}) {
	self.elementCount += 1
}

func make_linkedlist() listRoot {
	return listRoot{}
}

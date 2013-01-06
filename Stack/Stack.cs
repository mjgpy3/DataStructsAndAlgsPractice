using System;

namespace Stack
{
	public class Stack
	{
		private Node _root;
		private int _count;
		
		public Stack()
		{
			_count = 0;
			_root = null;
		}
		
		public void Push(object toAdd)
		{
			Node newNode = new Node(toAdd);
			
			if (_count++ == 0)
			{
				_root = newNode;
				return;
			}
			
			newNode.Next = _root;
			_root = newNode;
		}
		
		public object Pop()
		{
			if (_root != null)
			{
				object data = _root.Data();
				_root = _root.Next;
				_count--;
				return data;
			}
			
			throw new Exception("Trying to pop from empty Stack");
		}
		
		public object Peek()
		{
			if (_root != null)
				return _root.Data();
			
			throw new Exception("Cannot peek into an empty Stack");
		}
		
		public int Count()
		{
			return _count;
		}
		
		public bool IsEmpty()
		{
			return _count == 0;
		}
		
		public override string ToString()
		{
			return (_root != null ? _root.ToString() : "EMPTY");
		}
	}
}


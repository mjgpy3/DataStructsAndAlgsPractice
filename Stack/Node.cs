using System;

namespace Stack
{
	public class Node
	{
		private object _data;
		public Node Next;
		
		public Node(object data)
		{
			_data = data;
			Next = null;
		}
		
		public object Data()
		{
			return _data;
		}
		
		public override string ToString()
		{
			return _data.ToString() + " -> " +
				(Next != null? Next.ToString() : "END");
		}
	}
}



public class Heap {

	public Node Root;
	private int _count;
	
	public Heap()
	{
		_count = 0;
		Root = null;
	}
	
	public int count()
	{
		return _count;
	}
	
	public void heapify(int [] array)
	{
		if (array.length == 0)
			return;
		
		if (_count == 0)
		{
			Root = new Node(array[array.length-1]);
			_count++;
		}
		
		for (int i = 0; i < array.length-1; i++)
		{
			addItem(array[i]);
		}
	}
	
	public void addItem(int item)
	{
		int i = ++_count;
		Node newNode = new Node(item);
		Node currentNode = Root;
		
		while (i != 1)
		{
			if (newNode.Data > currentNode.Data)
			{
				int temp = newNode.Data;
				newNode.Data = currentNode.Data;
				currentNode.Data = temp;
			}
			
			if (i%2 == 0)
			{
				if (currentNode.Left == null)
					currentNode.Left = newNode;
				else
					currentNode = currentNode.Left;
			}
			else
			{
				if (currentNode.Right == null)
					currentNode.Right = newNode;
				else
					currentNode = currentNode.Right;
			}
			
			i /= 2;
		}
	}
	
	public String toString()
	{
		return Root.toString();
	}
}

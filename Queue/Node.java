
public class Node 
{
	public Node Next;
	public Node Last;
	public Object Data;
	
	public Node(Object data)
	{
		Data = data;
		Next = null;
		Last = null;
	}
	
	public String toString()
	{
		return Data.toString() + " -> " +
	            (Next != null ? Next.toString() : "END");
	}
}

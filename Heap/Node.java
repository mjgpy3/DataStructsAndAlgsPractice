
public class Node {

	public int Data;
	public Node Left;
	public Node Right;
	
	public Node(int data)
	{
		Data = data;
		Left = null;
		Right = null;
	}
	
	public String toString()
	{
		return "[" + (Left != null ? Left.toString() : "END") + " <- " + Data + " -> " +  (Right != null ? Right.toString() : "END") +"]";
	}
}
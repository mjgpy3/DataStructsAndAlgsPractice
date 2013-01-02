
public class FromTheSidesSearch {

	public static void main(String [] args)
	{
		int[] a = {1, 4623, 21, 23, 1234, 763, 134, 74, 13};
		
		System.out.println("89 was found at " + fromTheSidesSearch(a, 89));
		
		for (int i : a)
		{
			System.out.println(i + " was found at " + fromTheSidesSearch(a, i));
		}
	}
	
	/*
	 * Searches an array for a specific value from the sides in.
	 * If it's not found, it returns -1.
	 */
	public static int fromTheSidesSearch(int [] array, int val)
	{
		int bottom = 0, top = array.length-1;
		
		while (bottom <= top)
		{
			if (array[bottom++] == val)
				return bottom-1;
			else if (array[top--] == val)
				return top+1;
		}
		
		return -1;
	}
	
}

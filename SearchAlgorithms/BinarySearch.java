
public class BinarySearch {

	public static void main(String [] args)
	{
		int[] searchMe = {1, 2, 3, 6, 234, 6463, 1256243};
		
		System.out.println("7 was found at " + binarySearch(searchMe, 7));
		System.out.println("6 was found at " + binarySearch(searchMe, 6));
	}
	
	public static int binarySearch(int[] array, int val)
	{
		return meatOfSearch(array, val, 0, array.length);
	}
	
	/* Searches a sorted array for a value. Returns -1 if the value
	 * is not found.
	 */
	private static int meatOfSearch(int[] array, int val, int beg, int end)
	{
		int half = (beg + end) / 2;
		
		if (array[half] == val)
			return half;
		else if (half == beg || half == end)
			return -1;
		else if (array[half] < val)
			return meatOfSearch(array, val, half, end);
		else 
			return meatOfSearch(array, val, beg, half);
	}
}

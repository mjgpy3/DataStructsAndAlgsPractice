
public class SelectionSort {

	public static void main(String [] args)
	{
		int [] a = {1, 213, 3, 123, 63, 13, 3, 2134, 4, 23, 74, 21, 76, 2, 4, 5};
		
		selectionSort(a);
		
		for (int i : a)
		{
			System.out.println(i + ", ");
		}
	}
	
	public static void selectionSort(int [] array)
	{	
		for (int i = 0; i < array.length; i++)
		{
			int minIndex = i;
			
			for (int k = i+1; k < array.length; k++)
				if (array[k] < array[minIndex])
					minIndex = k;
				
			if (minIndex != i)
			{
				int temp = array[i];
				array[i] = array[minIndex];
				array[minIndex] = temp; 
			}
		}
	}
}

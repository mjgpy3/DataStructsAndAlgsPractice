using System;

namespace IterativeBinarySearch
{
	class MainClass
	{
		public static void Main(string[] args)
		{
			int[] a = {1, 2, 3, 4, 6, 7, 8};
			
			System.Console.WriteLine("{0} was found at {1}", 100, binarySearch(a, 100));
			
			foreach (int i in a)
			{
				System.Console.WriteLine("{0} was found at {1}", i, binarySearch(a, i));
			}
		}
		
		public static int binarySearch(int [] array, int val)
		{
			int half, beg = 0, end = array.Length;			
			
			do
			{
				half = (beg+end)/2;
				
				if (array[half] == val)
					return half;
				else if (array[half] < val)
					beg = half;
				else
					end = half;
				
			} while (half != (beg+end)/2);
			
			return -1;
		}
	}
}

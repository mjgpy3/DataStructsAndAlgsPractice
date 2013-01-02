using System;

namespace BruteForceSearch
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			int[] searchMe = {543,4,74,123,64,1234,74,1,7,9768,2342};
			
			System.Console.WriteLine("{0} found at {1}", 7, bruteForceSearch(searchMe, 7));
			System.Console.WriteLine("{0} found at {1}", 9, bruteForceSearch(searchMe, 9));
		}
		
		/* Iterates all elements, if not found returns -1
                   also known as an exhaustive search and "generate and
                   test"
                */
		public static int bruteForceSearch(int[] array, int val)
		{
			for (int i = 0; i < array.Length; i++)
				if (array[i] == val)
					return i;
			
			return -1;
		}
	}
}

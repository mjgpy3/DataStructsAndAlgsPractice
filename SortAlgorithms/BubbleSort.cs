using System;

namespace BubbleSort
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			int [] a = {123, 2, 12, 452, 885, 13, 634, 123, 45, 1, 54, 2};
			
			bubbleSort(a);
			
			foreach(int i in a)
				System.Console.Write(i + ", ");
		}
		
		public static void bubbleSort(int [] array)
		{
			bool keepLooping = true;
			
			for (int i = 0; i < array.Length-1; i++)
			{
				while (keepLooping)
				{
					keepLooping = false;
					if (array[k] > array[k+1])
					{
						int temp = array[k];
						array[k] = array[k+1];
						array[k+1] = temp;
						keepLooping = true;
					}
				}
			}
		}
	}
}

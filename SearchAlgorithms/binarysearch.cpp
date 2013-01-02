#include <iostream>
using namespace std;

int binarySearch(int array[], int val, int size);
int meatOfSearch(int array[], int val, int beg, int end);

int main()
{
	int a[] = {1, 2, 4, 7, 9, 10};

	cout << 2 << " found at " << binarySearch(a, 2, 6) << endl;
	cout << 20 << " found at " << binarySearch(a, 20, 6) << endl;

	return 0;
}

// Calls meatOfSearch to do a binary search
int binarySearch(int array[], int val, int size)
{
	return meatOfSearch(array, val, 0, size);
}

// Performs a binary search on the passed array.
// If no value if found, returns -1
int meatOfSearch(int array[], int val, int beg, int end)
{
	int half = (beg + end)/2;

	if (array[half] == val)
		return half;
	else if (half == beg || half == end)
		return -1;
	else if (array[half] < val)
		return meatOfSearch(array, val, half, end);
	else
		return meatOfSearch(array, val, beg, half);
}

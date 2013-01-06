#include <iostream>
using namespace std;

int binarysearch(int array [], int value, int arraysize);

int main()
{

	int a[] = {1, 12, 16, 17, 17, 20, 21, 22, 27, 99};
	int size = 10;

	for (int i = 0; i < size; i++)
		cout << a[i] << " at " << binarysearch(a, a[i], size) << endl;

	cout << 10 << " at " << binarysearch(a, 10, size) << endl;

	return 0;
}

int binarysearch(int array [], int value, int arraysize)
{
	int newhalf = arraysize/2,
	    half,
            beg = 0,
            end = arraysize;

	do
	{
		half = newhalf;

		if (array[half] == value)
			return half;
		else if (array[half] < value)
			beg = half;
		else
			end = half;

		newhalf = (beg+end)/2;

	} while (half != newhalf);

	return -1;
}

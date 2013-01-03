#include <iostream>
using namespace std;

void insertionsort(int arr [], int size);

int main()
{
	int a[12] = {123, 1, 235, 123, 1, 34, 2, 656, 22, 54, 27, 27};

	int b[1] = {4};

	insertionsort(a, 12);
        insertionsort(b, 1);

	for (int i = 0; i < 12; i++)
		cout << a[i] << ", ";

	cout << endl;

	for (int i = 0; i < 1; i++)
		cout << b[i] << ", ";

	cout << endl;

	return 0;
}

void insertionsort(int arr [], int size)
{
        if (size < 2)
        	return;

	for (int i = 1; i < size; i++)
	{
		int index = i, item = arr[index];

		for (index = i; index > 0 && item < arr[index-1]; index--)
			arr[index] = arr[index-1];

		arr[index] = item;
	}
}

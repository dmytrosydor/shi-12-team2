//�������� 2. �������� �������, ��� �������� ��
//��������� �� ������������� ����� � �����������.
//���������, ����� 10 11 12 11 10 - �����������, � �����
//20 11 12 11 10 - �������������.

#include <iostream>
using namespace std;

void array_input(int ar[], int length)
{

	for (int i = 0; i < length; i++)
	{
		cout << "[" << i + 1 << "]= ";
		cin >> ar[i];
	}
}



bool array_symmetrical(int ar[], int length)
{
	for (int i = 0; i < length / 2; i++)
	{
		if (ar[i] != ar[length - (i + 1)])
		{
			return false;
		}

	}
	return true;
}

int main()
{
	const int SIZE = 6;
	int array[SIZE];
	array_input(array, SIZE);
	array_symmetrical(array, SIZE);
	cout << "\nIs massive symmetrical: " << boolalpha << array_symmetrical(array, SIZE) << endl;
	cout << endl;
	return 0;
}

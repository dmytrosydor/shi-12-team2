//�������� 1. �������� �������, ��� �������� ����
//�������� ���������� �� ������ ����� �����, ��
//����������� � ������� �� a �� b.��� ��������
//����������� � ������� � ������ ���� �������� ��
//�������������.



#include <iostream>
using namespace std;

double sum(double array[], int length, double lower_bound = -1.0, double upper_bound = 1.0)
{
	double s = 0.0;
	for (int i = 0; i < length; i++)
	{
		if (array[i] >= lower_bound && array[i] <= upper_bound)
			s += array[i];
	}
	return s;
}

int main()
{
	double array[] = { 4.6, 7.1, 2.8, 1.4, 6.7, 2.8, 1.1 };
	cout << sum(array, size(array), 1.5, 4.5) << endl;
  return 0;
}
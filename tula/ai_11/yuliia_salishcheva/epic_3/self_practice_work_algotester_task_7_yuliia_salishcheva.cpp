//�������� 7. �� ���� ����� ���������� ���.³� ���������� �
//����, �� �� ������������.�������� ��������, ���
//������ �� ������ ��� ��������� ����.� �����
//��������, ������ ���� ����������� ��� ��������
//����� � ������ �������, ���� �� ���� ����� ����
//����������� 3 �������.

#include <iostream>
using namespace std;

int main()
{
	int sum = 0;
	for (int i = 0; i <= 9; i++)
	{
		for (int j = 0; j <= 9; j++)
		{
			for (int m = 0; m <= 9; m++)
			{
				if (i != j && j != m && i != m)
				{
					cout << i << j << m << endl;
					sum += 1;
				}
			}
		}
	}
	cout << (sum * 3)/60 << " minute worst case" << endl;
}
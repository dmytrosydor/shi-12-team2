////�������� 9. �������� ���������� �������, ���
////�������� N ���� � ���, ����� N ���� ����������.
////������������ ������ ������� ���������.

#include <iostream>
using namespace std;

void output_star(int number);


int main()
{
	output_star(5);
}

void output_star(int number)
{
	if (!number) 
		return;
	cout << '*';
	output_star(number - 1);

}

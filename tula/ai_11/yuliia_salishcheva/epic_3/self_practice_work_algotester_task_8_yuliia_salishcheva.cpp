//�������� 8. �������� ���������� �������, ��� ��������
//���� ��� ����� � ������� �� a �� b.
//������������ ������ ������� ���������.

#include <iostream>
using namespace std;

int sum(int a, int b) 
{
    if (b == a - 1) return 0;
    return b + sum(a, b - 1);
}

int main()
{
    int a, b;
    cout << "Enter first number: ";
    cin >> a;
    cout << "Enter second number: ";
    cin >> b;

    cout << sum(a, b);

    return 0;
}

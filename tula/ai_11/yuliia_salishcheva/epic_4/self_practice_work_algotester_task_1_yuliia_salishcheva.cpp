//�������� 1. ���������� ������� �������� ����� �� ��(12
//	������).���� ���������� ������� �������(���������,
//	3 � 6 � ����� �� ����� � ������ ������).���������
//	��������� �����, � ����� �������� ��� ������������, �
//	�����, � ����� �������� ��� ���������, � �����������
//	�������� ��������.

#include <iostream>
using namespace std;
int main()
{
    const int SIZE = 5;
    int m_1, m_2;
    int max = 0, min = 0;
    int list[SIZE];
    for (int i = 0; i < SIZE; i++)
    {
        cout << "Enter salary for |"<<i + 1<<"| month: ";
        cin >> list[i];
    }

    cout << "Enter from which month: ";
    cin >> m_1;
    cout << "Enter until what month : ";
    cin >> m_2;


    for (int i = (m_1 - 1) ; i <= (m_2 - 1) ; i++)
    {
        cout << i + 1 << endl;
        if (i == m_1 - 1)
        {
            max = i;
            min = i;
        }
        if (list[i] >= list[max])
        {
            max = i;
        }
        if (list[i] <= list[min])
        {
            min = i;
        }
    }
    cout << "\nThe minimum salary was this month --- |" << min + 1 << "|    SUMA: " << list[min]  << " $" << endl;
    cout << "The maximum salary was this month --- |" << max + 1 << "|    SUMA: " << list[max] << " $" << endl;
}







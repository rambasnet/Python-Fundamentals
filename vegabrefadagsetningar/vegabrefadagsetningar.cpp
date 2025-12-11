#include <iostream>
#include <string>

using namespace std;

int main()
{

    string first, second, third, fourth;
    cin >> first >> second >> third >> fourth;
    cout << "20" << fourth << "-";
    if (third.find('JAN') != string::npos)
        cout << "01";
    else if (third.find('FEB') != string::npos)
        cout << "02";
    else if (third.find('MAR') != string::npos)
        cout << "03";
    else if (third.find('APR') != string::npos)
        cout << "04";
    else if (third.find('MAY') != string::npos)
        cout << "05";
    else if (third.find('JUN') != string::npos)
        cout << "06";
    else if (third.find('JUL') != string::npos)
        cout << "07";
    else if (third.find('AUG') != string::npos)
        cout << "08";
    else if (third.find('SEP') != string::npos)
        cout << "09";
    else if (third.find('OCT') != string::npos)
        cout << "10";
    else if (third.find('NOV') != string::npos)
        cout << "11";
    else if (third.find('DEC') != string::npos)
        cout << "12";
    cout << "-" << first << endl;
    return 0;
}
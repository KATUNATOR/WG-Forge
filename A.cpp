#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int nm;
    cin >> nm;

    int *meals = new int[nm];
    for (int i = 0; i < nm; i++)
        cin >> meals[i];
    sort(meals, meals + nm);

    int nd;
    cin >> nd;   

    int *days = new int[nd];        
    for (int i = 0; i < nd; i++)
        cin >> days[i];

    int *days_sort = days;
    sort(days_sort, days_sort + nd);

    int *days_res = new int[200000];

    int count = 0;
    int prew = -1;

    for (int i = 0; i < nd; i++)
    {
        if (days_sort[i] != prew)
        {
            while (count < nm)
                if (days_sort[i] >= meals[count])
                {
                    count++;
                    nm--;
                }
                else
                    break;
        }
        days_res[days_sort[i] - 1] = count;
        prew = days_sort[i];
    }

    for (int i = 0; i < nd; i++)
        cout << days_res[days_sort[i] - 1];
        

    delete [] meals;
    delete [] days;
    delete [] days_res;
    delete [] days_sort;

    return 0;
}
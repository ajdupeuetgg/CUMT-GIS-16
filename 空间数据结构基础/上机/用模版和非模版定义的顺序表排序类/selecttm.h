#ifndef SELECTTM_H
#define SELECTTM_H
#include "datalist.h"
using namespace std;

template<class Type>
void dataList
<Type> :: Swap (int m1,  int m2)
{
    Type temp = Element [m1];
    Element [m1] = Element [m2];
    Element [m2] = temp;
}

template <class Type>
int dataList<Type>::MaxKey (int low, int high)
{
    int max = low;
    for (int k = low+1;k <= high;k++)
        if ( Element[max] < Element[k] )
            max = k;
    return max;
}

template <class Type>
void dataList<Type>::Sort ( )
{
    for ( int i = ArraySize -1; i > 0; i-- )
    {
        int j = MaxKey (0, i);
        if ( j != i ) swap (j, i);
    }
}
#endif

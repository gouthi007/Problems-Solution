#include <stdio.h>

void sort(int *a)
{
    int i, j, key;
    for (i = 1; i< 5; i++)
    {
        key = a[i];
        j = i-1;
        while(j >= 0 && a[j] > key)
        {
            a[j+1] = a[j];
            j -= 1;
        }
        a[j + 1] = key;
    }
}

void main()
{
    int a[6] = {12,101,14,111,123};
    for(int i = 0; i < 5; i++)
        printf("%d\n", a[i]);
    printf("Sorted Array is \n");
    sort(a);
    for(int i = 0; i < 5; i++)
        printf("%d\n", a[i]);
}

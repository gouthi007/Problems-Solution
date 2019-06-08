#include <stdio.h>
#include <stdlib.h>
int comparator(const void *p, const void *q)
{
    int l,r;
    l = *(const int *)p;
    r = *(const int *)q;
    if(l&1 && r&1)
        return r-l;
    if(!(l&1) && !(r&1))
        return l-r;
    if(l&1)
        return -1;
    return 1;
    
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    for (int i=0; i <size; i++)
        printf("%d\t", arr[i]);
    printf("\n\n\n");
    qsort(arr, size, sizeof(arr[0]), comparator);
    
    for (int i=0; i <size; i++)
        printf("%d\t", arr[i]);
}

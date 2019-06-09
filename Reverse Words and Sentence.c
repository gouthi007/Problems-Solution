#include <stdio.h>

void reverseWords(char *s)
{
    char *temp = s;
    char *begin = s;
    
    while(*temp)
    {
        temp++;
        if(*temp == "\0")
            reverse(begin, temp - 1);
        else if(*temp == " ")
        {
            reverse(begin, temp -1);
            begin = temp + 1;
        }
    }
    reverse(s, temp - 1);
    
}

void reverse(char *a, char *b)
{
    char temp;
    while(a < b)
    {
        temp = *a;
        *a++ = *b;
        *b-- = temp;
    }
}
int main() 
{ 
    char s[] = "i like this program very much"; 
    char* temp = s; 
    reverseWords(s); 
    printf("%s", s); 
    getchar(); 
    return 0; 
} 

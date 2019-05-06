#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;
int count = 0;
void printfirst()
{
    if(head == NULL)
    {
        printf("asfsaa0\n");
        return;
    
    }else
    {
        struct node *current = head;
        for(current = head; current != NULL; current = current->next)
                printf("%d\t", current->data);
    }
}

void insertfirst(int num)
{
    struct node *new;
    new = malloc(sizeof(struct node));
    new->data = num;
    new->next = head;
    head = new;
    count += 1;
}

void accuratedelete(int data)
{
    struct node *current = head;
    struct node *previous = NULL;
    
    if(current == NULL)
        return 0;
    while (current->data != data)
    {
        if(current->next == NULL)
            return 0;
        else
        {
            previous = current;
            current = current->next;
        }
    if(current == head)
    {
        printf("Deketerd     %d", head->data);
        head = head->next;
        count -= 1;
    }
    else
        {
        printf("Deketerd     %d", current->data);
        previous->next = current->next;
        count -= 1;
            
        }
            
        }
    return;
}
void deletefirst()
{
    printf("Deleted %d\n\n",head->data );
    head = head->next;
    count = count - 1;
}

int isempty()
{
    return (head == NULL);
}

void countfn()
{
    printf("Length = %d\n\n", count);
}
void main()
{
    
    printfirst();
    countfn();
    printf("\nis isempty = %d\n", isempty() );
    insertfirst(3);
    countfn();
    insertfirst(4);
    countfn();
    insertfirst(5);
    countfn();
    insertfirst(6);
    countfn();
    printfirst();
    deletefirst();
    countfn();
    printfirst();
    accuratedelete(4);
    printfirst();
    
}

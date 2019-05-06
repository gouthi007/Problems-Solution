#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;

int count = 0;

void insertfirst(int datain)
{
    struct node *new;
    new = malloc(sizeof(struct node));
    new->data = datain;
    new->next = head;
    head = new;
    count += 1;
    printf("insert succ\n");
}

void printfirst()
{
    struct node *current;
    current = head;
    if (head == NULL)
    {
        printf("empty\n");
        return;
    }
    
    else
    {
        for(current = head; current != NULL; current = current->next )
            printf("Data: %d\n", current->data);
        
    }
}

void deletefirst()
{
    if(head == NULL)
    {    
        printf("empty list");
        return;
    } 
    
    printf("Deleted Number : %d\n", head->data);
    head = head->next;
    count -= 1;
    
}

void isempty()
{
    return count;
}

void deleteaccurate(int data)
{
    struct node *current = head;
    struct node *previous = NULL;
    
    if(head == NULL)
        return;
    
    while(current->data != data)
    {
        if(current->next == NULL)
        {
            printf("not present");
            return;
        }
        else
        {
            previous = current;
            current = current->next;
        }
    }
    
    if(current == head)
    {
        printf("Accurate Deleted number : %d\n\n", current->data);
        head = head->next;
    }
    else
    {
        printf("Accurate Deleted number : %d\n\n", current->data);
        previous->next = current->next;
    }
    
}

void reverse()
{
    struct node *current = head;
    struct node *previous = NULL;
    struct node *next = NULL;
    
    while(current != NULL)
    {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }
    head = previous;
}
void main()

{   
    printfirst();
    insertfirst(2);
    printfirst();
    insertfirst(3);
    printfirst();
    insertfirst(4);
    printfirst();
    printfirst();
    insertfirst(5);
    printfirst();
    reverse();
    printf("reversed\n");
    printfirst();
    insertfirst(9);
    printfirst();
    reverse();
    printf("reversed\n");
    printfirst();
}

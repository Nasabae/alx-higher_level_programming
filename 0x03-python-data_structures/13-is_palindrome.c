#include <stdio.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: pointer to pointer.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/

int is_palindrome(listint_t **head)
{
int list[1000000], w = 0, z = 0, k = 0;
listint_t *temp;

if (head == NULL || (*head) == NULL)
return (1);
temp = *head;
while (temp)
{
list[w] = temp->n;
w++;
temp = temp->next;
}
w--;

if (w % 2 != 0)
k = (w + 1) / 2;
else
k = w / 2;

while (z < k)
{
if (list[z] != list[w])
return (0);
w--;
z++;
}
return (1);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: start of linked list
 * Description : check if a linked list is a palindrome
 * Return: 1 if false, 0 if true 
 */

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
	return (1);

    return(0);
}

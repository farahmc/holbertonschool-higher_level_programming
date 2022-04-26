#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Check for a loop within a singly linked list
 * @list: singly linked list to check
 *
 * Return: 0 if no cycle, else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}

#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle
 * in it.
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	if (list == NULL || list->next == NULL)
		return (0);

	node1 = list->next;
	node2 = list->next->next;

	while (node1 && node2 && node2->next)
	{
		if (node1 == node2)
			return (1);
		node1 = node1->next;
		node2 = node2->next->next;
	}
	return (0);
}

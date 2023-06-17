#include "lists.h"

/**
 * dlistint_len - function that returns the number of elements in a linked
 * dlistint_t list
 * @h: doubly linked list
 *
 * Return: the number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t nodes = 0;
	const dlistint_t *tmp = h;

	while (tmp)
	{
		nodes += 1;
		tmp = tmp->next;
	}
	return (nodes);
}

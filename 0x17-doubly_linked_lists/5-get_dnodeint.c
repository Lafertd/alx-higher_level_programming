#include "lists.h"

/**
 * get_dnodeint_at_index -  function that returns the nth node of
 * a dlistint_t linked list.
 * @head: pointer to rhe list
 * @index: index of node
 *
 * Return: returns the nth node  or NULL
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (head == NULL)
		return (NULL);

	tmp = head;
	for (i = 0; i < index && tmp != NULL; i++)
		tmp = tmp->next;

	if (tmp == NULL)
		return (NULL);

	return (tmp);
}

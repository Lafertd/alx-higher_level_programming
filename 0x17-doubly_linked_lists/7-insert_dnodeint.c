#include "lists.h"

/**
 * insert_dnodeint_at_index - function that inserts a new node at a
 * given position
 * @h: pointer to pointer to head
 * @idx: index of the list where the new node should be added
 * @n: data of the new node
 *
 * Return: he address of the new node, or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *tmp, *new;
	unsigned int i;

	if (h == NULL)
		return (NULL);
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	new->prev = NULL;
	if (*h == NULL && idx == 0)
	{
		*h = new;
		return (new);
	}
	else if (idx == 0)
	{
		new->next = *h;
		(new->next)->prev = new;
		*h = new;
		return (new);
	}
	tmp = *h;
	for (i = 0; i < idx && tmp->next != NULL; i++)
		tmp = tmp->next;
	if (tmp->next == NULL && i + 1 == idx)
	{
		tmp->next = new, new->prev = tmp;
	}
	else if (tmp->next == NULL && i + 1 < idx)
	{
		return (NULL);
	}
	else
	{
		(tmp->prev)->next = new, new->prev = tmp->prev;
		tmp->prev = new, new->next = tmp;
	}
	return (new);
}

#include "lists.h"

/**
 * delete_dnodeint_at_index - function that deletes the node at index index
 * of a dlistint_t linked list
 * @head: header of the list
 * @index: is the index of the node that should be deleted
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	tmp = *head;

	if (tmp->next == NULL && index == 0)
	{
		*head = NULL;
		free(tmp);
		return (1);
	}
	if (index == 0)
	{
		*head = tmp->next;
		(tmp->next)->prev = NULL;
		free(tmp);
		return (1);
	}

	for (i = 0; i < index && tmp != NULL; i++)
		tmp = tmp->next;

	if (tmp == NULL)
		return (-1);
	if (tmp->next == NULL)
	{
		(tmp->prev)->next = NULL;
		free(tmp);
	}
	else
	{
		(tmp->prev)->next = tmp->next;
		(tmp->next)->prev = tmp->prev;
		free(tmp);
	}
	return (1);
}

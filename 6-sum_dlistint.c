#include "lists.h"

/**
 * sum_dlistint - function that returns the sum of all the data (n) of a
 * dlistint_t linked list
 * @head: head of the list
 *
 * Return: the sum of all the data (n) or 0 if list is empty
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;
	int sum = 0;

	if (head == NULL)
		return (0);
	tmp = head;

	while (tmp)
	{
		sum += tmp->n;
		tmp = tmp->next;
	}
	return (sum);
}

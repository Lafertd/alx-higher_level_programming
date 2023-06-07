#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - function that inserts a number into a sorted singly
 * linked list
 * @head: pointer to pointer to head
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp1, *tmp2;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	tmp1 = NULL, tmp2 = *head;
	while (tmp2->next)
	{
		if (tmp2->n < new->n)
		{
			tmp1 = tmp2, tmp2 = tmp2->next;
		}
		else
		{
			if (tmp1 == NULL)
			{
				new->next = tmp2, *head = new;
			}
			else
			{
				tmp1->next = new, new->next = tmp2;
			}
			return (new);
		}
	}
	if (tmp2->n < new->n)
	{
		tmp2->next = new;
		return (new);
	}
	new->next = tmp2, *head = new;
	return (new);
}

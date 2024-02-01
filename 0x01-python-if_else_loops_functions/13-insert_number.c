#include "lists.h"

/**
 * insert_node - inserts a num into a
 * sorted list
 * @head: head
 * @number: number
 *
 * Return: pointer to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *prev;

	tmp = *head;
	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (tmp == NULL)
	{
		*head = new;
		return (new);
	}

	if (number < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	prev = tmp;
	tmp = tmp->next;

	while (tmp)
	{
		if (number < tmp->n)
		{
			prev->next = new;
			new->next = tmp;
			return (new);
		}
		else
		{
			prev = tmp;
			tmp = tmp->next;
		}
	}
	prev->next = new;
	return (new);
}

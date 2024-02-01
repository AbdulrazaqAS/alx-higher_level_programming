#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks whether a linked list
 * is a palindrome
 * @head: ptr to head
 *
 * Return: 1 if ll is a palindrome,
 * 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j = 0;
	listint_t *tmp, *mid, *tmp2;

	if (head == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		len++;
	}

	tmp = *head;
	if (len == 0 || len == 1)
		return (1);

	while (i < len / 2)
	{
		tmp = tmp->next;
		i++;
	}
	mid = tmp;

	tmp = *head;
	for (i = 0; i < len / 2; i++)
	{
		tmp2 = mid;
		for (j = len / 2; j < len - 1 - i; j++)
			tmp2 = tmp2->next;

		if (tmp->n == tmp2->n)
		{
			if (len % 2 != 0 && j - i == 2)
				return (1);
			if (j - i == 1)
				return (1);
			else
				tmp = tmp->next;
		}
		else
			break;
	}
	return (0);
}

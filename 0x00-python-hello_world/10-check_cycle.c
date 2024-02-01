#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the linked list
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *tmp2;
	
	if (list == NULL)
		return (0);

	tmp = list;

	while(tmp)
	{
		if (tmp == tmp->next)
			return (1);

		tmp2 = list;
		while(tmp2 != tmp)
		{
			if (tmp->next == tmp2)
				return (1);
			tmp2 = tmp2->next;
		}

		tmp = tmp->next;
	}

	return (0);
}

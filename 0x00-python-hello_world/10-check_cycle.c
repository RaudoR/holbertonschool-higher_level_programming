#include "lists.h"
/**
 * check_cycle - check a linked list for cycles in it
 * @list: listint_t
 * Return: 1 on success or 0 if no cycle was found
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *new;

	temp = list;
	new = list;
	while (temp != NULL && new != NULL && new->next != NULL)
	{
		new = new->next->next;
		temp = temp->next;
		if (new == temp)
			return (1);
	}
	return (0);


}

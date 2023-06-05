#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle or not 
 *
 * @list: linked list to be checked check
 *
 * Return: 1 if the list has a cycle, 0 if it not
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list;
	listint_t *node2 = list;

	if (!list)
		return (0);

	for (; node->next != NULL && node->next->next != NULL;)
		{
			node = node->next->next;
			node2 = node2->next;

			if (node == node2)
				return (1);
		}
	return (0);
}

#include "lists.h"
/**
 * @brief Check if a linked list contains a cycle.
 *
 * This function checks if a linked list
 * contains a cycle by using the "tortoise
 * and hare" algorithm.
 *
 * @param head A pointer to the head of the linked list.
 *
 * @return 1 if the linked list contains a cycle, 0 otherwise.
 */
int has_cycle(listint_t *head)
{
	listint_t *slow_ptr, *fast_ptr;

	if (!head)
	{
		return (0);
	}
	slow_ptr = head;
	fast_ptr = head->next;

	while (fast_ptr && slow_ptr && fast_ptr->next)
	{
		if (slow_ptr == fast_ptr)
		{
			return 1;
		}
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	return (0);
}

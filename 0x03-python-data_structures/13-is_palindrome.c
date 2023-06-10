#include"lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *prev = NULL;
    listint_t *next;

    /* Find the middle of the list using Floyd's cycle-finding algorithm */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    /* Reverse the second half of the list */
    while (slow != NULL)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    /* Compare the first half of the list with the reversed second half */
    slow = prev;
    fast = *head;
    while (slow != NULL)
    {
        if (slow->n != fast->n)
            return 0;
        slow = slow->next;
        fast = fast->next;
    }

    return 1;
}

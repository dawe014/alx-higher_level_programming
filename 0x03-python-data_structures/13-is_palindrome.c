#include "lists.h"
/**
 * rev_list - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void rev_list(listint_t **head)
{
	listint_t *pre = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}

	*head = pre;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}

	rev_list(&d);

	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}

	if (!d)
		return (1);

	return (0);
}

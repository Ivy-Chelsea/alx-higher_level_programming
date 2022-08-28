#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the list
 * Return: 0 if not, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *prev, *next, *left_head, *right_head;
	int list_len = 0, q = 0, not_p = 0;

	if (*head == NULL || head == NULL)
		return (1);
	while (current != NULL)
		list_len++, current = current->next;
	if (list_len == 1)
		return (1);
	current = *head;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		else
			current->next = NULL;
		prev = current, current = next;
	}
	right_head = current, left_head = prev;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		if (list_len % 2 != 0 && q == 1)
			current = current->next;
		if (current->n != prev->n)
		{
			not_p = 1;
			break;
		}
		current = current->next, prev = prev->next;
	}
	current = left_head, prev = right_head;
	for (q = 1; q <= list_len / 2 && current != NULL; q++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		prev = current, current = next;
	}
	return (not_p == 1 ? 0 : 1);
}

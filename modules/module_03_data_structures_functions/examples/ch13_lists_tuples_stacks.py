"""Module 3 — Chapter 13: Lists, Tuples, and Stacks (LIFO).

Line-by-line reverse-engineering examples covering lists, nested lists,
in-place mutability vs. string immutability, tuples, and LIFO stacks.
"""


def demonstrate_lists() -> dict:
    """Demonstrate list creation, 0-based indexing, methods, and nested lists."""
    # Mixed-type list matching the book's structure, including a nested sublist at index 4
    items = [1, 2, 4, "Paul", [2, 5, "Ana"]]

    first_item = items[0]
    nested_sublist = items[4]
    nested_name = items[4][2]  # "Ana"

    # .append() adds to the end of the list in-place
    items.append("Python")

    # Membership check with 'in' before removing by value using .remove()
    had_four = 4 in items
    if had_four:
        items.remove(4)

    # del removes by index position rather than value
    del items[0]  # removes integer 1

    # .index() finds the first matching index
    paul_index = items.index("Paul")

    # .reverse() mutates the list in-place and returns None
    numbers_to_reverse = [10, 20, 30]
    reverse_return = numbers_to_reverse.reverse()

    # Contrast: strings are immutable, whereas lists are mutable
    word = "home"
    updated_word = "H" + word[1:]  # word[0] = "H" would raise TypeError

    return {
        "first_item": first_item,
        "nested_sublist": nested_sublist,
        "nested_name": nested_name,
        "modified_list": items,
        "had_four": had_four,
        "paul_index": paul_index,
        "reversed_list": numbers_to_reverse,
        "reverse_return": reverse_return,
        "updated_word": updated_word,
    }


def demonstrate_tuples() -> dict:
    """Demonstrate tuples, single-element trailing comma, tuple('Ana'), and methods."""
    colors_tuple = ("blue", "green", "yellow", "blue", "red")

    # Classic gotcha: (1) is an int; (1,) with a trailing comma is a tuple
    not_a_tuple = (1)
    single_item_tuple = (1,)

    # tuple("Ana") iterates over string characters
    ana_characters = tuple("Ana")
    ana_single_tuple = ("Ana",)

    blue_count = colors_tuple.count("blue")
    green_index = colors_tuple.index("green")

    # Note: lists also allow duplicates; the real distinction is mutability
    list_with_duplicates = ["blue", "blue", "green"]

    return {
        "colors_tuple": colors_tuple,
        "not_a_tuple_type": type(not_a_tuple).__name__,
        "single_item_tuple_type": type(single_item_tuple).__name__,
        "ana_characters": ana_characters,
        "ana_single_tuple": ana_single_tuple,
        "blue_count": blue_count,
        "green_index": green_index,
        "list_with_duplicates": list_with_duplicates,
    }


def demonstrate_lifo_stack() -> dict:
    """Simulate a LIFO stack of papers using .append(), .pop(), and len()."""
    paper_stack = []

    # Push items onto the top of the stack (Last In)
    paper_stack.append("January Invoice")
    paper_stack.append("Signed Contract")
    paper_stack.append("Urgent Report")

    initial_size = len(paper_stack)

    # Pop items from the top of the stack (First Out)
    first_popped = paper_stack.pop()
    second_popped = paper_stack.pop()
    remaining_size = len(paper_stack)

    return {
        "initial_size": initial_size,
        "first_popped": first_popped,
        "second_popped": second_popped,
        "remaining_size": remaining_size,
        "remaining_stack": paper_stack,
    }


def main() -> None:
    """Run Chapter 13 demonstrations."""
    print("=== CH. 13: LISTS ===")
    print(demonstrate_lists())
    print("\n=== CH. 13: TUPLES ===")
    print(demonstrate_tuples())
    print("\n=== CH. 13: LIFO STACKS ===")
    print(demonstrate_lifo_stack())


if __name__ == "__main__":
    main()

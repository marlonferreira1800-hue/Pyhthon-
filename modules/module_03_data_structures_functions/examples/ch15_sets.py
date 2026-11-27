"""Module 3 — Chapter 15: Numeric Sets (set).

Demonstrates unindexed duplicate-free collections, .union(), .intersection(),
.update(), subset checks (<=), and set difference (-).
"""


def demonstrate_sets() -> dict:
    """Run fundamental set theory operations in Python."""
    a = {1, 2, 3}
    deduplicated = {1, 2, 2, 3, 3, 3}  # automatically becomes {1, 2, 3}

    s1 = {1, 2, 3, 4, 5}
    s2 = {2, 3}
    s3 = {3, 4, 6}

    union_set = a.union(s3)               # {1, 2, 3, 4, 6}
    intersection_set = s1.intersection(s3)  # {3, 4}
    is_subset = s2 <= s1                  # True
    not_subset = s3 <= s1                 # False (6 is not in s1)
    difference_set = {1, 2, 3} - {2}      # {1, 3}

    # .update() modifies the target set in-place
    a_updated = a.copy()
    a_updated.update({4, 5})

    return {
        "a": a,
        "deduplicated": deduplicated,
        "union": union_set,
        "intersection": intersection_set,
        "is_subset": is_subset,
        "not_subset": not_subset,
        "difference": difference_set,
        "a_updated": a_updated,
    }


def main() -> None:
    """Run Chapter 15 demonstration."""
    print("=== CH. 15: SETS ===")
    for label, value in demonstrate_sets().items():
        print(f"  {label}: {value}")


if __name__ == "__main__":
    main()

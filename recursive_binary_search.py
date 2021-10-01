from typing import Optional, List


def search(sorted_list: List[int], item, *, first: int = None, last: int = None) -> Optional[int]:
    first = 0 if not first else first
    last = len(sorted_list) - 1 if not last else last  # List index starts at 0 -> len - 1
    mid = (first + last) // 2

    if first >= last:
        return None

    # Check if element was found
    if sorted_list[mid] == item:
        return mid

    # Call function
    if sorted_list[mid] > item:
        return search(sorted_list, item, first=first, last=mid - 1)

    return search(sorted_list, item, first=mid + 1, last=last)

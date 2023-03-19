# These fields are used to match list items by checking the elements within the list item dictionary.
matching_fields = [
    ["Name"],
    ["Element", "RowName"],
    ["RowName"],
    ["TagName"],
]

# Always copy the entire contents of these fields, do not attempt to merge them.
# This is important for fields that are glorified lists that you might remove elements from them.
noindex_fields = [
    "GameplayTags",
]

# A special key, if it exists in a dict and the value matches, the element will be removed
delete_key = "~delete"
delete_value = True


def merge(schema: dict, key, value):
    """
    Check the value of a dict key and recursively merge.

    Typically called inside of `merge_xxx()`
    """
    if key in noindex_fields:
        schema[key] = value
    elif isinstance(value, list):
        merge_list(schema[key], value)
    elif isinstance(value, dict):
        if delete_key in value and value[delete_key] == delete_value:
            if key in schema:
                del schema[key]
        else:
            merge_dict(schema[key], value)
    else:
        schema[key] = value


def merge_dict(a: dict, b: dict):
    """
    Merge two dictionaries.
    """
    for key, value in b.items():
        merge(a, key, value)


def merge_list(a: list, b: list):
    """
    Merge two lists.

    In order for this to work, the lists must be lists of dictionaries and contain some kind of identifying feature.
    This is commonly the "Name" element, or the "Element" > "Row Name" elements.
    """
    for item in b:
        if not isinstance(item, dict):
            # cannot merge anonymous lists
            print("WARN: cannot merge non-dictionary list items ({}}".format(item))
            continue

        # Find element in `a` with matching "Name" key
        match = match_list_element(a, item)
        if match is None:
            a.append(item)
        else:
            if delete_key in item and item[delete_key] == delete_value:
                a.remove(match)
            else:
                for key, value in item.items():
                    merge(match, key, value)


def match_list_element(arr, item):
    """
    Scans the list item for elements inside the item dictionary and tries to match it to a corresponding item in `arr`.

    Returns `None` if it cannot find a match.
    """
    for opt in arr:
        if not isinstance(opt, dict):
            continue

        # Loop of different fields we can use to match list elements
        for match_set in matching_fields:
            # all the fields must match a nested dict structure
            left = opt
            right = item
            last = len(match_set) - 1
            for index, match_field in enumerate(match_set):
                if match_field in left and match_field in right:
                    if index == last:
                        # For the last field in the match set, we compare the actual value instead of nesting
                        if left[match_field] == right[match_field]:
                            return opt
                        else:
                            break
                    else:
                        # Not the last field, continue recursion
                        left = left[match_field]
                        right = right[match_field]
                else:
                    break

    return None

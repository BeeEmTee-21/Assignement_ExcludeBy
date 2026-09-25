# Collection Comparison Utility

## Description
This is a comparison python utility that takes two lists, compares
them against one another, identifies matching values and returns the 
non-matching values as a new list.

## Problem
While working on a project, I realized I had two lists which I wanted
to identify the values that were not present in the second list. Those are the 
non-matching values.

## Features

- Compares values between two lists
- Uses exact equality to identify matching and non-matching values
- Adds all non-matching values to a new list
- Returns a list containing all non-matching values

## How It Works

The utility is implemented as a reusable Python function that accepts two parameters: `source` and `comparison`.

The function loops through the `source` list and checks whether each value is present in the `comparison` list. If a value exists in the `source` list but not in the `comparison` list, it is considered a non-matching value.

Each non-matching value is appended to a new list that is created when the function is called. After all values in the `source` list have been checked, the function returns the new list containing the non-matching values.

## Usage

Import the `exclude_by` function from the utility:

```python
from collection_comparison_utility import exclude_by as eb

names_of_students = [
    "Prince",
    "Abigail",
    "Vivian",
    "Hannah",
    "Richard",
    "Pius",
    "Bernard"
]

names_of_students_present = [
    "Bernard",
    "Abigail",
    "Richard",
    "Pius"
]

results = eb(names_of_students, names_of_students_present)

print(f"List of students not present: {results}")
```

### Expected Output

```text
List of students not present: ['Prince', 'Vivian', 'Hannah']
```

## Parameters

The function accepts two parameters: `source` and `comparison`.

### `source`

The `source` parameter represents the original list of values that will be checked. It acts as the main collection from which non-matching values will be returned.

### `comparison`

The `comparison` parameter represents the list of values that will be compared against the `source` list. Any value from `source` that is not found in `comparison` is treated as a non-matching value.


## Limitations

The current implementation has the following limitations:

- It supports exact matching only.
- Matching is case-sensitive.
- The function is currently designed to work with lists.

## Future Improvements

The current implementation provides a simple foundation for comparing two lists using exact matching. Future versions of the utility are intended to make the comparison process more flexible and reusable.

Planned improvements include:

- Allowing users to define their own comparison rules.
- Supporting case-insensitive matching.
- Supporting partial or substring matching.
- Allowing users to decide whether matching or non-matching values should be returned.
- Expanding support beyond lists to other iterable data structures.
- Adding built-in comparison strategies for common use cases.
- Improving error handling for invalid inputs or comparison rules.
- Adding automated tests to verify expected behavior.
- Packaging the utility as a reusable Python library that can be imported into other projects.

## Installation / Setup

The utility can be used by placing the Python file containing the `exclude_by` function in the same project directory as the file where it will be used.

The function can then be imported with:

```python
from collection_comparison_utility import exclude_by
```

It can also be imported with an alias:

```python
from collection_comparison_utility import exclude_by as eb
```

No external Python libraries are required for the current implementation.

## What I Learned

While building this project, I learned that modifying a list while iterating through it can lead to unexpected results because the structure of the list changes during the loop.

I also learned that creating a new list for the result is a safer approach because it allows the original source data to remain unchanged.

This project also helped me understand how the `in` and `not in` operators can be used to check whether values are present in a collection.

Another important lesson was the value of writing reusable functions. By using generic parameters such as `source` and `comparison`, the function is not limited to only names and can be reused with different kinds of list data.

Finally, the project introduced me to the idea of designing software for future expansion. Although the current implementation uses exact matching, future versions can allow users to provide their own comparison rules and decide how values should be considered a match.
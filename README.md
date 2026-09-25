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


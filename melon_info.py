"""Print out all the melons in our inventory."""


from melons import melon_types


def print_melons(types):
    """Print each melon with corresponding attribute information."""
    # iterate over passed in dictionary grabbing the key(melon) and the value (dictionary of melon attributes)
    for melon, attributes in types.items():
        print(melon.upper())
        # iterate over the dictionary associated with each melon key printing each key value pair
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

print_melons(melon_types)
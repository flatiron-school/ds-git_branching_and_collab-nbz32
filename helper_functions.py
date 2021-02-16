def first_no_spaces(str_list):
    """This function will remove whitespace from
    a list of strings and then return the one that
    is alphabetically first."""
    return min([x.replace(' ', '') for x in str_list])
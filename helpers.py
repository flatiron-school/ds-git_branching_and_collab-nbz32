def first_no_spaces(str_list):
    return min([x.replace(' ', '') for x in str_list])

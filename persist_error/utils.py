"""
Utility functions.

"""


def search_dictionary_list(dict_list, search_key, search_value):
    """
    Search through a list of dictionary for particular key value pair.

    :param list dict_list: list of dictionaries
    :param str search_key: the key to search for
    :param search_value: the value to look for
    :return: a list of matching dictionaries
    :rtype: list

    """
    result = list(filter(lambda x: x[search_key] == search_value, dict_list))
    return result

"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    [wagon_one, wagon_two, locomotive, *other_wagons] = each_wagons_id
    wagons_list = [locomotive, *missing_wagons,  *other_wagons, wagon_one, wagon_two]
    return wagons_list


def add_missing_stops(route,**args):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = [*args.values()]
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route_info = {**route, **more_route_information}
    return extended_route_info

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    row_one = []
    row_two = []
    row_three = []
    
    for item in wagons_rows:
        row_one.append(item[0])
        row_two.append(item[1])
        row_three.append(item[2])
    sorted_wagons = [row_one,row_two,row_three]

    return sorted_wagons

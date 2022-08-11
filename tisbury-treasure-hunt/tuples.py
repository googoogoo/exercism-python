def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    coordinate = record[1]
    return coordinate


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    coordinate_characters = list(coordinate)
    coordinate_new = (coordinate_characters[0], coordinate_characters[1])
    return coordinate_new


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    azara = convert_coordinate(azara_record[1])

    rui = rui_record[1]

    return bool(azara == rui)


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    comparison = compare_records(azara_record, rui_record)

    if comparison is True:
        c_c = azara_record + rui_record
        return c_c
    if comparison is False:
        return 'not a match'


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """

    clean_coordinates = []
    formated_coordinates = []
    report = []

    for coordinate in combined_record_group:
        clean_coordinate = (coordinate[0], coordinate[2],coordinate[3], coordinate[4])
        clean_coordinates.append(clean_coordinate)

    for coordinate in clean_coordinates:
        formated_coordinate = format(coordinate)
        formated_coordinates.append(formated_coordinate)

    report = "\n".join(formated_coordinates)

    final_report = report + '\n'

    return final_report

def export_flashcards(
    flashcards,
    field_option='tab',
    record_option='newline',
    custom_field=None,
    custom_record=None,
):
    """
    Export flashcards to a formatted string.

    Args:
        flashcards (list of dict): A list of flashcards, where each flashcard
            is a dictionary with 'front' and 'back' keys.
        field_option (str, optional): The field delimiter option. Can be 'tab',
            'comma', or 'custom'. Defaults to 'tab'.
        record_option (str, optional): The record delimiter option. Can be
            'newline', 'semicolon', or 'custom'. Defaults to 'newline'.
        custom_field (str, optional): Custom field delimiter if field_option
            is 'custom'. Defaults to None.
        custom_record (str, optional): Custom record delimiter if record_option
            is 'custom'. Defaults to None.

    Returns:
        str: The formatted string of flashcards.
    """
    if field_option == 'custom' and custom_field:
        field_delim = custom_field
    elif field_option == 'comma':
        field_delim = ','
    else:
        field_delim = '\t'

    if record_option == 'custom' and custom_record:
        record_delim = custom_record
    elif record_option == 'semicolon':
        record_delim = ';'
    else:
        record_delim = '\n'

    exported_lines = [
        f'{card["front"]}{field_delim}{card["back"]}' for card in flashcards
    ]
    export_text = record_delim.join(exported_lines)
    return export_text

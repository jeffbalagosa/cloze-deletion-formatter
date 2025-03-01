def export_flashcards(
    flashcards,
    field_option="tab",
    record_option="newline",
    custom_field=None,
    custom_record=None,
):
    # Determine the actual field separator.
    if field_option == "custom" and custom_field:
        field_delim = custom_field
    elif field_option == "comma":
        field_delim = ","
    else:
        field_delim = "\t"  # Default Tab

    # Determine the actual record separator.
    if record_option == "custom" and custom_record:
        record_delim = custom_record
    elif record_option == "semicolon":
        record_delim = ";"
    else:
        record_delim = "\n"  # Default New Line

    # Build the export string.
    exported_lines = [
        f"{card['front']}{field_delim}{card['back']}" for card in flashcards
    ]
    export_text = record_delim.join(exported_lines)
    return export_text

"""Constants for the ``server_guardian_api`` app."""

SERVER_STATUS = {  # pragma: no cover
    'OK': 'OK',
    'WARNING': 'WARNING',
    'DANGER': 'DANGER',
}

ERROR_RESPONSE = {
    'status': SERVER_STATUS['DANGER'],
    'info': 'The server encountered an error while running the processor. '
}

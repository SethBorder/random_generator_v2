

VARIABLE_REGEX = r'([a-zA-Z]\w*)'
NUMBER_RE = r'(\d+(?:\.\d+)?)'
ARGUMENT_RE = fr'({NUMBER_RE}|{VARIABLE_REGEX})'
ARGUMENT_WITH_COMMA_RE = fr'({ARGUMENT_RE}, *)'
FUNCTION_REGEX = fr'({VARIABLE_REGEX}\({ARGUMENT_WITH_COMMA_RE}*{ARGUMENT_RE}?\))'

import logger

# Check one test case: assert it, then print whether it passed
def check(description, actual, expected):
    assert actual == expected, description
    print("PASS: " + description)

# Test is_valid_name
check("valid last name, letters only", logger.is_valid_name("Smith"), True)
check("valid hyphenated name", logger.is_valid_name("Smith-Jones"), True)
check("valid name with apostrophe", logger.is_valid_name("O'Brien"), True)
check("empty name is invalid", logger.is_valid_name(""), False)
check("name with a digit is invalid", logger.is_valid_name("Sm1th"), False)
check("name with punctuation other than hyphen/apostrophe is invalid", logger.is_valid_name("Smith!"), False)
check("name that is only a hyphen (no letters) is invalid", logger.is_valid_name("-"), False)
check("name that is only an apostrophe (no letters) is invalid", logger.is_valid_name("'"), False)

# Test to_sentence_case
check("capitalizes first letter and letter after hyphen", logger.to_sentence_case("smith-jones"), "Smith-Jones")
check("normalizes all-caps name and capitalizes letter after apostrophe", logger.to_sentence_case("O'BRIEN"), "O'Brien")
check("capitalizes letter after each of multiple hyphens", logger.to_sentence_case("mary-jane-smith"), "Mary-Jane-Smith")
check("normalizes all-caps hyphenated name", logger.to_sentence_case("SMITH-JONES"), "Smith-Jones")

# Test is_valid_email
check("valid .mil email", logger.is_valid_email("john.doe@af.mil"), True)
check("valid .gov email", logger.is_valid_email("john.doe@af.gov"), True)
check("domain is not .mil or .gov", logger.is_valid_email("john.doe@gmail.com"), False)
check("missing @ symbol", logger.is_valid_email("johndoe.mil"), False)
check("uppercase domain is still valid (case-insensitive)", logger.is_valid_email("JOHN.DOE@AF.MIL"), True)
check("multiple @ symbols", logger.is_valid_email("john@doe@af.mil"), False)
check("missing username before @", logger.is_valid_email("@af.mil"), False)
check("missing domain after @", logger.is_valid_email("john@"), False)
check("domain contains .mil but does not end with it", logger.is_valid_email("john@af.mil.com"), False)

# Test is_valid_phone
check("valid 10-digit phone number", logger.is_valid_phone("1234567890"), True)
check("phone number too short (9 digits)", logger.is_valid_phone("123456789"), False)
check("phone number has hyphens", logger.is_valid_phone("123-456-7890"), False)
check("phone number has a letter mixed in", logger.is_valid_phone("123456789a"), False)

# Test is_not_empty
check("non-empty text is valid", logger.is_not_empty("something"), True)
check("empty text is invalid", logger.is_not_empty(""), False)

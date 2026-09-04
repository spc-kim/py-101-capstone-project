import logger

# Check one test case: assert it, then print whether it passed
def check(description, actual, expected):
    assert actual == expected, description
    print("PASS: " + description)

# Test is_valid_name
check("is_valid_name('Smith')", logger.is_valid_name("Smith"), True)
check("is_valid_name('Smith-Jones')", logger.is_valid_name("Smith-Jones"), True)
check("is_valid_name(\"O'Brien\")", logger.is_valid_name("O'Brien"), True)
check("is_valid_name('')", logger.is_valid_name(""), False)
check("is_valid_name('Sm1th')", logger.is_valid_name("Sm1th"), False)
check("is_valid_name('Smith!')", logger.is_valid_name("Smith!"), False)
check("is_valid_name('-')", logger.is_valid_name("-"), False)
check("is_valid_name(\"'\")", logger.is_valid_name("'"), False)

# Test to_sentence_case
check("to_sentence_case('smith-jones')", logger.to_sentence_case("smith-jones"), "Smith-Jones")
check("to_sentence_case(\"O'BRIEN\")", logger.to_sentence_case("O'BRIEN"), "O'Brien")
check("to_sentence_case('mary-jane-smith')", logger.to_sentence_case("mary-jane-smith"), "Mary-Jane-Smith")
check("to_sentence_case('SMITH-JONES')", logger.to_sentence_case("SMITH-JONES"), "Smith-Jones")

# Test is_valid_email
check("is_valid_email('john.doe@af.mil')", logger.is_valid_email("john.doe@af.mil"), True)
check("is_valid_email('john.doe@af.gov')", logger.is_valid_email("john.doe@af.gov"), True)
check("is_valid_email('john.doe@gmail.com')", logger.is_valid_email("john.doe@gmail.com"), False)
check("is_valid_email('johndoe.mil')", logger.is_valid_email("johndoe.mil"), False)
check("is_valid_email('JOHN.DOE@AF.MIL')", logger.is_valid_email("JOHN.DOE@AF.MIL"), True)
check("is_valid_email('john@doe@af.mil')", logger.is_valid_email("john@doe@af.mil"), False)
check("is_valid_email('@af.mil')", logger.is_valid_email("@af.mil"), False)
check("is_valid_email('john@')", logger.is_valid_email("john@"), False)
check("is_valid_email('john@af.mil.com')", logger.is_valid_email("john@af.mil.com"), False)

# Test is_valid_phone
check("is_valid_phone('1234567890')", logger.is_valid_phone("1234567890"), True)
check("is_valid_phone('123456789')", logger.is_valid_phone("123456789"), False)
check("is_valid_phone('123-456-7890')", logger.is_valid_phone("123-456-7890"), False)
check("is_valid_phone('123456789a')", logger.is_valid_phone("123456789a"), False)

# Test is_not_empty
check("is_not_empty('something')", logger.is_not_empty("something"), True)
check("is_not_empty('')", logger.is_not_empty(""), False)

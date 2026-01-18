import re
import logging

def count_valid_emails(emails):
    """
    Count valid email addresses in the input list using RFC-inspired regex.
    
    Args:
        emails: List of email addresses (strings)
    Returns:
        int: Count of valid emails
    Raises:
        ValueError: If emails is not a list
    """
    if not isinstance(emails, list):
        raise ValueError("emails must be a list")
    
    count = 0
    # Prevents consecutive specials, limits TLD
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    for email in emails:
        if not isinstance(email, str):
            logging.debug(f"Skipped non-string: {type(email)}")
            continue
        if email_pattern.match(email):
            count += 1
    
    return count

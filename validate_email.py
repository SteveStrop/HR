def fun(s):
    # return True if s is a valid email, else return False
    s = s.replace('@', ' ',1).replace('.', ' ',1).split()
    if len(s) != 3:
        return False

    username, website, ext = s[0], s[1], s[2]

    # check if ext is valid
    if len(ext) > 3:
        return False
    # check if username is valid
    if not (website + username.replace('-', '').replace('_', '')).isalnum():
        return False

    return True


def filter_mail(emails):
    filtered_emails = list(filter(fun, emails))
    filtered_emails.sort()
    return filtered_emails


emails = ['lara@hackerrank.com', 'brian*23@hackerrank.com', 'britts_54@hackerrank.com']
filtered_emails = filter_mail(emails)
print(filtered_emails)

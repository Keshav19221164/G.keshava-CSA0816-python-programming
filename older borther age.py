def find_younger_brother_age(older_brother_age, older_brother_age_when_younger_was_5):
    age_difference = older_brother_age - older_brother_age_when_younger_was_5
    younger_brother_age = older_brother_age - age_difference
    return younger_brother_age

def find_older_brother_age_when_younger_was_5(older_brother_age, younger_brother_age):
    age_difference = older_brother_age - younger_brother_age
    older_brother_age_when_younger_was_5 = older_brother_age - age_difference
    return older_brother_age_when_younger_was_5

def main():
    older_brother_age = 56
    younger_brother_age = 24
    older_brother_age_when_younger_was_5 = find_older_brother_age_when_younger_was_5(older_brother_age, younger_brother_age)
    younger_brother_age_when_older_was_5 = find_younger_brother_age(older_brother_age, older_brother_age_when_younger_was_5)
    print("Younger brother's age when older brother was 5:", younger_brother_age_when_older_was_5)


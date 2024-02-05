def gather_credits(credits_needed, *args):
    gathered_credits = 0
    courses = []

    for course, credits in args:
        if gathered_credits >= credits_needed:
            break

        if course in courses:
            continue

        courses.append(course)
        gathered_credits += credits

    result = ""
    if gathered_credits >= credits_needed:

        result += f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
        result += f"Courses: "

        for c in sorted(courses):
            result += c + ", "

        result = result.strip(", ")

    else:
        result += f"You need to enroll in more courses! You have to gather {credits_needed - gathered_credits} credits more."

    return result

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))



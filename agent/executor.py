from tools.email_sender import send_email
from tools.logger import log_message
def get_template(goal):
    goal = goal.lower()
    if "welcome" in goal:

        file = "templates/welcome.txt"

    elif "reminder" in goal:

        file = "templates/reminder.txt"

    else:

        file = "templates/internship.txt"

    with open(file, "r") as f:
        return f.read()


def execute_plan(
    receiver,
    goal
):
    content = get_template(goal)

    lines = content.split("\n")

    subject = lines[0].replace(
        "Subject:",
        ""
    ).strip()

    body = "\n".join(lines[1:])

    send_email(
        receiver,
        subject,
        body
    )

    log_message(
        f"Email sent to {receiver}"
    )

    return content
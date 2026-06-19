def generate_bullets(job_title, experience, skill):
    bullets = [
        f"Supported daily operations related to {job_title} in a fast-paced environment.",
        f"Used experience in {experience} to improve productivity, communication, and workflow.",
        f"Applied {skill} to solve problems, support team goals, and stay organized.",
        "Demonstrated reliability, teamwork, and adaptability while meeting business needs."
    ]

    return bullets


print("AI Resume Helper")
print("----------------")

job_title = input("What job are you applying for? ")
experience = input("What experience do you want to highlight? ")
skill = input("What is one skill you want to include? ")

resume_bullets = generate_bullets(job_title, experience, skill)

print("\nSuggested Resume Bullet Points:\n")

for bullet in resume_bullets:
    print("- " + bullet)

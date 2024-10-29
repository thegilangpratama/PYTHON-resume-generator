import random
from faker import Faker
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Initialize faker with locale for realistic names
fake = Faker()

# Skill options to choose from
skills = [
    "Python", "JavaScript", "React", "Node.js", "SQL", "MongoDB",
    "Docker", "Kubernetes", "Git", "AWS", "Azure", "Java", "C++",
    "Swift", "HTML", "CSS", "TypeScript", "GraphQL", "Machine Learning",
    "Data Analysis", "UI/UX Design", "Agile Methodology", "REST API"
]

# Job titles to randomly assign
job_titles = [
    "Software Engineer", "Data Scientist", "Frontend Developer",
    "Backend Developer", "Full Stack Developer", "Product Manager",
    "System Administrator", "DevOps Engineer", "Data Analyst",
    "AI Researcher", "QA Engineer", "Network Engineer"
]

# Education backgrounds
education_levels = [
    "Bachelor of Science in Computer Science",
    "Bachelor of Engineering in Information Technology",
    "Master of Science in Data Science",
    "Bachelor of Arts in Graphic Design",
    "Master of Science in Artificial Intelligence",
    "Bachelor of Commerce in Information Systems"
]

# Generate a random resume


def generate_resume():
    resume = {
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Location": fake.city() + ", " + fake.country(),
        "Job Title": random.choice(job_titles),
        "Summary": fake.text(max_nb_chars=200),
        "Skills": random.sample(skills, k=5),
        "Education": random.choice(education_levels),
        "Experience": [
            {
                "Company": fake.company(),
                "Position": random.choice(job_titles),
                "Duration": f"{random.randint(1, 5)} years",
                "Description": fake.text(max_nb_chars=100)
            }
            for _ in range(2)
        ]
    }
    return resume

# Function to create a PDF for each resume


def save_resume_to_pdf(resume, filename):
    pdf = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    pdf.setFont("Helvetica", 12)

    # Define starting position
    x, y = 50, height - 50
    line_spacing = 14

    # Header
    pdf.setFillColor(colors.darkblue)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(x, y, resume["Name"])
    pdf.setFont("Helvetica", 12)
    y -= line_spacing
    pdf.drawString(x, y, resume["Job Title"])
    y -= line_spacing * 2

    # Contact Information
    pdf.setFillColor(colors.black)
    pdf.drawString(x, y, f"Email: {resume['Email']}")
    y -= line_spacing
    pdf.drawString(x, y, f"Phone: {resume['Phone']}")
    y -= line_spacing
    pdf.drawString(x, y, f"Location: {resume['Location']}")
    y -= line_spacing * 2

    # Summary
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, "Summary:")
    pdf.setFont("Helvetica", 12)
    y -= line_spacing
    pdf.drawString(x, y, resume["Summary"])
    y -= line_spacing * 2

    # Skills
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, "Skills:")
    pdf.setFont("Helvetica", 12)
    y -= line_spacing
    pdf.drawString(x, y, ", ".join(resume["Skills"]))
    y -= line_spacing * 2

    # Education
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, "Education:")
    pdf.setFont("Helvetica", 12)
    y -= line_spacing
    pdf.drawString(x, y, resume["Education"])
    y -= line_spacing * 2

    # Experience
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, "Experience:")
    pdf.setFont("Helvetica", 12)
    for exp in resume["Experience"]:
        y -= line_spacing
        pdf.drawString(x, y, f"Company: {exp['Company']}")
        y -= line_spacing
        pdf.drawString(x, y, f"Position: {exp['Position']}")
        y -= line_spacing
        pdf.drawString(x, y, f"Duration: {exp['Duration']}")
        y -= line_spacing
        pdf.drawString(x, y, f"Description: {exp['Description']}")
        y -= line_spacing * 2

    pdf.save()


# Generate and save 20 resumes as PDF
for i in range(1, 21):
    resume = generate_resume()
    filename = f"resume_{i}.pdf"
    save_resume_to_pdf(resume, filename)
    print(f"Generated {filename}")

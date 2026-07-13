"""
Institutional Knowledge Base — College Admission RAG Context
This module provides structured admission data used as retrieved context
for the Watsonx.ai Granite model (RAG pattern).
"""

INSTITUTION_NAME = "Greenfield University"
INSTITUTION_TAGLINE = "Shaping Tomorrow's Leaders"

# ─────────────────────────────────────────────
# COURSES & PROGRAMMES
# ─────────────────────────────────────────────
COURSES = {
    "B.Tech Computer Science & Engineering": {
        "duration": "4 Years",
        "seats": 120,
        "eligibility": "10+2 with Physics, Chemistry, Maths (PCM) with minimum 60% aggregate. JEE Main score required.",
        "cutoff_general": 85,
        "cutoff_obc": 75,
        "cutoff_sc_st": 65,
        "annual_fee": "₹1,20,000",
        "hostel_fee": "₹60,000/year",
        "specializations": ["AI & Machine Learning", "Cybersecurity", "Cloud Computing", "Data Science"],
        "placement_avg": "₹8.5 LPA",
        "placement_highest": "₹42 LPA",
    },
    "B.Tech Electronics & Communication Engineering": {
        "duration": "4 Years",
        "seats": 90,
        "eligibility": "10+2 with PCM, minimum 60% aggregate. JEE Main score required.",
        "cutoff_general": 78,
        "cutoff_obc": 68,
        "cutoff_sc_st": 58,
        "annual_fee": "₹1,10,000",
        "hostel_fee": "₹60,000/year",
        "specializations": ["VLSI Design", "Embedded Systems", "IoT"],
        "placement_avg": "₹7.2 LPA",
        "placement_highest": "₹35 LPA",
    },
    "B.Tech Mechanical Engineering": {
        "duration": "4 Years",
        "seats": 90,
        "eligibility": "10+2 with PCM, minimum 55% aggregate. JEE Main score required.",
        "cutoff_general": 72,
        "cutoff_obc": 62,
        "cutoff_sc_st": 52,
        "annual_fee": "₹1,00,000",
        "hostel_fee": "₹60,000/year",
        "specializations": ["Robotics", "Thermal Engineering", "Manufacturing"],
        "placement_avg": "₹6.5 LPA",
        "placement_highest": "₹28 LPA",
    },
    "BCA (Bachelor of Computer Applications)": {
        "duration": "3 Years",
        "seats": 60,
        "eligibility": "10+2 in any stream with Mathematics, minimum 50% aggregate.",
        "cutoff_general": 70,
        "cutoff_obc": 60,
        "cutoff_sc_st": 50,
        "annual_fee": "₹75,000",
        "hostel_fee": "₹55,000/year",
        "specializations": ["Web Development", "Mobile Applications", "Database Management"],
        "placement_avg": "₹5.5 LPA",
        "placement_highest": "₹22 LPA",
    },
    "MBA (Master of Business Administration)": {
        "duration": "2 Years",
        "seats": 80,
        "eligibility": "Graduation in any stream with minimum 50% aggregate. CAT/MAT/XAT score required.",
        "cutoff_general": 80,
        "cutoff_obc": 70,
        "cutoff_sc_st": 60,
        "annual_fee": "₹1,50,000",
        "hostel_fee": "₹65,000/year",
        "specializations": ["Finance", "Marketing", "HR", "Operations", "Business Analytics"],
        "placement_avg": "₹10.2 LPA",
        "placement_highest": "₹48 LPA",
    },
    "M.Tech Computer Science": {
        "duration": "2 Years",
        "seats": 40,
        "eligibility": "B.Tech/B.E. in CS/IT or related field with minimum 60% aggregate. GATE score preferred.",
        "cutoff_general": 75,
        "cutoff_obc": 65,
        "cutoff_sc_st": 55,
        "annual_fee": "₹1,30,000",
        "hostel_fee": "₹60,000/year",
        "specializations": ["AI/ML", "Software Engineering", "Distributed Systems"],
        "placement_avg": "₹12.5 LPA",
        "placement_highest": "₹55 LPA",
    },
    "B.Sc Data Science": {
        "duration": "3 Years",
        "seats": 50,
        "eligibility": "10+2 with Mathematics, minimum 55% aggregate.",
        "cutoff_general": 68,
        "cutoff_obc": 58,
        "cutoff_sc_st": 48,
        "annual_fee": "₹80,000",
        "hostel_fee": "₹55,000/year",
        "specializations": ["Machine Learning", "Business Intelligence", "Statistical Analysis"],
        "placement_avg": "₹6.8 LPA",
        "placement_highest": "₹30 LPA",
    },
}

# ─────────────────────────────────────────────
# ADMISSION DEADLINES
# ─────────────────────────────────────────────
ADMISSION_DEADLINES = {
    "Application Form Opens": "1st March 2025",
    "Last Date for Application (UG)": "30th April 2025",
    "Last Date for Application (PG)": "15th May 2025",
    "Merit List Declaration (Round 1)": "10th June 2025",
    "Merit List Declaration (Round 2)": "25th June 2025",
    "Document Verification": "15th June – 5th July 2025",
    "Fee Payment Deadline (Round 1)": "20th June 2025",
    "Fee Payment Deadline (Round 2)": "5th July 2025",
    "Classes Commence": "1st August 2025",
    "Lateral Entry Application Deadline": "20th May 2025",
    "Scholarship Application Deadline": "10th June 2025",
}

# ─────────────────────────────────────────────
# SCHOLARSHIP PROGRAMMES
# ─────────────────────────────────────────────
SCHOLARSHIPS = [
    {
        "name": "Merit Excellence Scholarship",
        "eligibility": "Students with 90%+ in 10+2 board exams",
        "benefit": "50% tuition fee waiver for Year 1; continued with CGPA ≥ 8.5",
        "seats": 20,
    },
    {
        "name": "Need-Based Financial Aid",
        "eligibility": "Annual family income below ₹3 Lakhs",
        "benefit": "Up to 75% tuition fee waiver",
        "seats": 30,
    },
    {
        "name": "Sports Excellence Scholarship",
        "eligibility": "National or State level sports representation",
        "benefit": "25% tuition fee waiver + hostel benefit",
        "seats": 15,
    },
    {
        "name": "SC/ST/OBC Scholarship",
        "eligibility": "Students from reserved categories with valid certificate",
        "benefit": "As per Government of India norms; additional institutional top-up of ₹10,000/year",
        "seats": "As per reservation policy",
    },
    {
        "name": "Women in STEM Scholarship",
        "eligibility": "Female students admitted to B.Tech programs",
        "benefit": "₹20,000/year fee reduction for all 4 years",
        "seats": 25,
    },
]

# ─────────────────────────────────────────────
# ADMISSION PROCESS
# ─────────────────────────────────────────────
ADMISSION_PROCESS = """
**Step-by-Step Admission Process at Greenfield University:**

1. **Register Online**: Visit the official admissions portal and create an account using a valid email ID and mobile number.
2. **Fill Application Form**: Complete the application form with accurate personal, academic, and contact details.
3. **Upload Documents**: Upload scanned copies of required documents (10th & 12th mark sheets, ID proof, passport photo, category certificate if applicable).
4. **Pay Application Fee**: Pay the non-refundable application fee of ₹500 via online payment (UPI/Net Banking/Card).
5. **Entrance Score Submission**: Submit your JEE Main/CAT/MAT/GATE score as applicable for the chosen programme.
6. **Merit List Check**: Monitor the official portal for merit list announcements.
7. **Counselling/Document Verification**: Attend physical or online document verification as per the schedule.
8. **Fee Payment**: Complete the semester/annual fee payment to confirm your seat.
9. **Report to Campus**: Collect your admission kit and report on the specified orientation date.
"""

# ─────────────────────────────────────────────
# REQUIRED DOCUMENTS
# ─────────────────────────────────────────────
REQUIRED_DOCUMENTS = [
    "Class 10 Mark Sheet and Certificate",
    "Class 12 Mark Sheet and Certificate",
    "Transfer Certificate (TC) from last institution",
    "Character Certificate",
    "Valid Government-issued Photo ID (Aadhar/Passport/Voter ID)",
    "Passport-size Photographs (6 copies)",
    "JEE Main / CAT / MAT / GATE Score Card (as applicable)",
    "Category Certificate (SC/ST/OBC/EWS) – if applicable",
    "Income Certificate – for scholarship applicants",
    "Sports Certificate – for sports quota applicants",
    "Medical Fitness Certificate",
    "Migration Certificate (for students from other state boards)",
]

# ─────────────────────────────────────────────
# FACILITIES
# ─────────────────────────────────────────────
FACILITIES = {
    "Campus": "150-acre fully Wi-Fi enabled green campus",
    "Library": "Digital library with 50,000+ books, e-journals, IEEE/Springer access",
    "Hostel": "Separate AC/Non-AC hostels for boys and girls with 24×7 security",
    "Labs": "State-of-the-art computing, electronics, robotics, and research labs",
    "Sports": "Olympic-size swimming pool, cricket ground, football field, indoor sports complex",
    "Healthcare": "24×7 campus medical centre with ambulance facility",
    "Transport": "University buses covering 30+ city routes",
    "Cafeteria": "Multi-cuisine food court with hygiene-certified vendors",
    "Banking": "On-campus ATMs and bank branch (SBI)",
    "Placement Cell": "Dedicated Training & Placement office with 300+ recruiting companies",
}

# ─────────────────────────────────────────────
# FAQ — FREQUENTLY ASKED QUESTIONS
# ─────────────────────────────────────────────
FAQS = [
    {
        "category": "Eligibility & Entrance",
        "icon": "bi-patch-question-fill",
        "color": "indigo",
        "questions": [
            {
                "q": "What is the minimum percentage required for B.Tech admission?",
                "a": "For B.Tech programmes, you need a minimum of 60% aggregate in 10+2 with Physics, Chemistry, and Mathematics (PCM). For Mechanical Engineering, the minimum is 55%. A valid JEE Main score is also required."
            },
            {
                "q": "Is JEE Main score mandatory for all B.Tech programmes?",
                "a": "Yes, a valid JEE Main score is required for all B.Tech programmes at Greenfield University. However, there is no minimum JEE percentile cutoff — your merit rank is determined by a combination of board percentage and JEE score."
            },
            {
                "q": "Can students from Commerce or Arts background apply for BCA?",
                "a": "Yes! BCA (Bachelor of Computer Applications) is open to students from any stream (Science, Commerce, or Arts) in 10+2, provided they have Mathematics as a subject and a minimum 50% aggregate."
            },
            {
                "q": "What entrance exam is required for MBA admission?",
                "a": "For MBA admission, a valid score from CAT, MAT, or XAT is required. The minimum qualifying aggregate for graduation is 50% in any stream. Group Discussion (GD) and Personal Interview (PI) rounds follow shortlisting."
            },
            {
                "q": "Is GATE score compulsory for M.Tech admission?",
                "a": "GATE score is preferred and gives additional weightage in the merit list for M.Tech Computer Science. However, candidates without GATE may also apply and will be considered based on their B.Tech/B.E. academic performance."
            },
            {
                "q": "Is there a lateral entry option for B.Tech?",
                "a": "Yes, lateral entry admission to the 2nd year of B.Tech is available for Diploma holders in relevant engineering disciplines. The application deadline for lateral entry is 20th May 2025."
            },
        ],
    },
    {
        "category": "Fees & Payment",
        "icon": "bi-currency-rupee",
        "color": "green",
        "questions": [
            {
                "q": "What is the total fee for B.Tech CSE over 4 years?",
                "a": "The annual tuition fee for B.Tech CSE is ₹1,20,000. Over 4 years, the total tuition fee is approximately ₹4,80,000. Hostel fee (optional) is ₹60,000/year. Other charges such as library, sports, and examination fees may apply."
            },
            {
                "q": "Are there any payment plan options for fees?",
                "a": "Yes. Greenfield University offers semester-wise fee payment (2 instalments per year). Students facing financial hardship may apply for the Need-Based Financial Aid scheme, which can waive up to 75% of tuition fees."
            },
            {
                "q": "What is the application fee and is it refundable?",
                "a": "The application form processing fee is ₹500, payable online via UPI, Net Banking, or Debit/Credit Card. This fee is non-refundable once the application is submitted."
            },
            {
                "q": "Is the hostel fee included in the tuition fee?",
                "a": "No. Hostel accommodation is optional and charged separately. The hostel fee ranges from ₹55,000 to ₹65,000 per year depending on the programme, and covers accommodation, basic amenities, and mess facility."
            },
            {
                "q": "What happens if I miss the fee payment deadline?",
                "a": "If you miss the Round 1 fee payment deadline (20th June 2025), your provisional seat will be released to the next eligible candidate. A Round 2 opportunity is available until 5th July 2025. It is strongly advised to pay on time."
            },
        ],
    },
    {
        "category": "Admission Process",
        "icon": "bi-clipboard2-check-fill",
        "color": "cyan",
        "questions": [
            {
                "q": "How do I apply for admission to Greenfield University?",
                "a": "Visit the official admissions portal, register with your email and mobile number, fill the application form, upload required documents, pay the ₹500 application fee, and submit your entrance score. Applications open from 1st March 2025."
            },
            {
                "q": "What documents are required during admission?",
                "a": "You will need: Class 10 & 12 mark sheets, Transfer Certificate, Character Certificate, Photo ID (Aadhar/Passport/Voter ID), 6 passport-size photographs, JEE/CAT/MAT/GATE score card, and category certificate (if applicable)."
            },
            {
                "q": "Can I apply to more than one programme?",
                "a": "Yes, you can apply for up to 3 programmes in a single application form. A separate preference order must be specified. Seat allotment is based on merit and availability at the time of counselling."
            },
            {
                "q": "How is the merit list prepared?",
                "a": "The merit list for UG programmes is based on 60% weightage to board exam percentage and 40% to entrance exam score (JEE Main). For PG, it is based on 50% academic score and 50% entrance exam score, followed by GD/PI for MBA."
            },
            {
                "q": "When does the academic session begin?",
                "a": "Classes for the 2025–26 academic session commence on 1st August 2025. Students are required to report to campus before this date as per the orientation schedule communicated at the time of admission."
            },
        ],
    },
    {
        "category": "Scholarships & Financial Aid",
        "icon": "bi-award-fill",
        "color": "amber",
        "questions": [
            {
                "q": "How can I apply for the Merit Excellence Scholarship?",
                "a": "The Merit Excellence Scholarship is automatically awarded to students who scored 90% or above in their 10+2 board exams and are admitted to Greenfield University. No separate application is needed — eligibility is verified during document processing."
            },
            {
                "q": "What is the income limit for need-based financial aid?",
                "a": "The Need-Based Financial Aid programme supports students from families with an annual income below ₹3 Lakhs. Eligible students can receive up to 75% tuition fee waiver. You must submit a valid income certificate issued by a government authority."
            },
            {
                "q": "Is there a scholarship for female students in engineering?",
                "a": "Yes! The Women in STEM Scholarship offers a ₹20,000/year fee reduction for all 4 years of B.Tech programmes to female students. This is automatically applied at the time of admission for qualifying students."
            },
            {
                "q": "What is the deadline to apply for scholarships?",
                "a": "The scholarship application deadline is 10th June 2025. Late applications may not be considered. Ensure all supporting documents (income certificate, caste certificate, sports certificate) are submitted before the deadline."
            },
        ],
    },
    {
        "category": "Campus & Facilities",
        "icon": "bi-building-fill",
        "color": "purple",
        "questions": [
            {
                "q": "Does Greenfield University have hostel facilities?",
                "a": "Yes. The university has separate, fully secured hostels for boys and girls. Both AC and Non-AC options are available. Hostels are equipped with 24×7 security, Wi-Fi, laundry, and mess facilities. Hostel fee is ₹55,000–₹65,000/year."
            },
            {
                "q": "What sports facilities are available on campus?",
                "a": "The campus features an Olympic-size swimming pool, cricket ground, football field, basketball and volleyball courts, a fully equipped gymnasium, and an indoor sports complex. Sports excellence scholarships are also available."
            },
            {
                "q": "Is there a medical facility on campus?",
                "a": "Yes, a 24×7 medical centre staffed by qualified doctors and nurses is available on campus, along with an ambulance service. Tie-ups with nearby hospitals ensure emergency care is always accessible."
            },
            {
                "q": "How is the placement track record at Greenfield University?",
                "a": "The university has an excellent placement record with a 94% placement rate. Over 300 companies recruit from campus annually. The highest package offered is ₹55 LPA (M.Tech CS) and the average for B.Tech CSE is ₹8.5 LPA."
            },
            {
                "q": "Is the campus Wi-Fi enabled?",
                "a": "Yes, the entire 150-acre campus is fully Wi-Fi enabled with high-speed internet access in all academic buildings, hostels, library, and common areas. Students are issued a personal login upon admission."
            },
        ],
    },
]

# ─────────────────────────────────────────────
# DASHBOARD STATISTICS
# ─────────────────────────────────────────────
DASHBOARD_STATS = {
    "placement_by_year": {
        "labels": ["2020", "2021", "2022", "2023", "2024"],
        "avg_package": [5.2, 6.1, 6.8, 7.9, 8.5],
        "highest_package": [22, 28, 34, 38, 42],
        "placement_rate": [88, 89, 91, 93, 94],
    },
    "seats_by_course": {
        "labels": ["B.Tech CSE", "B.Tech ECE", "B.Tech Mech", "BCA", "MBA", "M.Tech CS", "B.Sc DS"],
        "seats":  [120, 90, 90, 60, 80, 40, 50],
        "colors": ["#4f46e5", "#06b6d4", "#10b981", "#f59e0b", "#8b5cf6", "#ef4444", "#ec4899"],
    },
    "applications_trend": {
        "labels": ["2020", "2021", "2022", "2023", "2024"],
        "applications": [3200, 4100, 5300, 6800, 8400],
    },
    "category_distribution": {
        "labels": ["General", "OBC", "SC", "ST", "EWS"],
        "values": [50, 27, 15, 5, 3],
        "colors": ["#4f46e5", "#06b6d4", "#10b981", "#f59e0b", "#8b5cf6"],
    },
}

# ─────────────────────────────────────────────
# COLLEGE PHOTO GALLERY
# ─────────────────────────────────────────────
GALLERY = [
    {
        "title": "Main Academic Block",
        "category": "Campus",
        "emoji": "🏛️",
        "bg": "linear-gradient(135deg, #1e3a5f 0%, #2d6a4f 100%)",
        "description": "The iconic main academic building with state-of-the-art classrooms and seminar halls.",
    },
    {
        "title": "Central Library",
        "category": "Academics",
        "emoji": "📚",
        "bg": "linear-gradient(135deg, #2c1654 0%, #4f46e5 100%)",
        "description": "Digital library with 50,000+ books, e-journals, IEEE, and Springer access.",
    },
    {
        "title": "Computer Science Lab",
        "category": "Academics",
        "emoji": "💻",
        "bg": "linear-gradient(135deg, #064e3b 0%, #0d9488 100%)",
        "description": "Advanced computing labs with the latest hardware and AI/ML software tools.",
    },
    {
        "title": "Sports Complex",
        "category": "Sports",
        "emoji": "🏊",
        "bg": "linear-gradient(135deg, #1e3a5f 0%, #0284c7 100%)",
        "description": "Olympic-size swimming pool and multi-sport indoor complex.",
    },
    {
        "title": "Boys Hostel — Block A",
        "category": "Hostel",
        "emoji": "🏠",
        "bg": "linear-gradient(135deg, #431407 0%, #c2410c 100%)",
        "description": "Modern AC hostel with 24×7 security, Wi-Fi, and fully equipped mess.",
    },
    {
        "title": "Girls Hostel — Ananya Hall",
        "category": "Hostel",
        "emoji": "🏡",
        "bg": "linear-gradient(135deg, #500724 0%, #be185d 100%)",
        "description": "Exclusively designed girls hostel with biometric access and security.",
    },
    {
        "title": "Robotics & AI Lab",
        "category": "Academics",
        "emoji": "🤖",
        "bg": "linear-gradient(135deg, #0c1445 0%, #312e81 100%)",
        "description": "Cutting-edge robotics lab featuring industrial robots, drones, and AI workstations.",
    },
    {
        "title": "Annual Tech Fest — Innovate",
        "category": "Events",
        "emoji": "🎉",
        "bg": "linear-gradient(135deg, #14532d 0%, #16a34a 100%)",
        "description": "University's flagship annual tech festival attracting 10,000+ participants.",
    },
    {
        "title": "Placement Drive 2024",
        "category": "Placements",
        "emoji": "💼",
        "bg": "linear-gradient(135deg, #1c1917 0%, #78350f 100%)",
        "description": "Campus placement drive with 300+ top companies including Google, TCS, and Infosys.",
    },
    {
        "title": "Green Campus",
        "category": "Campus",
        "emoji": "🌳",
        "bg": "linear-gradient(135deg, #052e16 0%, #15803d 100%)",
        "description": "Lush 150-acre eco-certified campus with sustainable energy and rainwater harvesting.",
    },
    {
        "title": "Cafeteria & Food Court",
        "category": "Campus",
        "emoji": "🍽️",
        "bg": "linear-gradient(135deg, #3b0764 0%, #7e22ce 100%)",
        "description": "Multi-cuisine food court with FSSAI-certified vendors and 500-seat capacity.",
    },
    {
        "title": "Convocation Ceremony 2024",
        "category": "Events",
        "emoji": "🎓",
        "bg": "linear-gradient(135deg, #1e3a5f 0%, #7c3aed 100%)",
        "description": "Annual convocation ceremony celebrating graduating students from all programmes.",
    },
]

GALLERY_CATEGORIES = ["All", "Campus", "Academics", "Hostel", "Sports", "Events", "Placements"]

# ─────────────────────────────────────────────
# CONTACT INFORMATION
# ─────────────────────────────────────────────
CONTACT = {
    "Admission Office": "+91-9876543210",
    "Email": "admissions@greenfielduniversity.edu.in",
    "Website": "www.greenfielduniversity.edu.in",
    "Address": "Greenfield University, Tech Valley Road, Bangalore – 560001, Karnataka, India",
    "Office Hours": "Monday to Saturday, 9:00 AM – 5:00 PM",
    "WhatsApp Helpline": "+91-9988776655",
}

# ─────────────────────────────────────────────
# RAG CONTEXT BUILDER
# ─────────────────────────────────────────────
def build_rag_context() -> str:
    """Build a comprehensive context string from all institutional data for RAG injection."""
    lines = [f"INSTITUTION: {INSTITUTION_NAME} — {INSTITUTION_TAGLINE}\n"]
    # FAQ section for RAG
    lines.append("\n=== FREQUENTLY ASKED QUESTIONS ===")
    for cat in FAQS:
        lines.append(f"\n[{cat['category']}]")
        for item in cat["questions"]:
            lines.append(f"  Q: {item['q']}")
            lines.append(f"  A: {item['a']}")

    lines.append("=== COURSES & ELIGIBILITY ===")
    for course, info in COURSES.items():
        lines.append(f"\n[{course}]")
        lines.append(f"  Duration: {info['duration']} | Seats: {info['seats']}")
        lines.append(f"  Eligibility: {info['eligibility']}")
        lines.append(f"  Cutoff (General/OBC/SC-ST): {info['cutoff_general']}% / {info['cutoff_obc']}% / {info['cutoff_sc_st']}%")
        lines.append(f"  Annual Fee: {info['annual_fee']} | Hostel: {info['hostel_fee']}")
        lines.append(f"  Specializations: {', '.join(info['specializations'])}")
        lines.append(f"  Avg Placement: {info['placement_avg']} | Highest: {info['placement_highest']}")

    lines.append("\n=== ADMISSION DEADLINES ===")
    for event, date in ADMISSION_DEADLINES.items():
        lines.append(f"  {event}: {date}")

    lines.append("\n=== SCHOLARSHIPS ===")
    for s in SCHOLARSHIPS:
        lines.append(f"  [{s['name']}] Eligibility: {s['eligibility']} | Benefit: {s['benefit']} | Seats: {s['seats']}")

    lines.append(f"\n=== ADMISSION PROCESS ===\n{ADMISSION_PROCESS}")

    lines.append("\n=== REQUIRED DOCUMENTS ===")
    for doc in REQUIRED_DOCUMENTS:
        lines.append(f"  - {doc}")

    lines.append("\n=== CAMPUS FACILITIES ===")
    for facility, desc in FACILITIES.items():
        lines.append(f"  {facility}: {desc}")

    lines.append("\n=== CONTACT ===")
    for key, val in CONTACT.items():
        lines.append(f"  {key}: {val}")

    return "\n".join(lines)


# Pre-built context for quick access
RAG_CONTEXT = build_rag_context()

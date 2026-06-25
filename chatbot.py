import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

# Download required NLTK resources (safe on import; quiet)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('stopwords', quiet=True)


# ==========================================
# TEXT PREPROCESSOR
# ==========================================
class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def preprocess(self, text: str) -> str:
        text = (text or '').lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        return " ".join(tokens)


# ==========================================
# PORTFOLIO ASSISTANT
# ==========================================
class PortfolioAssistant:
    def _has_words(self, text: str, words: list[str]) -> bool:
        return all(word in text for word in words)

    def _matches_phrase(self, text: str, phrases: list[str]) -> bool:
        return any(phrase in text for phrase in phrases)

    def get_response(self, raw_text: str, processed_text: str) -> dict:
        # Greeting — return short text and options
        if self._matches_phrase(raw_text, ["hello", "hi", "hey"]) or self._has_words(processed_text, ["hello"]):
            return {
                "text": "Hi — I'm Dhushyandh. I can help with:",
                "options": ["Skills", "Projects", "Education", "Experience", "AWS", "Azure", "Contact"]
            }

        # About
        if self._matches_phrase(raw_text, ["who are you", "about yourself"]) or self._has_words(processed_text, ["who", "you"]):
            return {"text": "I'm  Dhushyandh.", "options": []}

        # Name
        if self._matches_phrase(raw_text, ["your name"]) or processed_text.strip() == "name":
            return {"text": "Dhushyandh N.", "options": []}

        # Skills
        if self._has_words(processed_text, ["skill"]) or self._has_words(processed_text, ["technology"]):
            return {"text": "Frontend: HTML, CSS, JS, React, Tailwind;\n Backend: Node, Express;\n DB: MongoDB;\n Languages: Python, Java;\n Cloud: AWS, Azure.", "options": []}

        # Projects
        if self._has_words(processed_text, ["project"]):
            return {"text": "Projects: SmartMart; Portfolio Website; Voting System; Gemini Clone.", "options": []}

        # SmartMart
        if self._has_words(processed_text, ["smartmart"]):
            return {"text": "SmartMart — MERN e-commerce. Features: Auth, Products, Cart, Orders, Admin.", "options": []}

        # AWS
        if self._has_words(processed_text, ["aws"]) and not self._has_words(processed_text, ["service"]):
            return {"text": "AWS: IAM, S3, EC2, Cloud fundamentals, deployments.", "options": []}

        # Azure
        if self._has_words(processed_text, ["azure"]):
            return {"text": "Azure: Fundamentals, Hosting, Resource management.", "options": []}

        # Education
        if self._has_words(processed_text, ["education"]) or self._has_words(processed_text, ["college"]):
            return {"text": "I'm Currently pursuing B.E. — Computer Science Engineering.", "options": []}

        # Experience
        if self._has_words(processed_text, ["experience"]) or self._has_words(processed_text, ["internship"]):
            return {"text": "Experience: MERN stack, backend APIs, DB integration, cloud.", "options": []}

        # Goals
        if self._has_words(processed_text, ["goal"]) or self._has_words(processed_text, ["future"]):
            return {"text": "Goals: Full-stack role, cloud architecture, AI, scalable systems.", "options": []}

        # Resume
        if self._has_words(processed_text, ["resume"]):
            return {"text": "Resume: available on the portfolio (download link: https://dhushyandh.me/resume/Dhushyandh_Resume.pdf).", "options": []}

        # Contact
        if self._has_words(processed_text, ["contact"]):
            return {"text": "Contact:\n GitHub: https://github.com/dhushyandh \n LinkedIn: https://linkedin.com/in/dhushyandh \n Portfolio: https://dhushyandh.me\n Mobile: +91 9342763553", "options": []}

        # Goodbye
        if self._matches_phrase(raw_text, ["bye", "goodbye", "exit"]):
            return {"text": "Thanks — have a great day.", "options": []}

        # About Me / Extended
        if self._matches_phrase(raw_text, ["tell me about yourself", "introduce yourself", "who is dhushyandh", "about dhushyandh"]) or self._has_words(processed_text, ["tell", "yourself"]):
            return {
                "text": (
                    "Dhushyandh is a Computer Science Engineering student with a strong interest in Full-Stack Development, "
                    "Cloud Computing, and Software Engineering. He enjoys building practical applications, learning modern "
                    "technologies, and solving real-world problems through software development."
                ),
                "options": []
            }

        # Strengths
        if "strength" in processed_text:
            return {
                "text": (
                    "Key strengths include: Problem Solving; Quick Learning Ability; Full-Stack Development; Adaptability; "
                    "Continuous Improvement Mindset; Strong Interest in Emerging Technologies."
                ),
                "options": []
            }

        # Why Software Engineering
        if "why software engineering" in processed_text:
            return {
                "text": (
                    "Software engineering combines creativity, problem-solving, and technology to build impactful solutions. "
                    "Dhushyandh enjoys creating applications that solve real-world problems and continuously learning new technologies."
                ),
                "options": []
            }

        # Tech Stack
        if "tech stack" in processed_text:
            return {
                "text": (
                    "Primary Technology Stack: Frontend: React.js, JavaScript, Tailwind CSS; Backend: Node.js, Express.js; "
                    "Database: MongoDB; Cloud: AWS, Azure."
                ),
                "options": []
            }

        # Programming Languages
        if "programming language" in processed_text:
            return {
                "text": "Programming Languages: Java, Python, JavaScript.",
                "options": []
            }

        # Favorite Project
        if "proud project" in processed_text or "favorite project" in processed_text:
            return {
                "text": (
                    "SmartMart is one of the most significant projects developed by Dhushyandh. The project involved building a "
                    "complete MERN-stack e-commerce platform with authentication, product management, shopping cart functionality, and administrative controls."
                ),
                "options": []
            }

        # SmartMart Challenges
        if "challenge" in processed_text and "smartmart" in processed_text:
            return {
                "text": (
                    "During SmartMart development, challenges included authentication workflows, deployment configuration, "
                    "database integration, and debugging production issues. These experiences improved problem-solving and debugging skills."
                ),
                "options": []
            }

        # Learning from Projects
        if "learn from project" in processed_text:
            return {
                "text": (
                    "Projects have strengthened skills in Full-Stack Development, API Integration, Database Design, Deployment, "
                    "Debugging, and Software Architecture. They also improved independent learning ability."
                ),
                "options": []
            }

        # AI Projects
        if "ai project" in processed_text:
            return {"text": "Explored chatbot development and AI-inspired web applications.", "options": []}

        # AWS Services
        if "aws service" in processed_text:
            return {"text": "AWS Technologies: IAM, EC2, S3, Cloud fundamentals, Security Concepts, Deployment Workflows.", "options": []}

        # Deployment
        if "deploy" in processed_text or "hosting" in processed_text:
            return {"text": "Deployment experience includes Render, GitHub Pages, Vercel, and learning AWS/Azure deployment workflows.", "options": []}

        # Current Learning
        if "currently learning" in processed_text:
            return {"text": "Currently focusing on Cloud Computing, Advanced React, Backend Architecture, and Software Engineering best practices.", "options": []}

        # Team Work
        if "team" in processed_text:
            return {"text": "Comfortable collaborating, sharing ideas, and contributing to project goals; values communication and teamwork.", "options": []}

        # Debugging
        if "debug" in processed_text or "bug" in processed_text:
            return {"text": "Debugging approach: identify logs, reproduce, test incrementally, review docs, verify fixes.", "options": []}

        # Certifications
        if "certificate" in processed_text or "certification" in processed_text:
            return {"text": "Completed cloud and web development coursework and practical projects; certificates listed in portfolio.", "options": []}

        # Achievements
        if "achievement" in processed_text:
            return {"text": "Built multiple full-stack applications, deployed projects, learned cloud technologies, maintained active portfolio.", "options": []}

        # Why Hire You
        if "why should i hire you" in processed_text:
            return {"text": "Combines technical knowledge with willingness to learn; practical full-stack experience and cloud familiarity.", "options": []}

        # Five Year Plan
        if "five year" in processed_text:
            return {"text": "Aims to become a skilled Software Engineer with expertise in Full-Stack Development and Cloud Architecture.", "options": []}

        # Contact Recruiter
        if "linkedin" in processed_text or "github" in processed_text:
            return {"text": "Professional profiles: GitHub and LinkedIn links available on the portfolio.", "options": []}

        # Default
        return {"text": "Ask about: Skills, Projects, SmartMart, Education, Experience, AWS, Azure, Goals, Resume, Contact.", "options": []}


# Helper for external callers
preprocessor = TextPreprocessor()
assistant = PortfolioAssistant()

def get_chat_response(message: str) -> dict:
    raw = (message or '').strip().lower()
    processed = preprocessor.preprocess(message or '')
    return assistant.get_response(raw, processed)

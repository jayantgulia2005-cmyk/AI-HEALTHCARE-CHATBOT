from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime
import os


# Function to generate PDF report
def generate_pdf(chat_history):

    # Create reports folder
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Create timestamp
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    # PDF filename
    filename = (
        f"reports/Health_Report_{timestamp}.pdf"
    )

    # Create PDF document
    document = SimpleDocTemplate(
        filename
    )

    # Load styles
    styles = getSampleStyleSheet()

    # Store PDF content
    content = []

    # Report title
    title = Paragraph(
        "AI Public Health Chatbot Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    # Report generation date
    report_date = Paragraph(
        f"Generated On: {datetime.now()}",
        styles["Normal"]
    )

    content.append(report_date)

    content.append(
        Spacer(1, 20)
    )

    # If no chat history exists
    if len(chat_history) == 0:

        content.append(

            Paragraph(
                "No chat history available.",
                styles["BodyText"]
            )
        )

    else:

        # Add each conversation
        for index, chat in enumerate(
            chat_history,
            start=1
        ):

            # Conversation heading
            content.append(

                Paragraph(
                    f"<b>Conversation {index}</b>",
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

            # Time
            content.append(

                Paragraph(
                    f"<b>Time:</b> {chat['time']}",
                    styles["BodyText"]
                )
            )

            # User question
            content.append(

                Paragraph(
                    f"<b>Question:</b> {chat['question']}",
                    styles["BodyText"]
                )
            )

            # Chatbot response
            content.append(

                Paragraph(
                    f"<b>Response:</b> {chat['response']}",
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 15)
            )

        # Add new page
        content.append(
            PageBreak()
        )

        # Summary heading
        content.append(

            Paragraph(
                "Health Awareness Summary",
                styles["Heading1"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        # Summary text
        summary = """
This report was generated using the
AI Healthcare Chatbot.

The information provided is for
educational and awareness purposes only.

Please consult healthcare professionals
for medical advice, diagnosis,
and treatment.
"""

        content.append(

            Paragraph(
                summary,
                styles["BodyText"]
            )
        )

    # Build PDF
    document.build(content)

    return filename
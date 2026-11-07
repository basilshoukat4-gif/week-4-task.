class RuleClassifier:
    """Simple classifier implementation."""

    def classify(
        self,
        text: str,
    ) -> str:

        if not text:
            raise ValueError(
                "Text cannot be empty."
            )

        # account
        if (
            "password" in text
            or "Login" in text
            or "username" in text
            or "account" in text
        ):
            return "account"

        # finance
        if (
            "fee" in text
            or "Payment" in text
            or "refund" in text
            or "invoice" in text
            or "voucher" in text
        ):
            return "finance"

        # technical
        if (
            "server" in text
            or "api" in text
            or "Network" in text
            or "wifi" in text
            or "internet" in text
            or "website" in text
            or "error" in text
        ):
            return "technical"

        # admission
        if (
            "admission" in text
            or "apply" in text
            or "enroll" in text
            or "registration" in text
        ):
            return "admission"

        # academic
        if (
            "exam" in text
            or "result" in text
            or "Grade" in text
            or "timetable" in text
        ):
            return "academic"

        return "other"


if __name__ == "__main__":

    classifier = RuleClassifier()

    print(
        classifier.classify(
            "I forgot my password"
        )
    )

    print(
        classifier.classify(
            "My fee payment is missing"
        )
    )

    print(
        classifier.classify(
            "The API server is down"
        )
    )

    print(
        classifier.classify(
            "When will the exam result come"
        )
    )

    print(
        classifier.classify(
            "How do I apply for admission"
        )
    )

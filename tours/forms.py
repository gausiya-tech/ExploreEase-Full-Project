from django import forms
from .models import Booking, Contact, Review, Feedback

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "mobile", "address", "fromdate", "todate", "totalperson", "package"]
        widgets = {
            "fromdate": forms.DateInput(attrs={"type": "date"}),
            "todate": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("fromdate")
        end = cleaned.get("todate")
        if start and end and end < start:
            self.add_error("todate", "End date cannot be before start date.")
        return cleaned


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "mobile", "message"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "picture", "message"]



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]
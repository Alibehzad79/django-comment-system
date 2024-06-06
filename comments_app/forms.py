from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Alibehzad"},
        ),
        label="Name",
        required=True,
        max_length=50,
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "row": 3},
        ),
        label="Your Comment",
        required=True,
        max_length=5000
    )

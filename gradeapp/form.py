from django import forms
from . models import GradeTrack

class GradeForm(forms.ModelForm):
    class Meta:
        model=GradeTrack
        fields = ['name','Kannada_mark','English_mark','Hindi_mark','Maths_mark']

        widgets={
            'name':forms.TextInput(attrs={
                'placeholder':"Enter Student Name..",
                'style':'padding:10px;'
            }),
            'Kannada_mark':forms.TextInput(attrs={
                            'placeholder':"Enter Kannada Mark..",
                            'style':'padding:10px;'
                        }),
            'English_mark':forms.TextInput(attrs={
                                        'placeholder':"Enter English Mark..",
                                        'style':'padding:10px;'
                                    }),
            'Hindi_mark':forms.TextInput(attrs={
                                                    'placeholder':"Enter Hindi Mark..",
                                                    'style':'padding:10px;'
                                                }),
            'Maths_mark':forms.TextInput(attrs={
                                                    'placeholder':"Enter Maths Mark..",
                                                    'style':'padding:10px;'
                                                }),
        }
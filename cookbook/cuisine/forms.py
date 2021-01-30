from django import forms 
from .models import dish_Comment
  
class CommentForm(forms.ModelForm): 
    content = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':4, 
        'cols':50
    })) 
    class Meta: 
        model = dish_Comment
        fields =['content']
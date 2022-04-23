from django import forms

class PessoaFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaFormAdmin, self).__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
        self.fields['whatsapp'].widget.attrs['class'] = 'mask-telefone'
        self.fields['cnpj'].widget.attrs['class'] = 'mask-cnpj'
        self.fields['cpf_responsavel'].widget.attrs['class'] = 'mask-cpf'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
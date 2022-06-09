from django import forms
from user import models
from user.models import Warehouse, Provinsi, Kabupaten, Kecamatan, Kelurahan


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WarehouseForm, self).__init__(*args, **kwargs)

        # when there is instance key, select the default value
        # Provinsi always loaded for initial data, because Provinsi is on the first level
        try:
            self.initial['provinsi'] = kwargs['instance'].provinsi.id
            print(kwargs['instance'].provinsi.id)
        except:
            pass
        provinsi_list = [('', '---------')] + [(i.id, i.name) for i in Provinsi.objects.all()]

        # Kabupaten, Kecamatan, and Kelurahan is on the child level, it will be loaded when user click the parent level
        try:
            self.initial['kabupaten'] = kwargs['instance'].kabupaten.id
            kabupaten_init_form = [(i.id, i.name) for i in Kabupaten.objects.filter(
                provinsi=kwargs['instance'].provinsi
            )]
        except:
            kabupaten_init_form = [('', '---------')]

        try:
            self.initial['kecamatan'] = kwargs['instance'].kecamatan.id
            kecamatan_init_form = [(i.id, i.name) for i in Kecamatan.objects.filter(
                kabupaten=kwargs['instance'].kabupaten
            )]
        except:
            kecamatan_init_form = [('', '---------')]

        try:
            self.initial['kelurahan'] = kwargs['instance'].kelurahan.id
            kelurahan_init_form = [(i.id, i.name) for i in Kelurahan.objects.filter(
                kecamatan=kwargs['instance'].kecamatan
            )]
        except:
            kelurahan_init_form = [('', '---------')]

        # Override the form, add onchange attribute to call the ajax function
        self.fields['provinsi'].widget = forms.Select(
            attrs={
                'id': 'id_provinsi',
                'onchange': 'getKabupaten(this.value)',
                'style': 'width:200px'
            },
            choices=provinsi_list,
        )
        self.fields['kabupaten'].widget = forms.Select(
            attrs={
                'id': 'id_kabupaten',
                'onchange': 'getKecamatan(this.value)',
                'style': 'width:200px'
            },
            choices=kabupaten_init_form
        )
        self.fields['kecamatan'].widget = forms.Select(
            attrs={
                'id': 'id_kecamatan',
                'onchange': 'getKelurahan(this.value)',
                'style': 'width:200px'
            },
            choices=kecamatan_init_form
        )
        self.fields['kelurahan'].widget = forms.Select(
            attrs={
                'id': 'id_kelurahan',
                'style': 'width:200px'
            },
            choices=kelurahan_init_form
        )

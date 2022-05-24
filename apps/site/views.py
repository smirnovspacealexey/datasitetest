from django.shortcuts import render
from .backend import APIForm, get_forms_uids


def edit_form_view(request):
    context = {}

    if request.POST:
        print(request.POST)
        request_data = dict(request.POST)
        form_uid = request_data.get('formUid')[0]
        api_form = APIForm(form_uid)
        api_form.set_result({'select': request_data.get('select'),
                             'textarea': request_data.get('textarea'),
                             'input': request_data.get('input'),
                             })
    uids = get_forms_uids()

    if uids:
        forms = {}

        for form_uid in uids:
            api_form = APIForm(form_uid)
            rows = api_form.get_rows()
            forms[form_uid] = rows
        context.update({'forms': forms})

    return render(request, 'site/edit.html', context)


def result_view(request):
    context = {}
    uids = get_forms_uids()

    if uids:
        forms = {}
        for form_uid in uids:
            api_form = APIForm(form_uid)
            rows = api_form.get_result()
            forms[form_uid] = rows if rows else []
        context.update({'forms': forms})
    return render(request, 'data/result.html', context)



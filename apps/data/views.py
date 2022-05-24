from django.shortcuts import render
from .models import Form, Row


def form_view(request):

    if request.POST:
        request_data = dict(request.POST)

        form_uid = request_data.get('formUid')[0]
        if form_uid == 'new':
            current_form = Form.objects.create()
        else:
            current_form = Form.objects.filter(pk=form_uid.split()[0]).first()
            current_form.rows.all().delete()

        row_number = 0
        for item in request_data.get('type'):
            Row.objects.create(form=current_form,
                               form_type=item,
                               name=request_data.get('name')[row_number],
                               description=request_data.get('description')[row_number],
                               )
            row_number += 1

    context = {'forms': Form.objects.all()}

    return render(request, 'data/form.html', context)


def result_view(request):
    forms = {}
    for current_form in Form.objects.all():
        rows = []
        for row in current_form.rows.all():
            rows.append([row.form_type, row.name, row.result.result if row.result.result else ''])
        forms[current_form.__str__()] = rows

    context = {'forms': forms}
    return render(request, 'data/result.html', context)


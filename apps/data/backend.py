from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Form, Result


@csrf_exempt
def api_rpc(request):
    try:
        if request.POST:
            print(request.POST)

            method = request.POST['method']
            if method == 'get-uids':
                uids = []
                for form in Form.objects.all():
                    uids.append(form.__str__())
                return JsonResponse({"jsonrpc": "2.0", "result": uids, "id": request.POST['id']})

            elif method == 'get-rows':
                form_uid = request.POST['params']
                current_form = Form.objects.filter(pk=form_uid.split()[0]).first()
                rows = []
                for row in current_form.rows.all():
                    rows.append([row.form_type, row.name, row.description])

                return JsonResponse({"jsonrpc": "2.0", "result": rows, "id": request.POST['id']})

            elif method == 'set-result':
                params = json.loads(request.POST.get('params'))
                form_uid = params['uid']
                current_form = Form.objects.filter(pk=form_uid.split()[0]).first()

                if params['textarea']:
                    i = 0
                    for row in current_form.rows.filter(form_type="textarea"):
                        result, created = Result.objects.get_or_create(row=row)
                        result.result = params['textarea'][i]
                        result.save()
                        i += 1

                if params['input']:
                    i = 0
                    for row in current_form.rows.filter(form_type="input"):
                        result, created = Result.objects.get_or_create(row=row)
                        result.result = params['input'][i]
                        result.save()
                        i += 1

                if params['select']:
                    for row in current_form.rows.filter(form_type="select"):
                        result, created = Result.objects.get_or_create(row=row)
                        result.result = None
                        result.save()

                    for select in params['select']:
                        row = current_form.rows.filter(form_type="select", name=select).first()
                        result = Result.objects.filter(row=row).first()
                        result.result = 'True'
                        result.save()

            elif method == 'get-result':
                form_uid = request.POST['params']
                current_form = Form.objects.filter(pk=form_uid.split()[0]).first()
                rows = []
                for row in current_form.rows.all():
                    if hasattr(row, 'result'):
                        result = row.result.result if row.result.result else ''
                    else:
                        result = ''
                    rows.append([row.form_type, row.name, result])

                return JsonResponse({"jsonrpc": "2.0", "result": rows, "id": request.POST['id']})

        return JsonResponse({"jsonrpc": "2.0", "error": {"message": "Invalid JSON-RPC."}, "id": None})
    except:
        return JsonResponse({"jsonrpc": "2.0", "error": {"message": "Something went wrong"}, "id": None})


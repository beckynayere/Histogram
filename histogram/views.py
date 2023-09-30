from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .histogram import Histogram

histogram = Histogram([(3, 4.1), (8.5, 8.7), (4, 4.5), (0, 1.1), (31.5, 41.27)])

@require_POST
def insert_samples(request):
    data = json.loads(request.body.decode('utf-8'))
    samples = data.get('samples', [])
    if not samples:
        return JsonResponse({'error': 'No samples provided'}, status=400)

    histogram.insert_samples(samples)
    return JsonResponse({'message': 'Samples inserted successfully'})

def get_metrics(request):
    metrics = histogram.get_metrics()
    return JsonResponse(metrics)

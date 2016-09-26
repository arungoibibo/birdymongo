import datetime
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import get_connection


@csrf_exempt
def birds(request, bid=None):
	if request.method == 'GET':
		data = {}
		try:
			conn = get_connection('birds')
			if bid:
				data = conn.find({'_id': ObjectId(bid), 'visible': True})
			else:
				data = conn.find({'visible': True})
			if data.count():
				return HttpResponse(
			        dumps(data), status=200)
			else:
				return HttpResponse(status=200)

		except Exception, e:
			return HttpResponse(status=404)

	if request.method == 'POST':
		try:
			data = request.POST
			if not data:
				data = loads(request.body)
			if valid_data(data):
				data['added'] = datetime.datetime.strftime(
					datetime.datetime.now(), "%Y-%m-%d")
				if 'visible' not in data:
					data['visible'] = False
				conn = get_connection('birds')
				conn.insert_one(data)
				return HttpResponse(status=201)
			else:
				raise

		except Exception, e:
			return HttpResponse(status=400)

	if request.method == 'DELETE':
		try:
			conn = get_connection('birds')
			doc = conn.remove({'_id': ObjectId(bid)})
			if doc.get('n', False):
				return HttpResponse(status=200)
			else:
				raise

		except Exception, e:
			return HttpResponse(status=404)


def valid_data(data):
	try:
		if (('name' in data)
			and ('family' in data)
				and ('continents' in data)
					and (data['continents'])):

			return True
		else:
			raise

	except Exception, e:
		return False
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def searchStock(request):
    import json
    import finnhub
    import datetime
    import time

    finnhub_client = finnhub.Client(api_key="cepnf9iad3icn6bbfqh0cepnf9iad3icn6bbfqhg")

    sName = request.POST['stockName']

    # api call for searching the stock-name 
    # get the data using json.loads(apiReq.get(api-call))   
    api_reponse = finnhub_client.symbol_lookup(sName)
    api = json.loads(api_reponse)
    ticker = api_reponse.symbol    
    
    presentDate = datetime.datetime.now()
    startDate = presentDate - datetime.timedelta(days=362)  #52 weeks

    presentDate_unix = time.mktime(presentDate.timetuple())
    startDate_unix = time.mktime(startDate.timetuple())

    # return the ticker,, use it to call API for stock and then display data
    week_data = json.loads(finnhub_client.stock_candles(ticker, 'W', startDate_unix, presentDate_unix)).content
    month_data = json.loads(finnhub_client.stock_candles(ticker, 'M', startDate_unix, presentDate_unix)).content

    return render(request, 'search.html', {'name' : sName, 'week' : week_data, 'month' : month_data})


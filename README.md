# WeatherAPI Scraping

A weather scraping for different variation of temperature, humidity and forecast using yahoo weather API.

## Description

scraping weather details like temperature, humidity and forecast details from yahoo weather api. Getting the details and ploting
graph using matplotlib module in python. So, here we need to input the location name for what we need to get weather details.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib.

```bash
pip install import urllib.request
pip install matplotlib
import hmac, hashlib
from base64 import b64encode
```

## Method

GET

## Usage

```python
from matplotlib import pyplot as plt

#using matplotlib to plot graph
plt.title("Temperature anomalies")
plt.xlabel("no. of days")
plt.ylabel("Temperature in Fahrenhiet")
ax = plt.gca()
report.plot(kind = 'line', x = 'day', y = 'high', ax = ax)
report.plot(kind = 'line', x = 'day', y = 'low', color = 'red', ax = ax)
report.plot(kind = 'bar', x = 'day', y = 'humidity', color = 'green', ax = ax)
report.plot(kind = 'bar', x = 'day', y = 'temperature', color = 'red', ax = ax)
plt.show()

#Prepare signature
merged_params = self.query.copy()
merged_params.update(self.oauth)
sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str =  self.method + self.concat + urllib.parse.quote(self.url, safe='') + self.concat + urllib.parse.quote(self.concat.join(sorted_params), safe='')

#Generate signature
composite_key = urllib.parse.quote(self.consumer_secret, safe='') + self.concat
oauth_signature = b64encode(hmac.new( bytes(composite_key , 'latin-1') , bytes(signature_base_str,'latin-1'), hashlib.sha1).digest())
oauth_signature = oauth_signature.decode('utf-8')

#Authorization header
self.oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k,v) for k,v in self.oauth.items()])

#Send request
self.url = self.url + '?' + urllib.parse.urlencode(self.query)
opener = urllib.request.build_opener()
opener.addheaders = [('Authorization', auth_header),
                        ('X-Yahoo-App-Id', self.app_id),
                        ('Pragma', 'no-cache'),
                        ('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(self.url)
data = response.read().decode('utf-8')
del response
del opener
target = json.loads(data)
return target
```

## Contributing

Getting token from the yahoo API and including authorization header and sending request using basic endpoint
[basic url](https://weather-ydn-yql.media.yahoo.com/forecastrss).

## Endpoints used here

For example I am entering the location name here
For another endpoint if we know the exact lattitude and longitude we can make use of the function.

[forecast_endpoint](https://weather-ydn-yql.media.yahoo.com/forecastrss?location=chennai)
[lat_and_lon_endpoint](https://weather-ydn-yql.media.yahoo.com/forecastrss?lat=13.0827&lon=80.2707)


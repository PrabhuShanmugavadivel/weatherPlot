import time, uuid, json
import urllib.request
import hmac, hashlib
from base64 import b64encode

class weather():
    def __init__ (self, url):
        self.url = url
        self.app_id = "sXLhOtWI"
        self.consumer_key = "dj0yJmk9MEJPaG9BYnE0S0tXJmQ9WVdrOWMxaE1hRTkwVjBrbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTBj"
        self.consumer_secret = "4870a9ec3fe4f5dc9fb56bb589a7be7c9b2574cb"
        self.method = 'GET'
        self.concat = '&'    
          
    def send_request(self):
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

    def get_forcastrss(self, location, unit = 'c'):
        # Returns a dictionary of weather data
        self.query = {'location': location, 'format': 'json' , 'u' : unit}
        self.url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
        self.oauth = {
        'oauth_consumer_key': self.consumer_key,
        'oauth_nonce': uuid.uuid4().hex,
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_timestamp': str(int(time.time())),
        'oauth_version': '1.0'
        }
        return self.send_request()
    
    def lat_lon(self, lat, lon):
        # Returns a dictionary of weather data with lattitude and longitude
        self.query = {'lat' : lat, 'lon' : lon, 'format': 'json'}
        self.url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
        self.oauth = {
        'oauth_consumer_key': self.consumer_key,
        'oauth_nonce': uuid.uuid4().hex,
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_timestamp': str(int(time.time())),
        'oauth_version': '1.0'
        }
        return self.send_request()

import os
from cfbd import Configuration, ApiClient

class CFBDClient():
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            API_KEY=os.environ.get("API_KEY")
            configuration = Configuration()
            configuration.api_key['Authorization'] = API_KEY
            # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            configuration.api_key_prefix['Authorization'] = 'Bearer'

            # create an instance of the API class
            api_instance = ApiClient(configuration)
            cls._instance = api_instance
        return cls._instance

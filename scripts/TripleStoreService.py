from SPARQLWrapper import SPARQLWrapper, JSON, POST, BASIC
import Config
import logging

class TripleStoreService:

    ENDPOINT = SPARQLWrapper(Config.TRIPLE_STORE_URL)
    ENDPOINT.setHTTPAuth(BASIC)
    ENDPOINT.setCredentials(Config.TRIPLE_STORE_USERNAME, Config.TRIPLE_STORE_PASSWORD)
    ENDPOINT.setMethod(POST)

    def get_query_result(self, query):
        self.ENDPOINT.setQuery(query)
        self.ENDPOINT.setReturnFormat(JSON)
        try:
            result = self.ENDPOINT.query().convert()
        except Exception as e:
            logging.error("Issue with SPARQL endpoint")
            logging.error(e)
            return None
        return result

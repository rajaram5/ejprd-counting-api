import chevron
import TripleStoreService

class IndividualsService:

    TRIPLE_STORE_SERVICE = TripleStoreService.TripleStoreService()

    def get_count(self, filters):
        count = None

        disease_uri = None
        gender_uri = None

        for filter in filters:
            if filter.id == "disease":
                disease_uri = filter.value
            elif filter.id == "gender":
                gender_uri = filter.value
            else:
                return count

        if disease_uri is not None and gender_uri is None:
            query = None
            with open('templates/count_person_with_disease.mustache', 'r') as f:
                query = chevron.render(f, {'disease_url': disease_uri})

            if query is not None:
                result = self.TRIPLE_STORE_SERVICE.get_query_result(query)
                for result in result["results"]["bindings"]:
                    if result["count"]["value"]:
                        count = int(result["count"]["value"])
        return count
from fastapi import FastAPI
import uvicorn
import Types
import IndividualsService

app = FastAPI()
individual_service = IndividualsService.IndividualsService()

@app.post("/individuals")
def get_individuals(request: Types.Request):
    print(request.json())
    filters = request.query.filters
    count = individual_service.get_count(filters)
    does_data_exist = False
    if count is not None:
        does_data_exist = True
    else:
        count = 0
    return Types.Response(responseSummary={'numTotalResults': count, 'exists': does_data_exist})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
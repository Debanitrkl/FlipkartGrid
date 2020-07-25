def function(request,context):
    print(request.Ratings)
    response = request.Ratings_count * request.Ratings
    return response

# Prediction model stays here(Both Attribute & Fashion Category CLassification)

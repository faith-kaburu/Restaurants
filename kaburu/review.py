class Review:
    # Class attribute to store all instances of Review
    all_reviews = []

    def __init__(self, customer, restaurant, rating=None):
        # Initialize instance attributes
        self.customer = customer
        self.restaurant = restaurant
        # Initialize the private attribute _rating
        self._rating = None
        # Adding the review to the all_reviews list
        Review.all_reviews.append(self)
        if rating is not None:
            self.set_rating(rating)

    # Used to retrieve the value of the 'rating' property
    def get_rating(self):
        return self._rating

    # Used setter to ensure the rating is an integer
    def set_rating(self, rating):
        if isinstance(rating, int):
            self._rating = rating
        else:
            print("Rating must be an integer")

    # Create the 'rating' property using get_rating and set_rating methods
    rating = property(get_rating, set_rating)

# use @classmethod decorator to define a method that operates on the class itself
    @classmethod
    #  the  method all() takes the class itself as the an argument(cls) method returns all reviews that have been created
    def all(cls):
        # created a variable with an empty list
        printedReviews = []
        for review in cls.all_reviews:
            # append cause it has an empty list
             printedReviews.append(f"Customer: {review.customer}, Rating: {review.rating}")

        return printedReviews
    
    # creating an instance of the review class
myreview = Review("Faith Kaburu", "Baguette Bistro", 30)
# newreview = Review("Taylor swift", "Kyeo", " 20")

# getting the ratings of the reviews using the rating() method
print(myreview.rating)
# print(newreview.rating)

# getting all the reviews
all_reviews = Review.all()
print(all_reviews)



    
     
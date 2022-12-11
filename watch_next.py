"""here we will compare the description of a movie to a list of descriptions to define which one is most similar and
suggest it as the next movie."""

import spacy

nlp = spacy.load('en_core_web_md')  # using advanced language model

# movie to compare
movie_compare = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too " \
                "dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him " \
                "into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land " \
                "on the planet Sakaar where he is sold into slavery and trained as a gladiator."


def description(movie):
    """function that receives the array with title and description and returns the description."""
    return movie.strip("\n").split(" :")[1]


def title(movie):
    """function that receives the array with title and description and returns the title."""
    return movie.strip("\n").split(" :")[0]


def watchNext(movie):
    """function that receives the movie to be compared, reads the list of movies in the file comparing their
    descriptions to define which one to suggest as next and returns the name of the next movie."""
    probNext = 0.0
    compare = nlp(description(movie))
    with open('movies.txt', 'r', encoding='utf-8') as file:
        for line in file:
            prob = compare.similarity(nlp(description(line)))
            if prob > probNext:
                probNext = prob
                nextMovie = title(line)

    return nextMovie


# Call function
print(watchNext(movie_compare))

import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "
    for language in languages:
        query += f"language: {language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    # https://docs.github.com/en/rest/search?apiVersion=2022-11-28
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages=languages)
    params = {
        "q": query,
        "sort": sort,
        "order": order,
    }
    response = requests.get(gh_api_repo_search_url, params=params)

    # status_code = response.status_code
    status_code = 500

    if status_code != 200:
        raise RuntimeError(f"An error ocurred. Status code was: {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json


# Have a main method here.
if __name__ == "__main__":
    languages = ["python", "javascript"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        star = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {star} stars.")

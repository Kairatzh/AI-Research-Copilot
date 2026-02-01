"""
    Модуль для анализа данных, полученных из веб-поиска.
"""

def analyze_search_results(results):
    analyzed_data = []
    for result in results:
        title_length = len(result['title'])
        snippet_length = len(result['snippet'])
        analyzed_data.append({
            'title': result['title'],
            'link': result['link'],
            'snippet': result['snippet'],
            'title_length': title_length,
            'snippet_length': snippet_length
        })
    return analyzed_data

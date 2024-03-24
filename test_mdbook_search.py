import mdbook_search

if __name__ == '__main__':
    results = mdbook_search.search_wiki("error")
    for result in results:
        title = result["title"]
        href = result["href"]
        paragraph_preview = result["paragraph_preview"]
        print(f"title: {title},href: {href}, paragraph_preview: {paragraph_preview}")

import time
import asyncio
from async_fetcher import AsyncFetcher
from html_parser import HTMLParser
from data_analyzer import DataAnalyzer

async def main():
    urls = [
        'https://python.org',
        'https://github.com',
    ]

    print("Fetching HTML content asynchronously")
    fetcher = AsyncFetcher(urls)
    start_time = time.time()
    html_contents = await fetcher.fetch_all()
    print(f"Fetched content in {time.time() - start_time:.2f} seconds")


    print("\nParsing HTML content using multithreading...")
    parser = HTMLParser(html_contents)
    start_time = time.time()
    parsed_data = parser.parse_all()
    print(f"Parsed content in {time.time() - start_time:.2f} seconds")

  
    print("\nAnalyzing data using multiprocessing...")
    analyzer = DataAnalyzer(parsed_data)
    start_time = time.time()
    analysis_results = analyzer.analyze_all()
    print(f"Analyzed content in {time.time() - start_time:.2f} seconds")

    for i, result in enumerate(analysis_results):
        print(f"\nAnalysis result for {urls[i]}:")
        print(result)

# Entry point
if __name__ == "__main__":
    asyncio.run(main())

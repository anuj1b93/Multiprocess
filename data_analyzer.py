from multiprocessing import Pool

class DataAnalyzer:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data

    def analyze_data(self, links):
        internal_links = [link for link in links if link.startswith('/')]
        external_links = [link for link in links if not link.startswith('/')]
        
        return {'internal': len(internal_links), 'external': len(external_links)}

    # Multiprocessing (Parallel analysis) 
    def analyze_all(self):
        with Pool() as pool:
            results = pool.map(self.analyze_data, self.parsed_data)
        return results

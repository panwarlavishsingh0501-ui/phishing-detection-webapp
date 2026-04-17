def extract_features(url):
    # Example placeholder features
    features = {
        "url_length": len(url),
        "has_https": 1 if "https" in url else 0,
        "contains_at_symbol": 1 if "@" in url else 0
    }
    # Convert dict to list for ML model
    return list(features.values())

def parse_data(text: str) -> list:
    import re

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    stop_words = {
        'the', 'and', 'or', 'but', 'to', 'of', 'in', 'a', 'an', 'is', 'it', 'was', 'were',
        'this', 'that', 'these', 'those', 'have', 'has', 'had', 'been', 'will', 'would',
        'could', 'should', 'not', 'be', 'by', 'on', 'at', 'for', 'with', 'as', 'if',
        'end', 'about', 'sample', 'text', 'domain', 'use', 'may', 'you', 'us', 'we'
    }
    
    return [word for word in words if word not in stop_words and len(word) > 1]
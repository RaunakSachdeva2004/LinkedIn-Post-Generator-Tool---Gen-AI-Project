import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def extract_metadata(post):
    # Extract metadata from the text
    template = '''
        You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
        1. Return a valid JSON. No preamble. 
        2. JSON object should have exactly three keys: line_count, language and tags. 
        3. tags is an array of text tags. Extract maximum two tags.
        4. Language should be English or Hinglish (Hinglish means hindi + english)
        
        Here is the actual post on which you need to perform this task:  
        {post}
        '''

    
    return {
        'line_count':10,
        'language': 'english',
        'tags':['Mental Health','motivation']
        }
    
    
def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadat = extract_metadata(post['text'])
            post = {'text',}
            
        
        
        
if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
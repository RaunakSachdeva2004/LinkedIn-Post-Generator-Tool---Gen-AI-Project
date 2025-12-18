import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def sanitize_text(text):
    """
    Removes surrogate characters (broken emojis) that cause UnicodeEncodeError.
    """
    if not isinstance(text, str):
        return text
    # This encodes the text to utf-8, ignoring any errors (bad characters), 
    # and then decodes it back to a clean string.
    return text.encode('utf-8', 'ignore').decode('utf-8')

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadat = extract_metadata(post['text'])
            post = {'text',}
            
        
        

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
    
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({'post': post})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(str(response.content))
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res
    
    

        
if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
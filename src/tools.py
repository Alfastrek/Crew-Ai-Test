import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchToolset:
    @staticmethod
    def _exa():
        return Exa(api_key=os.environ['EXA_API_KEY'])


    @tool

    def search(query: str):
        """Search for a webpage based on the query."""
        return ExaSearchToolset._exa().search(f"{query}", use_autoprompt=True, num_results=3)
    
    @tool
    def find_similar(url:str):
        """Search for similar webpages based on the url.
        The url must be passed in as a string, the url returned from 'search'"""
        return ExaSearchToolset._exa().find_similar(url, num_results=3)
    
    @tool
    def get_content(ids:str):
        """Get the content of a webpage.
         The ids must be passed in as a list, a list of ids returned from 'search'.
        """
        ids= eval(ids)
        contents= str(ExaSearchToolset._exa().get_content(ids))
        contents.split("URL:")
        contents=[content[0] for content in contents] 
        return "\n\n".join(contents)
    
def tools():
    return [
        ExaSearchToolset.search,
        ExaSearchToolset.find_similar,
        ExaSearchToolset.get_content
    ]



    
    
import asyncio
from crawl4ai import *
from openai import AsyncOpenAI
import os
from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()


client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class UrlRequest(BaseModel):
    url: str

# your_url = input("Enter URL: ")
async def main(your_url: str):



    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            # "https://www.nbcnews.com/business"
            url= your_url,
        )

    response = await client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": f"""
                You are an assistant specialized in summarizing news. Your tasks are:

                                    -Summarize the latest news based on the provided context: {result.markdown}.

                                    -Use web search to find the most recent and relevant updates related to the context.

                                    -Suggest additional ideas or angles based on the latest news.

                                    -Attach a referral link (source link) to each piece of summarized news.

                                    -Format your response like this example:

                                   
                                    
                           
                                   print all referral url
                                    
                                    """
            },
            # {
            #     "role": "user",
            #     "content": "Are semicolons optional in JavaScript?"
            # }
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


    # print(result.markdown)
    # return result.markdown



@app.post("/")
async def APIHandle(body: UrlRequest):
   
    try:
        result = await main(body.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    return result

    





# if __name__ == "__main__":
#     asyncio.run(main())

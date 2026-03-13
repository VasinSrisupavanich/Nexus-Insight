import os
import json
from typing import List, Dict, Any
from pydantic import BaseModel
from openai import OpenAI

# Initialize OpenAI Client (ensure OPENAI_API_KEY is in your environment)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-key-here"))

class InsightResponse(BaseModel):
    summary: str
    key_entities: List[str]
    sentiment: str
    confidence_score: float
    next_steps: List[str]

class NexusEngine:
    def __init__(self, model: str = "gpt-4o"):
        self.model = model

    def analyze_knowledge_base(self, query: str, context: str) -> InsightResponse:
        """
        Processes knowledge base context to extract structured insights.
        """
        prompt = (
            "You are a Nexus Insight Engine. Analyze the following knowledge base context "
            "to answer the user query. Provide a concise summary, "
            "list key entities (names, organizations, dates), detect sentiment, "
            "provide a confidence score (0-1), and suggest next steps.\n\n"
            f"Query: {query}\n"
            f"Context:\n{context}"
        )

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return InsightResponse(**result)

if __name__ == "__main__":
    # Example usage with dummy text
    engine = NexusEngine()
    sample_query = "What is the strategic impact of the GlobalTech acquisition?"
    sample_context = (
        "On October 12, 2023, GlobalTech Solutions acquired NextGen AI for  million. "
        "The acquisition aims to strengthen GlobalTech's position in the cloud infrastructure market "
        "by integrating specialized AI agents for autonomous server management."
    )
    
    print("🔍 Nexus: Processing Autonomous Insight...")
    insights = engine.analyze_knowledge_base(sample_query, sample_context)
    print(f"Summary: {insights.summary}")
    print(f"Entities: {', '.join(insights.key_entities)}")
    print(f"Confidence: {insights.confidence_score}")
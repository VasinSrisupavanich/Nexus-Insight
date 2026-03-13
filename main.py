import argparse
from nexus.core import NexusEngine
from nexus.vector_memory import VectorMemory

def main():
    parser = argparse.ArgumentParser(description="Nexus Insight Engine CLI")
    parser.add_argument("--query", type=str, required=True, help="Knowledge query to analyze")
    parser.add_argument("--add_context", type=str, help="Add a context document to the knowledge base")
    args = parser.parse_args()

    engine = NexusEngine()
    memory = VectorMemory()

    # Pre-populate with dummy context if nothing provided
    memory.commit("AI Platform Engineering is a key trend for 2026.")
    memory.commit("MLOps is foundational for scalable AI deployments.")

    if args.add_context:
        memory.commit(args.add_context)

    # Simple retrieval logic
    retrieved_docs = memory.retrieve(args.query)
    combined_context = "\n".join(retrieved_docs) if retrieved_docs else "No specific context found."

    print(f"🚀 Nexus: Initializing Autonomous Insight for: '{args.query}'")
    insight = engine.analyze_knowledge_base(args.query, combined_context)
    
    print("\n" + "="*50)
    print("📈 FINAL INSIGHT")
    print("="*50)
    print(f"Summary: {insight.summary}")
    print(f"Confidence: {insight.confidence_score}")
    print(f"Sentiment: {insight.sentiment}")
    print(f"Key Entities: {', '.join(insight.key_entities)}")
    print(f"Next Steps: {', '.join(insight.next_steps)}")
    print("="*50)

if __name__ == "__main__":
    main()
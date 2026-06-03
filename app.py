from services.ingest import ingest_docs
from services.rag_pipeline import rag_chat

def main():

    print("\nBuilding Vector Store..." )

    total_chunks = ingest_docs()

    print(f"Loaded {total_chunks} chunks.")

    print("\nRAG System Ready!")

    while True:

        user_input = input("\nAsk a question (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        answer = rag_chat(user_input)

        print(f"\nResponse:\n{answer}")


if __name__ == "__main__":
    main()
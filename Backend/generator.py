def generate_answer(query, context):
    """
    Simple answer generator using retrieved context.
    """
    answer = f"Question: {query}\n\nAnswer:\n{context}"
    return answer


# Example (simulate output from retriever)
query = "What is blockchain?"
retrieved_chunk = "Blockchain is an advanced database mechanism"

final_answer = generate_answer(query, retrieved_chunk)
print(final_answer)
from duckduckgo_search import DDGS

try:
    with DDGS() as ddgs:
        results = list(
            ddgs.text(
                "Tesla latest business strategy",
                max_results=5
            )
        )

    print("\nSUCCESS\n")

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}")
        print(result)

except Exception as e:
    print("\nERROR:")
    print(type(e).__name__)
    print(str(e))
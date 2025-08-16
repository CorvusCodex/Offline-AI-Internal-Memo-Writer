from utils import run_llama

def memo_writer(notes):
    prompt = f"Turn these notes into a professional internal memo:\n{notes}"
    return run_llama(prompt)

if __name__ == "__main__":
    notes = input("Notes: ")
    print(memo_writer(notes))

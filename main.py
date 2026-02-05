from .config import (
    OPENAI_API_KEY,
    GOOGLE_API_KEY,
    configure_langsmith_env,
)

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    """
    Simple smoke test: call one OpenAI model and one Google Gemini model
    and print their responses.
    """
    # Configure LangSmith tracing if enabled in .env
    configure_langsmith_env()

    # Basic safety checks so failures are clear
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set. Check your .env file.")

    if not GOOGLE_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY is not set. Check your .env file.")

    # --- OpenAI chat model setup ---
    # ChatOpenAI reads OPENAI_API_KEY from the environment by default.
    # We could also pass api_key=OPENAI_API_KEY explicitly, but it is not required.
    openai_model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0.2,
    )

    # --- Google Gemini chat model setup ---
    # ChatGoogleGenerativeAI reads GOOGLE_API_KEY from the environment.
    # We only need to specify which model to use.
    google_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
    )

    prompt = "Say hello from my new LangChain environment in one short sentence."

    # Call OpenAI
    openai_response = openai_model.invoke(prompt)
    print("OpenAI replied:")
    print(openai_response.content)
    print()

    # Call Google Gemini
    google_response = google_model.invoke(prompt)
    # For Gemini 3 models, .text is a convenient shortcut for the main text content
    print("Google Gemini replied:")
    print(google_response.text)


if __name__ == "__main__":
    main()

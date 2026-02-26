## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM

from tools import search_tool, FinancialDocumentTool

### Loading LLM (Ollama)
llm = LLM(
    model=os.getenv("OLLAMA_MODEL", "ollama/llama3"),
    provider="ollama",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    temperature=0.0,
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze the user's financial document and answer their query {query} with clear, "
        "evidence‑based insights drawn only from the document."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with a strong background in accounting and corporate finance. "
        "You carefully read financial statements, notes, and disclosures before forming any conclusions. "
        "You focus on explaining key metrics, trends, and risks in simple, professional language, and you avoid "
        "speculation that is not supported by the document."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True,
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Check whether the uploaded document is primarily a financial document and identify its type "
        "(e.g., annual report, quarterly report, investor presentation, invoice, bank statement)."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You have a background in accounting and financial reporting. "
        "You look for headings, tables, numerical disclosures, and standard financial terminology to decide "
        "whether something is a financial document. "
        "You are cautious and honest: if the content is ambiguous, you say that clearly instead of guessing."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True,
)

investment_advisor = Agent(
    role="Investment Analysis Specialist",
    goal=(
        "Highlight the investment‑relevant implications of the financial document for the user's query {query}, "
        "without giving personalized buy/sell recommendations."
    ),
    verbose=True,
    backstory=(
        "You have experience in equity and credit analysis, focusing on fundamentals such as revenue growth, "
        "profitability, cash flows, leverage, and valuation. "
        "You describe opportunities and risks in neutral language, and you make it clear that you are providing "
        "general analysis, not individualized investment advice."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False,
)


risk_assessor = Agent(
    role="Financial Risk Analyst",
    goal=(
        "Identify and explain the main financial and business risks present in the document, in the context of "
        "the user's query {query}."
    ),
    verbose=True,
    backstory=(
        "You specialize in risk management and credit analysis. "
        "You systematically evaluate liquidity, leverage, market, operational, and other relevant risks. "
        "You clearly distinguish between what is directly supported by the document and what is uncertain or not stated."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False,
)

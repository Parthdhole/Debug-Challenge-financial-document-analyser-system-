## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description=(
        "You are a professional financial analyst AI. Your task is to analyze the uploaded financial document "
        "strictly based on its content and answer the user's query: {query}.\n\n"
        "Rules:\n"
        "1. Do NOT fabricate any information.\n"
        "2. Do NOT include external URLs or sources.\n"
        "3. Only use information present in the document.\n"
        "4. If specific data is missing, respond with \"Not Available\".\n"
        "5. Keep your analysis neutral, factual, and professional.\n"
        "6. Return your response strictly in the specified structured JSON format."
    ),
    expected_output=(
        "{\n"
        "  \"company_name\": \"\",\n"
        "  \"revenue\": \"\",\n"
        "  \"net_profit\": \"\",\n"
        "  \"key_financial_risks\": [],\n"
        "  \"investment_summary\": []\n"
        "}\n\n"
        "Instructions:\n"
        "- Provide all numerical data exactly as found in the document.\n"
        "- If any field cannot be determined, set its value to \"Not Available\".\n"
        "- Summarize risks as bullet‑like short strings inside \"key_financial_risks\".\n"
        "- Summarize investment‑relevant insights as bullet‑like short strings inside \"investment_summary\".\n"
        "- Do not add any extra fields or text outside this JSON object."
    ),
    agent=financial_analyst,
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description=(
        "Using the financial document and the user's query {query}, provide a high‑level investment‑oriented "
        "analysis of the company or entity. Focus on fundamentals (growth, profitability, cash flows, leverage) "
        "and explain what an investor might pay attention to."
    ),
    expected_output=(
        "A concise, user‑friendly summary that includes:\n"
        "- Key financial metrics and trends relevant to an investor.\n"
        "- Potential strengths and opportunities suggested by the document.\n"
        "- Potential weaknesses and risks that could affect investment outcomes.\n"
        "- How the information in the document relates to the user's query.\n"
        "Avoid personalized buy/sell recommendations; stay at the level of analysis and considerations."
    ),
    agent=financial_analyst,
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description=(
        "Based on the financial document and the user's query {query}, identify and explain the main financial "
        "and business risks. Stay grounded in what is actually stated or clearly implied in the document."
    ),
    expected_output=(
        "A structured risk assessment that includes:\n"
        "- The main categories of risk (e.g., liquidity, leverage, market, operational) that are relevant here.\n"
        "- For each category, a short explanation of what in the document indicates that risk.\n"
        "- Any important uncertainties or missing information that limit your ability to assess risk.\n"
        "- A short overall view of the risk profile (e.g., relatively low/medium/high) with a brief justification."
    ),
    agent=financial_analyst,
    async_execution=False,
)

verification = Task(
    description=(
        "Determine whether the uploaded file is primarily a financial document and, if so, what type it is. "
        "Base your judgment only on the text and structure of the document."
    ),
    expected_output=(
        "A short verification report that includes:\n"
        "- A clear yes/no answer to whether this is primarily a financial document.\n"
        "- If yes, the most likely document type (e.g., annual report, quarterly report, investor presentation, invoice).\n"
        "- A brief explanation citing the main clues from the document (headings, tables, terminology, etc.).\n"
        "- If classification is uncertain, explain why."
    ),
    agent=financial_analyst,
    async_execution=False,
)
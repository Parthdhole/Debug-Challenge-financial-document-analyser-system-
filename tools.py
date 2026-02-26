## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
import pdfplumber

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path: str = "data/sample.pdf") -> str:
        """Tool to read data from a PDF file from a path.

        Args:
            path (str, optional): Path of the PDF file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full financial document text, cleaned and concatenated.
        """
        full_report = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                content = page.extract_text() or ""

                # Remove extra blank lines and normalize spacing
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"
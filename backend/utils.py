import tempfile
import os
from datetime import datetime
import io
from weasyprint import HTML, CSS
from flask import url_for

def generate_pdf(submission_data):
    """
    Generate a PDF from submission data
    
    Args:
        submission_data (dict): Dictionary containing form submission data
        
    Returns:
        bytes: PDF file as bytes
    """
    # Function to format a list of items for HTML display
    def format_list_items(items):
        if not items:
            return "None"
        return "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    
    # Format dates nicely
    def format_date(date_str):
        if not date_str:
            return "Not specified"
        try:
            date_obj = datetime.fromisoformat(date_str)
            return date_obj.strftime("%B %d, %Y")
        except (ValueError, TypeError):
            return date_str
    
    # Build HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Data Visualization Pricing Analysis</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #2c3e50;
                font-size: 24px;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            h2 {{
                color: #2c3e50;
                font-size: 20px;
                border-bottom: 1px solid #bdc3c7;
                padding-bottom: 5px;
                margin-top: 25px;
                margin-bottom: 15px;
            }}
            .section {{
                margin-bottom: 30px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                padding: 12px 15px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }}
            th {{
                background-color: #f5f5f5;
                font-weight: bold;
            }}
            ul {{
                margin-top: 5px;
                margin-bottom: 5px;
            }}
            .footer {{
                margin-top: 30px;
                text-align: center;
                color: #7f8c8d;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <h1>Data Visualization Pricing Analysis</h1>
        
        <div class="section">
            <h2>1. Client Information</h2>
            <table>
                <tr>
                    <th>Client Name</th>
                    <td>{submission_data.get('client_name', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Client Type</th>
                    <td>{submission_data.get('client_type', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Industry Sector</th>
                    <td>{submission_data.get('industry_sector', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Company Size</th>
                    <td>{submission_data.get('company_size', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Annual Revenue</th>
                    <td>{submission_data.get('annual_revenue', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Primary Contact</th>
                    <td>{submission_data.get('primary_contact_name', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Email</th>
                    <td>{submission_data.get('email', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Phone Number</th>
                    <td>{submission_data.get('phone_number', 'Not specified')}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>2. Project Overview</h2>
            <table>
                <tr>
                    <th>Project Title</th>
                    <td>{submission_data.get('project_title', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Project Description</th>
                    <td>{submission_data.get('project_description', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Business Objective</th>
                    <td>{submission_data.get('business_objective', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Expected Deliverables</th>
                    <td>{format_list_items(submission_data.get('deliverables', []))}</td>
                </tr>
                <tr>
                    <th>Target Audience</th>
                    <td>{format_list_items(submission_data.get('audience', []))}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>3. Technical Scope</h2>
            <table>
                <tr>
                    <th>Data Sources</th>
                    <td>{format_list_items(submission_data.get('data_sources', []))}</td>
                </tr>
                <tr>
                    <th>Volume of Data</th>
                    <td>{submission_data.get('data_volume', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Required Integrations</th>
                    <td>{format_list_items(submission_data.get('integrations', []))}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>4. Features & Functionalities</h2>
            <table>
                <tr>
                    <th>Interactivity Needed</th>
                    <td>{format_list_items(submission_data.get('interactivity', []))}</td>
                </tr>
                <tr>
                    <th>User Access Levels</th>
                    <td>{format_list_items(submission_data.get('access_levels', []))}</td>
                </tr>
                <tr>
                    <th>Customization Needs</th>
                    <td>{format_list_items(submission_data.get('customizations', []))}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>5. Pricing Factors</h2>
            <table>
                <tr>
                    <th>Engagement Type</th>
                    <td>{submission_data.get('engagement_type', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Estimated Timeline</th>
                    <td>Start: {format_date(submission_data.get('estimated_start_date'))}<br>
                        End: {format_date(submission_data.get('estimated_end_date'))}</td>
                </tr>
                <tr>
                    <th>Delivery Model</th>
                    <td>{submission_data.get('delivery_model', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Support Plan Required</th>
                    <td>{submission_data.get('support_plan', 'Not specified')}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>6. Competitive/Value-based Inputs</h2>
            <table>
                <tr>
                    <th>Budget Range</th>
                    <td>{submission_data.get('budget_range', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Competitor Comparison</th>
                    <td>{submission_data.get('competitor_comparison', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>ROI Expectations</th>
                    <td>{submission_data.get('roi_expectations', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Tiered Pricing Model Needed</th>
                    <td>{'Yes' if submission_data.get('tiered_pricing_needed') else 'No'}</td>
                </tr>
                <tr>
                    <th>Tiered Pricing Details</th>
                    <td>{submission_data.get('tiered_pricing_details', 'Not specified')}</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2>7. Analyst Notes & Recommendations</h2>
            <table>
                <tr>
                    <th>Internal Analyst Notes</th>
                    <td>{submission_data.get('analyst_notes', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Suggested Pricing Model</th>
                    <td>{submission_data.get('suggested_pricing_model', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Risk Factors / Considerations</th>
                    <td>{submission_data.get('risk_factors', 'Not specified')}</td>
                </tr>
                <tr>
                    <th>Suggested Next Steps</th>
                    <td>{submission_data.get('next_steps', 'Not specified')}</td>
                </tr>
            </table>
        </div>
        
        <div class="footer">
            <p>Generated on {datetime.now().strftime("%B %d, %Y at %H:%M")}</p>
        </div>
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    pdf_bytes = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_bytes)
    pdf_bytes.seek(0)
    
    return pdf_bytes.getvalue()
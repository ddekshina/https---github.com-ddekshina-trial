from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from models import Client, Project
from database import db, init_db
import json
from datetime import datetime
from xhtml2pdf import pisa
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize database
init_db(app)

@app.route('/api/pricing-analysis', methods=['POST'])
def create_pricing_analysis():
    """Endpoint to create a new pricing analysis record"""
    try:
        data = request.get_json()
        
        # Create Client
        client = Client(
            client_name=data['client']['client_name'],
            client_type=data['client']['client_type'],
            industry_sector=data['client']['industry_sector'],
            company_size=data['client']['company_size'],
            annual_revenue=data['client']['annual_revenue'],
            primary_contact=data['client']['primary_contact'],
            email=data['client']['email'],
            phone=data['client']['phone']
        )
        db.session.add(client)
        db.session.commit()
        
        # Create Project
        project = Project(
            client_id=client.id,
            title=data['project']['title'],
            description=data['project']['description'],
            business_objective=data['project']['business_objective'],
            expected_deliverables=json.dumps(data['project']['expected_deliverables']),
            target_audience=json.dumps(data['project']['target_audience']),
            data_sources=json.dumps(data['technical']['data_sources']),
            data_volume=data['technical']['data_volume'],
            required_integrations=json.dumps(data['technical']['required_integrations']),
            interactivity_needed=json.dumps(data['features']['interactivity_needed']),
            user_access_levels=json.dumps(data['features']['user_access_levels']),
            customization_needs=json.dumps(data['features']['customization_needs']),
            engagement_type=data['pricing']['engagement_type'],
            start_date=datetime.strptime(data['pricing']['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['pricing']['end_date'], '%Y-%m-%d') if data['pricing']['end_date'] else None,
            delivery_model=data['pricing']['delivery_model'],
            support_plan=data['pricing']['support_plan'],
            budget_range=data['competitive']['budget_range'],
            competitor_comparison=data['competitive']['competitor_comparison'],
            roi_expectations=data['competitive']['roi_expectations'],
            tiered_pricing_needed=data['competitive']['tiered_pricing_needed'],
            tiered_pricing_details=data['competitive']['tiered_pricing_details'],
            internal_notes=data['analyst']['internal_notes'],
            suggested_pricing_model=data['analyst']['suggested_pricing_model'],
            risk_factors=data['analyst']['risk_factors'],
            next_steps=data['analyst']['next_steps']
        )
        db.session.add(project)
        db.session.commit()
        
        return jsonify({
            'message': 'Pricing analysis created successfully',
            'client_id': client.id,
            'project_id': project.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/pricing-analysis/<int:id>', methods=['GET'])
def get_pricing_analysis(id):
    """Endpoint to get a pricing analysis record by ID"""
    try:
        client = Client.query.get_or_404(id)
        project = Project.query.filter_by(client_id=id).first_or_404()
        
        response = {
            'client': {
                'client_name': client.client_name,
                'client_type': client.client_type,
                'industry_sector': client.industry_sector,
                'company_size': client.company_size,
                'annual_revenue': client.annual_revenue,
                'primary_contact': client.primary_contact,
                'email': client.email,
                'phone': client.phone
            },
            'project': {
                'title': project.title,
                'description': project.description,
                'business_objective': project.business_objective,
                'expected_deliverables': json.loads(project.expected_deliverables),
                'target_audience': json.loads(project.target_audience),
                'data_sources': json.loads(project.data_sources),
                'data_volume': project.data_volume,
                'required_integrations': json.loads(project.required_integrations),
                'interactivity_needed': json.loads(project.interactivity_needed),
                'user_access_levels': json.loads(project.user_access_levels),
                'customization_needs': json.loads(project.customization_needs),
                'engagement_type': project.engagement_type,
                'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
                'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
                'delivery_model': project.delivery_model,
                'support_plan': project.support_plan,
                'budget_range': project.budget_range,
                'competitor_comparison': project.competitor_comparison,
                'roi_expectations': project.roi_expectations,
                'tiered_pricing_needed': project.tiered_pricing_needed,
                'tiered_pricing_details': project.tiered_pricing_details,
                'internal_notes': project.internal_notes,
                'suggested_pricing_model': project.suggested_pricing_model,
                'risk_factors': project.risk_factors,
                'next_steps': project.next_steps,
                'created_at': project.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'updated_at': project.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 404
    
@app.route('/api/generate-pdf/<int:project_id>', methods=['GET'])
def generate_pdf(project_id):
    try:
        # Get project data
        project = Project.query.get_or_404(project_id)
        client = Client.query.get_or_404(project.client_id)

        # Create HTML template
        html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                .section {{ margin-bottom: 20px; }}
                .section-title {{ font-weight: bold; margin-bottom: 10px; }}
                .field {{ margin-bottom: 5px; }}
                .field-label {{ font-weight: bold; display: inline-block; width: 200px; }}
            </style>
        </head>
        <body>
            <h1>Pricing Analysis Report</h1>
            
            <div class="section">
                <div class="section-title">1. Client Information</div>
                <div class="field"><span class="field-label">Client Name:</span> {client.client_name}</div>
                <div class="field"><span class="field-label">Client Type:</span> {client.client_type}</div>
                <!-- Add all other fields similarly -->
            </div>
            
            <!-- Add all other sections similarly -->
        </body>
        </html>
        """

        # Generate PDF
        pdf = BytesIO()
        pisa.CreatePDF(BytesIO(html.encode('UTF-8')), pdf)
        pdf.seek(0)

        return send_file(
            pdf,
            as_attachment=True,
            download_name=f"pricing_analysis_{project_id}.pdf",
            mimetype='application/pdf'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
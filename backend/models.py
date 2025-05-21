from database import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_type = db.Column(db.String(20), nullable=False)  # B2B or B2B2B
    industry_sector = db.Column(db.String(100))
    company_size = db.Column(db.String(50))
    annual_revenue = db.Column(db.String(50))
    primary_contact = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    
    # Relationship to Project
    project = db.relationship('Project', backref='client', uselist=False, cascade="all, delete-orphan")

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    business_objective = db.Column(db.Text)
    expected_deliverables = db.Column(db.Text)  # JSON string of selected options
    target_audience = db.Column(db.Text)  # JSON string of selected options
    
    # Technical Scope
    data_sources = db.Column(db.Text)  # JSON string
    data_volume = db.Column(db.String(50))
    required_integrations = db.Column(db.Text)  # JSON string
    
    # Features
    interactivity_needed = db.Column(db.Text)  # JSON string
    user_access_levels = db.Column(db.Text)  # JSON string
    customization_needs = db.Column(db.Text)  # JSON string
    
    # Pricing
    engagement_type = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    delivery_model = db.Column(db.String(100))
    support_plan = db.Column(db.String(50))
    
    # Competitive
    budget_range = db.Column(db.String(100))
    competitor_comparison = db.Column(db.Text)
    roi_expectations = db.Column(db.Text)
    tiered_pricing_needed = db.Column(db.Boolean)
    tiered_pricing_details = db.Column(db.Text)
    
    # Analyst
    internal_notes = db.Column(db.Text)
    suggested_pricing_model = db.Column(db.Text)
    risk_factors = db.Column(db.Text)
    next_steps = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
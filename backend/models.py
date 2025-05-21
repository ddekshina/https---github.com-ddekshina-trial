from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

# Association tables for many-to-many relationships
project_deliverables = db.Table('project_deliverables',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('deliverable', db.String(50))
)

project_audience = db.Table('project_audience',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('audience', db.String(50))
)

data_sources = db.Table('data_sources',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('source', db.String(50))
)

required_integrations = db.Table('required_integrations',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('integration', db.String(50))
)

interactivity_needs = db.Table('interactivity_needs',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('need', db.String(50))
)

user_access_levels = db.Table('user_access_levels',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('level', db.String(50))
)

customization_needs = db.Table('customization_needs',
    db.Column('submission_id', db.Integer, db.ForeignKey('submission.id')),
    db.Column('need', db.String(50))
)

class Submission(db.Model):
    """Main submission model that holds all form data."""
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Client Information
    client_name = db.Column(db.String(100), nullable=False)
    client_type = db.Column(db.String(10), nullable=False)  # B2B or B2B2B
    industry_sector = db.Column(db.String(100))
    company_size = db.Column(db.String(100))
    annual_revenue = db.Column(db.String(100))
    primary_contact_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    
    # Project Overview
    project_title = db.Column(db.String(200))
    project_description = db.Column(db.Text)
    business_objective = db.Column(db.Text)
    # Expected Deliverables - Many-to-many relationship
    deliverables = db.relationship('Submission', secondary=project_deliverables,
                                   primaryjoin=(id == project_deliverables.c.submission_id),
                                   backref=db.backref('project_deliverables_assoc', lazy='dynamic'),
                                   lazy='dynamic')
    # Target Audience - Many-to-many relationship
    audience = db.relationship('Submission', secondary=project_audience,
                               primaryjoin=(id == project_audience.c.submission_id),
                               backref=db.backref('project_audience_assoc', lazy='dynamic'),
                               lazy='dynamic')
    
    # Technical Scope
    # Data Sources - Many-to-many relationship
    data_sources_rel = db.relationship('Submission', secondary=data_sources,
                                    primaryjoin=(id == data_sources.c.submission_id),
                                    backref=db.backref('data_sources_assoc', lazy='dynamic'),
                                    lazy='dynamic')
    data_volume = db.Column(db.String(50))
    # Required Integrations - Many-to-many relationship
    integrations = db.relationship('Submission', secondary=required_integrations,
                                  primaryjoin=(id == required_integrations.c.submission_id),
                                  backref=db.backref('required_integrations_assoc', lazy='dynamic'),
                                  lazy='dynamic')
    
    # Features & Functionalities
    # Interactivity Needed - Many-to-many relationship
    interactivity = db.relationship('Submission', secondary=interactivity_needs,
                                   primaryjoin=(id == interactivity_needs.c.submission_id),
                                   backref=db.backref('interactivity_needs_assoc', lazy='dynamic'),
                                   lazy='dynamic')
    # User Access Levels - Many-to-many relationship
    access_levels = db.relationship('Submission', secondary=user_access_levels,
                                   primaryjoin=(id == user_access_levels.c.submission_id),
                                   backref=db.backref('user_access_levels_assoc', lazy='dynamic'),
                                   lazy='dynamic')
    # Customization Needs - Many-to-many relationship
    customizations = db.relationship('Submission', secondary=customization_needs,
                                    primaryjoin=(id == customization_needs.c.submission_id),
                                    backref=db.backref('customization_needs_assoc', lazy='dynamic'),
                                    lazy='dynamic')
    
    # Pricing Factors
    engagement_type = db.Column(db.String(50))
    estimated_start_date = db.Column(db.Date)
    estimated_end_date = db.Column(db.Date)
    delivery_model = db.Column(db.String(50))
    support_plan = db.Column(db.String(50))
    
    # Competitive/Value-based Inputs
    budget_range = db.Column(db.String(100))
    competitor_comparison = db.Column(db.Text)
    roi_expectations = db.Column(db.Text)
    tiered_pricing_needed = db.Column(db.Boolean, default=False)
    tiered_pricing_details = db.Column(db.Text)
    
    # Analyst Notes & Recommendations
    analyst_notes = db.Column(db.Text)
    suggested_pricing_model = db.Column(db.Text)
    risk_factors = db.Column(db.Text)
    next_steps = db.Column(db.Text)

    def to_dict(self):
        """Convert submission to dictionary for JSON serialization."""
        # Helper function to get values from many-to-many relationships
        def get_relationship_values(relationship_table, submission_id, value_col):
            query = db.session.query(relationship_table.c[value_col]).filter(
                relationship_table.c.submission_id == submission_id
            )
            return [row[0] for row in query.all()]
        
        data = {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            
            # Client Information
            'client_name': self.client_name,
            'client_type': self.client_type,
            'industry_sector': self.industry_sector,
            'company_size': self.company_size,
            'annual_revenue': self.annual_revenue,
            'primary_contact_name': self.primary_contact_name,
            'email': self.email,
            'phone_number': self.phone_number,
            
            # Project Overview
            'project_title': self.project_title,
            'project_description': self.project_description,
            'business_objective': self.business_objective,
            'deliverables': get_relationship_values(project_deliverables, self.id, 'deliverable'),
            'audience': get_relationship_values(project_audience, self.id, 'audience'),
            
            # Technical Scope
            'data_sources': get_relationship_values(data_sources, self.id, 'source'),
            'data_volume': self.data_volume,
            'integrations': get_relationship_values(required_integrations, self.id, 'integration'),
            
            # Features & Functionalities
            'interactivity': get_relationship_values(interactivity_needs, self.id, 'need'),
            'access_levels': get_relationship_values(user_access_levels, self.id, 'level'),
            'customizations': get_relationship_values(customization_needs, self.id, 'need'),
            
            # Pricing Factors
            'engagement_type': self.engagement_type,
            'estimated_start_date': self.estimated_start_date.isoformat() if self.estimated_start_date else None,
            'estimated_end_date': self.estimated_end_date.isoformat() if self.estimated_end_date else None,
            'delivery_model': self.delivery_model,
            'support_plan': self.support_plan,
            
            # Competitive/Value-based Inputs
            'budget_range': self.budget_range,
            'competitor_comparison': self.competitor_comparison,
            'roi_expectations': self.roi_expectations,
            'tiered_pricing_needed': self.tiered_pricing_needed,
            'tiered_pricing_details': self.tiered_pricing_details,
            
            # Analyst Notes & Recommendations
            'analyst_notes': self.analyst_notes,
            'suggested_pricing_model': self.suggested_pricing_model,
            'risk_factors': self.risk_factors,
            'next_steps': self.next_steps
        }
        
        return data

    @classmethod
    def create_from_dict(cls, data):
        """Create a new submission from dictionary data."""
        submission = cls(
            # Client Information
            client_name=data.get('client_name'),
            client_type=data.get('client_type'),
            industry_sector=data.get('industry_sector'),
            company_size=data.get('company_size'),
            annual_revenue=data.get('annual_revenue'),
            primary_contact_name=data.get('primary_contact_name'),
            email=data.get('email'),
            phone_number=data.get('phone_number'),
            
            # Project Overview
            project_title=data.get('project_title'),
            project_description=data.get('project_description'),
            business_objective=data.get('business_objective'),
            
            # Technical Scope
            data_volume=data.get('data_volume'),
            
            # Pricing Factors
            engagement_type=data.get('engagement_type'),
            estimated_start_date=datetime.fromisoformat(data.get('estimated_start_date')) if data.get('estimated_start_date') else None,
            estimated_end_date=datetime.fromisoformat(data.get('estimated_end_date')) if data.get('estimated_end_date') else None,
            delivery_model=data.get('delivery_model'),
            support_plan=data.get('support_plan'),
            
            # Competitive/Value-based Inputs
            budget_range=data.get('budget_range'),
            competitor_comparison=data.get('competitor_comparison'),
            roi_expectations=data.get('roi_expectations'),
            tiered_pricing_needed=data.get('tiered_pricing_needed', False),
            tiered_pricing_details=data.get('tiered_pricing_details'),
            
            # Analyst Notes & Recommendations
            analyst_notes=data.get('analyst_notes'),
            suggested_pricing_model=data.get('suggested_pricing_model'),
            risk_factors=data.get('risk_factors'),
            next_steps=data.get('next_steps')
        )
        
        db.session.add(submission)
        db.session.flush()  # Get ID before committing
        
        # Handle many-to-many relationships
        if data.get('deliverables'):
            for item in data['deliverables']:
                db.session.execute(project_deliverables.insert().values(
                    submission_id=submission.id, deliverable=item
                ))
                
        if data.get('audience'):
            for item in data['audience']:
                db.session.execute(project_audience.insert().values(
                    submission_id=submission.id, audience=item
                ))
                
        if data.get('data_sources'):
            for item in data['data_sources']:
                db.session.execute(data_sources.insert().values(
                    submission_id=submission.id, source=item
                ))
                
        if data.get('integrations'):
            for item in data['integrations']:
                db.session.execute(required_integrations.insert().values(
                    submission_id=submission.id, integration=item
                ))
                
        if data.get('interactivity'):
            for item in data['interactivity']:
                db.session.execute(interactivity_needs.insert().values(
                    submission_id=submission.id, need=item
                ))
                
        if data.get('access_levels'):
            for item in data['access_levels']:
                db.session.execute(user_access_levels.insert().values(
                    submission_id=submission.id, level=item
                ))
                
        if data.get('customizations'):
            for item in data['customizations']:
                db.session.execute(customization_needs.insert().values(
                    submission_id=submission.id, need=item
                ))
        
        db.session.commit()
        return submission
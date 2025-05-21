import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import FormSection from '../components/FormSection';
import '../index.css';

const FormPage = () => {
  const [formData, setFormData] = useState({
    client: {
      client_name: '',
      client_type: 'B2B',
      industry_sector: '',
      company_size: '',
      annual_revenue: '',
      primary_contact: '',
      email: '',
      phone: ''
    },
    project: {
      title: '',
      description: '',
      business_objective: '',
      expected_deliverables: [],
      target_audience: []
    },
    technical: {
      data_sources: [],
      data_volume: '',
      required_integrations: []
    },
    features: {
      interactivity_needed: [],
      user_access_levels: [],
      customization_needs: []
    },
    pricing: {
      engagement_type: '',
      start_date: '',
      end_date: '',
      delivery_model: '',
      support_plan: ''
    },
    competitive: {
      budget_range: '',
      competitor_comparison: '',
      roi_expectations: '',
      tiered_pricing_needed: false,
      tiered_pricing_details: ''
    },
    analyst: {
      internal_notes: '',
      suggested_pricing_model: '',
      risk_factors: '',
      next_steps: ''
    }
  });

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/pricing-analysis', formData);
      navigate(`/success/${response.data.project_id}`);
    } catch (error) {
      console.error('Error submitting form:', error);
      alert('Error submitting form. Please check console for details.');
    }
  };

  const handleChange = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value
      }
    }));
  };

  const handleMultiSelect = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value
      }
    }));
  };

  const handleCheckboxChange = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value === 'true' || value === true
      }
    }));
  };

  return (
    <div className="form-container">
      <h1>Data Visualization Pricing Analyst Form</h1>
      <form onSubmit={handleSubmit}>
        <FormSection 
          title="1. Client Information"
          fields={[
            { type: 'text', id: 'client_name', label: 'Client Name:', required: true },
            { type: 'select', id: 'client_type', label: 'Client Type:', 
              options: ['B2B', 'B2B2B'], required: true },
            { type: 'text', id: 'industry_sector', label: 'Industry Sector:' },
            { type: 'text', id: 'company_size', label: 'Company Size (Employees):' },
            { type: 'text', id: 'annual_revenue', label: 'Annual Revenue (USD):' },
            { type: 'text', id: 'primary_contact', label: 'Primary Contact Name:' },
            { type: 'email', id: 'email', label: 'Email:', required: true },
            { type: 'tel', id: 'phone', label: 'Phone Number:' },
          ]}
          data={formData.client}
          section="client"
          onChange={handleChange}
        />
        
        <FormSection 
          title="2. Project Overview"
          fields={[
            { type: 'text', id: 'title', label: 'Project Title / Name:', required: true },
            { type: 'textarea', id: 'description', label: 'Project Description:' },
            { type: 'textarea', id: 'business_objective', label: 'Business Objective:' },
            { type: 'multiselect', id: 'expected_deliverables', label: 'Expected Deliverables (Select all that apply):',
              options: ['Dashboards', 'Charts / Graphs', 'KPI Reporting', 'Interactive Reports', 
                'Embedded Analytics', 'Infographics', 'White-labeled Portals'] },
            { type: 'multiselect', id: 'target_audience', label: 'Target Audience:',
              options: ['Internal Teams', 'External Clients', 'Partners / Vendors'] },
          ]}
          data={formData.project}
          section="project"
          onChange={handleChange}
          onMultiSelect={handleMultiSelect}
        />
        
        <FormSection 
          title="3. Technical Scope"
          fields={[
            { type: 'multiselect', id: 'data_sources', label: 'Data Sources (Select all that apply):',
              options: ['Excel/CSV', 'APIs', 'Databases (SQL/NoSQL)', 'Cloud Storage (Google Drive, S3, etc.)'] },
            { type: 'select', id: 'data_volume', label: 'Volume of Data:',
              options: ['Small (<1M rows)', 'Medium (1M–10M rows)', 'Large (10M+ rows)'] },
            { type: 'multiselect', id: 'required_integrations', label: 'Required Integrations:',
              options: ['CRM (e.g., Salesforce)', 'ERP (e.g., SAP)', 'BI Tools (e.g., Power BI, Tableau)', 'Custom APIs'] },
          ]}
          data={formData.technical}
          section="technical"
          onChange={handleChange}
          onMultiSelect={handleMultiSelect}
        />
        
        <FormSection 
          title="4. Features & Functionalities"
          fields={[
            { type: 'multiselect', id: 'interactivity_needed', label: 'Interactivity Needed:',
              options: ['Drill-down', 'Filtering', 'Export Options', 'Real-time Updates'] },
            { type: 'multiselect', id: 'user_access_levels', label: 'User Access Levels:',
              options: ['Admin', 'Viewer', 'Editor'] },
            { type: 'multiselect', id: 'customization_needs', label: 'Customization Needs:',
              options: ['Branding / White-labeling', 'Theming (Light/Dark)', 'Language Localization'] },
          ]}
          data={formData.features}
          section="features"
          onChange={handleChange}
          onMultiSelect={handleMultiSelect}
        />
        
        <FormSection 
          title="5. Pricing Factors"
          fields={[
            { type: 'select', id: 'engagement_type', label: 'Engagement Type:',
              options: ['One-time Project', 'Monthly Retainer', 'Subscription (SaaS-style)'] },
            { type: 'date', id: 'start_date', label: 'Start Date:' },
            { type: 'date', id: 'end_date', label: 'End Date:' },
            { type: 'select', id: 'delivery_model', label: 'Delivery Model:',
              options: ['Web Portal', 'API-based Delivery', 'Downloadable Reports'] },
            { type: 'select', id: 'support_plan', label: 'Support Plan Required:',
              options: ['Basic (Email)', 'Priority (Phone + Email)', 'Dedicated Account Manager'] },
          ]}
          data={formData.pricing}
          section="pricing"
          onChange={handleChange}
        />
        
        <FormSection 
          title="6. Competitive/Value-based Inputs"
          fields={[
            { type: 'select', id: 'budget_range', label: 'Client\'s Budget Range (USD):',
              options: ['$0-$5,000', '$5,000-$20,000', '$20,000-$50,000', '$50,000-$100,000', '$100,000+'] },
            { type: 'textarea', id: 'competitor_comparison', label: 'Competitor Comparison (if known):' },
            { type: 'textarea', id: 'roi_expectations', label: 'ROI Expectations or KPIs to Measure Success:' },
            { type: 'select', id: 'tiered_pricing_needed', label: 'Any Tiered Pricing Model Needed (for B2B2B resale)?',
              options: ['true', 'false'] },
            { type: 'textarea', id: 'tiered_pricing_details', label: 'If yes, provide details:' },
          ]}
          data={formData.competitive}
          section="competitive"
          onChange={(section, field, value) => {
            if (field === 'tiered_pricing_needed') {
              handleCheckboxChange(section, field, value);
            } else {
              handleChange(section, field, value);
            }
          }}
        />
        
        <FormSection 
          title="7. Analyst Notes & Recommendations"
          fields={[
            { type: 'textarea', id: 'internal_notes', label: 'Internal Analyst Notes:' },
            { type: 'textarea', id: 'suggested_pricing_model', label: 'Suggested Pricing Model:' },
            { type: 'textarea', id: 'risk_factors', label: 'Risk Factors / Considerations:' },
            { type: 'textarea', id: 'next_steps', label: 'Suggested Next Steps:' },
          ]}
          data={formData.analyst}
          section="analyst"
          onChange={handleChange}
        />
        
        <button type="submit" className="submit-btn">Submit Form</button>
      </form>
    </div>
  );
};

export default FormPage;
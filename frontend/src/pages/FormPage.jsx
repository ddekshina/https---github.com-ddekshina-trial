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
    // ... other sections
  });

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/pricing-analysis', formData);
      navigate(`/success/${response.data.project_id}`);
    } catch (error) {
      console.error('Error submitting form:', error);
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

  return (
    <div className="form-container">
      <h1>Data Visualization Pricing Analyst Form</h1>
      <form onSubmit={handleSubmit}>
        <FormSection 
          title="1. Client Information"
          fields={[
            { type: 'text', id: 'client_name', label: 'Client Name:', required: true },
            { type: 'select', id: 'client_type', label: 'Client Type:', 
              options: ['B2B', 'B2B2B'] },
            // ... other fields
          ]}
          data={formData.client}
          section="client"
          onChange={handleChange}
        />
        
        {/* Other sections */}
        
        <button type="submit" className="submit-btn">Submit Form</button>
      </form>
    </div>
  );
};

export default FormPage;
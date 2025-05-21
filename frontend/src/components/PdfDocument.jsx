import React from 'react';
import { Document, Page, Text, View, StyleSheet } from '@react-pdf/renderer';

const styles = StyleSheet.create({
  page: {
    padding: 40,
    fontFamily: 'Helvetica',
  },
  header: {
    fontSize: 24,
    marginBottom: 20,
    color: '#2c3e50',
    borderBottomWidth: 2,
    borderBottomColor: '#3498db',
    paddingBottom: 10,
  },
  section: {
    marginBottom: 25,
  },
  sectionTitle: {
    fontSize: 18,
    marginBottom: 10,
    color: '#3498db',
    fontWeight: 'bold',
  },
  field: {
    flexDirection: 'row',
    marginBottom: 6,
  },
  label: {
    width: 160,
    fontWeight: 'bold',
    color: '#2c3e50',
  },
  value: {
    flex: 1,
    color: '#34495e',
  },
  list: {
    marginLeft: 20,
  },
  listItem: {
    marginBottom: 3,
  }
});

const PdfDocument = ({ projectId, data = {} }) => {
  const client = data?.client || {};
  const project = data?.project || {};
  
  const renderArrayField = (array = []) => {
    if (!array || array.length === 0) return 'None';
    return array.join(', ');
  };

  return (
    <Document>
      <Page size="A4" style={styles.page}>
        <Text style={styles.header}>Pricing Analysis Report</Text>

        {/* Section 1: Client Information */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>1. Client Information</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Client Name:</Text>
            <Text style={styles.value}>{client.client_name || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Client Type:</Text>
            <Text style={styles.value}>{client.client_type || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Industry Sector:</Text>
            <Text style={styles.value}>{client.industry_sector || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Company Size:</Text>
            <Text style={styles.value}>{client.company_size || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Annual Revenue:</Text>
            <Text style={styles.value}>{client.annual_revenue || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Primary Contact:</Text>
            <Text style={styles.value}>{client.primary_contact || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Email:</Text>
            <Text style={styles.value}>{client.email || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Phone:</Text>
            <Text style={styles.value}>{client.phone || 'N/A'}</Text>
          </View>
        </View>

        {/* Section 2: Project Overview */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>2. Project Overview</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Project Title:</Text>
            <Text style={styles.value}>{project.title || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Description:</Text>
            <Text style={styles.value}>{project.description || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Business Objective:</Text>
            <Text style={styles.value}>{project.business_objective || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Expected Deliverables:</Text>
            <Text style={styles.value}>{renderArrayField(project.expected_deliverables)}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Target Audience:</Text>
            <Text style={styles.value}>{renderArrayField(project.target_audience)}</Text>
          </View>
        </View>

        {/* Technical Scope */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>3. Technical Scope</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Data Sources:</Text>
            <Text style={styles.value}>{renderArrayField(project.data_sources)}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Data Volume:</Text>
            <Text style={styles.value}>{project.data_volume || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Required Integrations:</Text>
            <Text style={styles.value}>{renderArrayField(project.required_integrations)}</Text>
          </View>
        </View>

        {/* Features & Functionalities */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>4. Features & Functionalities</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Interactivity Needed:</Text>
            <Text style={styles.value}>{renderArrayField(project.interactivity_needed)}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>User Access Levels:</Text>
            <Text style={styles.value}>{renderArrayField(project.user_access_levels)}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Customization Needs:</Text>
            <Text style={styles.value}>{renderArrayField(project.customization_needs)}</Text>
          </View>
        </View>

        {/* Pricing Factors */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>5. Pricing Factors</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Engagement Type:</Text>
            <Text style={styles.value}>{project.engagement_type || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Start Date:</Text>
            <Text style={styles.value}>{project.start_date || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>End Date:</Text>
            <Text style={styles.value}>{project.end_date || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Delivery Model:</Text>
            <Text style={styles.value}>{project.delivery_model || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Support Plan:</Text>
            <Text style={styles.value}>{project.support_plan || 'N/A'}</Text>
          </View>
        </View>

        {/* Competitive Value-based Inputs */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>6. Competitive/Value-based Inputs</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Budget Range:</Text>
            <Text style={styles.value}>{project.budget_range || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Competitor Comparison:</Text>
            <Text style={styles.value}>{project.competitor_comparison || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>ROI Expectations:</Text>
            <Text style={styles.value}>{project.roi_expectations || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Tiered Pricing Needed:</Text>
            <Text style={styles.value}>{project.tiered_pricing_needed ? 'Yes' : 'No'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Tiered Pricing Details:</Text>
            <Text style={styles.value}>{project.tiered_pricing_details || 'N/A'}</Text>
          </View>
        </View>

        {/* Analyst Notes */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>7. Analyst Notes & Recommendations</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Internal Notes:</Text>
            <Text style={styles.value}>{project.internal_notes || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Pricing Model:</Text>
            <Text style={styles.value}>{project.suggested_pricing_model || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Risk Factors:</Text>
            <Text style={styles.value}>{project.risk_factors || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Next Steps:</Text>
            <Text style={styles.value}>{project.next_steps || 'N/A'}</Text>
          </View>
        </View>
      </Page>
    </Document>
  );
};

export default PdfDocument;
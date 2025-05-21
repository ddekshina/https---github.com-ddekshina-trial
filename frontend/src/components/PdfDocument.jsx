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
});

const PdfDocument = ({ projectId, clientData = {}, projectData = {} }) => {
  return (
    <Document>
      <Page size="A4" style={styles.page}>
        <Text style={styles.header}>Pricing Analysis Report</Text>

        {/* Section 1: Client Information */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>1. Client Information</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Client Name:</Text>
            <Text style={styles.value}>{clientData.client_name || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Email:</Text>
            <Text style={styles.value}>{clientData.email || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Phone:</Text>
            <Text style={styles.value}>{clientData.phone || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Organization:</Text>
            <Text style={styles.value}>{clientData.organization || 'N/A'}</Text>
          </View>
        </View>

        {/* Section 2: Project Overview */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>2. Project Overview</Text>

          <View style={styles.field}>
            <Text style={styles.label}>Project Title:</Text>
            <Text style={styles.value}>{projectData.title || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Description:</Text>
            <Text style={styles.value}>{projectData.description || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Start Date:</Text>
            <Text style={styles.value}>{projectData.start_date || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>End Date:</Text>
            <Text style={styles.value}>{projectData.end_date || 'N/A'}</Text>
          </View>

          <View style={styles.field}>
            <Text style={styles.label}>Budget:</Text>
            <Text style={styles.value}>
              {projectData.budget ? `$${projectData.budget}` : 'N/A'}
            </Text>
          </View>
        </View>

        {/* Section 3: Project ID */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>3. Project ID</Text>
          <View style={styles.field}>
            <Text style={styles.label}>ID:</Text>
            <Text style={styles.value}>{projectId || 'N/A'}</Text>
          </View>
        </View>

        {/* You can continue adding more sections like: Pricing Breakdown, Analysis Summary, etc. */}

      </Page>
    </Document>
  );
};

export default PdfDocument;

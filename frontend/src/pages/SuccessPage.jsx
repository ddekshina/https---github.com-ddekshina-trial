import { useParams } from 'react-router-dom';
import ReportActions from '../components/ReportActions';
import { useEffect, useState } from 'react';
import axios from 'axios';

const SuccessPage = () => {
  const { projectId } = useParams();
  const [reportData, setReportData] = useState(null);

  useEffect(() => {
    const fetchReportData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/pricing-analysis/${projectId}`
        );
        setReportData(response.data);
      } catch (error) {
        console.error('Error fetching report data:', error);
      }
    };

    fetchReportData();
  }, [projectId]);

  return (
    <div className="success-container">
      <h1>Analysis Submitted Successfully!</h1>
      <p>Your pricing analysis has been saved with ID: {projectId}</p>
      
      {reportData && (
        <div className="report-summary">
          <h2>Report Summary</h2>
          <div className="summary-item">
            <strong>Client:</strong> {reportData.client.client_name}
          </div>
          <div className="summary-item">
            <strong>Project:</strong> {reportData.project.title}
          </div>
          {/* Add more summary items */}
        </div>
      )}

      <ReportActions projectId={projectId} />
    </div>
  );
};

export default SuccessPage;
import { PDFDownloadLink } from '@react-pdf/renderer';
import {
  EmailShareButton,
  LinkedinShareButton,
  WhatsappShareButton,
  EmailIcon,
  LinkedinIcon,
  WhatsappIcon
} from 'react-share';

const ReportActions = ({ projectId }) => {
  const shareUrl = `${window.location.origin}/success/${projectId}`;
  const title = 'Pricing Analysis Report';

  const handleNativeShare = async () => {
    try {
      await navigator.share({
        title,
        text: 'Check out this pricing analysis report',
        url: shareUrl,
      });
    } catch (err) {
      console.log('Native share not supported', err);
    }
  };

  return (
    <div className="report-actions">
      <PDFDownloadLink
        document={<PdfDocument projectId={projectId} />}
        fileName={`pricing_analysis_${projectId}.pdf`}
        className="download-link"
      >
        {({ loading }) => (
          <button className="action-btn download">
            {loading ? 'Preparing PDF...' : 'Download PDF'}
          </button>
        )}
      </PDFDownloadLink>

      <button onClick={handleNativeShare} className="action-btn share">
        Share Report
      </button>

      <div className="social-share">
        <EmailShareButton url={shareUrl} subject={title} body="Check out this pricing analysis report:">
          <EmailIcon size={32} round />
        </EmailShareButton>
        <LinkedinShareButton url={shareUrl} title={title}>
          <LinkedinIcon size={32} round />
        </LinkedinShareButton>
        <WhatsappShareButton url={shareUrl} title={title}>
          <WhatsappIcon size={32} round />
        </WhatsappShareButton>
      </div>
    </div>
  );
};

export default ReportActions;
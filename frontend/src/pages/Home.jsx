import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <h1>Welcome to Pricing Analyst Tool</h1>
      <p>
        This tool helps you analyze and create pricing proposals for data visualization projects.
      </p>
      <button 
        onClick={() => navigate('/form')}
        className="cta-button"
      >
        Start New Analysis
      </button>
    </div>
  );
};

export default Home;
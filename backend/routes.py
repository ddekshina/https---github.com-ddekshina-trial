from flask import Blueprint, request, jsonify, send_file
from datetime import datetime, timedelta
import json
import io
from models import db, Submission
from utils import generate_pdf

# Create a blueprint for API routes
api = Blueprint('api', __name__)

@api.route('/submissions', methods=['POST'])
def create_submission():
    """
    Create a new form submission
    
    Expects:
        - JSON data in request body containing form submission data
        
    Returns:
        - JSON response with submission ID and status
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # Validate required fields
        if not data.get('client_name'):
            return jsonify({'error': 'Client name is required'}), 400
            
        if not data.get('client_type'):
            return jsonify({'error': 'Client type is required'}), 400
        
        # Create new submission
        submission = Submission.create_from_dict(data)
        
        # Return success response
        return jsonify({
            'message': 'Submission created successfully',
            'id': submission.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api.route('/submissions', methods=['GET'])
def list_submissions():
    """
    List all submissions
    
    Returns:
        - JSON response with list of submissions
    """
    try:
        submissions = Submission.query.order_by(Submission.created_at.desc()).all()
        return jsonify({
            'submissions': [submission.to_dict() for submission in submissions]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/submissions/<int:submission_id>', methods=['GET'])
def get_submission(submission_id):
    """
    Get a specific submission by ID
    
    Args:
        submission_id (int): Submission ID
        
    Returns:
        - JSON response with submission data
    """
    try:
        submission = Submission.query.get(submission_id)
        
        if not submission:
            return jsonify({'error': 'Submission not found'}), 404
            
        return jsonify(submission.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/submissions/<int:submission_id>/pdf', methods=['GET'])
def get_submission_pdf(submission_id):
    """
    Generate and download PDF for a submission
    
    Args:
        submission_id (int): Submission ID
        
    Returns:
        - PDF file download
    """
    try:
        submission = Submission.query.get(submission_id)
        
        if not submission:
            return jsonify({'error': 'Submission not found'}), 404
        
        # Generate PDF using utility function
        pdf_data = generate_pdf(submission)
        
        # Create in-memory file-like object
        pdf_io = io.BytesIO(pdf_data)
        pdf_io.seek(0)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"submission_{submission_id}_{timestamp}.pdf"
        
        # Return PDF file
        return send_file(
            pdf_io,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/submissions/<int:submission_id>', methods=['PUT'])
def update_submission(submission_id):
    """
    Update an existing submission
    
    Args:
        submission_id (int): Submission ID
        
    Expects:
        - JSON data in request body containing updated submission data
        
    Returns:
        - JSON response with updated submission data
    """
    try:
        submission = Submission.query.get(submission_id)
        
        if not submission:
            return jsonify({'error': 'Submission not found'}), 404
        
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update submission with new data
        submission.update_from_dict(data)
        
        return jsonify({
            'message': 'Submission updated successfully',
            'submission': submission.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api.route('/submissions/<int:submission_id>', methods=['DELETE'])
def delete_submission(submission_id):
    """
    Delete a submission
    
    Args:
        submission_id (int): Submission ID
        
    Returns:
        - JSON response with deletion status
    """
    try:
        submission = Submission.query.get(submission_id)
        
        if not submission:
            return jsonify({'error': 'Submission not found'}), 404
        
        # Delete the submission
        db.session.delete(submission)
        db.session.commit()
        
        return jsonify({
            'message': 'Submission deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Note: This endpoint is not listed in app.py documentation
@api.route('/submissions/stats', methods=['GET'])
def get_submission_stats():
    """
    Get statistics about submissions
    
    Returns:
        - JSON response with statistics
    """
    try:
        # Count total submissions
        total_count = Submission.query.count()
        
        # Count submissions by client type
        client_types = db.session.query(
            Submission.client_type,
            db.func.count(Submission.id).label('count')
        ).group_by(Submission.client_type).all()
        
        # Get submissions from the last 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        recent_count = Submission.query.filter(
            Submission.created_at >= thirty_days_ago
        ).count()
        
        return jsonify({
            'total_submissions': total_count,
            'recent_submissions': recent_count,
            'by_client_type': {t.client_type: t.count for t in client_types}
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
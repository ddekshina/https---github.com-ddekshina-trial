import { useState } from 'react';

const MultiSelect = ({ label, options, selected, onChange }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleOption = (option) => {
    const newSelected = selected.includes(option)
      ? selected.filter((item) => item !== option)
      : [...selected, option];
    onChange(newSelected);
  };

  return (
    <div className="form-group">
      <label>{label}</label>
      <div className="multiselect">
        <div className="selected-options" onClick={() => setIsOpen(!isOpen)}>
          {selected.length > 0 ? selected.join(', ') : 'Select options...'}
        </div>
        {isOpen && (
          <div className="options-list">
            {options.map((option) => (
              <div
                key={option}
                className={`option ${selected.includes(option) ? 'selected' : ''}`}
                onClick={() => toggleOption(option)}
              >
                {option}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default MultiSelect;
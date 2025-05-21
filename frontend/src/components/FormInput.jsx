const FormInput = ({ type, id, label, value, required, options, onChange }) => {
  if (type === 'select') {
    return (
      <div className="form-group">
        <label htmlFor={id}>{label}</label>
        <select
          id={id}
          value={value}
          onChange={onChange}
          required={required}
        >
          <option value="">Select an option</option>
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </div>
    );
  }

  if (type === 'textarea') {
    return (
      <div className="form-group">
        <label htmlFor={id}>{label}</label>
        <textarea
          id={id}
          value={value}
          onChange={onChange}
          required={required}
          rows={4}
        />
      </div>
    );
  }

  return (
    <div className="form-group">
      <label htmlFor={id}>{label}</label>
      <input
        type={type}
        id={id}
        value={value}
        onChange={onChange}
        required={required}
      />
    </div>
  );
};

export default FormInput;
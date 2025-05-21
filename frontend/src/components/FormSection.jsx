import FormInput from './FormInput';
import MultiSelect from './MultiSelect';

const FormSection = ({ title, fields, data, section, onChange, onMultiSelect }) => {
  return (
    <div className="form-section">
      <h2>{title}</h2>
      {fields.map((field) => {
        if (field.type === 'multiselect') {
          return (
            <MultiSelect
              key={field.id}
              label={field.label}
              options={field.options}
              selected={data[field.id] || []}
              onChange={(selected) => onMultiSelect(section, field.id, selected)}
            />
          );
        }
        return (
          <FormInput
            key={field.id}
            type={field.type}
            id={field.id}
            label={field.label}
            value={data[field.id] || ''}
            required={field.required}
            options={field.options}
            onChange={(e) => onChange(section, field.id, e.target.value)}
          />
        );
      })}
    </div>
  );
};

export default FormSection;
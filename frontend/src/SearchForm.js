import React, { useState } from 'react';
import axios from 'axios';

function SearchForm() {
  const [formData, setFormData] = useState({
    make: '',
    model: '',
    price: '',
    email: '',
    anyModel: false
  });

  const [isLoading, setIsLoading] = useState(false)
  const [successMessage, setSuccessMessage] = useState('')

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if(type === "checkbox") {
      setFormData({
        ...formData,
        [name]: checked, 
        ...(checked ? { make: '', model: ''} : {})
      });
    } else {
      setFormData({
        ...formData,
        [name]:  value
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true)
    try {
      const payload = {
        price: formData.price,
        email: formData.email,
        anyModel: formData.anyModel
      };
      
      if (!formData.anyModel) {
        payload.make = formData.make;
        payload.model = formData.model;
      }
      
      // POST request to Flask backend
      const response = await axios.post('http://localhost:5000/api/save', payload);
      setFormData({
        make: '',
        model: '',
        price: '',
        email: '',
        anyModel: false
      })
      setSuccessMessage(`We have received your information. Once we find a vehicle that matches your price point, we will send you an email to ${formData.email}.`);

      setTimeout(() => {
        setSuccessMessage('');
      }, 5000);
      
    } catch (error) {
      console.error('An error occurred:', error);
      setSuccessMessage('');
    } finally {
      setIsLoading(false)
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label className='anyModelCheckbox'>
          Any Model:
          <input
            type="checkbox"
            name="anyModel"
            checked={formData.anyModel}
            onChange={handleChange}
          />
        </label>
        {!formData.anyModel && (
          <>
            <label>
              Make:
              <input
                type="text"
                name="make"
                value={formData.make}
                onChange={handleChange}
              />
            </label>
            <label>
              Model:
              <input
                type="text"
                name="model"
                value={formData.model}
                onChange={handleChange}
              />
            </label>
          </>
        )}
        <label>
          Max price:
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
          />
        </label>
        <label>
          Your email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </label>
        <button type="submit"  disabled={isLoading}>{isLoading ? 'Loading...' : 'Email me car prices'}</button>
      </form>
      {successMessage && <div className='success-message'>{successMessage}</div>}
    </div>
  );
}

export default SearchForm;

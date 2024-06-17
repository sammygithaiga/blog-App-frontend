import React, { useState } from 'react';
import '../index.css'; // Import App.css for styles

function AddBlogPage() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your submit logic here
    console.log('Submitted:', { title, content });
    // Reset the form after submission
    setTitle('');
    setContent('');
  };

  return (
    <div className="add-blog-page">
      <div className="container add-blog-content">
        <h1 className="section-title">Add a New Blog Post</h1>
        <form className="blog-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="title">Title</label>
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="content">Content</label>
            <textarea
              id="content"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
            ></textarea>
          </div>
          <button type="submit" className="cta-button">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default AddBlogPage;

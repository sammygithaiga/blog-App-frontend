import React from 'react';
import { useParams } from 'react-router-dom';


function BlogPost() {
  let { id } = useParams();
  // Fetch the blog post using the id
  // Example: const post = fetchPostById(id);
  return (
    <div className="container">
      <h1 className="title">Blog Post Title</h1>
      <p className="content">Blog post content...</p>
    </div>
  );
}

export default BlogPost;

<html>
<head>
  <title>🚀 Capstone Guide 🤖</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.7.2/dist/css/bootstrap.min.css">
  <style>
    body {
      background-color: #55CDFC;
      color: #FFFFFF;
      padding: 20px;
      font-family: Arial, sans-serif;
    }

    h1, h2, h3 {
      color: #F7A8B8;
    }

    summary {
      color: #F7A8B8;
      cursor: pointer;
    }

    summary::-webkit-details-marker {
      color: #F7A8B8;
    }

    summary:focus {
      outline: none;
    }

    ul li::before {
      content: '🔘';
      margin-right: 5px;
    }

    ol li::before {
      content: '🔢';
      margin-right: 5px;
    }

    code {
      background-color: #F7A8B8;
      color: #FFFFFF;
      padding: 2px 5px;
      border-radius: 3px;
    }
  </style>
</head>
  
<body>
<div class="container">
  <h1 class="display-4 mt-4">🚀 Capstone Guide 🤖</h1>
  <p>Hello, students of the cosmos! 🌍🪐</p>

  <details>
    <summary class="mt-4"> Expand to Understand </summary>
  
    <div class="mt-4">
      <p>In this repository, you'll find several resources to guide you along your journey:</p>
    </div>

    <ul class="list-group mt-4">
      <li class="list-group-item">📜 A detailed <strong>Rubric</strong> with our project expectations and grading criteria.</li>
      <li class="list-group-item">🧙‍♀️ A <strong>README.md Template</strong> to help you create a thorough and concise project description.</li>
      <li class="list-group-item">🤖 Clear <strong>Instructions for Pushing to Github</strong> to ensure your work is shared and preserved.</li>
      <li class="list-group-item">🌍 A simple guide on <strong>Turning a Github Repo into GH-Pages</strong>, making your project easily accessible and presentable to anyone in the universe!</li>
    </ul>

    <div class="mt-4">
      <p>Please read through all the materials carefully. As always, don't hesitate to ask questions if anything is unclear—we're here to help. Most importantly, remember that this project is a chance for you to showcase your learning and creativity. So, be bold, have fun, and reach for the stars!</p>
    </div>
  </details>

  <h2 class="mt-4">🪄💫 Rubric 🌟🔮</h2>
  <p>Happy coding, data wizards! 🧙‍♀️💻🔮</p>

  <details>
    <summary class="mt-4"> Rubric </summary>

    <h3>Project Understanding and Implementation (40 points)</h3>
    <ul>
      <li>[ ] Demonstrates a clear understanding of the statistical methods used in the project (10 points)</li>
      <li>[ ] Applies appropriate statistical techniques to analyze the data (10 points)</li>
      <li>[ ] Implements code correctly and efficiently (10 points)</li>
      <li>[ ] Produces correct and meaningful results (10 points)</li>
    </ul>

    <h3>Documentation and Communication (30 points)</h3>
    <ul>
      <li>[ ] Provides clear explanations of the code and analysis steps (10 points)</li>
      <li>[ ] Includes well-organized and readable code comments (5 points)</li>
      <li>[ ] Clearly explains the data used and its relevance to the project (5 points)</li>
      <li>[ ] Describes the analysis conducted and the results obtained (10 points)</li>
      <li>[ ] Presents clear conclusions based on the analysis (5 points)</li>
    </ul>

    <h3>Version Control and Project Management (30 points)</h3>
    <ul>
      <li>[ ] Utilizes Git for version control and pushes regular commits (10 points)</li>
      <li>[ ] Maintains a well-organized project structure with appropriate file naming and documentation (10 points)</li>
      <li>[ ] Collaborates effectively on GitHub, demonstrating the ability to clone, pull, and push changes (10 points)</li>
    </ul>
  </details>

  <h2 class="mt-4">🧙‍♀️ Your Readme 🧙‍♀️</h2>
  <p>Learn how to structure and create your project readme</p>

  <details>
  <summary class="mt-4"> Readme Template </summary>
    
  ```md
  
  # 🌠 Project Title

  ## 🚀 Introduction

  Describe the goal of your project here.

  ## 🧩 Dependencies

  - R (version)
  - R packages: dplyr, ggplot2, etc.

  ## 📊 Data

  Describe your data here.

  ## 🔬 Analysis

  Describe your analysis here.

  ## 📈 Results

  Describe your results here.

  ## 💡 Conclusion

  What conclusions can be drawn from your analysis?

  ## 🎬 Example Run

  Explain how to run an example of your project.
  
  ```
  </details>

  <h2 class="mt-4">🔬 Detailed Github Guide 🔬</h2>
  <p>Everything you need to know to interface with GitHub</p>

  <details>
    <summary class="mt-4"> The magic and power of Git </summary>

    <h2 class="mt-4">🤖 Instructions for Pushing to GitHub 🌌</h2>

    <p>Follow these steps to push your project to GitHub:</p>

    <ol>
      <li>📍 <strong>Navigate to your local project in your terminal</strong></li>
        <p>Open your terminal or command prompt and use the <code>cd</code> command to navigate to the directory where your project is located.</p>
        <pre><code>cd path/to/your/project</code></pre>
      <li>📁 <strong>Initialize Git in your project directory</strong></li>
        <p>Run the following command to initialize Git:</p>
        <pre><code>git init</code></pre>
      <li>🌟 <strong>Create a new repository on GitHub</strong></li>
        <p>Go to GitHub and create a new repository. Make sure not to initialize it with a README file, as we already have our own.</p>
      <li>🔗 <strong>Link your local repository to the remote repository on GitHub</strong></li>
        <p>Run the following command, replacing <code>username</code> with your GitHub username and <code>repository</code> with the name of your repository:</p>
        <pre><code>git remote add origin https://github.com/username/repository.git</code></pre>
      <li>📥 <strong>Add your files to Git</strong></li>
        <p>Run the following command to add all files in your project to Git:</p>
        <pre><code>git add .</code></pre>
      <li>💬 <strong>Commit your changes</strong></li>
        <p>Run the following command to commit your changes:</p>
        <pre><code>git commit -m "Initial commit"</code></pre>
      <li>📤 <strong>Push your project to GitHub</strong></li>
        <p>Run the following command to push your project to GitHub:</p>
        <pre><code>git push -u origin master</code></pre>
      <li>🌟 <strong>Celebrate!</strong></li>
        <p>Your project is now pushed to GitHub! 🎉</p>
    </ol>
  </details>

  <h2 class="mt-4">🌍 Turning a Github Repo into GH-Pages</h2>
  <p>Learn how to make your project accessible to the world</p>

  <details>
    <summary class="mt-4"> GH-Pages Guide </summary>

    <h2 class="mt-4">🔧 Steps to Publish Your Project on GitHub Pages</h2>

    <p>Follow these steps to turn your GitHub repository into a live website using GitHub Pages:</p>

    <ol>
      <li>🌟 <strong>Create a new branch named gh-pages</strong></li>
        <p>Go to your repository on GitHub and create a new branch named <code>gh-pages</code>. This branch will be used to host your website.</p>
      <li>📄 <strong>Ensure you have an index.html file</strong></li>
        <p>Make sure you have an <code>index.html</code> file in your repository. This file will act as the main page of your website.</p>
      <li>🔗 <strong>Push the branch to GitHub</strong></li>
        <p>Use the following command to push the <code>gh-pages</code> branch to GitHub:</p>
        <pre><code>git push origin gh-pages</code></pre>
      <li>🌐 <strong>Access your website</strong></li>
        <p>Your website should now be accessible at <code>https://username.github.io/repository</code>, where <code>username</code> is your GitHub username and <code>repository</code> is the name of your repository.</p>
      <li>🌟 <strong>Celebrate!</strong></li>
        <p>Your project is now live on GitHub Pages! 🎉</p>
    </ol>
  </details>
</div>
</body>
</html>

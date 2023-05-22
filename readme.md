<!DOCTYPE html>
<html>
<head>
  <title>🚀 Capstone Guide 🤖</title>
</head>
<body>
<h1>🚀 Capstone Guide 🤖</h1>
<p>Hello, students of the cosmos! 🌍🪐</p>

<details>
<summary> Expand to Understand </summary>
  
  <br>
  <p>In this repository, you'll find several resources to guide you along your journey:</p>
  <br>

  <ul>
    <li>📜 A detailed <strong>Rubric</strong> with our project expectations and grading criteria.</li>
    <li>🧙‍♀️ A <strong>README.md Template</strong> to help you create a thorough and concise project description.</li>
    <li>🤖 Clear <strong>Instructions for Pushing to Github</strong> to ensure your work is shared and preserved.</li>
    <li>🌍 A simple guide on <strong>Turning a Github Repo into GH-Pages</strong>, making your project easily accessible and presentable to anyone in the universe!</li>
  </ul>

   <br>

  <p>Please read through all the materials carefully. As always, don't hesitate to ask questions if anything is unclear—we're here to help. Most importantly, remember that this project is a chance for you to showcase your learning and creativity. So, be bold, have fun, and reach for the stars!</p>

</details>
<br>

<h2>🪄💫 Rubric 🌟🔮</h2>
<p>Happy coding, data wizards! 🧙‍♀️💻🔮</p>

<details>
<summary> Rubric </summary>

<h3>Project Understanding and Implementation (40 points)</h3>
<ul>
  <li>[ ] Demonstrates a clear understanding of the statistical methods used in the project (10 points)</li>
  <li>[ ] Applies appropriate statistical techniques to analyze the data (15 points)</li>
  <li>[ ] Implements the analysis in R or Python with correct usage of relevant libraries (15 points)</li>
</ul>

<h3>Communication of Findings (30 points)</h3>
<ul>
  <li>[ ] Provides a thorough and concise project description in the README.md file (10 points)</li>
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

<br>
  
<h2>🧙‍♀️ Your Readme 🧙‍♀️</h2>
 
<p>Learn how to structure and create your project readme</p>
 
<details>
<summary> Readme Template </summary>
   
<h1>🌠 Project Title</h1>

<h2>🚀 Introduction</h2>

<p>Describe the goal of your project here.</p>

<h2>🧩 Dependencies</h2>

<ul>
  <li>R (version)</li>
  <li>R packages: dplyr, ggplot2, etc.</li>
</ul>

<h2>📊 Data</h2>

<p>Describe your data here.</p>

<h2>🔬 Analysis</h2>

<p>Describe your analysis here.</p>

<h2>📈 Results</h2>

<p>Describe your results here.</p>

<h2>💡 Conclusion</h2>

<p>What conclusions can be drawn from your analysis?</p>

<h2>🎬 Example Run</h2>

<p>Explain how to run an example of your project.</p>
  
</details>

<br>

<h2>🔬 Detailed Github Guide 🔬</h2>
<p>Everything you need to know to interface with github</p>
  
<details>
<summary> The magic and power of Git </summary>
  
<h2>🤖 Instructions for Pushing to Github 🌌</h2>

<p>Follow these steps to push your project to Github:</p>

<ol>
  <li>📍 <strong>Navigate to your local project in your terminal</strong></li>
    <p>Open your terminal or command prompt and use the <code>cd</code> command to navigate to the directory where your project is located.</p>
    <pre><code>cd path/to/your/project</code></pre>
  <li>📚 <strong>Initialize a Git repository</strong></li>
    <p>Initialize a new Git repository in your project directory.</p>
    <pre><code>git init</code></pre>
  <li>➕ <strong>Add all project files</strong></li>
    <p>Use the <code>git add</code> command to stage all the files in your project for commit. The <code>.</code> tells Git to add all the files in the current directory.</p>
    <pre><code>git add .</code></pre>
  <li>✍️ <strong>Commit your files</strong></li>
    <p>Commit the staged files. This is like creating a snapshot of your project at this point in time.</p>
    <pre><code>git commit -m "Initial commit"</code></pre>
  <li>🌐 <strong>Create a new repository on GitHub</strong></li>
    <p>Navigate to <a href="https://github.com">GitHub</a> in your web browser and create a new repository. Do not initialize the new repository with a README, .gitignore, or License. We will push these files from our local repository.</p>
  <li>🔄 <strong>Add the remote repository</strong></li>
    <p>Back in your terminal, use the <code>git remote add</code> command to link your local repository to the remote repository on GitHub. Replace <code>[Your GitHub Repo URL]</code> with the URL of your new GitHub repository.</p>
    <pre><code>git remote add origin [Your GitHub Repo URL]</code></pre>
  <li>⬆️ <strong>Push your code</strong></li>
    <p>Use the <code>git push</code> command to push your local commits to the remote repository on GitHub.</p>
    <pre><code>git push -u origin master</code></pre>
</ol>

<p>Congratulations! 🎉 Your project is now on GitHub!</p>
  
<p>To be done via the terminal:</p>

<ol>
  <li>Make sure you are in the project's root directory in your terminal.</li>
  <li>Run the following commands:</li>
</ol>

<pre><code>git init
git add .
git commit -m "Initial commit"
git remote add origin [Your GitHub Repo URL]
git push -u origin master</code></pre>
  
<p>That's it! Your project should now be available on your GitHub repository.</p>
  
</details>

<br>

<h2>🌍 Turning a Github Repo into GH-Pages 🌐</h2>
<p>Make your project easily accessible and presentable to anyone in the universe!</p>

<details>
<summary> Github Pages Setup Guide </summary>
   
<p>To turn your GitHub repository into a live website using GitHub Pages, follow these steps:</p>

<ol>
  <li>📁 <strong>Create a new branch</strong></li>
    <p>In your repository on GitHub, create a new branch called <code>gh-pages</code>.</p>
  <li>🔧 <strong>Configure branch settings</strong></li>
    <p>In the repository settings, go to the "Branches" section and set the default branch to <code>gh-pages</code>.</p>
  <li>🔃 <strong>Push your changes</strong></li>
    <p>In your local project, switch to the <code>gh-pages</code> branch and push it to GitHub.</p>
    <pre><code>git checkout -b gh-pages
git push origin gh-pages</code></pre>
  <li>🌐 <strong>Access your site</strong></li>
    <p>Your site should now be accessible at <code>https://[your-username].github.io/[your-repository-name]/</code>.</p>
  <li>🌟 <strong>Custom domain (optional)</strong></li>
    <p>If you have a custom domain, you can set it up in the repository settings. Follow the instructions provided by GitHub to configure your DNS settings.</p>
</ol>

<p>That's it! Your project is now live on GitHub Pages!</p>
  
</details>

</body>
</html>
